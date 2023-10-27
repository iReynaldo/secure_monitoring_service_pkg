from secure_monitoring_service_pkg.report import Report

num_reports = 1
expected_time = 0.009
reports_path_list = list()


reports_path_list.append(
    Report(reporting_asn=271063, prefix="1.2.3.0/24", as_path=(271063, 271397)).as_path
)
