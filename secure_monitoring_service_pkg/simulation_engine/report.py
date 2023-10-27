class Report:
    def __init__(self, reporting_asn, prefix, as_path):
        self.reporting_asn: int = reporting_asn
        self.prefix: str = prefix
        self.as_path: list = as_path
