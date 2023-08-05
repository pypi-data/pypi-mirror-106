import functools
from logging import Logger
from pathlib import Path
from typing import Callable, Optional, Sequence

import numpy as np

import cytoskeleton_analyser.fitting as fts
from ..cells import organizing_centers
from ..summary import Summary
from ..visualization import Multiplot
from .records import Records


def report(
        recs: Records,
        signature: str,
        path: Path,
        show: bool,
) -> None:

    fts.set_logger(recs.logger)
    Summary.logger = recs.logger

    UnpolymerizedTubulin(recs, signature, show).report(path)
    MictorubuleNumbers(recs, signature, show).report(path)
    MictorubuleMasses(recs, signature, show).report(path)
    MictorubuleAges(recs, signature, show).report(path)
    MictorubuleStates(recs, signature, show).report(path)
    CellReactionPropensities(recs, signature, show).report(path)

    print('')


def restore(
        recs: Records,
        signature: str,
        path: Path,
        show: bool,
        savefig: bool = False,
) -> dict:

    fts.set_logger(recs.logger)
    Summary.logger = recs.logger

    res = {
        'UnpolymerizedTubulin':
            UnpolymerizedTubulin(recs, signature, show)
                .restore(path, savefig),

        'MictorubuleNumbers':
            MictorubuleNumbers(recs, signature, show)
                .restore(path, savefig),

        'MictorubuleMasses':
            MictorubuleMasses(recs, signature, show)
                .restore(path, savefig),

        'MictorubuleAges':
            MictorubuleAges(recs, signature, show)
                .restore(path, savefig),

        'MictorubuleStates':
            MictorubuleStates(recs, signature, show)
                .restore(path, savefig),

        'CellReactionPropensities':
            CellReactionPropensities(recs, signature, show)
                .restore(path, savefig),
    }
    print('')

    return res


class Report:
    """Base class for reporting time-dependent parameters.
    """

    def __init__(
            self,
            recs: Records,
            signature: str,
            show: bool = True,
    ):

        self.signature = signature
        self.title = None
        self.recs = recs
        self.time_unit = recs.time_unit
        self.logger = recs.logger
        self.names = None
        self.x = recs.tt
        self.x_label = f"time ({self.time_unit})"
        self.y = None
        self.y_label = None
        self.fits = None
        self.colormap = 'tab20'
        self.show = show

    def plot(
            self,
            path: Optional[Path] = None,
    ) -> None:

        figtitle = self.title + ': ' + self.signature \
            if len(self.names) > 1 else self.signature
        exportfile = path / self.title if path is not None else None
        Multiplot(Multiplot.Data(
                figtitle=figtitle,
                axtitles=self.names,
                x=self.x,
                x_label=self.x_label,
                y=self.y,
                y_label=self.y_label,
                fit=self.fits,
                colormap=self.colormap,
            ),
            exportfile,
            self.show)

    def restore(
            self,
            path: Path,
            savefig: bool,
    ) -> dict:

        self.recs.logger.info('Restoring ' + self.title + ':')

        smr = Summary().read(path, self.title).data

        fc = [fts.class_from_classname(fts, s['model']['name'])
              if s['model']['name'] is not None else None for s in smr]

        ee = [e.create() if hasattr(e, 'create') else e for e in fc]

        cc = [fts.subtype_from_classname(e, s['model']['name'])
              if e is not None else None for e, s in zip(ee, smr)]

        self.fits = []
        for c, d, e, y in zip(cc, smr, ee, self.y):
            if c is not None:
                self.recs.logger.info(f"{d['name']}: ")
                self.fits.append(
                    [
                     fts.restore(c, d['model']['p'], self.time_unit, self.x, y)
                    ]
                )
            else:
                self.fits.append(None)

        self.plot(path=path if savefig else None)

        self.recs.logger.info('')

        return {s['name']: {k: v for k, v in s.items() if k != 'name'}
                for s in smr}


# ======================================================================================================================
class UnpolymerizedTubulin(Report):

    def __init__(
            self,
            recs: Records,
            signature: str,
            show: bool = True,
    ):

        super().__init__(recs, signature, show)
        self.title = 'unpolymerized tubulin'
        self.names = ['unpolymerized Tu']
        self.base_factor = float(Records.TUBULIN_TOTAL)
        self.y = [recs.fT / self.base_factor]
        self.y_label = 'cell free tubulin as a fraction of total'

    def report(
            self,
            path: Optional[Path] = None
    ) -> None:

        self.logger.info('Processing ' + self.title)

        y = self.y[0]
        e = fts.Exponential.create()
        p: type = fts.Exponential.Pars
        tu = self.recs.time_unit

        total = y.max()
        d = y.min()
        a = y.max() - d
        tau1 = self.x.max() / 100.
        tau2 = 100. * tau1
        self.fits = [fts.fit([
            (e.d_i, p(a=a, tau1=tau1, d=d), tu),
            (e.d_d_i, p(a=a, tau1=tau1, b=0.9, tau2=tau2, d=d), tu),
            (e.d_d_sg_i, p(a=9*total/10, tau1=tau1/10, b=0.9, tau2=tau2*5,
                           c=total/10, tau3=tau1*20, d=d), tu),
        ], self.x, y)]

        self.plot()

        ibest = [2]

        smr = Summary().init(self.names, ibest, self.fits)
        smr.add_items([{'base_factor': self.base_factor}])
        if path is not None:
            smr.save(path, self.title)


# ======================================================================================================================
class MictorubuleNumbers(Report):

    def __init__(
            self,
            recs: Records,
            signature: str,
            show: bool = True,
    ):

        super().__init__(recs, signature, show)
        self.title = 'microtubule numbers'
        self.names = [oc for oc in organizing_centers]
        self.y = recs.nf
        self.y_label = 'number of filaments'

    def report(
            self,
            path: Optional[Path] = None
    ) -> None:

        self.logger.info('\nProcessing ' + self.title)

        @_decor(self.logger, self.x, self.names)
        def fnc(yy: np.ndarray) -> list[tuple]:
            e = fts.Exponential.create()
            p = fts.Exponential.Pars
            tu = self.recs.time_unit
            a = yy.mean()
            tau1 = self.x.max() / 100.
            tau2 = 100. * tau1
            return [
                (e.sg_h, p(a=a, tau1=tau1), tu),
                (e.sg_sg_h, p(a=a, tau1=tau1, b=0.9, tau2=tau2), tu),
            ]

        self.fits = fnc(self.y)

        self.plot()

        ibest = [1, 0, 0, 0, 1]

        smr = Summary().init(self.names, ibest, self.fits)
        if path is not None:
            smr.save(path, self.title)


# ======================================================================================================================
class MictorubuleMasses(Report):

    def __init__(
            self,
            recs: Records,
            signature: str,
            show: bool = True,
    ):

        super().__init__(recs, signature, show)
        self.title = 'microtubule masses'
        self.names = [f"mass {oc}" for oc in organizing_centers]
        self.base_factor = \
            float(Records.TUBULIN_TOTAL) / \
            float(Records.DIMERS_PER_UNIT)
        self.y = np.array([csm / self.base_factor for csm in recs.csmass])
        self.y_label = 'fraction of the cell total tubulin'

    def report(
            self,
            path: Optional[Path] = None
    ) -> None:

        self.logger.info('Processing ' + self.title)

        @_decor(self.logger, self.x, self.names)
        def fnc(yy: np.ndarray) -> list[tuple]:
            e = fts.Exponential.create()
            p: type = fts.Exponential.Pars
            tu = self.recs.time_unit
            total = yy.max()
            a = yy.mean()
            tau1 = self.x.max() / 100.
            tau2 = 100. * tau1
            tau3 = tau1 * 10.
            return [
                    (e.sg_h, p(a=a, tau1=tau1), tu),
                    (e.sg_sg_h, p(a=a, tau1=tau1, b=0.9, tau2=tau2), tu),
                    (e.sg_sg_d_h, p(a=2*total/3, tau1=tau1/10, b=0.9,
                                    tau2=tau2*5, c=total/3, tau3=tau3), tu),
                   ]

        self.fits = fnc(self.y)

        self.plot()

        ibest = [2, 0, 2, 0, 0]

        smr = Summary().init(self.names, ibest, self.fits)
        smr.add_items([{'base_factor': self.base_factor}])
        if path is not None:
            smr.save(path, self.title)


# ======================================================================================================================
class MictorubuleAges(Report):

    def __init__(
            self,
            recs: Records,
            signature: str,
            show: bool = True,
    ):

        super().__init__(recs, signature, show)
        self.title = 'microtubule ages'
        self.names = ['MT age']
        self.y = [recs.age]
        self.y_label = 'age (sec)'

    def report(
            self,
            path: Optional[Path] = None
    ) -> None:

        self.logger.info('Processing ' + self.title)

        y = self.y[0]
        e = fts.Exponential.create()
        p = fts.Exponential.Pars
        tu = self.recs.time_unit
        a = y.max()
        tau1 = self.x.max() / 100.
        tau2 = 100. * tau1
        self.fits = [fts.fit([
                    (e.sg_h, p(a=a, tau1=tau1), tu),
                    (e.sg_sg_h, p(a=a, tau1=tau1, b=0.9, tau2=tau2), tu),
                    (e.sg_line, p(a=10000., tau1=tau1, c=3000.,
                                  d=10.*tau1), tu),
                    ], self.x, y)]

        self.plot()

        ibest = [2]

        smr = Summary().init(self.names, ibest, self.fits)
        if path is not None:
            smr.save(path, self.title)


# ======================================================================================================================
class MictorubuleStates(Report):

    def __init__(
            self,
            recs: Records,
            signature: str,
            show: bool = True,
    ):

        super().__init__(recs, signature, show)
        self.title = 'microtubule states'
        state_names = ['growing', 'shrinking', 'paused', 'anchored'] * 2

        def end(i):
            return '-' if int(2 * i / len(state_names)) < 1 else '+'

        self.names = [f"{s} at '{end(i)}'-end"
                      for i, s in enumerate(state_names)]
        exclude = [4, 9] if recs.nSts > 8 else []
        self.y = np.array([s / recs.nf[0]
                           for i, s in enumerate(recs.sts)
                           if i not in exclude])

        self.y_label = 'fraction of the cell microtubules'

    def report(
            self,
            path: Optional[Path] = None
    ) -> None:

        self.logger.info('\nProcessing ' + self.title)

        total = max([u.max() for u in self.y])

        @_decor(self.logger, self.x, self.names)
        def fnc(yy: np.ndarray) -> list[tuple]:
            e = fts.Exponential.create()
            p = fts.Exponential.Pars
            tu = self.recs.time_unit
            m = yy.mean()
            m0 = yy[:3].mean()
            d = yy.min()
            tau1 = self.x.max() / 100.
            tau2 = 100. * tau1
            tau3 = tau1 * 10.
            if m > m0:
                return [
                    (e.sg_h, p(a=m, tau1=tau1), tu),
                    (e.sg_sg_h, p(a=m, tau1=tau1, b=0.9, tau2=tau2), tu),
                    (e.sg_sg_d_h, p(a=2*total/3, tau1=tau1/10, b=0.9,
                                    tau2=tau2*5, c=total/3, tau3=tau3), tu),
                ]
            else:
                return [
                    (e.d_i, p(a=m0-m, tau1=tau1, d=m), tu),
                    (e.d_d_i, p(a=m0-m, tau1=tau1, b=0.9, tau2=tau2, d=m), tu),
                    (e.d_d_sg_h, p(a=total, tau1=tau1/10, b=0.9, tau2=tau2*5,
                                   c=total/3, tau3=tau3), tu),
                    (e.d_d_sg_i, p(a=total, tau1=tau1/10, b=0.9, tau2=tau2*5,
                                   c=total/3, tau3=tau3, d=d), tu),
                ]

        self.fits = fnc(self.y)

        self.plot()

        ibest = [0, 0, 0, 0, 0, 0, 0, 0]

        smr = Summary().init(self.names, ibest, self.fits)
        if path is not None:
            smr.save(path, self.title)


# ======================================================================================================================
class CellReactionPropensities(Report):

    def __init__(
            self,
            recs: Records,
            signature: str,
            show: bool = True,
    ):

        super().__init__(recs, signature, show)
        self.title = 'cell reaction propensities'
        self.names = ['reaction: '+r.name[0] for r in self.recs.reacts]
        self.y = np.array([r.prop for r in recs.reacts])
        self.y_label = 'prop/sed'

    def report(
            self,
            path: Optional[Path] = None
    ) -> None:

        self.logger.info('\nProcessing ' + self.title)

        total = max([u.max() for u in self.y])

        @_decor(self.logger, self.x, self.names)
        def fnc(yy: np.ndarray) -> list[tuple]:
            e = fts.Exponential.create()
            p = fts.Exponential.Pars
            tu = self.recs.time_unit
            m = yy.mean()
            m0 = yy[:3].mean()
            tau1 = self.x.max() / 100.
            tau2 = 100. * tau1
            tau3 = tau1 * 10.
            if m > m0:
                return [
                    (e.sg_h, p(a=m, tau1=tau1), tu),
                    (e.sg_sg_h, p(a=m, tau1=tau1, b=0.9, tau2=tau2), tu),
                    (e.sg_sg_d_h, p(a=2*total/3, tau1=tau1, b=0.9, tau2=tau2,
                                    c=total/3, tau3=tau3), tu),
                ]
            else:
                return [
                    (e.d_i, p(a=m0-m, tau1=tau1, d=m), tu),
                    (e.d_d_i, p(a=m0-m, tau1=tau1, b=0.9, tau2=tau2, d=m), tu),
                    (e.d_d_sg_h, p(a=total, tau1=tau1/10, b=0.9, tau2=tau2*5,
                                   c=total/3, tau3=tau3), tu),
                ]

        self.fits = fnc(self.y)

        self.plot()

        ibest = [0, 1, 0, 0, 0, 0, 0, 0, 0]

        smr = Summary().init(self.names, ibest, self.fits)
        if path is not None:
            smr.save(path, self.title)


# ======================================================================================================================
def _decor(
        logger: Logger,
        x: np.array,
        names: list[str]
) -> Callable:
    """Decorator function for fit generation.
    """

    def decorator(func: Callable):

        @functools.wraps(func)
        def wrapper(y: Sequence) -> list:

            res = []
            for yy, name in zip(y, names):
                assert isinstance(yy, np.ndarray)
                logger.info('')
                logger.info(name + ':')
                m = yy.mean()
                v = yy.var()
                if v > 0.:
                    res.append(fts.fit(func(yy), x, yy))
                else:
                    res.append([fts.MockConst(x, [m]).f().report()])

            return res

        return wrapper

    return decorator
