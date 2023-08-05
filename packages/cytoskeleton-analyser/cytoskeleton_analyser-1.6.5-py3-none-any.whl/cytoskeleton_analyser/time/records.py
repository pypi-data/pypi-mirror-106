from __future__ import annotations
import csv
import gzip
from logging import Logger
from pathlib import Path
from typing import Final, Union

import numpy as np


class Reaction:

    def __init__(self):
        self.name: list[str] = []
        self.num: Union[list[int], np.ndarray] = []
        self.prop: Union[list[float], np.ndarray] = []

    def sort(self, sis):
        """ Inplace sorting according to time.
        """
        self.name = self.name[sis]
        self.num = self.num[sis]
        self.prop = self.prop[sis]
        return self

    def append(self, rec, j):
        self.name.append(rec[j])
        self.num.append(int(rec[j + 1]))
        self.prop.append(float(rec[j + 2]))
        return self

    def to_numpy(self):
        self.num = np.array(self.num, dtype=np.float64)
        self.prop = np.array(self.prop, dtype=np.float64)
        return self

    def __add__(self, other):
        r = Reaction()
        r.name = np.hstack((self.name, other.name))
        r.num = np.hstack((self.num, other.num))
        r.prop = np.hstack((self.prop, other.prop))
        return r

    def row(self, i):
        return self.name[i], int(self.num[i]), self.prop[i]


class Records:

    DATA_INDS: Final[slice] = slice(0, -2, None)  # exclude {reacts, time_unit}
    nNf: Final[int] = 5
    nIcM: Final[int] = 3
    nSts: Final[int] = 8
    nCas: Final[int] = 6
    nR: Final[int] = 9
    TUBULIN_TOTAL: Final[int] = 29059381
    DIMERS_PER_UNIT: Final[int] = 13  #: Dimers used per fine-graned node.

    logger: Logger

    def __init__(
            self,
            logger: Logger,
            time_unit: str = 'sec',
    ):

        Records.logger = logger

        self.run = []
        self.logcnt = []
        self.iter = []
        self.t = []
        self.tt = []
        self.tau = []
        self.rtI = []
        self.rtS = []
        self.nf = [[] for _ in range(Records.nNf)]
        self.csmass = [[] for _ in range(Records.nNf)]
        self.ndLen = []
        self.age = []
        self.icF = []
        self.icM = [[] for _ in range(Records.nIcM)]
        self.sts = [[] for _ in range(Records.nSts)]
        self.fT = []
        self.cas = [[] for _ in range(Records.nCas)]
        self.reacts = [Reaction() for _ in range(Records.nR)]
        self.time_unit: str = time_unit

    def from_original(
            self,
            fname: Path,
            run,
    ) -> Records:

        self.logger.info("reading from: " + str(fname))
        with open(fname, 'r') as f:
            is_rec = False
            for sl in f:
                if sl:
                    if sl == 'Starting main loop \n':
                        is_rec = True
                        continue
                    if is_rec:
                        sp = sl.split()
                        if len(sp):
                            if sp[0].isnumeric():
                                self.append(sp, run, 1)

        self.logger.info(f"read in: {len(self.iter)} records")
        self.to_numpy()
        return self

    def sort(self) -> None:
        """ Inplace sorting according to time.
        """

        assert isinstance(self.t, np.ndarray)
        sis = np.argsort(self.t)  # sort indexes
        self.run = self.run[sis]
        self.logcnt = self.logcnt[sis]
        self.iter = self.iter[sis]
        self.t = self.t[sis]
        if len(self.tt):
            self.tt = self.tt[sis]
        self.tau = self.tau[sis]
        self.rtI = self.rtI[sis]
        self.rtS = self.rtS[sis]
        self.nf = [x[sis] for x in self.nf]
        self.csmass = [x[sis] for x in self.csmass]
        self.ndLen = self.ndLen[sis]
        self.age = self.age[sis]
        self.icF = self.icF[sis]
        self.icM = [x[sis] for x in self.icM]
        self.sts = [x[sis] for x in self.sts]
        self.fT = self.fT[sis]
        self.cas = [x[sis] for x in self.cas]
        self.reacts = [r.sort(sis) for r in self.reacts]

    def append(
            self,
            rec,
            run,
            s: int = 1
    ) -> None:

        self.run.append(run)
        i = 0

        self.logcnt.append(int(rec[i]))
        i += 1

        self.iter.append(int(rec[i]))
        i += 1 + s

        self.t.append(float(rec[i]))
        i += 1 + s

        if s == 0:
            self.tt.append(float(rec[i]))
            i += 1

        self.tau.append(float(rec[i]))
        i += 1 + s

        self.rtI.append(int(rec[i]))
        if self.t[-1]:
            i += 1
            self.rtS.append(rec[i])
        else:
            if rec[i + 1] == '':
                i += 1
            self.rtS.append('')
        i += 1 + s

        [self.nf[m].append(int(rec[i + m])) for m in range(len(self.nf))]
        i += Records.nNf + s

        [self.csmass[m].append(float(rec[i + m])) for m in range(Records.nNf)]
        i += Records.nNf + s

        self.ndLen.append(float(rec[i]))
        i += 1 + s

        self.age.append(float(rec[i]))
        i += 1 + s

        self.icF.append(int(rec[i]))
        i += 1 + s

        [self.icM[m].append(int(rec[i + m])) for m in range(Records.nIcM)]
        i += Records.nIcM + s

        [self.sts[m].append(int(rec[i + m])) for m in range(Records.nSts)]
        i += Records.nSts + s

        self.fT.append(int(rec[i]))
        i += 1 + s

        [self.cas[m].append(float(rec[i + m])) for m in range(Records.nCas)]
        i += Records.nCas + s  # 'scores:'

        self.reacts = [r.append(rec, i + 3 * m) for m, r in enumerate(self.reacts)]

    def to_numpy(self) -> None:

        for k in list(vars(self).keys())[self.DATA_INDS]:
            setattr(self, k, np.array(getattr(self, k)))
        self.reacts = [r.to_numpy() for r in self.reacts]

    def __add__(self, other):

        assert isinstance(other, Records)
        if not isinstance(self.t, np.ndarray):
            self.to_numpy()
        if not isinstance(other.t, np.ndarray):
            other.to_numpy()

        if other.logger is not None:
            self.logger = other.logger
        elif self.logger is not None:
            other.logger = self.logger

        res = Records(self.logger)

        for k in list(vars(self).keys())[self.DATA_INDS]:
            setattr(res, k, np.hstack((getattr(self, k), getattr(other, k))))

        res.reacts = [srs + ors for srs, ors in zip(self.reacts, other.reacts)]

        return res

    def scale_time_to(
            self,
            s: str
    ) -> None:

        if s == 'd':
            self.tt = np.array([t / 3600 / 24 for t in self.t])
        elif s == 'hours':
            self.tt = np.array([t / 3600 for t in self.t])
        elif s == 'min':
            self.tt = np.array([t / 60 for t in self.t])
        elif s == 's' or s == 'sec':
            self.tt = np.array([self.t])
        else:
            assert (False, 'Wrong time unit')

        self.time_unit = s

    def csv_columns(self) -> list[str]:

        columns = []
        for k in list(vars(self).keys())[self.DATA_INDS]:
            a = getattr(self, k)
            if isinstance(a, np.ndarray):
                columns.append(k)
            else:
                columns.extend([k + '_' + str(i) for i in range(len(a))])

        columns.extend([f"reacts_{i}" for i in range(Records.nR)])

        return columns

    def to_csv(
            self,
            path: Path,
            gzipped: bool = False,
    ) -> None:

        fname = path / 'records.csv.gz' if gzipped else \
                path / 'records.csv'
        self.logger.info("exporting to: " + str(fname))
        opn = gzip.open if gzipped else open
        with opn(fname, 'wt', newline='') as f:
            w = csv.writer(f, delimiter=',')
            w.writerow(self.csv_columns())
            for i in range(len(self.run)):
                w.writerow([
                    int(self.run[i]),
                    int(self.logcnt[i]),
                    int(self.iter[i]),
                    self.t[i],
                    self.tt[i],
                    self.tau[i],
                    int(self.rtI[i]),
                    self.rtS[i],
                    *[int(v[i]) for v in self.nf],
                    *[int(v[i]) for v in self.csmass],
                    self.ndLen[i],
                    self.age[i],
                    int(self.icF[i]),
                    *[int(v[i]) for v in self.icM],
                    *[int(v[i]) for v in self.sts],
                    int(self.fT[i]),
                    *[v[i] for v in self.cas],
                    *[u for v in self.reacts for u in v.row(i)]
                ])
        self.logger.info(f"exported: {len(self.iter)} records\n")

    def from_csv(
            self,
            path: Path,
    ) -> Records:

        fname = path / 'records.csv'
        if not fname.is_file():
            fname = path / 'records.csv.gz'
        self.logger.info("importing from: " + str(fname))
        opn = gzip.open if str(fname).split('.')[-1] == 'gz' else open
        with opn(fname, 'rt', newline='') as f:
            r = csv.reader(f, delimiter=',')
            r.__next__()  # caption
            for a in r:
                self.append(a[1:], a[0], 0)
        self.to_numpy()
        self.logger.info(f"imported: {len(self.iter)} records\n")

        return self

