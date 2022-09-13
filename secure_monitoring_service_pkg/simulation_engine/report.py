from dataclasses import dataclass

@dataclass
class Report:
    reporting_asn: int
    prefix: str
    as_path: list