from logging import Logger
from pathlib import Path
from typing import Optional, Sequence, Union

from ..cells import CellType
from ..inout import Paths
from ..inout import set_logger
from .records import Records
from .reporting import report
from .reporting import restore


def process(
        paths: Paths,
        rind: Union[Sequence[int], int],
        cell: CellType,
        original: bool = False,
        show: bool = True
) -> Optional[dict]:

    if isinstance(rind, int):
        rind = [rind]
    paths.data_out = paths.data_out / 'time'
    Paths.ensure(paths.data_out)

    logger = set_logger(f'time ind {rind}', paths.data_out / 'processing.log')

    signature = cell.typename + \
                f" plm {cell.plmind}" \
                f" csk {rind}\n"
    #    Records.nSts = 10

    if original:
        recs = import_runs(paths.plasma_in, cell.plmind, rind, logger)
        recs.to_csv(paths.data_out)
        report(recs, signature, paths.data_out, show)
        return None
    else:
        recs = Records(logger, 'hours').from_csv(paths.data_out)
        return restore(recs, signature, paths.data_out, show, savefig=False)


def import_runs(
        path: Path,
        plmind: int,
        rinds: Sequence[int],
        logger: Logger
) -> Records:

    recs = Records(logger)

    for ri in rinds:
        filename = path / f'csk{ri}' / f'cskLog_m{ri}_cG_{ri}_p_{plmind}.txt'
        recs = recs + Records(logger).from_original(filename, ri)
    recs.sort()
    recs.scale_time_to('hours')

    return recs
