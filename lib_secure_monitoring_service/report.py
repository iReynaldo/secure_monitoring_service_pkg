from typing import NamedTuple

class Report(NamedTuple):
    reporting_asn: int
    prefix: str
    as_path: list