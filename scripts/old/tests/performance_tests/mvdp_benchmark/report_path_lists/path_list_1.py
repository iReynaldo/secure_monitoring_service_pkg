from secure_monitoring_service_pkg.report import Report

num_reports = 3243
expected_time = 124  # About 2 minutes
reports_path_list = list()

reports_path_list.append(
    Report(reporting_asn=1239, prefix="1.2.3.0/24", as_path=(1239, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=3356, prefix="1.2.3.0/24", as_path=(3356, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=31727, prefix="1.2.3.0/24", as_path=(31727, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=4637, prefix="1.2.3.0/24", as_path=(4637, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=6939, prefix="1.2.3.0/24", as_path=(6939, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=7575, prefix="1.2.3.0/24", as_path=(7575, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=7713, prefix="1.2.3.0/24", as_path=(7713, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=9002, prefix="1.2.3.0/24", as_path=(9002, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=13237, prefix="1.2.3.0/24", as_path=(13237, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=13786, prefix="1.2.3.0/24", as_path=(13786, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=14840, prefix="1.2.3.0/24", as_path=(14840, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=18106, prefix="1.2.3.0/24", as_path=(18106, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=20764, prefix="1.2.3.0/24", as_path=(20764, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=24482, prefix="1.2.3.0/24", as_path=(24482, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=28716, prefix="1.2.3.0/24", as_path=(28716, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=33891, prefix="1.2.3.0/24", as_path=(33891, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=34224, prefix="1.2.3.0/24", as_path=(34224, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=34288, prefix="1.2.3.0/24", as_path=(34288, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=35598, prefix="1.2.3.0/24", as_path=(35598, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=37239, prefix="1.2.3.0/24", as_path=(37239, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=37497, prefix="1.2.3.0/24", as_path=(37497, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=37640, prefix="1.2.3.0/24", as_path=(37640, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=39120, prefix="1.2.3.0/24", as_path=(39120, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=39122, prefix="1.2.3.0/24", as_path=(39122, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=39351, prefix="1.2.3.0/24", as_path=(39351, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=39737, prefix="1.2.3.0/24", as_path=(39737, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=41695, prefix="1.2.3.0/24", as_path=(41695, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=41805, prefix="1.2.3.0/24", as_path=(41805, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=41811, prefix="1.2.3.0/24", as_path=(41811, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=47787, prefix="1.2.3.0/24", as_path=(47787, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=48362, prefix="1.2.3.0/24", as_path=(48362, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=50629, prefix="1.2.3.0/24", as_path=(50629, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=50877, prefix="1.2.3.0/24", as_path=(50877, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=51185, prefix="1.2.3.0/24", as_path=(51185, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=55329, prefix="1.2.3.0/24", as_path=(55329, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=61568, prefix="1.2.3.0/24", as_path=(61568, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=61955, prefix="1.2.3.0/24", as_path=(61955, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=63927, prefix="1.2.3.0/24", as_path=(63927, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=199524, prefix="1.2.3.0/24", as_path=(199524, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=328832, prefix="1.2.3.0/24", as_path=(328832, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=398465, prefix="1.2.3.0/24", as_path=(398465, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=1680, prefix="1.2.3.0/24", as_path=(1680, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=2497, prefix="1.2.3.0/24", as_path=(2497, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=3235, prefix="1.2.3.0/24", as_path=(3235, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=3253, prefix="1.2.3.0/24", as_path=(3253, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=4637, prefix="1.2.3.0/24", as_path=(4637, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=4766, prefix="1.2.3.0/24", as_path=(4766, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=4788, prefix="1.2.3.0/24", as_path=(4788, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=5468, prefix="1.2.3.0/24", as_path=(5468, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=5473, prefix="1.2.3.0/24", as_path=(5473, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=5495, prefix="1.2.3.0/24", as_path=(5495, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=5589, prefix="1.2.3.0/24", as_path=(5589, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=6507, prefix="1.2.3.0/24", as_path=(6507, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=6820, prefix="1.2.3.0/24", as_path=(6820, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=6894, prefix="1.2.3.0/24", as_path=(6894, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=7979, prefix="1.2.3.0/24", as_path=(7979, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=8075, prefix="1.2.3.0/24", as_path=(8075, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=8299, prefix="1.2.3.0/24", as_path=(8299, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=8350, prefix="1.2.3.0/24", as_path=(8350, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=8359, prefix="1.2.3.0/24", as_path=(8359, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=8369, prefix="1.2.3.0/24", as_path=(8369, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=8371, prefix="1.2.3.0/24", as_path=(8371, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=8416, prefix="1.2.3.0/24", as_path=(8416, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=8491, prefix="1.2.3.0/24", as_path=(8491, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=8507, prefix="1.2.3.0/24", as_path=(8507, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=8595, prefix="1.2.3.0/24", as_path=(8595, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=8662, prefix="1.2.3.0/24", as_path=(8662, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=8684, prefix="1.2.3.0/24", as_path=(8684, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=8781, prefix="1.2.3.0/24", as_path=(8781, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=8872, prefix="1.2.3.0/24", as_path=(8872, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=8888, prefix="1.2.3.0/24", as_path=(8888, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=8932, prefix="1.2.3.0/24", as_path=(8932, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=8966, prefix="1.2.3.0/24", as_path=(8966, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=9009, prefix="1.2.3.0/24", as_path=(9009, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=9049, prefix="1.2.3.0/24", as_path=(9049, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=9124, prefix="1.2.3.0/24", as_path=(9124, 3216, 29452)).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12418, prefix="1.2.3.0/24", as_path=(12418, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12440, prefix="1.2.3.0/24", as_path=(12440, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12543, prefix="1.2.3.0/24", as_path=(12543, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12686, prefix="1.2.3.0/24", as_path=(12686, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12695, prefix="1.2.3.0/24", as_path=(12695, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12737, prefix="1.2.3.0/24", as_path=(12737, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12874, prefix="1.2.3.0/24", as_path=(12874, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13105, prefix="1.2.3.0/24", as_path=(13105, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13192, prefix="1.2.3.0/24", as_path=(13192, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13227, prefix="1.2.3.0/24", as_path=(13227, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13257, prefix="1.2.3.0/24", as_path=(13257, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13296, prefix="1.2.3.0/24", as_path=(13296, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13335, prefix="1.2.3.0/24", as_path=(13335, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15412, prefix="1.2.3.0/24", as_path=(15412, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15672, prefix="1.2.3.0/24", as_path=(15672, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15682, prefix="1.2.3.0/24", as_path=(15682, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15707, prefix="1.2.3.0/24", as_path=(15707, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15850, prefix="1.2.3.0/24", as_path=(15850, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15868, prefix="1.2.3.0/24", as_path=(15868, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15886, prefix="1.2.3.0/24", as_path=(15886, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15913, prefix="1.2.3.0/24", as_path=(15913, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=16043, prefix="1.2.3.0/24", as_path=(16043, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=16143, prefix="1.2.3.0/24", as_path=(16143, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=16173, prefix="1.2.3.0/24", as_path=(16173, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=16249, prefix="1.2.3.0/24", as_path=(16249, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=16477, prefix="1.2.3.0/24", as_path=(16477, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20597, prefix="1.2.3.0/24", as_path=(20597, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20764, prefix="1.2.3.0/24", as_path=(20764, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20848, prefix="1.2.3.0/24", as_path=(20848, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20866, prefix="1.2.3.0/24", as_path=(20866, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20895, prefix="1.2.3.0/24", as_path=(20895, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20919, prefix="1.2.3.0/24", as_path=(20919, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20940, prefix="1.2.3.0/24", as_path=(20940, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21020, prefix="1.2.3.0/24", as_path=(21020, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21030, prefix="1.2.3.0/24", as_path=(21030, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21184, prefix="1.2.3.0/24", as_path=(21184, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21332, prefix="1.2.3.0/24", as_path=(21332, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21446, prefix="1.2.3.0/24", as_path=(21446, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21483, prefix="1.2.3.0/24", as_path=(21483, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21859, prefix="1.2.3.0/24", as_path=(21859, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24638, prefix="1.2.3.0/24", as_path=(24638, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24739, prefix="1.2.3.0/24", as_path=(24739, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24787, prefix="1.2.3.0/24", as_path=(24787, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24811, prefix="1.2.3.0/24", as_path=(24811, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24823, prefix="1.2.3.0/24", as_path=(24823, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24832, prefix="1.2.3.0/24", as_path=(24832, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24837, prefix="1.2.3.0/24", as_path=(24837, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25355, prefix="1.2.3.0/24", as_path=(25355, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25437, prefix="1.2.3.0/24", as_path=(25437, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25549, prefix="1.2.3.0/24", as_path=(25549, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25592, prefix="1.2.3.0/24", as_path=(25592, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=27263, prefix="1.2.3.0/24", as_path=(27263, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=28703, prefix="1.2.3.0/24", as_path=(28703, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=28736, prefix="1.2.3.0/24", as_path=(28736, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=28775, prefix="1.2.3.0/24", as_path=(28775, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=28910, prefix="1.2.3.0/24", as_path=(28910, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=28989, prefix="1.2.3.0/24", as_path=(28989, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29041, prefix="1.2.3.0/24", as_path=(29041, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29071, prefix="1.2.3.0/24", as_path=(29071, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29076, prefix="1.2.3.0/24", as_path=(29076, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29125, prefix="1.2.3.0/24", as_path=(29125, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29226, prefix="1.2.3.0/24", as_path=(29226, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29554, prefix="1.2.3.0/24", as_path=(29554, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=30767, prefix="1.2.3.0/24", as_path=(30767, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=30831, prefix="1.2.3.0/24", as_path=(30831, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=30835, prefix="1.2.3.0/24", as_path=(30835, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=30943, prefix="1.2.3.0/24", as_path=(30943, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=30960, prefix="1.2.3.0/24", as_path=(30960, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31028, prefix="1.2.3.0/24", as_path=(31028, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31059, prefix="1.2.3.0/24", as_path=(31059, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31257, prefix="1.2.3.0/24", as_path=(31257, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31357, prefix="1.2.3.0/24", as_path=(31357, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31368, prefix="1.2.3.0/24", as_path=(31368, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31425, prefix="1.2.3.0/24", as_path=(31425, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31430, prefix="1.2.3.0/24", as_path=(31430, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31499, prefix="1.2.3.0/24", as_path=(31499, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31500, prefix="1.2.3.0/24", as_path=(31500, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=33819, prefix="1.2.3.0/24", as_path=(33819, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=33871, prefix="1.2.3.0/24", as_path=(33871, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=33891, prefix="1.2.3.0/24", as_path=(33891, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=33991, prefix="1.2.3.0/24", as_path=(33991, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34038, prefix="1.2.3.0/24", as_path=(34038, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34085, prefix="1.2.3.0/24", as_path=(34085, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34098, prefix="1.2.3.0/24", as_path=(34098, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34147, prefix="1.2.3.0/24", as_path=(34147, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34241, prefix="1.2.3.0/24", as_path=(34241, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34303, prefix="1.2.3.0/24", as_path=(34303, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34322, prefix="1.2.3.0/24", as_path=(34322, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34329, prefix="1.2.3.0/24", as_path=(34329, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34381, prefix="1.2.3.0/24", as_path=(34381, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34389, prefix="1.2.3.0/24", as_path=(34389, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34518, prefix="1.2.3.0/24", as_path=(34518, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34559, prefix="1.2.3.0/24", as_path=(34559, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34574, prefix="1.2.3.0/24", as_path=(34574, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34644, prefix="1.2.3.0/24", as_path=(34644, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34698, prefix="1.2.3.0/24", as_path=(34698, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34706, prefix="1.2.3.0/24", as_path=(34706, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34709, prefix="1.2.3.0/24", as_path=(34709, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34747, prefix="1.2.3.0/24", as_path=(34747, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34757, prefix="1.2.3.0/24", as_path=(34757, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34777, prefix="1.2.3.0/24", as_path=(34777, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34824, prefix="1.2.3.0/24", as_path=(34824, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34879, prefix="1.2.3.0/24", as_path=(34879, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34882, prefix="1.2.3.0/24", as_path=(34882, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34894, prefix="1.2.3.0/24", as_path=(34894, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35018, prefix="1.2.3.0/24", as_path=(35018, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35032, prefix="1.2.3.0/24", as_path=(35032, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35104, prefix="1.2.3.0/24", as_path=(35104, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35119, prefix="1.2.3.0/24", as_path=(35119, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35168, prefix="1.2.3.0/24", as_path=(35168, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35195, prefix="1.2.3.0/24", as_path=(35195, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35237, prefix="1.2.3.0/24", as_path=(35237, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35354, prefix="1.2.3.0/24", as_path=(35354, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35423, prefix="1.2.3.0/24", as_path=(35423, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35479, prefix="1.2.3.0/24", as_path=(35479, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35522, prefix="1.2.3.0/24", as_path=(35522, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35558, prefix="1.2.3.0/24", as_path=(35558, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35591, prefix="1.2.3.0/24", as_path=(35591, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35598, prefix="1.2.3.0/24", as_path=(35598, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35810, prefix="1.2.3.0/24", as_path=(35810, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=38917, prefix="1.2.3.0/24", as_path=(38917, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=38928, prefix="1.2.3.0/24", as_path=(38928, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=38934, prefix="1.2.3.0/24", as_path=(38934, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=38958, prefix="1.2.3.0/24", as_path=(38958, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39058, prefix="1.2.3.0/24", as_path=(39058, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39092, prefix="1.2.3.0/24", as_path=(39092, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39101, prefix="1.2.3.0/24", as_path=(39101, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39134, prefix="1.2.3.0/24", as_path=(39134, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39143, prefix="1.2.3.0/24", as_path=(39143, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39150, prefix="1.2.3.0/24", as_path=(39150, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39167, prefix="1.2.3.0/24", as_path=(39167, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39321, prefix="1.2.3.0/24", as_path=(39321, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39376, prefix="1.2.3.0/24", as_path=(39376, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39429, prefix="1.2.3.0/24", as_path=(39429, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39539, prefix="1.2.3.0/24", as_path=(39539, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39585, prefix="1.2.3.0/24", as_path=(39585, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39593, prefix="1.2.3.0/24", as_path=(39593, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39612, prefix="1.2.3.0/24", as_path=(39612, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39684, prefix="1.2.3.0/24", as_path=(39684, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39688, prefix="1.2.3.0/24", as_path=(39688, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39749, prefix="1.2.3.0/24", as_path=(39749, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39775, prefix="1.2.3.0/24", as_path=(39775, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39789, prefix="1.2.3.0/24", as_path=(39789, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39812, prefix="1.2.3.0/24", as_path=(39812, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39864, prefix="1.2.3.0/24", as_path=(39864, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39927, prefix="1.2.3.0/24", as_path=(39927, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41095, prefix="1.2.3.0/24", as_path=(41095, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41118, prefix="1.2.3.0/24", as_path=(41118, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41123, prefix="1.2.3.0/24", as_path=(41123, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41187, prefix="1.2.3.0/24", as_path=(41187, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41190, prefix="1.2.3.0/24", as_path=(41190, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41212, prefix="1.2.3.0/24", as_path=(41212, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41388, prefix="1.2.3.0/24", as_path=(41388, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41389, prefix="1.2.3.0/24", as_path=(41389, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41475, prefix="1.2.3.0/24", as_path=(41475, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41500, prefix="1.2.3.0/24", as_path=(41500, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41554, prefix="1.2.3.0/24", as_path=(41554, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41560, prefix="1.2.3.0/24", as_path=(41560, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41616, prefix="1.2.3.0/24", as_path=(41616, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41719, prefix="1.2.3.0/24", as_path=(41719, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41794, prefix="1.2.3.0/24", as_path=(41794, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41816, prefix="1.2.3.0/24", as_path=(41816, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41929, prefix="1.2.3.0/24", as_path=(41929, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41942, prefix="1.2.3.0/24", as_path=(41942, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42027, prefix="1.2.3.0/24", as_path=(42027, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42033, prefix="1.2.3.0/24", as_path=(42033, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42038, prefix="1.2.3.0/24", as_path=(42038, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42110, prefix="1.2.3.0/24", as_path=(42110, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42119, prefix="1.2.3.0/24", as_path=(42119, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42149, prefix="1.2.3.0/24", as_path=(42149, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42151, prefix="1.2.3.0/24", as_path=(42151, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42187, prefix="1.2.3.0/24", as_path=(42187, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42245, prefix="1.2.3.0/24", as_path=(42245, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42339, prefix="1.2.3.0/24", as_path=(42339, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42394, prefix="1.2.3.0/24", as_path=(42394, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42444, prefix="1.2.3.0/24", as_path=(42444, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42478, prefix="1.2.3.0/24", as_path=(42478, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42526, prefix="1.2.3.0/24", as_path=(42526, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42527, prefix="1.2.3.0/24", as_path=(42527, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42529, prefix="1.2.3.0/24", as_path=(42529, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42558, prefix="1.2.3.0/24", as_path=(42558, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42758, prefix="1.2.3.0/24", as_path=(42758, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42971, prefix="1.2.3.0/24", as_path=(42971, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43045, prefix="1.2.3.0/24", as_path=(43045, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43087, prefix="1.2.3.0/24", as_path=(43087, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43132, prefix="1.2.3.0/24", as_path=(43132, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43152, prefix="1.2.3.0/24", as_path=(43152, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43170, prefix="1.2.3.0/24", as_path=(43170, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43182, prefix="1.2.3.0/24", as_path=(43182, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43199, prefix="1.2.3.0/24", as_path=(43199, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43247, prefix="1.2.3.0/24", as_path=(43247, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43265, prefix="1.2.3.0/24", as_path=(43265, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43275, prefix="1.2.3.0/24", as_path=(43275, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43346, prefix="1.2.3.0/24", as_path=(43346, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43350, prefix="1.2.3.0/24", as_path=(43350, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43444, prefix="1.2.3.0/24", as_path=(43444, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43502, prefix="1.2.3.0/24", as_path=(43502, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43530, prefix="1.2.3.0/24", as_path=(43530, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43537, prefix="1.2.3.0/24", as_path=(43537, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43684, prefix="1.2.3.0/24", as_path=(43684, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43687, prefix="1.2.3.0/24", as_path=(43687, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43696, prefix="1.2.3.0/24", as_path=(43696, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43727, prefix="1.2.3.0/24", as_path=(43727, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43728, prefix="1.2.3.0/24", as_path=(43728, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43730, prefix="1.2.3.0/24", as_path=(43730, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43801, prefix="1.2.3.0/24", as_path=(43801, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43805, prefix="1.2.3.0/24", as_path=(43805, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43820, prefix="1.2.3.0/24", as_path=(43820, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43832, prefix="1.2.3.0/24", as_path=(43832, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43849, prefix="1.2.3.0/24", as_path=(43849, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43874, prefix="1.2.3.0/24", as_path=(43874, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43882, prefix="1.2.3.0/24", as_path=(43882, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43970, prefix="1.2.3.0/24", as_path=(43970, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43973, prefix="1.2.3.0/24", as_path=(43973, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44056, prefix="1.2.3.0/24", as_path=(44056, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44151, prefix="1.2.3.0/24", as_path=(44151, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44192, prefix="1.2.3.0/24", as_path=(44192, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44206, prefix="1.2.3.0/24", as_path=(44206, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44315, prefix="1.2.3.0/24", as_path=(44315, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44322, prefix="1.2.3.0/24", as_path=(44322, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44386, prefix="1.2.3.0/24", as_path=(44386, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44405, prefix="1.2.3.0/24", as_path=(44405, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44417, prefix="1.2.3.0/24", as_path=(44417, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44572, prefix="1.2.3.0/24", as_path=(44572, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44699, prefix="1.2.3.0/24", as_path=(44699, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44797, prefix="1.2.3.0/24", as_path=(44797, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44799, prefix="1.2.3.0/24", as_path=(44799, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44915, prefix="1.2.3.0/24", as_path=(44915, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44943, prefix="1.2.3.0/24", as_path=(44943, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=45003, prefix="1.2.3.0/24", as_path=(45003, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=45102, prefix="1.2.3.0/24", as_path=(45102, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47117, prefix="1.2.3.0/24", as_path=(47117, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47307, prefix="1.2.3.0/24", as_path=(47307, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47342, prefix="1.2.3.0/24", as_path=(47342, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47354, prefix="1.2.3.0/24", as_path=(47354, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47481, prefix="1.2.3.0/24", as_path=(47481, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47586, prefix="1.2.3.0/24", as_path=(47586, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47684, prefix="1.2.3.0/24", as_path=(47684, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47763, prefix="1.2.3.0/24", as_path=(47763, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47808, prefix="1.2.3.0/24", as_path=(47808, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47852, prefix="1.2.3.0/24", as_path=(47852, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47963, prefix="1.2.3.0/24", as_path=(47963, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48041, prefix="1.2.3.0/24", as_path=(48041, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48061, prefix="1.2.3.0/24", as_path=(48061, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48166, prefix="1.2.3.0/24", as_path=(48166, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48176, prefix="1.2.3.0/24", as_path=(48176, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48228, prefix="1.2.3.0/24", as_path=(48228, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48347, prefix="1.2.3.0/24", as_path=(48347, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48396, prefix="1.2.3.0/24", as_path=(48396, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48470, prefix="1.2.3.0/24", as_path=(48470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48477, prefix="1.2.3.0/24", as_path=(48477, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48479, prefix="1.2.3.0/24", as_path=(48479, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48485, prefix="1.2.3.0/24", as_path=(48485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48499, prefix="1.2.3.0/24", as_path=(48499, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48530, prefix="1.2.3.0/24", as_path=(48530, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48667, prefix="1.2.3.0/24", as_path=(48667, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48738, prefix="1.2.3.0/24", as_path=(48738, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48757, prefix="1.2.3.0/24", as_path=(48757, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48780, prefix="1.2.3.0/24", as_path=(48780, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48951, prefix="1.2.3.0/24", as_path=(48951, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48978, prefix="1.2.3.0/24", as_path=(48978, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49055, prefix="1.2.3.0/24", as_path=(49055, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49064, prefix="1.2.3.0/24", as_path=(49064, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49107, prefix="1.2.3.0/24", as_path=(49107, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49181, prefix="1.2.3.0/24", as_path=(49181, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49246, prefix="1.2.3.0/24", as_path=(49246, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49253, prefix="1.2.3.0/24", as_path=(49253, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49325, prefix="1.2.3.0/24", as_path=(49325, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49326, prefix="1.2.3.0/24", as_path=(49326, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49478, prefix="1.2.3.0/24", as_path=(49478, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49530, prefix="1.2.3.0/24", as_path=(49530, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49557, prefix="1.2.3.0/24", as_path=(49557, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49569, prefix="1.2.3.0/24", as_path=(49569, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49577, prefix="1.2.3.0/24", as_path=(49577, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49673, prefix="1.2.3.0/24", as_path=(49673, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49684, prefix="1.2.3.0/24", as_path=(49684, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49759, prefix="1.2.3.0/24", as_path=(49759, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49813, prefix="1.2.3.0/24", as_path=(49813, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49821, prefix="1.2.3.0/24", as_path=(49821, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49886, prefix="1.2.3.0/24", as_path=(49886, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49897, prefix="1.2.3.0/24", as_path=(49897, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49916, prefix="1.2.3.0/24", as_path=(49916, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49994, prefix="1.2.3.0/24", as_path=(49994, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50003, prefix="1.2.3.0/24", as_path=(50003, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50024, prefix="1.2.3.0/24", as_path=(50024, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50038, prefix="1.2.3.0/24", as_path=(50038, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50048, prefix="1.2.3.0/24", as_path=(50048, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50159, prefix="1.2.3.0/24", as_path=(50159, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50166, prefix="1.2.3.0/24", as_path=(50166, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50241, prefix="1.2.3.0/24", as_path=(50241, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50245, prefix="1.2.3.0/24", as_path=(50245, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50257, prefix="1.2.3.0/24", as_path=(50257, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50265, prefix="1.2.3.0/24", as_path=(50265, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50341, prefix="1.2.3.0/24", as_path=(50341, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50342, prefix="1.2.3.0/24", as_path=(50342, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50464, prefix="1.2.3.0/24", as_path=(50464, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50644, prefix="1.2.3.0/24", as_path=(50644, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50671, prefix="1.2.3.0/24", as_path=(50671, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50701, prefix="1.2.3.0/24", as_path=(50701, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50761, prefix="1.2.3.0/24", as_path=(50761, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50889, prefix="1.2.3.0/24", as_path=(50889, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50923, prefix="1.2.3.0/24", as_path=(50923, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51136, prefix="1.2.3.0/24", as_path=(51136, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51158, prefix="1.2.3.0/24", as_path=(51158, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51193, prefix="1.2.3.0/24", as_path=(51193, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51200, prefix="1.2.3.0/24", as_path=(51200, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51213, prefix="1.2.3.0/24", as_path=(51213, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51234, prefix="1.2.3.0/24", as_path=(51234, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51283, prefix="1.2.3.0/24", as_path=(51283, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51316, prefix="1.2.3.0/24", as_path=(51316, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51339, prefix="1.2.3.0/24", as_path=(51339, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51346, prefix="1.2.3.0/24", as_path=(51346, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51360, prefix="1.2.3.0/24", as_path=(51360, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51389, prefix="1.2.3.0/24", as_path=(51389, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51418, prefix="1.2.3.0/24", as_path=(51418, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51446, prefix="1.2.3.0/24", as_path=(51446, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51471, prefix="1.2.3.0/24", as_path=(51471, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51506, prefix="1.2.3.0/24", as_path=(51506, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51523, prefix="1.2.3.0/24", as_path=(51523, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51536, prefix="1.2.3.0/24", as_path=(51536, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51593, prefix="1.2.3.0/24", as_path=(51593, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51667, prefix="1.2.3.0/24", as_path=(51667, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51705, prefix="1.2.3.0/24", as_path=(51705, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51721, prefix="1.2.3.0/24", as_path=(51721, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51952, prefix="1.2.3.0/24", as_path=(51952, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51981, prefix="1.2.3.0/24", as_path=(51981, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=52006, prefix="1.2.3.0/24", as_path=(52006, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=52046, prefix="1.2.3.0/24", as_path=(52046, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=52047, prefix="1.2.3.0/24", as_path=(52047, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=52069, prefix="1.2.3.0/24", as_path=(52069, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=52096, prefix="1.2.3.0/24", as_path=(52096, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=52194, prefix="1.2.3.0/24", as_path=(52194, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=52198, prefix="1.2.3.0/24", as_path=(52198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=54994, prefix="1.2.3.0/24", as_path=(54994, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56340, prefix="1.2.3.0/24", as_path=(56340, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56383, prefix="1.2.3.0/24", as_path=(56383, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56384, prefix="1.2.3.0/24", as_path=(56384, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56392, prefix="1.2.3.0/24", as_path=(56392, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56440, prefix="1.2.3.0/24", as_path=(56440, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56445, prefix="1.2.3.0/24", as_path=(56445, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56483, prefix="1.2.3.0/24", as_path=(56483, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56535, prefix="1.2.3.0/24", as_path=(56535, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56541, prefix="1.2.3.0/24", as_path=(56541, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56542, prefix="1.2.3.0/24", as_path=(56542, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56562, prefix="1.2.3.0/24", as_path=(56562, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56618, prefix="1.2.3.0/24", as_path=(56618, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56634, prefix="1.2.3.0/24", as_path=(56634, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56679, prefix="1.2.3.0/24", as_path=(56679, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56685, prefix="1.2.3.0/24", as_path=(56685, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56689, prefix="1.2.3.0/24", as_path=(56689, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56701, prefix="1.2.3.0/24", as_path=(56701, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56776, prefix="1.2.3.0/24", as_path=(56776, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56820, prefix="1.2.3.0/24", as_path=(56820, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56879, prefix="1.2.3.0/24", as_path=(56879, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56936, prefix="1.2.3.0/24", as_path=(56936, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57108, prefix="1.2.3.0/24", as_path=(57108, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57174, prefix="1.2.3.0/24", as_path=(57174, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57212, prefix="1.2.3.0/24", as_path=(57212, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57274, prefix="1.2.3.0/24", as_path=(57274, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57296, prefix="1.2.3.0/24", as_path=(57296, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57363, prefix="1.2.3.0/24", as_path=(57363, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57372, prefix="1.2.3.0/24", as_path=(57372, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57380, prefix="1.2.3.0/24", as_path=(57380, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57494, prefix="1.2.3.0/24", as_path=(57494, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57503, prefix="1.2.3.0/24", as_path=(57503, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57512, prefix="1.2.3.0/24", as_path=(57512, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57580, prefix="1.2.3.0/24", as_path=(57580, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57609, prefix="1.2.3.0/24", as_path=(57609, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57631, prefix="1.2.3.0/24", as_path=(57631, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57658, prefix="1.2.3.0/24", as_path=(57658, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57671, prefix="1.2.3.0/24", as_path=(57671, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57683, prefix="1.2.3.0/24", as_path=(57683, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57711, prefix="1.2.3.0/24", as_path=(57711, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57798, prefix="1.2.3.0/24", as_path=(57798, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57828, prefix="1.2.3.0/24", as_path=(57828, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57843, prefix="1.2.3.0/24", as_path=(57843, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57871, prefix="1.2.3.0/24", as_path=(57871, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57876, prefix="1.2.3.0/24", as_path=(57876, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58071, prefix="1.2.3.0/24", as_path=(58071, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58086, prefix="1.2.3.0/24", as_path=(58086, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58136, prefix="1.2.3.0/24", as_path=(58136, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58147, prefix="1.2.3.0/24", as_path=(58147, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58163, prefix="1.2.3.0/24", as_path=(58163, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58187, prefix="1.2.3.0/24", as_path=(58187, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58194, prefix="1.2.3.0/24", as_path=(58194, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58225, prefix="1.2.3.0/24", as_path=(58225, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58310, prefix="1.2.3.0/24", as_path=(58310, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59416, prefix="1.2.3.0/24", as_path=(59416, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59465, prefix="1.2.3.0/24", as_path=(59465, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59483, prefix="1.2.3.0/24", as_path=(59483, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59494, prefix="1.2.3.0/24", as_path=(59494, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59509, prefix="1.2.3.0/24", as_path=(59509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59525, prefix="1.2.3.0/24", as_path=(59525, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59549, prefix="1.2.3.0/24", as_path=(59549, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59604, prefix="1.2.3.0/24", as_path=(59604, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59605, prefix="1.2.3.0/24", as_path=(59605, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59614, prefix="1.2.3.0/24", as_path=(59614, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59640, prefix="1.2.3.0/24", as_path=(59640, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59667, prefix="1.2.3.0/24", as_path=(59667, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59722, prefix="1.2.3.0/24", as_path=(59722, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59825, prefix="1.2.3.0/24", as_path=(59825, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59986, prefix="1.2.3.0/24", as_path=(59986, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60048, prefix="1.2.3.0/24", as_path=(60048, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60075, prefix="1.2.3.0/24", as_path=(60075, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60095, prefix="1.2.3.0/24", as_path=(60095, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60102, prefix="1.2.3.0/24", as_path=(60102, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60108, prefix="1.2.3.0/24", as_path=(60108, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60119, prefix="1.2.3.0/24", as_path=(60119, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60122, prefix="1.2.3.0/24", as_path=(60122, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60172, prefix="1.2.3.0/24", as_path=(60172, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60177, prefix="1.2.3.0/24", as_path=(60177, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60328, prefix="1.2.3.0/24", as_path=(60328, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60575, prefix="1.2.3.0/24", as_path=(60575, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60684, prefix="1.2.3.0/24", as_path=(60684, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60764, prefix="1.2.3.0/24", as_path=(60764, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60771, prefix="1.2.3.0/24", as_path=(60771, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60832, prefix="1.2.3.0/24", as_path=(60832, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60833, prefix="1.2.3.0/24", as_path=(60833, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60835, prefix="1.2.3.0/24", as_path=(60835, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60864, prefix="1.2.3.0/24", as_path=(60864, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60879, prefix="1.2.3.0/24", as_path=(60879, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60957, prefix="1.2.3.0/24", as_path=(60957, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61039, prefix="1.2.3.0/24", as_path=(61039, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61052, prefix="1.2.3.0/24", as_path=(61052, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61111, prefix="1.2.3.0/24", as_path=(61111, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61324, prefix="1.2.3.0/24", as_path=(61324, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61360, prefix="1.2.3.0/24", as_path=(61360, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61372, prefix="1.2.3.0/24", as_path=(61372, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61390, prefix="1.2.3.0/24", as_path=(61390, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61411, prefix="1.2.3.0/24", as_path=(61411, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61980, prefix="1.2.3.0/24", as_path=(61980, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61991, prefix="1.2.3.0/24", as_path=(61991, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62008, prefix="1.2.3.0/24", as_path=(62008, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62069, prefix="1.2.3.0/24", as_path=(62069, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62103, prefix="1.2.3.0/24", as_path=(62103, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62218, prefix="1.2.3.0/24", as_path=(62218, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62272, prefix="1.2.3.0/24", as_path=(62272, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62316, prefix="1.2.3.0/24", as_path=(62316, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62404, prefix="1.2.3.0/24", as_path=(62404, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62423, prefix="1.2.3.0/24", as_path=(62423, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=63258, prefix="1.2.3.0/24", as_path=(63258, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=64492, prefix="1.2.3.0/24", as_path=(64492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=138322, prefix="1.2.3.0/24", as_path=(138322, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=196657, prefix="1.2.3.0/24", as_path=(196657, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=196768, prefix="1.2.3.0/24", as_path=(196768, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=196847, prefix="1.2.3.0/24", as_path=(196847, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=196850, prefix="1.2.3.0/24", as_path=(196850, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197062, prefix="1.2.3.0/24", as_path=(197062, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197084, prefix="1.2.3.0/24", as_path=(197084, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197311, prefix="1.2.3.0/24", as_path=(197311, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197315, prefix="1.2.3.0/24", as_path=(197315, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197394, prefix="1.2.3.0/24", as_path=(197394, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197574, prefix="1.2.3.0/24", as_path=(197574, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197756, prefix="1.2.3.0/24", as_path=(197756, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197760, prefix="1.2.3.0/24", as_path=(197760, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197857, prefix="1.2.3.0/24", as_path=(197857, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197878, prefix="1.2.3.0/24", as_path=(197878, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197888, prefix="1.2.3.0/24", as_path=(197888, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198086, prefix="1.2.3.0/24", as_path=(198086, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198212, prefix="1.2.3.0/24", as_path=(198212, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198255, prefix="1.2.3.0/24", as_path=(198255, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198502, prefix="1.2.3.0/24", as_path=(198502, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198716, prefix="1.2.3.0/24", as_path=(198716, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198826, prefix="1.2.3.0/24", as_path=(198826, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198873, prefix="1.2.3.0/24", as_path=(198873, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199014, prefix="1.2.3.0/24", as_path=(199014, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199120, prefix="1.2.3.0/24", as_path=(199120, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199179, prefix="1.2.3.0/24", as_path=(199179, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199261, prefix="1.2.3.0/24", as_path=(199261, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199316, prefix="1.2.3.0/24", as_path=(199316, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199317, prefix="1.2.3.0/24", as_path=(199317, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199463, prefix="1.2.3.0/24", as_path=(199463, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199524, prefix="1.2.3.0/24", as_path=(199524, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199599, prefix="1.2.3.0/24", as_path=(199599, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199602, prefix="1.2.3.0/24", as_path=(199602, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199728, prefix="1.2.3.0/24", as_path=(199728, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199862, prefix="1.2.3.0/24", as_path=(199862, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200095, prefix="1.2.3.0/24", as_path=(200095, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200152, prefix="1.2.3.0/24", as_path=(200152, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200350, prefix="1.2.3.0/24", as_path=(200350, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200473, prefix="1.2.3.0/24", as_path=(200473, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200575, prefix="1.2.3.0/24", as_path=(200575, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200662, prefix="1.2.3.0/24", as_path=(200662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200982, prefix="1.2.3.0/24", as_path=(200982, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201123, prefix="1.2.3.0/24", as_path=(201123, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201137, prefix="1.2.3.0/24", as_path=(201137, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201147, prefix="1.2.3.0/24", as_path=(201147, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201250, prefix="1.2.3.0/24", as_path=(201250, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201270, prefix="1.2.3.0/24", as_path=(201270, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201282, prefix="1.2.3.0/24", as_path=(201282, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201394, prefix="1.2.3.0/24", as_path=(201394, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201452, prefix="1.2.3.0/24", as_path=(201452, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201468, prefix="1.2.3.0/24", as_path=(201468, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201556, prefix="1.2.3.0/24", as_path=(201556, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201570, prefix="1.2.3.0/24", as_path=(201570, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201571, prefix="1.2.3.0/24", as_path=(201571, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201593, prefix="1.2.3.0/24", as_path=(201593, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201804, prefix="1.2.3.0/24", as_path=(201804, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201858, prefix="1.2.3.0/24", as_path=(201858, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201861, prefix="1.2.3.0/24", as_path=(201861, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202136, prefix="1.2.3.0/24", as_path=(202136, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202156, prefix="1.2.3.0/24", as_path=(202156, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202164, prefix="1.2.3.0/24", as_path=(202164, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202202, prefix="1.2.3.0/24", as_path=(202202, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202486, prefix="1.2.3.0/24", as_path=(202486, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202493, prefix="1.2.3.0/24", as_path=(202493, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202700, prefix="1.2.3.0/24", as_path=(202700, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202734, prefix="1.2.3.0/24", as_path=(202734, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202752, prefix="1.2.3.0/24", as_path=(202752, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202758, prefix="1.2.3.0/24", as_path=(202758, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202760, prefix="1.2.3.0/24", as_path=(202760, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202768, prefix="1.2.3.0/24", as_path=(202768, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202802, prefix="1.2.3.0/24", as_path=(202802, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202871, prefix="1.2.3.0/24", as_path=(202871, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202873, prefix="1.2.3.0/24", as_path=(202873, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202934, prefix="1.2.3.0/24", as_path=(202934, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202984, prefix="1.2.3.0/24", as_path=(202984, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202999, prefix="1.2.3.0/24", as_path=(202999, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203054, prefix="1.2.3.0/24", as_path=(203054, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203163, prefix="1.2.3.0/24", as_path=(203163, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203190, prefix="1.2.3.0/24", as_path=(203190, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203203, prefix="1.2.3.0/24", as_path=(203203, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203514, prefix="1.2.3.0/24", as_path=(203514, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203517, prefix="1.2.3.0/24", as_path=(203517, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203542, prefix="1.2.3.0/24", as_path=(203542, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203599, prefix="1.2.3.0/24", as_path=(203599, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203747, prefix="1.2.3.0/24", as_path=(203747, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203972, prefix="1.2.3.0/24", as_path=(203972, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204102, prefix="1.2.3.0/24", as_path=(204102, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204238, prefix="1.2.3.0/24", as_path=(204238, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204296, prefix="1.2.3.0/24", as_path=(204296, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204298, prefix="1.2.3.0/24", as_path=(204298, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204304, prefix="1.2.3.0/24", as_path=(204304, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204507, prefix="1.2.3.0/24", as_path=(204507, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204720, prefix="1.2.3.0/24", as_path=(204720, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204738, prefix="1.2.3.0/24", as_path=(204738, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204752, prefix="1.2.3.0/24", as_path=(204752, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204833, prefix="1.2.3.0/24", as_path=(204833, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204910, prefix="1.2.3.0/24", as_path=(204910, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205047, prefix="1.2.3.0/24", as_path=(205047, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205460, prefix="1.2.3.0/24", as_path=(205460, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205682, prefix="1.2.3.0/24", as_path=(205682, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205720, prefix="1.2.3.0/24", as_path=(205720, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205963, prefix="1.2.3.0/24", as_path=(205963, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206011, prefix="1.2.3.0/24", as_path=(206011, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206069, prefix="1.2.3.0/24", as_path=(206069, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206171, prefix="1.2.3.0/24", as_path=(206171, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206179, prefix="1.2.3.0/24", as_path=(206179, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206323, prefix="1.2.3.0/24", as_path=(206323, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206333, prefix="1.2.3.0/24", as_path=(206333, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206538, prefix="1.2.3.0/24", as_path=(206538, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206661, prefix="1.2.3.0/24", as_path=(206661, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206673, prefix="1.2.3.0/24", as_path=(206673, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206728, prefix="1.2.3.0/24", as_path=(206728, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206846, prefix="1.2.3.0/24", as_path=(206846, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207078, prefix="1.2.3.0/24", as_path=(207078, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207228, prefix="1.2.3.0/24", as_path=(207228, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207353, prefix="1.2.3.0/24", as_path=(207353, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207382, prefix="1.2.3.0/24", as_path=(207382, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207438, prefix="1.2.3.0/24", as_path=(207438, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207501, prefix="1.2.3.0/24", as_path=(207501, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207518, prefix="1.2.3.0/24", as_path=(207518, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207547, prefix="1.2.3.0/24", as_path=(207547, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207634, prefix="1.2.3.0/24", as_path=(207634, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207859, prefix="1.2.3.0/24", as_path=(207859, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208087, prefix="1.2.3.0/24", as_path=(208087, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208155, prefix="1.2.3.0/24", as_path=(208155, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208177, prefix="1.2.3.0/24", as_path=(208177, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208303, prefix="1.2.3.0/24", as_path=(208303, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208349, prefix="1.2.3.0/24", as_path=(208349, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208388, prefix="1.2.3.0/24", as_path=(208388, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208541, prefix="1.2.3.0/24", as_path=(208541, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208629, prefix="1.2.3.0/24", as_path=(208629, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208811, prefix="1.2.3.0/24", as_path=(208811, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208955, prefix="1.2.3.0/24", as_path=(208955, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208977, prefix="1.2.3.0/24", as_path=(208977, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209005, prefix="1.2.3.0/24", as_path=(209005, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209206, prefix="1.2.3.0/24", as_path=(209206, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209284, prefix="1.2.3.0/24", as_path=(209284, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209456, prefix="1.2.3.0/24", as_path=(209456, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209599, prefix="1.2.3.0/24", as_path=(209599, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209684, prefix="1.2.3.0/24", as_path=(209684, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209739, prefix="1.2.3.0/24", as_path=(209739, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209779, prefix="1.2.3.0/24", as_path=(209779, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210109, prefix="1.2.3.0/24", as_path=(210109, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210720, prefix="1.2.3.0/24", as_path=(210720, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210889, prefix="1.2.3.0/24", as_path=(210889, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211164, prefix="1.2.3.0/24", as_path=(211164, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211609, prefix="1.2.3.0/24", as_path=(211609, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211618, prefix="1.2.3.0/24", as_path=(211618, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211625, prefix="1.2.3.0/24", as_path=(211625, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211641, prefix="1.2.3.0/24", as_path=(211641, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211697, prefix="1.2.3.0/24", as_path=(211697, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211762, prefix="1.2.3.0/24", as_path=(211762, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212275, prefix="1.2.3.0/24", as_path=(212275, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212410, prefix="1.2.3.0/24", as_path=(212410, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212414, prefix="1.2.3.0/24", as_path=(212414, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212421, prefix="1.2.3.0/24", as_path=(212421, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212614, prefix="1.2.3.0/24", as_path=(212614, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212713, prefix="1.2.3.0/24", as_path=(212713, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212748, prefix="1.2.3.0/24", as_path=(212748, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212750, prefix="1.2.3.0/24", as_path=(212750, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212959, prefix="1.2.3.0/24", as_path=(212959, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=213041, prefix="1.2.3.0/24", as_path=(213041, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=213075, prefix="1.2.3.0/24", as_path=(213075, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=213077, prefix="1.2.3.0/24", as_path=(213077, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=213348, prefix="1.2.3.0/24", as_path=(213348, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=213381, prefix="1.2.3.0/24", as_path=(213381, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=5433, prefix="1.2.3.0/24", as_path=(5433, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8732, prefix="1.2.3.0/24", as_path=(8732, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=9049, prefix="1.2.3.0/24", as_path=(9049, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13215, prefix="1.2.3.0/24", as_path=(13215, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25532, prefix="1.2.3.0/24", as_path=(25532, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31133, prefix="1.2.3.0/24", as_path=(31133, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34665, prefix="1.2.3.0/24", as_path=(34665, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35640, prefix="1.2.3.0/24", as_path=(35640, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41909, prefix="1.2.3.0/24", as_path=(41909, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42149, prefix="1.2.3.0/24", as_path=(42149, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42511, prefix="1.2.3.0/24", as_path=(42511, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43106, prefix="1.2.3.0/24", as_path=(43106, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=45054, prefix="1.2.3.0/24", as_path=(45054, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47363, prefix="1.2.3.0/24", as_path=(47363, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48416, prefix="1.2.3.0/24", as_path=(48416, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48558, prefix="1.2.3.0/24", as_path=(48558, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48763, prefix="1.2.3.0/24", as_path=(48763, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48781, prefix="1.2.3.0/24", as_path=(48781, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49106, prefix="1.2.3.0/24", as_path=(49106, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50488, prefix="1.2.3.0/24", as_path=(50488, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50538, prefix="1.2.3.0/24", as_path=(50538, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51178, prefix="1.2.3.0/24", as_path=(51178, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51601, prefix="1.2.3.0/24", as_path=(51601, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57246, prefix="1.2.3.0/24", as_path=(57246, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60771, prefix="1.2.3.0/24", as_path=(60771, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62251, prefix="1.2.3.0/24", as_path=(62251, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=196750, prefix="1.2.3.0/24", as_path=(196750, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=196938, prefix="1.2.3.0/24", as_path=(196938, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198610, prefix="1.2.3.0/24", as_path=(198610, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205226, prefix="1.2.3.0/24", as_path=(205226, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205460, prefix="1.2.3.0/24", as_path=(205460, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206804, prefix="1.2.3.0/24", as_path=(206804, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208056, prefix="1.2.3.0/24", as_path=(208056, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208825, prefix="1.2.3.0/24", as_path=(208825, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208992, prefix="1.2.3.0/24", as_path=(208992, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=267712, prefix="1.2.3.0/24", as_path=(267712, 50509, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(reporting_asn=42, prefix="1.2.3.0/24", as_path=(42, 4455, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=714, prefix="1.2.3.0/24", as_path=(714, 4455, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=2110, prefix="1.2.3.0/24", as_path=(2110, 4455, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=2686, prefix="1.2.3.0/24", as_path=(2686, 4455, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=2906, prefix="1.2.3.0/24", as_path=(2906, 4455, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=3262, prefix="1.2.3.0/24", as_path=(3262, 4455, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=6853, prefix="1.2.3.0/24", as_path=(6853, 4455, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=6895, prefix="1.2.3.0/24", as_path=(6895, 4455, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=8262, prefix="1.2.3.0/24", as_path=(8262, 4455, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=8764, prefix="1.2.3.0/24", as_path=(8764, 4455, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=8781, prefix="1.2.3.0/24", as_path=(8781, 4455, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=8851, prefix="1.2.3.0/24", as_path=(8851, 4455, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=8932, prefix="1.2.3.0/24", as_path=(8932, 4455, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=9009, prefix="1.2.3.0/24", as_path=(9009, 4455, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=9498, prefix="1.2.3.0/24", as_path=(9498, 4455, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=9583, prefix="1.2.3.0/24", as_path=(9583, 4455, 29452)).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12387, prefix="1.2.3.0/24", as_path=(12387, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12390, prefix="1.2.3.0/24", as_path=(12390, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12430, prefix="1.2.3.0/24", as_path=(12430, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12536, prefix="1.2.3.0/24", as_path=(12536, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13037, prefix="1.2.3.0/24", as_path=(13037, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13280, prefix="1.2.3.0/24", as_path=(13280, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13335, prefix="1.2.3.0/24", as_path=(13335, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=14340, prefix="1.2.3.0/24", as_path=(14340, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15401, prefix="1.2.3.0/24", as_path=(15401, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15547, prefix="1.2.3.0/24", as_path=(15547, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15557, prefix="1.2.3.0/24", as_path=(15557, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15695, prefix="1.2.3.0/24", as_path=(15695, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15699, prefix="1.2.3.0/24", as_path=(15699, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=16168, prefix="1.2.3.0/24", as_path=(16168, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=16171, prefix="1.2.3.0/24", as_path=(16171, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=16247, prefix="1.2.3.0/24", as_path=(16247, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=16509, prefix="1.2.3.0/24", as_path=(16509, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=19551, prefix="1.2.3.0/24", as_path=(19551, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=19679, prefix="1.2.3.0/24", as_path=(19679, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20326, prefix="1.2.3.0/24", as_path=(20326, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20917, prefix="1.2.3.0/24", as_path=(20917, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20940, prefix="1.2.3.0/24", as_path=(20940, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=22822, prefix="1.2.3.0/24", as_path=(22822, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=23316, prefix="1.2.3.0/24", as_path=(23316, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24633, prefix="1.2.3.0/24", as_path=(24633, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24768, prefix="1.2.3.0/24", as_path=(24768, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24904, prefix="1.2.3.0/24", as_path=(24904, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25003, prefix="1.2.3.0/24", as_path=(25003, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25061, prefix="1.2.3.0/24", as_path=(25061, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25582, prefix="1.2.3.0/24", as_path=(25582, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=28695, prefix="1.2.3.0/24", as_path=(28695, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=28768, prefix="1.2.3.0/24", as_path=(28768, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29076, prefix="1.2.3.0/24", as_path=(29076, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29119, prefix="1.2.3.0/24", as_path=(29119, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29169, prefix="1.2.3.0/24", as_path=(29169, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29301, prefix="1.2.3.0/24", as_path=(29301, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29646, prefix="1.2.3.0/24", as_path=(29646, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31019, prefix="1.2.3.0/24", as_path=(31019, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31042, prefix="1.2.3.0/24", as_path=(31042, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31084, prefix="1.2.3.0/24", as_path=(31084, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31655, prefix="1.2.3.0/24", as_path=(31655, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=32402, prefix="1.2.3.0/24", as_path=(32402, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=32934, prefix="1.2.3.0/24", as_path=(32934, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=33920, prefix="1.2.3.0/24", as_path=(33920, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=33941, prefix="1.2.3.0/24", as_path=(33941, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35064, prefix="1.2.3.0/24", as_path=(35064, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35223, prefix="1.2.3.0/24", as_path=(35223, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35482, prefix="1.2.3.0/24", as_path=(35482, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35676, prefix="1.2.3.0/24", as_path=(35676, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=38016, prefix="1.2.3.0/24", as_path=(38016, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39072, prefix="1.2.3.0/24", as_path=(39072, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39875, prefix="1.2.3.0/24", as_path=(39875, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41495, prefix="1.2.3.0/24", as_path=(41495, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41669, prefix="1.2.3.0/24", as_path=(41669, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42004, prefix="1.2.3.0/24", as_path=(42004, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42090, prefix="1.2.3.0/24", as_path=(42090, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42227, prefix="1.2.3.0/24", as_path=(42227, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42228, prefix="1.2.3.0/24", as_path=(42228, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42929, prefix="1.2.3.0/24", as_path=(42929, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43192, prefix="1.2.3.0/24", as_path=(43192, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43271, prefix="1.2.3.0/24", as_path=(43271, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43406, prefix="1.2.3.0/24", as_path=(43406, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43408, prefix="1.2.3.0/24", as_path=(43408, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43424, prefix="1.2.3.0/24", as_path=(43424, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43833, prefix="1.2.3.0/24", as_path=(43833, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43885, prefix="1.2.3.0/24", as_path=(43885, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43984, prefix="1.2.3.0/24", as_path=(43984, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44212, prefix="1.2.3.0/24", as_path=(44212, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47049, prefix="1.2.3.0/24", as_path=(47049, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47172, prefix="1.2.3.0/24", as_path=(47172, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47704, prefix="1.2.3.0/24", as_path=(47704, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47762, prefix="1.2.3.0/24", as_path=(47762, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47820, prefix="1.2.3.0/24", as_path=(47820, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47942, prefix="1.2.3.0/24", as_path=(47942, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48072, prefix="1.2.3.0/24", as_path=(48072, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48294, prefix="1.2.3.0/24", as_path=(48294, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48804, prefix="1.2.3.0/24", as_path=(48804, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48954, prefix="1.2.3.0/24", as_path=(48954, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49127, prefix="1.2.3.0/24", as_path=(49127, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49354, prefix="1.2.3.0/24", as_path=(49354, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50088, prefix="1.2.3.0/24", as_path=(50088, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50314, prefix="1.2.3.0/24", as_path=(50314, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51043, prefix="1.2.3.0/24", as_path=(51043, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51059, prefix="1.2.3.0/24", as_path=(51059, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51677, prefix="1.2.3.0/24", as_path=(51677, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=52092, prefix="1.2.3.0/24", as_path=(52092, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=52580, prefix="1.2.3.0/24", as_path=(52580, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=53264, prefix="1.2.3.0/24", as_path=(53264, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=54113, prefix="1.2.3.0/24", as_path=(54113, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56595, prefix="1.2.3.0/24", as_path=(56595, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56767, prefix="1.2.3.0/24", as_path=(56767, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57168, prefix="1.2.3.0/24", as_path=(57168, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57877, prefix="1.2.3.0/24", as_path=(57877, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59445, prefix="1.2.3.0/24", as_path=(59445, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59717, prefix="1.2.3.0/24", as_path=(59717, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60277, prefix="1.2.3.0/24", as_path=(60277, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60333, prefix="1.2.3.0/24", as_path=(60333, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60426, prefix="1.2.3.0/24", as_path=(60426, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60572, prefix="1.2.3.0/24", as_path=(60572, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60595, prefix="1.2.3.0/24", as_path=(60595, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60653, prefix="1.2.3.0/24", as_path=(60653, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60737, prefix="1.2.3.0/24", as_path=(60737, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61049, prefix="1.2.3.0/24", as_path=(61049, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61193, prefix="1.2.3.0/24", as_path=(61193, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62001, prefix="1.2.3.0/24", as_path=(62001, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62044, prefix="1.2.3.0/24", as_path=(62044, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62832, prefix="1.2.3.0/24", as_path=(62832, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=63226, prefix="1.2.3.0/24", as_path=(63226, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=63287, prefix="1.2.3.0/24", as_path=(63287, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=63311, prefix="1.2.3.0/24", as_path=(63311, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197033, prefix="1.2.3.0/24", as_path=(197033, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197036, prefix="1.2.3.0/24", as_path=(197036, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197692, prefix="1.2.3.0/24", as_path=(197692, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198330, prefix="1.2.3.0/24", as_path=(198330, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198507, prefix="1.2.3.0/24", as_path=(198507, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199121, prefix="1.2.3.0/24", as_path=(199121, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199256, prefix="1.2.3.0/24", as_path=(199256, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199346, prefix="1.2.3.0/24", as_path=(199346, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199422, prefix="1.2.3.0/24", as_path=(199422, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199468, prefix="1.2.3.0/24", as_path=(199468, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200425, prefix="1.2.3.0/24", as_path=(200425, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200434, prefix="1.2.3.0/24", as_path=(200434, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200565, prefix="1.2.3.0/24", as_path=(200565, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200751, prefix="1.2.3.0/24", as_path=(200751, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200845, prefix="1.2.3.0/24", as_path=(200845, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201506, prefix="1.2.3.0/24", as_path=(201506, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201971, prefix="1.2.3.0/24", as_path=(201971, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202096, prefix="1.2.3.0/24", as_path=(202096, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202253, prefix="1.2.3.0/24", as_path=(202253, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202695, prefix="1.2.3.0/24", as_path=(202695, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203058, prefix="1.2.3.0/24", as_path=(203058, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203421, prefix="1.2.3.0/24", as_path=(203421, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203544, prefix="1.2.3.0/24", as_path=(203544, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203754, prefix="1.2.3.0/24", as_path=(203754, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204536, prefix="1.2.3.0/24", as_path=(204536, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205019, prefix="1.2.3.0/24", as_path=(205019, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205402, prefix="1.2.3.0/24", as_path=(205402, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205917, prefix="1.2.3.0/24", as_path=(205917, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206104, prefix="1.2.3.0/24", as_path=(206104, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206324, prefix="1.2.3.0/24", as_path=(206324, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208569, prefix="1.2.3.0/24", as_path=(208569, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209082, prefix="1.2.3.0/24", as_path=(209082, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209333, prefix="1.2.3.0/24", as_path=(209333, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209336, prefix="1.2.3.0/24", as_path=(209336, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209453, prefix="1.2.3.0/24", as_path=(209453, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209505, prefix="1.2.3.0/24", as_path=(209505, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209627, prefix="1.2.3.0/24", as_path=(209627, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210232, prefix="1.2.3.0/24", as_path=(210232, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211826, prefix="1.2.3.0/24", as_path=(211826, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212228, prefix="1.2.3.0/24", as_path=(212228, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212551, prefix="1.2.3.0/24", as_path=(212551, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212581, prefix="1.2.3.0/24", as_path=(212581, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212633, prefix="1.2.3.0/24", as_path=(212633, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212694, prefix="1.2.3.0/24", as_path=(212694, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212755, prefix="1.2.3.0/24", as_path=(212755, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=213035, prefix="1.2.3.0/24", as_path=(213035, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=213150, prefix="1.2.3.0/24", as_path=(213150, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=263009, prefix="1.2.3.0/24", as_path=(263009, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=394651, prefix="1.2.3.0/24", as_path=(394651, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=396986, prefix="1.2.3.0/24", as_path=(396986, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=2585, prefix="1.2.3.0/24", as_path=(2585, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=2854, prefix="1.2.3.0/24", as_path=(2854, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=3181, prefix="1.2.3.0/24", as_path=(3181, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=3203, prefix="1.2.3.0/24", as_path=(3203, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=3327, prefix="1.2.3.0/24", as_path=(3327, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=4809, prefix="1.2.3.0/24", as_path=(4809, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=5553, prefix="1.2.3.0/24", as_path=(5553, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=5589, prefix="1.2.3.0/24", as_path=(5589, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=6856, prefix="1.2.3.0/24", as_path=(6856, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8369, prefix="1.2.3.0/24", as_path=(8369, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8427, prefix="1.2.3.0/24", as_path=(8427, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8641, prefix="1.2.3.0/24", as_path=(8641, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8712, prefix="1.2.3.0/24", as_path=(8712, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8749, prefix="1.2.3.0/24", as_path=(8749, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8764, prefix="1.2.3.0/24", as_path=(8764, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8774, prefix="1.2.3.0/24", as_path=(8774, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8848, prefix="1.2.3.0/24", as_path=(8848, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8985, prefix="1.2.3.0/24", as_path=(8985, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=9049, prefix="1.2.3.0/24", as_path=(9049, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=9077, prefix="1.2.3.0/24", as_path=(9077, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=9122, prefix="1.2.3.0/24", as_path=(9122, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=9177, prefix="1.2.3.0/24", as_path=(9177, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12418, prefix="1.2.3.0/24", as_path=(12418, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12555, prefix="1.2.3.0/24", as_path=(12555, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12764, prefix="1.2.3.0/24", as_path=(12764, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12979, prefix="1.2.3.0/24", as_path=(12979, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13002, prefix="1.2.3.0/24", as_path=(13002, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13105, prefix="1.2.3.0/24", as_path=(13105, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13178, prefix="1.2.3.0/24", as_path=(13178, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15493, prefix="1.2.3.0/24", as_path=(15493, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15672, prefix="1.2.3.0/24", as_path=(15672, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15673, prefix="1.2.3.0/24", as_path=(15673, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15774, prefix="1.2.3.0/24", as_path=(15774, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15880, prefix="1.2.3.0/24", as_path=(15880, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15974, prefix="1.2.3.0/24", as_path=(15974, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=16143, prefix="1.2.3.0/24", as_path=(16143, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=16285, prefix="1.2.3.0/24", as_path=(16285, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20690, prefix="1.2.3.0/24", as_path=(20690, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20702, prefix="1.2.3.0/24", as_path=(20702, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20764, prefix="1.2.3.0/24", as_path=(20764, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20870, prefix="1.2.3.0/24", as_path=(20870, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20872, prefix="1.2.3.0/24", as_path=(20872, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20895, prefix="1.2.3.0/24", as_path=(20895, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20919, prefix="1.2.3.0/24", as_path=(20919, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20940, prefix="1.2.3.0/24", as_path=(20940, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21105, prefix="1.2.3.0/24", as_path=(21105, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21127, prefix="1.2.3.0/24", as_path=(21127, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21184, prefix="1.2.3.0/24", as_path=(21184, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21367, prefix="1.2.3.0/24", as_path=(21367, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=23242, prefix="1.2.3.0/24", as_path=(23242, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24599, prefix="1.2.3.0/24", as_path=(24599, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24626, prefix="1.2.3.0/24", as_path=(24626, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24638, prefix="1.2.3.0/24", as_path=(24638, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24739, prefix="1.2.3.0/24", as_path=(24739, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24832, prefix="1.2.3.0/24", as_path=(24832, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25221, prefix="1.2.3.0/24", as_path=(25221, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25231, prefix="1.2.3.0/24", as_path=(25231, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25381, prefix="1.2.3.0/24", as_path=(25381, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25478, prefix="1.2.3.0/24", as_path=(25478, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25549, prefix="1.2.3.0/24", as_path=(25549, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25592, prefix="1.2.3.0/24", as_path=(25592, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25880, prefix="1.2.3.0/24", as_path=(25880, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=28745, prefix="1.2.3.0/24", as_path=(28745, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=28769, prefix="1.2.3.0/24", as_path=(28769, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=28775, prefix="1.2.3.0/24", as_path=(28775, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=28890, prefix="1.2.3.0/24", as_path=(28890, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=28917, prefix="1.2.3.0/24", as_path=(28917, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=28991, prefix="1.2.3.0/24", as_path=(28991, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29071, prefix="1.2.3.0/24", as_path=(29071, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29072, prefix="1.2.3.0/24", as_path=(29072, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29182, prefix="1.2.3.0/24", as_path=(29182, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29226, prefix="1.2.3.0/24", as_path=(29226, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=30729, prefix="1.2.3.0/24", as_path=(30729, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=30767, prefix="1.2.3.0/24", as_path=(30767, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=30835, prefix="1.2.3.0/24", as_path=(30835, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=30855, prefix="1.2.3.0/24", as_path=(30855, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=30952, prefix="1.2.3.0/24", as_path=(30952, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=30960, prefix="1.2.3.0/24", as_path=(30960, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=30967, prefix="1.2.3.0/24", as_path=(30967, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31200, prefix="1.2.3.0/24", as_path=(31200, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31257, prefix="1.2.3.0/24", as_path=(31257, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31294, prefix="1.2.3.0/24", as_path=(31294, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31364, prefix="1.2.3.0/24", as_path=(31364, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31425, prefix="1.2.3.0/24", as_path=(31425, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31462, prefix="1.2.3.0/24", as_path=(31462, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31566, prefix="1.2.3.0/24", as_path=(31566, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31643, prefix="1.2.3.0/24", as_path=(31643, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=33991, prefix="1.2.3.0/24", as_path=(33991, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34164, prefix="1.2.3.0/24", as_path=(34164, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34241, prefix="1.2.3.0/24", as_path=(34241, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34389, prefix="1.2.3.0/24", as_path=(34389, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34470, prefix="1.2.3.0/24", as_path=(34470, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34550, prefix="1.2.3.0/24", as_path=(34550, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34580, prefix="1.2.3.0/24", as_path=(34580, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34582, prefix="1.2.3.0/24", as_path=(34582, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34642, prefix="1.2.3.0/24", as_path=(34642, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34858, prefix="1.2.3.0/24", as_path=(34858, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34879, prefix="1.2.3.0/24", as_path=(34879, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34887, prefix="1.2.3.0/24", as_path=(34887, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35032, prefix="1.2.3.0/24", as_path=(35032, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35168, prefix="1.2.3.0/24", as_path=(35168, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35237, prefix="1.2.3.0/24", as_path=(35237, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35420, prefix="1.2.3.0/24", as_path=(35420, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35723, prefix="1.2.3.0/24", as_path=(35723, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35770, prefix="1.2.3.0/24", as_path=(35770, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=38917, prefix="1.2.3.0/24", as_path=(38917, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39061, prefix="1.2.3.0/24", as_path=(39061, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39113, prefix="1.2.3.0/24", as_path=(39113, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39134, prefix="1.2.3.0/24", as_path=(39134, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39256, prefix="1.2.3.0/24", as_path=(39256, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39264, prefix="1.2.3.0/24", as_path=(39264, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39269, prefix="1.2.3.0/24", as_path=(39269, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39350, prefix="1.2.3.0/24", as_path=(39350, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39493, prefix="1.2.3.0/24", as_path=(39493, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39684, prefix="1.2.3.0/24", as_path=(39684, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39707, prefix="1.2.3.0/24", as_path=(39707, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39812, prefix="1.2.3.0/24", as_path=(39812, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39864, prefix="1.2.3.0/24", as_path=(39864, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39901, prefix="1.2.3.0/24", as_path=(39901, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39927, prefix="1.2.3.0/24", as_path=(39927, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=40966, prefix="1.2.3.0/24", as_path=(40966, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=40977, prefix="1.2.3.0/24", as_path=(40977, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41060, prefix="1.2.3.0/24", as_path=(41060, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41148, prefix="1.2.3.0/24", as_path=(41148, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41217, prefix="1.2.3.0/24", as_path=(41217, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41220, prefix="1.2.3.0/24", as_path=(41220, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41268, prefix="1.2.3.0/24", as_path=(41268, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41341, prefix="1.2.3.0/24", as_path=(41341, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41465, prefix="1.2.3.0/24", as_path=(41465, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41517, prefix="1.2.3.0/24", as_path=(41517, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41560, prefix="1.2.3.0/24", as_path=(41560, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41616, prefix="1.2.3.0/24", as_path=(41616, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41706, prefix="1.2.3.0/24", as_path=(41706, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41719, prefix="1.2.3.0/24", as_path=(41719, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41743, prefix="1.2.3.0/24", as_path=(41743, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41748, prefix="1.2.3.0/24", as_path=(41748, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41812, prefix="1.2.3.0/24", as_path=(41812, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41829, prefix="1.2.3.0/24", as_path=(41829, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41929, prefix="1.2.3.0/24", as_path=(41929, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41942, prefix="1.2.3.0/24", as_path=(41942, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42038, prefix="1.2.3.0/24", as_path=(42038, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42139, prefix="1.2.3.0/24", as_path=(42139, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42190, prefix="1.2.3.0/24", as_path=(42190, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42277, prefix="1.2.3.0/24", as_path=(42277, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42482, prefix="1.2.3.0/24", as_path=(42482, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42514, prefix="1.2.3.0/24", as_path=(42514, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42558, prefix="1.2.3.0/24", as_path=(42558, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42574, prefix="1.2.3.0/24", as_path=(42574, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42632, prefix="1.2.3.0/24", as_path=(42632, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42676, prefix="1.2.3.0/24", as_path=(42676, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42728, prefix="1.2.3.0/24", as_path=(42728, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42767, prefix="1.2.3.0/24", as_path=(42767, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42870, prefix="1.2.3.0/24", as_path=(42870, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42893, prefix="1.2.3.0/24", as_path=(42893, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42916, prefix="1.2.3.0/24", as_path=(42916, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42996, prefix="1.2.3.0/24", as_path=(42996, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42998, prefix="1.2.3.0/24", as_path=(42998, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43031, prefix="1.2.3.0/24", as_path=(43031, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43235, prefix="1.2.3.0/24", as_path=(43235, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43246, prefix="1.2.3.0/24", as_path=(43246, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43247, prefix="1.2.3.0/24", as_path=(43247, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43330, prefix="1.2.3.0/24", as_path=(43330, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43346, prefix="1.2.3.0/24", as_path=(43346, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43396, prefix="1.2.3.0/24", as_path=(43396, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43403, prefix="1.2.3.0/24", as_path=(43403, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43404, prefix="1.2.3.0/24", as_path=(43404, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43434, prefix="1.2.3.0/24", as_path=(43434, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43444, prefix="1.2.3.0/24", as_path=(43444, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43550, prefix="1.2.3.0/24", as_path=(43550, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43594, prefix="1.2.3.0/24", as_path=(43594, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43600, prefix="1.2.3.0/24", as_path=(43600, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43676, prefix="1.2.3.0/24", as_path=(43676, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43714, prefix="1.2.3.0/24", as_path=(43714, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43728, prefix="1.2.3.0/24", as_path=(43728, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43776, prefix="1.2.3.0/24", as_path=(43776, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43782, prefix="1.2.3.0/24", as_path=(43782, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43785, prefix="1.2.3.0/24", as_path=(43785, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43812, prefix="1.2.3.0/24", as_path=(43812, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43832, prefix="1.2.3.0/24", as_path=(43832, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43901, prefix="1.2.3.0/24", as_path=(43901, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43903, prefix="1.2.3.0/24", as_path=(43903, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43909, prefix="1.2.3.0/24", as_path=(43909, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44020, prefix="1.2.3.0/24", as_path=(44020, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44039, prefix="1.2.3.0/24", as_path=(44039, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44056, prefix="1.2.3.0/24", as_path=(44056, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44151, prefix="1.2.3.0/24", as_path=(44151, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44265, prefix="1.2.3.0/24", as_path=(44265, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44266, prefix="1.2.3.0/24", as_path=(44266, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44270, prefix="1.2.3.0/24", as_path=(44270, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44345, prefix="1.2.3.0/24", as_path=(44345, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44417, prefix="1.2.3.0/24", as_path=(44417, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44484, prefix="1.2.3.0/24", as_path=(44484, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44492, prefix="1.2.3.0/24", as_path=(44492, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44493, prefix="1.2.3.0/24", as_path=(44493, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44597, prefix="1.2.3.0/24", as_path=(44597, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44621, prefix="1.2.3.0/24", as_path=(44621, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44657, prefix="1.2.3.0/24", as_path=(44657, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44678, prefix="1.2.3.0/24", as_path=(44678, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44724, prefix="1.2.3.0/24", as_path=(44724, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44816, prefix="1.2.3.0/24", as_path=(44816, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44845, prefix="1.2.3.0/24", as_path=(44845, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44857, prefix="1.2.3.0/24", as_path=(44857, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44943, prefix="1.2.3.0/24", as_path=(44943, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=45000, prefix="1.2.3.0/24", as_path=(45000, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=45018, prefix="1.2.3.0/24", as_path=(45018, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=45029, prefix="1.2.3.0/24", as_path=(45029, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47118, prefix="1.2.3.0/24", as_path=(47118, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47165, prefix="1.2.3.0/24", as_path=(47165, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47236, prefix="1.2.3.0/24", as_path=(47236, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47259, prefix="1.2.3.0/24", as_path=(47259, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47370, prefix="1.2.3.0/24", as_path=(47370, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47407, prefix="1.2.3.0/24", as_path=(47407, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47438, prefix="1.2.3.0/24", as_path=(47438, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47445, prefix="1.2.3.0/24", as_path=(47445, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47530, prefix="1.2.3.0/24", as_path=(47530, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47531, prefix="1.2.3.0/24", as_path=(47531, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47551, prefix="1.2.3.0/24", as_path=(47551, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47594, prefix="1.2.3.0/24", as_path=(47594, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47620, prefix="1.2.3.0/24", as_path=(47620, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47656, prefix="1.2.3.0/24", as_path=(47656, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47684, prefix="1.2.3.0/24", as_path=(47684, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47873, prefix="1.2.3.0/24", as_path=(47873, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47989, prefix="1.2.3.0/24", as_path=(47989, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48061, prefix="1.2.3.0/24", as_path=(48061, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48104, prefix="1.2.3.0/24", as_path=(48104, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48143, prefix="1.2.3.0/24", as_path=(48143, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48209, prefix="1.2.3.0/24", as_path=(48209, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48228, prefix="1.2.3.0/24", as_path=(48228, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48347, prefix="1.2.3.0/24", as_path=(48347, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48349, prefix="1.2.3.0/24", as_path=(48349, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48366, prefix="1.2.3.0/24", as_path=(48366, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48442, prefix="1.2.3.0/24", as_path=(48442, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48467, prefix="1.2.3.0/24", as_path=(48467, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48472, prefix="1.2.3.0/24", as_path=(48472, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48475, prefix="1.2.3.0/24", as_path=(48475, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48524, prefix="1.2.3.0/24", as_path=(48524, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48583, prefix="1.2.3.0/24", as_path=(48583, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48642, prefix="1.2.3.0/24", as_path=(48642, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48677, prefix="1.2.3.0/24", as_path=(48677, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48711, prefix="1.2.3.0/24", as_path=(48711, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48739, prefix="1.2.3.0/24", as_path=(48739, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48877, prefix="1.2.3.0/24", as_path=(48877, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48909, prefix="1.2.3.0/24", as_path=(48909, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48949, prefix="1.2.3.0/24", as_path=(48949, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48978, prefix="1.2.3.0/24", as_path=(48978, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49002, prefix="1.2.3.0/24", as_path=(49002, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49055, prefix="1.2.3.0/24", as_path=(49055, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49106, prefix="1.2.3.0/24", as_path=(49106, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49107, prefix="1.2.3.0/24", as_path=(49107, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49128, prefix="1.2.3.0/24", as_path=(49128, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49136, prefix="1.2.3.0/24", as_path=(49136, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49311, prefix="1.2.3.0/24", as_path=(49311, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49377, prefix="1.2.3.0/24", as_path=(49377, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49439, prefix="1.2.3.0/24", as_path=(49439, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49458, prefix="1.2.3.0/24", as_path=(49458, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49481, prefix="1.2.3.0/24", as_path=(49481, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49483, prefix="1.2.3.0/24", as_path=(49483, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49545, prefix="1.2.3.0/24", as_path=(49545, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49554, prefix="1.2.3.0/24", as_path=(49554, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49569, prefix="1.2.3.0/24", as_path=(49569, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49577, prefix="1.2.3.0/24", as_path=(49577, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49587, prefix="1.2.3.0/24", as_path=(49587, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49637, prefix="1.2.3.0/24", as_path=(49637, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49701, prefix="1.2.3.0/24", as_path=(49701, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49723, prefix="1.2.3.0/24", as_path=(49723, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49759, prefix="1.2.3.0/24", as_path=(49759, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49764, prefix="1.2.3.0/24", as_path=(49764, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49777, prefix="1.2.3.0/24", as_path=(49777, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49821, prefix="1.2.3.0/24", as_path=(49821, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49848, prefix="1.2.3.0/24", as_path=(49848, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49892, prefix="1.2.3.0/24", as_path=(49892, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49963, prefix="1.2.3.0/24", as_path=(49963, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50022, prefix="1.2.3.0/24", as_path=(50022, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50048, prefix="1.2.3.0/24", as_path=(50048, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50147, prefix="1.2.3.0/24", as_path=(50147, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50166, prefix="1.2.3.0/24", as_path=(50166, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50182, prefix="1.2.3.0/24", as_path=(50182, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50187, prefix="1.2.3.0/24", as_path=(50187, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50248, prefix="1.2.3.0/24", as_path=(50248, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50257, prefix="1.2.3.0/24", as_path=(50257, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50283, prefix="1.2.3.0/24", as_path=(50283, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50340, prefix="1.2.3.0/24", as_path=(50340, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50466, prefix="1.2.3.0/24", as_path=(50466, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50556, prefix="1.2.3.0/24", as_path=(50556, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50645, prefix="1.2.3.0/24", as_path=(50645, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50676, prefix="1.2.3.0/24", as_path=(50676, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50732, prefix="1.2.3.0/24", as_path=(50732, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50859, prefix="1.2.3.0/24", as_path=(50859, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50867, prefix="1.2.3.0/24", as_path=(50867, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50885, prefix="1.2.3.0/24", as_path=(50885, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50923, prefix="1.2.3.0/24", as_path=(50923, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51004, prefix="1.2.3.0/24", as_path=(51004, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51028, prefix="1.2.3.0/24", as_path=(51028, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51054, prefix="1.2.3.0/24", as_path=(51054, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51071, prefix="1.2.3.0/24", as_path=(51071, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51092, prefix="1.2.3.0/24", as_path=(51092, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51136, prefix="1.2.3.0/24", as_path=(51136, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51156, prefix="1.2.3.0/24", as_path=(51156, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51178, prefix="1.2.3.0/24", as_path=(51178, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51190, prefix="1.2.3.0/24", as_path=(51190, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51213, prefix="1.2.3.0/24", as_path=(51213, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51218, prefix="1.2.3.0/24", as_path=(51218, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51515, prefix="1.2.3.0/24", as_path=(51515, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51583, prefix="1.2.3.0/24", as_path=(51583, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51599, prefix="1.2.3.0/24", as_path=(51599, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51613, prefix="1.2.3.0/24", as_path=(51613, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51623, prefix="1.2.3.0/24", as_path=(51623, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51663, prefix="1.2.3.0/24", as_path=(51663, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51715, prefix="1.2.3.0/24", as_path=(51715, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51764, prefix="1.2.3.0/24", as_path=(51764, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51771, prefix="1.2.3.0/24", as_path=(51771, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51781, prefix="1.2.3.0/24", as_path=(51781, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51811, prefix="1.2.3.0/24", as_path=(51811, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51812, prefix="1.2.3.0/24", as_path=(51812, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51813, prefix="1.2.3.0/24", as_path=(51813, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51880, prefix="1.2.3.0/24", as_path=(51880, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51912, prefix="1.2.3.0/24", as_path=(51912, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51957, prefix="1.2.3.0/24", as_path=(51957, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=52040, prefix="1.2.3.0/24", as_path=(52040, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=52094, prefix="1.2.3.0/24", as_path=(52094, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=52175, prefix="1.2.3.0/24", as_path=(52175, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=52208, prefix="1.2.3.0/24", as_path=(52208, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56326, prefix="1.2.3.0/24", as_path=(56326, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56340, prefix="1.2.3.0/24", as_path=(56340, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56342, prefix="1.2.3.0/24", as_path=(56342, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56361, prefix="1.2.3.0/24", as_path=(56361, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56407, prefix="1.2.3.0/24", as_path=(56407, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56409, prefix="1.2.3.0/24", as_path=(56409, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56426, prefix="1.2.3.0/24", as_path=(56426, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56463, prefix="1.2.3.0/24", as_path=(56463, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56534, prefix="1.2.3.0/24", as_path=(56534, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56581, prefix="1.2.3.0/24", as_path=(56581, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56592, prefix="1.2.3.0/24", as_path=(56592, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56621, prefix="1.2.3.0/24", as_path=(56621, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56634, prefix="1.2.3.0/24", as_path=(56634, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56676, prefix="1.2.3.0/24", as_path=(56676, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56677, prefix="1.2.3.0/24", as_path=(56677, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56699, prefix="1.2.3.0/24", as_path=(56699, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56741, prefix="1.2.3.0/24", as_path=(56741, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56791, prefix="1.2.3.0/24", as_path=(56791, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56793, prefix="1.2.3.0/24", as_path=(56793, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56806, prefix="1.2.3.0/24", as_path=(56806, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56820, prefix="1.2.3.0/24", as_path=(56820, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56846, prefix="1.2.3.0/24", as_path=(56846, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56977, prefix="1.2.3.0/24", as_path=(56977, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57123, prefix="1.2.3.0/24", as_path=(57123, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57214, prefix="1.2.3.0/24", as_path=(57214, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57261, prefix="1.2.3.0/24", as_path=(57261, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57313, prefix="1.2.3.0/24", as_path=(57313, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57320, prefix="1.2.3.0/24", as_path=(57320, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57328, prefix="1.2.3.0/24", as_path=(57328, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57339, prefix="1.2.3.0/24", as_path=(57339, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57354, prefix="1.2.3.0/24", as_path=(57354, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57363, prefix="1.2.3.0/24", as_path=(57363, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57380, prefix="1.2.3.0/24", as_path=(57380, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57396, prefix="1.2.3.0/24", as_path=(57396, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57503, prefix="1.2.3.0/24", as_path=(57503, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57712, prefix="1.2.3.0/24", as_path=(57712, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57724, prefix="1.2.3.0/24", as_path=(57724, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57742, prefix="1.2.3.0/24", as_path=(57742, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57798, prefix="1.2.3.0/24", as_path=(57798, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57805, prefix="1.2.3.0/24", as_path=(57805, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57812, prefix="1.2.3.0/24", as_path=(57812, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57827, prefix="1.2.3.0/24", as_path=(57827, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57871, prefix="1.2.3.0/24", as_path=(57871, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57898, prefix="1.2.3.0/24", as_path=(57898, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58084, prefix="1.2.3.0/24", as_path=(58084, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58100, prefix="1.2.3.0/24", as_path=(58100, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58107, prefix="1.2.3.0/24", as_path=(58107, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58136, prefix="1.2.3.0/24", as_path=(58136, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58158, prefix="1.2.3.0/24", as_path=(58158, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58230, prefix="1.2.3.0/24", as_path=(58230, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58231, prefix="1.2.3.0/24", as_path=(58231, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58238, prefix="1.2.3.0/24", as_path=(58238, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58304, prefix="1.2.3.0/24", as_path=(58304, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58439, prefix="1.2.3.0/24", as_path=(58439, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59483, prefix="1.2.3.0/24", as_path=(59483, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59502, prefix="1.2.3.0/24", as_path=(59502, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59517, prefix="1.2.3.0/24", as_path=(59517, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59525, prefix="1.2.3.0/24", as_path=(59525, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59533, prefix="1.2.3.0/24", as_path=(59533, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59537, prefix="1.2.3.0/24", as_path=(59537, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59595, prefix="1.2.3.0/24", as_path=(59595, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59600, prefix="1.2.3.0/24", as_path=(59600, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59637, prefix="1.2.3.0/24", as_path=(59637, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59693, prefix="1.2.3.0/24", as_path=(59693, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59881, prefix="1.2.3.0/24", as_path=(59881, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59883, prefix="1.2.3.0/24", as_path=(59883, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59975, prefix="1.2.3.0/24", as_path=(59975, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60006, prefix="1.2.3.0/24", as_path=(60006, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60042, prefix="1.2.3.0/24", as_path=(60042, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60067, prefix="1.2.3.0/24", as_path=(60067, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60072, prefix="1.2.3.0/24", as_path=(60072, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60098, prefix="1.2.3.0/24", as_path=(60098, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60122, prefix="1.2.3.0/24", as_path=(60122, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60139, prefix="1.2.3.0/24", as_path=(60139, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60165, prefix="1.2.3.0/24", as_path=(60165, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60172, prefix="1.2.3.0/24", as_path=(60172, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60290, prefix="1.2.3.0/24", as_path=(60290, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60329, prefix="1.2.3.0/24", as_path=(60329, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60442, prefix="1.2.3.0/24", as_path=(60442, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60486, prefix="1.2.3.0/24", as_path=(60486, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60556, prefix="1.2.3.0/24", as_path=(60556, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60569, prefix="1.2.3.0/24", as_path=(60569, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60651, prefix="1.2.3.0/24", as_path=(60651, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60693, prefix="1.2.3.0/24", as_path=(60693, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60747, prefix="1.2.3.0/24", as_path=(60747, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60753, prefix="1.2.3.0/24", as_path=(60753, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60771, prefix="1.2.3.0/24", as_path=(60771, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60873, prefix="1.2.3.0/24", as_path=(60873, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60879, prefix="1.2.3.0/24", as_path=(60879, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60957, prefix="1.2.3.0/24", as_path=(60957, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61031, prefix="1.2.3.0/24", as_path=(61031, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61111, prefix="1.2.3.0/24", as_path=(61111, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61206, prefix="1.2.3.0/24", as_path=(61206, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61249, prefix="1.2.3.0/24", as_path=(61249, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61308, prefix="1.2.3.0/24", as_path=(61308, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61360, prefix="1.2.3.0/24", as_path=(61360, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61390, prefix="1.2.3.0/24", as_path=(61390, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61403, prefix="1.2.3.0/24", as_path=(61403, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61407, prefix="1.2.3.0/24", as_path=(61407, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61431, prefix="1.2.3.0/24", as_path=(61431, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62143, prefix="1.2.3.0/24", as_path=(62143, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62200, prefix="1.2.3.0/24", as_path=(62200, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62247, prefix="1.2.3.0/24", as_path=(62247, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62382, prefix="1.2.3.0/24", as_path=(62382, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62439, prefix="1.2.3.0/24", as_path=(62439, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62443, prefix="1.2.3.0/24", as_path=(62443, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62444, prefix="1.2.3.0/24", as_path=(62444, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=64429, prefix="1.2.3.0/24", as_path=(64429, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=131279, prefix="1.2.3.0/24", as_path=(131279, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=139089, prefix="1.2.3.0/24", as_path=(139089, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=196688, prefix="1.2.3.0/24", as_path=(196688, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=196742, prefix="1.2.3.0/24", as_path=(196742, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=196791, prefix="1.2.3.0/24", as_path=(196791, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=196893, prefix="1.2.3.0/24", as_path=(196893, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=196949, prefix="1.2.3.0/24", as_path=(196949, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=196991, prefix="1.2.3.0/24", as_path=(196991, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197068, prefix="1.2.3.0/24", as_path=(197068, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197078, prefix="1.2.3.0/24", as_path=(197078, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197275, prefix="1.2.3.0/24", as_path=(197275, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197298, prefix="1.2.3.0/24", as_path=(197298, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197315, prefix="1.2.3.0/24", as_path=(197315, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197482, prefix="1.2.3.0/24", as_path=(197482, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197489, prefix="1.2.3.0/24", as_path=(197489, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197499, prefix="1.2.3.0/24", as_path=(197499, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197535, prefix="1.2.3.0/24", as_path=(197535, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197718, prefix="1.2.3.0/24", as_path=(197718, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197808, prefix="1.2.3.0/24", as_path=(197808, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198052, prefix="1.2.3.0/24", as_path=(198052, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198354, prefix="1.2.3.0/24", as_path=(198354, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198592, prefix="1.2.3.0/24", as_path=(198592, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198639, prefix="1.2.3.0/24", as_path=(198639, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198670, prefix="1.2.3.0/24", as_path=(198670, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198716, prefix="1.2.3.0/24", as_path=(198716, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198757, prefix="1.2.3.0/24", as_path=(198757, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198758, prefix="1.2.3.0/24", as_path=(198758, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198832, prefix="1.2.3.0/24", as_path=(198832, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198918, prefix="1.2.3.0/24", as_path=(198918, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199020, prefix="1.2.3.0/24", as_path=(199020, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199049, prefix="1.2.3.0/24", as_path=(199049, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199120, prefix="1.2.3.0/24", as_path=(199120, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199278, prefix="1.2.3.0/24", as_path=(199278, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199524, prefix="1.2.3.0/24", as_path=(199524, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199534, prefix="1.2.3.0/24", as_path=(199534, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199599, prefix="1.2.3.0/24", as_path=(199599, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199858, prefix="1.2.3.0/24", as_path=(199858, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199933, prefix="1.2.3.0/24", as_path=(199933, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199992, prefix="1.2.3.0/24", as_path=(199992, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200066, prefix="1.2.3.0/24", as_path=(200066, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200095, prefix="1.2.3.0/24", as_path=(200095, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200350, prefix="1.2.3.0/24", as_path=(200350, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200362, prefix="1.2.3.0/24", as_path=(200362, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200364, prefix="1.2.3.0/24", as_path=(200364, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200400, prefix="1.2.3.0/24", as_path=(200400, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200976, prefix="1.2.3.0/24", as_path=(200976, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201100, prefix="1.2.3.0/24", as_path=(201100, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201294, prefix="1.2.3.0/24", as_path=(201294, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201606, prefix="1.2.3.0/24", as_path=(201606, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201624, prefix="1.2.3.0/24", as_path=(201624, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202127, prefix="1.2.3.0/24", as_path=(202127, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202446, prefix="1.2.3.0/24", as_path=(202446, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202806, prefix="1.2.3.0/24", as_path=(202806, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203002, prefix="1.2.3.0/24", as_path=(203002, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203131, prefix="1.2.3.0/24", as_path=(203131, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203371, prefix="1.2.3.0/24", as_path=(203371, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203750, prefix="1.2.3.0/24", as_path=(203750, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203972, prefix="1.2.3.0/24", as_path=(203972, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204297, prefix="1.2.3.0/24", as_path=(204297, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204720, prefix="1.2.3.0/24", as_path=(204720, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204752, prefix="1.2.3.0/24", as_path=(204752, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204820, prefix="1.2.3.0/24", as_path=(204820, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204925, prefix="1.2.3.0/24", as_path=(204925, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205063, prefix="1.2.3.0/24", as_path=(205063, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205161, prefix="1.2.3.0/24", as_path=(205161, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205495, prefix="1.2.3.0/24", as_path=(205495, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205528, prefix="1.2.3.0/24", as_path=(205528, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205628, prefix="1.2.3.0/24", as_path=(205628, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205922, prefix="1.2.3.0/24", as_path=(205922, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206012, prefix="1.2.3.0/24", as_path=(206012, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206069, prefix="1.2.3.0/24", as_path=(206069, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206333, prefix="1.2.3.0/24", as_path=(206333, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207353, prefix="1.2.3.0/24", as_path=(207353, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207361, prefix="1.2.3.0/24", as_path=(207361, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207387, prefix="1.2.3.0/24", as_path=(207387, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207518, prefix="1.2.3.0/24", as_path=(207518, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207794, prefix="1.2.3.0/24", as_path=(207794, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207839, prefix="1.2.3.0/24", as_path=(207839, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207935, prefix="1.2.3.0/24", as_path=(207935, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208056, prefix="1.2.3.0/24", as_path=(208056, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208087, prefix="1.2.3.0/24", as_path=(208087, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208177, prefix="1.2.3.0/24", as_path=(208177, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208208, prefix="1.2.3.0/24", as_path=(208208, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208409, prefix="1.2.3.0/24", as_path=(208409, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208413, prefix="1.2.3.0/24", as_path=(208413, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208631, prefix="1.2.3.0/24", as_path=(208631, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208729, prefix="1.2.3.0/24", as_path=(208729, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208801, prefix="1.2.3.0/24", as_path=(208801, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208838, prefix="1.2.3.0/24", as_path=(208838, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209030, prefix="1.2.3.0/24", as_path=(209030, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209084, prefix="1.2.3.0/24", as_path=(209084, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209099, prefix="1.2.3.0/24", as_path=(209099, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209307, prefix="1.2.3.0/24", as_path=(209307, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209357, prefix="1.2.3.0/24", as_path=(209357, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209728, prefix="1.2.3.0/24", as_path=(209728, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209926, prefix="1.2.3.0/24", as_path=(209926, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209955, prefix="1.2.3.0/24", as_path=(209955, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210242, prefix="1.2.3.0/24", as_path=(210242, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211000, prefix="1.2.3.0/24", as_path=(211000, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211241, prefix="1.2.3.0/24", as_path=(211241, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211291, prefix="1.2.3.0/24", as_path=(211291, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211609, prefix="1.2.3.0/24", as_path=(211609, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211625, prefix="1.2.3.0/24", as_path=(211625, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211639, prefix="1.2.3.0/24", as_path=(211639, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211641, prefix="1.2.3.0/24", as_path=(211641, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211762, prefix="1.2.3.0/24", as_path=(211762, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211951, prefix="1.2.3.0/24", as_path=(211951, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212015, prefix="1.2.3.0/24", as_path=(212015, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212030, prefix="1.2.3.0/24", as_path=(212030, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212210, prefix="1.2.3.0/24", as_path=(212210, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212214, prefix="1.2.3.0/24", as_path=(212214, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212303, prefix="1.2.3.0/24", as_path=(212303, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212421, prefix="1.2.3.0/24", as_path=(212421, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212487, prefix="1.2.3.0/24", as_path=(212487, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212614, prefix="1.2.3.0/24", as_path=(212614, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=213067, prefix="1.2.3.0/24", as_path=(213067, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=3175,
        prefix="1.2.3.0/24",
        as_path=(3175, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8630,
        prefix="1.2.3.0/24",
        as_path=(8630, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8915,
        prefix="1.2.3.0/24",
        as_path=(8915, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12418,
        prefix="1.2.3.0/24",
        as_path=(12418, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13029,
        prefix="1.2.3.0/24",
        as_path=(13029, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20772,
        prefix="1.2.3.0/24",
        as_path=(20772, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29124,
        prefix="1.2.3.0/24",
        as_path=(29124, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=30784,
        prefix="1.2.3.0/24",
        as_path=(30784, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31500,
        prefix="1.2.3.0/24",
        as_path=(31500, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31512,
        prefix="1.2.3.0/24",
        as_path=(31512, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34164,
        prefix="1.2.3.0/24",
        as_path=(34164, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=38978,
        prefix="1.2.3.0/24",
        as_path=(38978, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41275,
        prefix="1.2.3.0/24",
        as_path=(41275, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43319,
        prefix="1.2.3.0/24",
        as_path=(43319, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43727,
        prefix="1.2.3.0/24",
        as_path=(43727, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47168,
        prefix="1.2.3.0/24",
        as_path=(47168, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47763,
        prefix="1.2.3.0/24",
        as_path=(47763, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49533,
        prefix="1.2.3.0/24",
        as_path=(49533, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50636,
        prefix="1.2.3.0/24",
        as_path=(50636, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50688,
        prefix="1.2.3.0/24",
        as_path=(50688, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50771,
        prefix="1.2.3.0/24",
        as_path=(50771, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51147,
        prefix="1.2.3.0/24",
        as_path=(51147, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51685,
        prefix="1.2.3.0/24",
        as_path=(51685, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56866,
        prefix="1.2.3.0/24",
        as_path=(56866, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57363,
        prefix="1.2.3.0/24",
        as_path=(57363, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57661,
        prefix="1.2.3.0/24",
        as_path=(57661, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58279,
        prefix="1.2.3.0/24",
        as_path=(58279, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59557,
        prefix="1.2.3.0/24",
        as_path=(59557, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59559,
        prefix="1.2.3.0/24",
        as_path=(59559, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60554,
        prefix="1.2.3.0/24",
        as_path=(60554, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61436,
        prefix="1.2.3.0/24",
        as_path=(61436, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=196963,
        prefix="1.2.3.0/24",
        as_path=(196963, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199576,
        prefix="1.2.3.0/24",
        as_path=(199576, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201511,
        prefix="1.2.3.0/24",
        as_path=(201511, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204720,
        prefix="1.2.3.0/24",
        as_path=(204720, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205047,
        prefix="1.2.3.0/24",
        as_path=(205047, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211506,
        prefix="1.2.3.0/24",
        as_path=(211506, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=213304,
        prefix="1.2.3.0/24",
        as_path=(213304, 12714, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=3067, prefix="1.2.3.0/24", as_path=(3067, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8336, prefix="1.2.3.0/24", as_path=(8336, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12455, prefix="1.2.3.0/24", as_path=(12455, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13150, prefix="1.2.3.0/24", as_path=(13150, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13335, prefix="1.2.3.0/24", as_path=(13335, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15808, prefix="1.2.3.0/24", as_path=(15808, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=18931, prefix="1.2.3.0/24", as_path=(18931, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20940, prefix="1.2.3.0/24", as_path=(20940, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21739, prefix="1.2.3.0/24", as_path=(21739, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=22354, prefix="1.2.3.0/24", as_path=(22354, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=23058, prefix="1.2.3.0/24", as_path=(23058, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=23889, prefix="1.2.3.0/24", as_path=(23889, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25139, prefix="1.2.3.0/24", as_path=(25139, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=30619, prefix="1.2.3.0/24", as_path=(30619, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=30999, prefix="1.2.3.0/24", as_path=(30999, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=32017, prefix="1.2.3.0/24", as_path=(32017, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=32437, prefix="1.2.3.0/24", as_path=(32437, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=32590, prefix="1.2.3.0/24", as_path=(32590, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=33765, prefix="1.2.3.0/24", as_path=(33765, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=33771, prefix="1.2.3.0/24", as_path=(33771, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=36236, prefix="1.2.3.0/24", as_path=(36236, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=36944, prefix="1.2.3.0/24", as_path=(36944, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=36975, prefix="1.2.3.0/24", as_path=(36975, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37013, prefix="1.2.3.0/24", as_path=(37013, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37019, prefix="1.2.3.0/24", as_path=(37019, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37027, prefix="1.2.3.0/24", as_path=(37027, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37052, prefix="1.2.3.0/24", as_path=(37052, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37079, prefix="1.2.3.0/24", as_path=(37079, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37084, prefix="1.2.3.0/24", as_path=(37084, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37110, prefix="1.2.3.0/24", as_path=(37110, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37126, prefix="1.2.3.0/24", as_path=(37126, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37129, prefix="1.2.3.0/24", as_path=(37129, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37168, prefix="1.2.3.0/24", as_path=(37168, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37179, prefix="1.2.3.0/24", as_path=(37179, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37298, prefix="1.2.3.0/24", as_path=(37298, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37317, prefix="1.2.3.0/24", as_path=(37317, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37342, prefix="1.2.3.0/24", as_path=(37342, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37349, prefix="1.2.3.0/24", as_path=(37349, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37353, prefix="1.2.3.0/24", as_path=(37353, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37356, prefix="1.2.3.0/24", as_path=(37356, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37358, prefix="1.2.3.0/24", as_path=(37358, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37395, prefix="1.2.3.0/24", as_path=(37395, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37421, prefix="1.2.3.0/24", as_path=(37421, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37482, prefix="1.2.3.0/24", as_path=(37482, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37499, prefix="1.2.3.0/24", as_path=(37499, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37519, prefix="1.2.3.0/24", as_path=(37519, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37542, prefix="1.2.3.0/24", as_path=(37542, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37546, prefix="1.2.3.0/24", as_path=(37546, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37579, prefix="1.2.3.0/24", as_path=(37579, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37599, prefix="1.2.3.0/24", as_path=(37599, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37618, prefix="1.2.3.0/24", as_path=(37618, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37619, prefix="1.2.3.0/24", as_path=(37619, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37634, prefix="1.2.3.0/24", as_path=(37634, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37691, prefix="1.2.3.0/24", as_path=(37691, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42473, prefix="1.2.3.0/24", as_path=(42473, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=54113, prefix="1.2.3.0/24", as_path=(54113, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=55256, prefix="1.2.3.0/24", as_path=(55256, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62044, prefix="1.2.3.0/24", as_path=(62044, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62597, prefix="1.2.3.0/24", as_path=(62597, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=63293, prefix="1.2.3.0/24", as_path=(63293, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=63399, prefix="1.2.3.0/24", as_path=(63399, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199524, prefix="1.2.3.0/24", as_path=(199524, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327687, prefix="1.2.3.0/24", as_path=(327687, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327701, prefix="1.2.3.0/24", as_path=(327701, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327713, prefix="1.2.3.0/24", as_path=(327713, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327724, prefix="1.2.3.0/24", as_path=(327724, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327727, prefix="1.2.3.0/24", as_path=(327727, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327733, prefix="1.2.3.0/24", as_path=(327733, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327749, prefix="1.2.3.0/24", as_path=(327749, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327766, prefix="1.2.3.0/24", as_path=(327766, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327772, prefix="1.2.3.0/24", as_path=(327772, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327787, prefix="1.2.3.0/24", as_path=(327787, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327808, prefix="1.2.3.0/24", as_path=(327808, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327812, prefix="1.2.3.0/24", as_path=(327812, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327822, prefix="1.2.3.0/24", as_path=(327822, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327849, prefix="1.2.3.0/24", as_path=(327849, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327850, prefix="1.2.3.0/24", as_path=(327850, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327859, prefix="1.2.3.0/24", as_path=(327859, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327884, prefix="1.2.3.0/24", as_path=(327884, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327894, prefix="1.2.3.0/24", as_path=(327894, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327900, prefix="1.2.3.0/24", as_path=(327900, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327908, prefix="1.2.3.0/24", as_path=(327908, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327910, prefix="1.2.3.0/24", as_path=(327910, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327923, prefix="1.2.3.0/24", as_path=(327923, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327927, prefix="1.2.3.0/24", as_path=(327927, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327961, prefix="1.2.3.0/24", as_path=(327961, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327994, prefix="1.2.3.0/24", as_path=(327994, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327996, prefix="1.2.3.0/24", as_path=(327996, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328016, prefix="1.2.3.0/24", as_path=(328016, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328024, prefix="1.2.3.0/24", as_path=(328024, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328037, prefix="1.2.3.0/24", as_path=(328037, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328038, prefix="1.2.3.0/24", as_path=(328038, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328041, prefix="1.2.3.0/24", as_path=(328041, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328093, prefix="1.2.3.0/24", as_path=(328093, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328106, prefix="1.2.3.0/24", as_path=(328106, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328112, prefix="1.2.3.0/24", as_path=(328112, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328142, prefix="1.2.3.0/24", as_path=(328142, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328155, prefix="1.2.3.0/24", as_path=(328155, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328162, prefix="1.2.3.0/24", as_path=(328162, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328163, prefix="1.2.3.0/24", as_path=(328163, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328164, prefix="1.2.3.0/24", as_path=(328164, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328172, prefix="1.2.3.0/24", as_path=(328172, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328179, prefix="1.2.3.0/24", as_path=(328179, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328209, prefix="1.2.3.0/24", as_path=(328209, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328246, prefix="1.2.3.0/24", as_path=(328246, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328255, prefix="1.2.3.0/24", as_path=(328255, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328275, prefix="1.2.3.0/24", as_path=(328275, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328287, prefix="1.2.3.0/24", as_path=(328287, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328302, prefix="1.2.3.0/24", as_path=(328302, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328306, prefix="1.2.3.0/24", as_path=(328306, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328323, prefix="1.2.3.0/24", as_path=(328323, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328327, prefix="1.2.3.0/24", as_path=(328327, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328331, prefix="1.2.3.0/24", as_path=(328331, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328337, prefix="1.2.3.0/24", as_path=(328337, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328347, prefix="1.2.3.0/24", as_path=(328347, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328351, prefix="1.2.3.0/24", as_path=(328351, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328373, prefix="1.2.3.0/24", as_path=(328373, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328375, prefix="1.2.3.0/24", as_path=(328375, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328386, prefix="1.2.3.0/24", as_path=(328386, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328388, prefix="1.2.3.0/24", as_path=(328388, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328404, prefix="1.2.3.0/24", as_path=(328404, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328441, prefix="1.2.3.0/24", as_path=(328441, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328444, prefix="1.2.3.0/24", as_path=(328444, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328465, prefix="1.2.3.0/24", as_path=(328465, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328480, prefix="1.2.3.0/24", as_path=(328480, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328498, prefix="1.2.3.0/24", as_path=(328498, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328501, prefix="1.2.3.0/24", as_path=(328501, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328510, prefix="1.2.3.0/24", as_path=(328510, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328512, prefix="1.2.3.0/24", as_path=(328512, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328514, prefix="1.2.3.0/24", as_path=(328514, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328519, prefix="1.2.3.0/24", as_path=(328519, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328536, prefix="1.2.3.0/24", as_path=(328536, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328538, prefix="1.2.3.0/24", as_path=(328538, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328543, prefix="1.2.3.0/24", as_path=(328543, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328560, prefix="1.2.3.0/24", as_path=(328560, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328576, prefix="1.2.3.0/24", as_path=(328576, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328580, prefix="1.2.3.0/24", as_path=(328580, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328598, prefix="1.2.3.0/24", as_path=(328598, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328603, prefix="1.2.3.0/24", as_path=(328603, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328616, prefix="1.2.3.0/24", as_path=(328616, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328637, prefix="1.2.3.0/24", as_path=(328637, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328656, prefix="1.2.3.0/24", as_path=(328656, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328657, prefix="1.2.3.0/24", as_path=(328657, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328672, prefix="1.2.3.0/24", as_path=(328672, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328695, prefix="1.2.3.0/24", as_path=(328695, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328727, prefix="1.2.3.0/24", as_path=(328727, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328732, prefix="1.2.3.0/24", as_path=(328732, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328750, prefix="1.2.3.0/24", as_path=(328750, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328777, prefix="1.2.3.0/24", as_path=(328777, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328818, prefix="1.2.3.0/24", as_path=(328818, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328821, prefix="1.2.3.0/24", as_path=(328821, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328829, prefix="1.2.3.0/24", as_path=(328829, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328851, prefix="1.2.3.0/24", as_path=(328851, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328912, prefix="1.2.3.0/24", as_path=(328912, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328964, prefix="1.2.3.0/24", as_path=(328964, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=329042, prefix="1.2.3.0/24", as_path=(329042, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=395363, prefix="1.2.3.0/24", as_path=(395363, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=72, prefix="1.2.3.0/24", as_path=(72, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=2134, prefix="1.2.3.0/24", as_path=(2134, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=2535, prefix="1.2.3.0/24", as_path=(2535, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=2559, prefix="1.2.3.0/24", as_path=(2559, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=3680, prefix="1.2.3.0/24", as_path=(3680, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=3738, prefix="1.2.3.0/24", as_path=(3738, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=3917, prefix="1.2.3.0/24", as_path=(3917, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=6072, prefix="1.2.3.0/24", as_path=(6072, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=6075, prefix="1.2.3.0/24", as_path=(6075, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=6468, prefix="1.2.3.0/24", as_path=(6468, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=6871, prefix="1.2.3.0/24", as_path=(6871, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8336, prefix="1.2.3.0/24", as_path=(8336, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8640, prefix="1.2.3.0/24", as_path=(8640, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=10655, prefix="1.2.3.0/24", as_path=(10655, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=10666, prefix="1.2.3.0/24", as_path=(10666, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=11528, prefix="1.2.3.0/24", as_path=(11528, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=11757, prefix="1.2.3.0/24", as_path=(11757, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12222, prefix="1.2.3.0/24", as_path=(12222, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12440, prefix="1.2.3.0/24", as_path=(12440, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13205, prefix="1.2.3.0/24", as_path=(13205, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13458, prefix="1.2.3.0/24", as_path=(13458, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=14039, prefix="1.2.3.0/24", as_path=(14039, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=14630, prefix="1.2.3.0/24", as_path=(14630, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15248, prefix="1.2.3.0/24", as_path=(15248, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15499, prefix="1.2.3.0/24", as_path=(15499, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15689, prefix="1.2.3.0/24", as_path=(15689, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15865, prefix="1.2.3.0/24", as_path=(15865, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=16477, prefix="1.2.3.0/24", as_path=(16477, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=16525, prefix="1.2.3.0/24", as_path=(16525, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=16807, prefix="1.2.3.0/24", as_path=(16807, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=16839, prefix="1.2.3.0/24", as_path=(16839, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=16931, prefix="1.2.3.0/24", as_path=(16931, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=17903, prefix="1.2.3.0/24", as_path=(17903, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=19812, prefix="1.2.3.0/24", as_path=(19812, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20163, prefix="1.2.3.0/24", as_path=(20163, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20464, prefix="1.2.3.0/24", as_path=(20464, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20695, prefix="1.2.3.0/24", as_path=(20695, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20705, prefix="1.2.3.0/24", as_path=(20705, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20955, prefix="1.2.3.0/24", as_path=(20955, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21054, prefix="1.2.3.0/24", as_path=(21054, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21110, prefix="1.2.3.0/24", as_path=(21110, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21267, prefix="1.2.3.0/24", as_path=(21267, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21301, prefix="1.2.3.0/24", as_path=(21301, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21464, prefix="1.2.3.0/24", as_path=(21464, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21470, prefix="1.2.3.0/24", as_path=(21470, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21758, prefix="1.2.3.0/24", as_path=(21758, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21874, prefix="1.2.3.0/24", as_path=(21874, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=22775, prefix="1.2.3.0/24", as_path=(22775, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24650, prefix="1.2.3.0/24", as_path=(24650, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24677, prefix="1.2.3.0/24", as_path=(24677, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24775, prefix="1.2.3.0/24", as_path=(24775, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25050, prefix="1.2.3.0/24", as_path=(25050, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25585, prefix="1.2.3.0/24", as_path=(25585, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=27447, prefix="1.2.3.0/24", as_path=(27447, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=28863, prefix="1.2.3.0/24", as_path=(28863, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29033, prefix="1.2.3.0/24", as_path=(29033, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29888, prefix="1.2.3.0/24", as_path=(29888, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31632, prefix="1.2.3.0/24", as_path=(31632, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=32033, prefix="1.2.3.0/24", as_path=(32033, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=33001, prefix="1.2.3.0/24", as_path=(33001, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=33442, prefix="1.2.3.0/24", as_path=(33442, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35452, prefix="1.2.3.0/24", as_path=(35452, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35928, prefix="1.2.3.0/24", as_path=(35928, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=36224, prefix="1.2.3.0/24", as_path=(36224, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=38936, prefix="1.2.3.0/24", as_path=(38936, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39173, prefix="1.2.3.0/24", as_path=(39173, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39461, prefix="1.2.3.0/24", as_path=(39461, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39552, prefix="1.2.3.0/24", as_path=(39552, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39957, prefix="1.2.3.0/24", as_path=(39957, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41021, prefix="1.2.3.0/24", as_path=(41021, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41373, prefix="1.2.3.0/24", as_path=(41373, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41380, prefix="1.2.3.0/24", as_path=(41380, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41919, prefix="1.2.3.0/24", as_path=(41919, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41988, prefix="1.2.3.0/24", as_path=(41988, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42536, prefix="1.2.3.0/24", as_path=(42536, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43014, prefix="1.2.3.0/24", as_path=(43014, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43259, prefix="1.2.3.0/24", as_path=(43259, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43453, prefix="1.2.3.0/24", as_path=(43453, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43949, prefix="1.2.3.0/24", as_path=(43949, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44008, prefix="1.2.3.0/24", as_path=(44008, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44268, prefix="1.2.3.0/24", as_path=(44268, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44371, prefix="1.2.3.0/24", as_path=(44371, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44480, prefix="1.2.3.0/24", as_path=(44480, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44617, prefix="1.2.3.0/24", as_path=(44617, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47113, prefix="1.2.3.0/24", as_path=(47113, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47534, prefix="1.2.3.0/24", as_path=(47534, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48549, prefix="1.2.3.0/24", as_path=(48549, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48639, prefix="1.2.3.0/24", as_path=(48639, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49318, prefix="1.2.3.0/24", as_path=(49318, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50203, prefix="1.2.3.0/24", as_path=(50203, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50287, prefix="1.2.3.0/24", as_path=(50287, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50826, prefix="1.2.3.0/24", as_path=(50826, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51953, prefix="1.2.3.0/24", as_path=(51953, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56644, prefix="1.2.3.0/24", as_path=(56644, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56745, prefix="1.2.3.0/24", as_path=(56745, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57002, prefix="1.2.3.0/24", as_path=(57002, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57377, prefix="1.2.3.0/24", as_path=(57377, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59345, prefix="1.2.3.0/24", as_path=(59345, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59445, prefix="1.2.3.0/24", as_path=(59445, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60677, prefix="1.2.3.0/24", as_path=(60677, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60925, prefix="1.2.3.0/24", as_path=(60925, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60962, prefix="1.2.3.0/24", as_path=(60962, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=63112, prefix="1.2.3.0/24", as_path=(63112, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=63399, prefix="1.2.3.0/24", as_path=(63399, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197122, prefix="1.2.3.0/24", as_path=(197122, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197409, prefix="1.2.3.0/24", as_path=(197409, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197568, prefix="1.2.3.0/24", as_path=(197568, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198032, prefix="1.2.3.0/24", as_path=(198032, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198189, prefix="1.2.3.0/24", as_path=(198189, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198386, prefix="1.2.3.0/24", as_path=(198386, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199055, prefix="1.2.3.0/24", as_path=(199055, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199262, prefix="1.2.3.0/24", as_path=(199262, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199462, prefix="1.2.3.0/24", as_path=(199462, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200614, prefix="1.2.3.0/24", as_path=(200614, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200870, prefix="1.2.3.0/24", as_path=(200870, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200961, prefix="1.2.3.0/24", as_path=(200961, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201528, prefix="1.2.3.0/24", as_path=(201528, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201529, prefix="1.2.3.0/24", as_path=(201529, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201536, prefix="1.2.3.0/24", as_path=(201536, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201971, prefix="1.2.3.0/24", as_path=(201971, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202364, prefix="1.2.3.0/24", as_path=(202364, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202466, prefix="1.2.3.0/24", as_path=(202466, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202679, prefix="1.2.3.0/24", as_path=(202679, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202907, prefix="1.2.3.0/24", as_path=(202907, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204045, prefix="1.2.3.0/24", as_path=(204045, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204819, prefix="1.2.3.0/24", as_path=(204819, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205006, prefix="1.2.3.0/24", as_path=(205006, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205080, prefix="1.2.3.0/24", as_path=(205080, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205114, prefix="1.2.3.0/24", as_path=(205114, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205514, prefix="1.2.3.0/24", as_path=(205514, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205693, prefix="1.2.3.0/24", as_path=(205693, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206132, prefix="1.2.3.0/24", as_path=(206132, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206166, prefix="1.2.3.0/24", as_path=(206166, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206237, prefix="1.2.3.0/24", as_path=(206237, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206289, prefix="1.2.3.0/24", as_path=(206289, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206335, prefix="1.2.3.0/24", as_path=(206335, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206467, prefix="1.2.3.0/24", as_path=(206467, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206686, prefix="1.2.3.0/24", as_path=(206686, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206773, prefix="1.2.3.0/24", as_path=(206773, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207072, prefix="1.2.3.0/24", as_path=(207072, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207087, prefix="1.2.3.0/24", as_path=(207087, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207120, prefix="1.2.3.0/24", as_path=(207120, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207245, prefix="1.2.3.0/24", as_path=(207245, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207310, prefix="1.2.3.0/24", as_path=(207310, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207312, prefix="1.2.3.0/24", as_path=(207312, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207552, prefix="1.2.3.0/24", as_path=(207552, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209997, prefix="1.2.3.0/24", as_path=(209997, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210326, prefix="1.2.3.0/24", as_path=(210326, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211303, prefix="1.2.3.0/24", as_path=(211303, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211389, prefix="1.2.3.0/24", as_path=(211389, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212329, prefix="1.2.3.0/24", as_path=(212329, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212565, prefix="1.2.3.0/24", as_path=(212565, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=394265, prefix="1.2.3.0/24", as_path=(394265, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=394583, prefix="1.2.3.0/24", as_path=(394583, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=394731, prefix="1.2.3.0/24", as_path=(394731, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=395971, prefix="1.2.3.0/24", as_path=(395971, 2856, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=4809, prefix="1.2.3.0/24", as_path=(4809, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12455, prefix="1.2.3.0/24", as_path=(12455, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15808, prefix="1.2.3.0/24", as_path=(15808, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15964, prefix="1.2.3.0/24", as_path=(15964, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=16637, prefix="1.2.3.0/24", as_path=(16637, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=19551, prefix="1.2.3.0/24", as_path=(19551, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20598, prefix="1.2.3.0/24", as_path=(20598, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20940, prefix="1.2.3.0/24", as_path=(20940, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21491, prefix="1.2.3.0/24", as_path=(21491, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=22355, prefix="1.2.3.0/24", as_path=(22355, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=22690, prefix="1.2.3.0/24", as_path=(22690, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24429, prefix="1.2.3.0/24", as_path=(24429, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25163, prefix="1.2.3.0/24", as_path=(25163, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25543, prefix="1.2.3.0/24", as_path=(25543, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25695, prefix="1.2.3.0/24", as_path=(25695, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=30619, prefix="1.2.3.0/24", as_path=(30619, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=30990, prefix="1.2.3.0/24", as_path=(30990, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=30998, prefix="1.2.3.0/24", as_path=(30998, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=30999, prefix="1.2.3.0/24", as_path=(30999, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31856, prefix="1.2.3.0/24", as_path=(31856, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35091, prefix="1.2.3.0/24", as_path=(35091, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=36866, prefix="1.2.3.0/24", as_path=(36866, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=36914, prefix="1.2.3.0/24", as_path=(36914, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=36920, prefix="1.2.3.0/24", as_path=(36920, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=36930, prefix="1.2.3.0/24", as_path=(36930, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=36944, prefix="1.2.3.0/24", as_path=(36944, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=36958, prefix="1.2.3.0/24", as_path=(36958, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=36963, prefix="1.2.3.0/24", as_path=(36963, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37004, prefix="1.2.3.0/24", as_path=(37004, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37014, prefix="1.2.3.0/24", as_path=(37014, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37018, prefix="1.2.3.0/24", as_path=(37018, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37037, prefix="1.2.3.0/24", as_path=(37037, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37053, prefix="1.2.3.0/24", as_path=(37053, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37057, prefix="1.2.3.0/24", as_path=(37057, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37098, prefix="1.2.3.0/24", as_path=(37098, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37105, prefix="1.2.3.0/24", as_path=(37105, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37110, prefix="1.2.3.0/24", as_path=(37110, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37126, prefix="1.2.3.0/24", as_path=(37126, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37154, prefix="1.2.3.0/24", as_path=(37154, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37168, prefix="1.2.3.0/24", as_path=(37168, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37183, prefix="1.2.3.0/24", as_path=(37183, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37184, prefix="1.2.3.0/24", as_path=(37184, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37185, prefix="1.2.3.0/24", as_path=(37185, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37187, prefix="1.2.3.0/24", as_path=(37187, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37204, prefix="1.2.3.0/24", as_path=(37204, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37228, prefix="1.2.3.0/24", as_path=(37228, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37236, prefix="1.2.3.0/24", as_path=(37236, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37248, prefix="1.2.3.0/24", as_path=(37248, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37273, prefix="1.2.3.0/24", as_path=(37273, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37286, prefix="1.2.3.0/24", as_path=(37286, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37287, prefix="1.2.3.0/24", as_path=(37287, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37294, prefix="1.2.3.0/24", as_path=(37294, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37308, prefix="1.2.3.0/24", as_path=(37308, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37315, prefix="1.2.3.0/24", as_path=(37315, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37340, prefix="1.2.3.0/24", as_path=(37340, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37342, prefix="1.2.3.0/24", as_path=(37342, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37358, prefix="1.2.3.0/24", as_path=(37358, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37371, prefix="1.2.3.0/24", as_path=(37371, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37540, prefix="1.2.3.0/24", as_path=(37540, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37545, prefix="1.2.3.0/24", as_path=(37545, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37546, prefix="1.2.3.0/24", as_path=(37546, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37564, prefix="1.2.3.0/24", as_path=(37564, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37586, prefix="1.2.3.0/24", as_path=(37586, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37605, prefix="1.2.3.0/24", as_path=(37605, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37614, prefix="1.2.3.0/24", as_path=(37614, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37622, prefix="1.2.3.0/24", as_path=(37622, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37688, prefix="1.2.3.0/24", as_path=(37688, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61317, prefix="1.2.3.0/24", as_path=(61317, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327768, prefix="1.2.3.0/24", as_path=(327768, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327794, prefix="1.2.3.0/24", as_path=(327794, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327861, prefix="1.2.3.0/24", as_path=(327861, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328171, prefix="1.2.3.0/24", as_path=(328171, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328266, prefix="1.2.3.0/24", as_path=(328266, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328460, prefix="1.2.3.0/24", as_path=(328460, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328518, prefix="1.2.3.0/24", as_path=(328518, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328555, prefix="1.2.3.0/24", as_path=(328555, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328564, prefix="1.2.3.0/24", as_path=(328564, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328576, prefix="1.2.3.0/24", as_path=(328576, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328644, prefix="1.2.3.0/24", as_path=(328644, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328646, prefix="1.2.3.0/24", as_path=(328646, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328658, prefix="1.2.3.0/24", as_path=(328658, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328720, prefix="1.2.3.0/24", as_path=(328720, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328748, prefix="1.2.3.0/24", as_path=(328748, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328825, prefix="1.2.3.0/24", as_path=(328825, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328901, prefix="1.2.3.0/24", as_path=(328901, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328919, prefix="1.2.3.0/24", as_path=(328919, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328938, prefix="1.2.3.0/24", as_path=(328938, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328971, prefix="1.2.3.0/24", as_path=(328971, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=329051, prefix="1.2.3.0/24", as_path=(329051, 37662, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13335,
        prefix="1.2.3.0/24",
        as_path=(13335, 327708, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=36873,
        prefix="1.2.3.0/24",
        as_path=(36873, 327708, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=36926,
        prefix="1.2.3.0/24",
        as_path=(36926, 327708, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37020,
        prefix="1.2.3.0/24",
        as_path=(37020, 327708, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37075,
        prefix="1.2.3.0/24",
        as_path=(37075, 327708, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37133,
        prefix="1.2.3.0/24",
        as_path=(37133, 327708, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37287,
        prefix="1.2.3.0/24",
        as_path=(37287, 327708, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37303,
        prefix="1.2.3.0/24",
        as_path=(37303, 327708, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37343,
        prefix="1.2.3.0/24",
        as_path=(37343, 327708, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37414,
        prefix="1.2.3.0/24",
        as_path=(37414, 327708, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37440,
        prefix="1.2.3.0/24",
        as_path=(37440, 327708, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37531,
        prefix="1.2.3.0/24",
        as_path=(37531, 327708, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37550,
        prefix="1.2.3.0/24",
        as_path=(37550, 327708, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37616,
        prefix="1.2.3.0/24",
        as_path=(37616, 327708, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=63293,
        prefix="1.2.3.0/24",
        as_path=(63293, 327708, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327738,
        prefix="1.2.3.0/24",
        as_path=(327738, 327708, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327875,
        prefix="1.2.3.0/24",
        as_path=(327875, 327708, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327941,
        prefix="1.2.3.0/24",
        as_path=(327941, 327708, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328300,
        prefix="1.2.3.0/24",
        as_path=(328300, 327708, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328452,
        prefix="1.2.3.0/24",
        as_path=(328452, 327708, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328500,
        prefix="1.2.3.0/24",
        as_path=(328500, 327708, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8200, prefix="1.2.3.0/24", as_path=(8200, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8393, prefix="1.2.3.0/24", as_path=(8393, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12764, prefix="1.2.3.0/24", as_path=(12764, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13335, prefix="1.2.3.0/24", as_path=(13335, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15549, prefix="1.2.3.0/24", as_path=(15549, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20578, prefix="1.2.3.0/24", as_path=(20578, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21282, prefix="1.2.3.0/24", as_path=(21282, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=22764, prefix="1.2.3.0/24", as_path=(22764, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35104, prefix="1.2.3.0/24", as_path=(35104, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35673, prefix="1.2.3.0/24", as_path=(35673, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39510, prefix="1.2.3.0/24", as_path=(39510, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39824, prefix="1.2.3.0/24", as_path=(39824, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41371, prefix="1.2.3.0/24", as_path=(41371, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41413, prefix="1.2.3.0/24", as_path=(41413, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41419, prefix="1.2.3.0/24", as_path=(41419, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42770, prefix="1.2.3.0/24", as_path=(42770, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43370, prefix="1.2.3.0/24", as_path=(43370, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43601, prefix="1.2.3.0/24", as_path=(43601, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43999, prefix="1.2.3.0/24", as_path=(43999, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44653, prefix="1.2.3.0/24", as_path=(44653, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48007, prefix="1.2.3.0/24", as_path=(48007, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48450, prefix="1.2.3.0/24", as_path=(48450, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50386, prefix="1.2.3.0/24", as_path=(50386, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50482, prefix="1.2.3.0/24", as_path=(50482, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51340, prefix="1.2.3.0/24", as_path=(51340, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51979, prefix="1.2.3.0/24", as_path=(51979, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56698, prefix="1.2.3.0/24", as_path=(56698, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57466, prefix="1.2.3.0/24", as_path=(57466, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58033, prefix="1.2.3.0/24", as_path=(58033, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59583, prefix="1.2.3.0/24", as_path=(59583, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60186, prefix="1.2.3.0/24", as_path=(60186, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60286, prefix="1.2.3.0/24", as_path=(60286, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60708, prefix="1.2.3.0/24", as_path=(60708, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198787, prefix="1.2.3.0/24", as_path=(198787, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199524, prefix="1.2.3.0/24", as_path=(199524, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203481, prefix="1.2.3.0/24", as_path=(203481, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203886, prefix="1.2.3.0/24", as_path=(203886, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204514, prefix="1.2.3.0/24", as_path=(204514, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204706, prefix="1.2.3.0/24", as_path=(204706, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206528, prefix="1.2.3.0/24", as_path=(206528, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207966, prefix="1.2.3.0/24", as_path=(207966, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208356, prefix="1.2.3.0/24", as_path=(208356, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208450, prefix="1.2.3.0/24", as_path=(208450, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209416, prefix="1.2.3.0/24", as_path=(209416, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209665, prefix="1.2.3.0/24", as_path=(209665, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211971, prefix="1.2.3.0/24", as_path=(211971, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212999, prefix="1.2.3.0/24", as_path=(212999, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=213048, prefix="1.2.3.0/24", as_path=(213048, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=213146, prefix="1.2.3.0/24", as_path=(213146, 9198, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=17666, prefix="1.2.3.0/24", as_path=(17666, 45352, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=45331, prefix="1.2.3.0/24", as_path=(45331, 45352, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=45887, prefix="1.2.3.0/24", as_path=(45887, 45352, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=55855, prefix="1.2.3.0/24", as_path=(55855, 45352, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58983, prefix="1.2.3.0/24", as_path=(58983, 45352, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61317, prefix="1.2.3.0/24", as_path=(61317, 45352, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=133437, prefix="1.2.3.0/24", as_path=(133437, 45352, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=133889, prefix="1.2.3.0/24", as_path=(133889, 45352, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=134066, prefix="1.2.3.0/24", as_path=(134066, 45352, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=134190, prefix="1.2.3.0/24", as_path=(134190, 45352, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=135542, prefix="1.2.3.0/24", as_path=(135542, 45352, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=137240, prefix="1.2.3.0/24", as_path=(137240, 45352, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=137510, prefix="1.2.3.0/24", as_path=(137510, 45352, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=138148, prefix="1.2.3.0/24", as_path=(138148, 45352, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=140344, prefix="1.2.3.0/24", as_path=(140344, 45352, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=141371, prefix="1.2.3.0/24", as_path=(141371, 45352, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=141424, prefix="1.2.3.0/24", as_path=(141424, 45352, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=6761, prefix="1.2.3.0/24", as_path=(6761, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=14576, prefix="1.2.3.0/24", as_path=(14576, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29172, prefix="1.2.3.0/24", as_path=(29172, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35802, prefix="1.2.3.0/24", as_path=(35802, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39697, prefix="1.2.3.0/24", as_path=(39697, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39711, prefix="1.2.3.0/24", as_path=(39711, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=40676, prefix="1.2.3.0/24", as_path=(40676, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42069, prefix="1.2.3.0/24", as_path=(42069, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42219, prefix="1.2.3.0/24", as_path=(42219, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42834, prefix="1.2.3.0/24", as_path=(42834, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43952, prefix="1.2.3.0/24", as_path=(43952, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44903, prefix="1.2.3.0/24", as_path=(44903, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44915, prefix="1.2.3.0/24", as_path=(44915, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47168, prefix="1.2.3.0/24", as_path=(47168, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47677, prefix="1.2.3.0/24", as_path=(47677, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48197, prefix="1.2.3.0/24", as_path=(48197, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48614, prefix="1.2.3.0/24", as_path=(48614, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49347, prefix="1.2.3.0/24", as_path=(49347, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49684, prefix="1.2.3.0/24", as_path=(49684, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50002, prefix="1.2.3.0/24", as_path=(50002, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51668, prefix="1.2.3.0/24", as_path=(51668, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51698, prefix="1.2.3.0/24", as_path=(51698, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56903, prefix="1.2.3.0/24", as_path=(56903, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57212, prefix="1.2.3.0/24", as_path=(57212, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57658, prefix="1.2.3.0/24", as_path=(57658, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57857, prefix="1.2.3.0/24", as_path=(57857, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57906, prefix="1.2.3.0/24", as_path=(57906, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58084, prefix="1.2.3.0/24", as_path=(58084, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58116, prefix="1.2.3.0/24", as_path=(58116, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58147, prefix="1.2.3.0/24", as_path=(58147, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58207, prefix="1.2.3.0/24", as_path=(58207, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59452, prefix="1.2.3.0/24", as_path=(59452, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61178, prefix="1.2.3.0/24", as_path=(61178, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61285, prefix="1.2.3.0/24", as_path=(61285, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61378, prefix="1.2.3.0/24", as_path=(61378, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62316, prefix="1.2.3.0/24", as_path=(62316, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62382, prefix="1.2.3.0/24", as_path=(62382, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198437, prefix="1.2.3.0/24", as_path=(198437, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198615, prefix="1.2.3.0/24", as_path=(198615, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198762, prefix="1.2.3.0/24", as_path=(198762, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199194, prefix="1.2.3.0/24", as_path=(199194, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200389, prefix="1.2.3.0/24", as_path=(200389, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200952, prefix="1.2.3.0/24", as_path=(200952, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201312, prefix="1.2.3.0/24", as_path=(201312, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201812, prefix="1.2.3.0/24", as_path=(201812, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202508, prefix="1.2.3.0/24", as_path=(202508, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202768, prefix="1.2.3.0/24", as_path=(202768, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202804, prefix="1.2.3.0/24", as_path=(202804, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203444, prefix="1.2.3.0/24", as_path=(203444, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203510, prefix="1.2.3.0/24", as_path=(203510, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203714, prefix="1.2.3.0/24", as_path=(203714, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203891, prefix="1.2.3.0/24", as_path=(203891, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204198, prefix="1.2.3.0/24", as_path=(204198, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205126, prefix="1.2.3.0/24", as_path=(205126, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205305, prefix="1.2.3.0/24", as_path=(205305, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206668, prefix="1.2.3.0/24", as_path=(206668, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206708, prefix="1.2.3.0/24", as_path=(206708, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206955, prefix="1.2.3.0/24", as_path=(206955, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207104, prefix="1.2.3.0/24", as_path=(207104, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209599, prefix="1.2.3.0/24", as_path=(209599, 49063, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(reporting_asn=3067, prefix="1.2.3.0/24", as_path=(3067, 5713, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=5734, prefix="1.2.3.0/24", as_path=(5734, 5713, 29452)).as_path
)
reports_path_list.append(
    Report(reporting_asn=7020, prefix="1.2.3.0/24", as_path=(7020, 5713, 29452)).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=11744, prefix="1.2.3.0/24", as_path=(11744, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=14115, prefix="1.2.3.0/24", as_path=(14115, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=19551, prefix="1.2.3.0/24", as_path=(19551, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=23058, prefix="1.2.3.0/24", as_path=(23058, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25818, prefix="1.2.3.0/24", as_path=(25818, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29606, prefix="1.2.3.0/24", as_path=(29606, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=36874, prefix="1.2.3.0/24", as_path=(36874, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37007, prefix="1.2.3.0/24", as_path=(37007, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37014, prefix="1.2.3.0/24", as_path=(37014, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37055, prefix="1.2.3.0/24", as_path=(37055, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37159, prefix="1.2.3.0/24", as_path=(37159, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37239, prefix="1.2.3.0/24", as_path=(37239, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37251, prefix="1.2.3.0/24", as_path=(37251, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37302, prefix="1.2.3.0/24", as_path=(37302, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37356, prefix="1.2.3.0/24", as_path=(37356, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37357, prefix="1.2.3.0/24", as_path=(37357, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37358, prefix="1.2.3.0/24", as_path=(37358, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37402, prefix="1.2.3.0/24", as_path=(37402, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37428, prefix="1.2.3.0/24", as_path=(37428, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37457, prefix="1.2.3.0/24", as_path=(37457, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37519, prefix="1.2.3.0/24", as_path=(37519, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37675, prefix="1.2.3.0/24", as_path=(37675, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37678, prefix="1.2.3.0/24", as_path=(37678, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327693, prefix="1.2.3.0/24", as_path=(327693, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327804, prefix="1.2.3.0/24", as_path=(327804, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327943, prefix="1.2.3.0/24", as_path=(327943, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328039, prefix="1.2.3.0/24", as_path=(328039, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328122, prefix="1.2.3.0/24", as_path=(328122, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328349, prefix="1.2.3.0/24", as_path=(328349, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328422, prefix="1.2.3.0/24", as_path=(328422, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328464, prefix="1.2.3.0/24", as_path=(328464, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328471, prefix="1.2.3.0/24", as_path=(328471, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328512, prefix="1.2.3.0/24", as_path=(328512, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328523, prefix="1.2.3.0/24", as_path=(328523, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328598, prefix="1.2.3.0/24", as_path=(328598, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328660, prefix="1.2.3.0/24", as_path=(328660, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328712, prefix="1.2.3.0/24", as_path=(328712, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328713, prefix="1.2.3.0/24", as_path=(328713, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328837, prefix="1.2.3.0/24", as_path=(328837, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328848, prefix="1.2.3.0/24", as_path=(328848, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328855, prefix="1.2.3.0/24", as_path=(328855, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8926, prefix="1.2.3.0/24", as_path=(8926, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12442, prefix="1.2.3.0/24", as_path=(12442, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13150, prefix="1.2.3.0/24", as_path=(13150, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=16157, prefix="1.2.3.0/24", as_path=(16157, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=16199, prefix="1.2.3.0/24", as_path=(16199, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21368, prefix="1.2.3.0/24", as_path=(21368, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25378, prefix="1.2.3.0/24", as_path=(25378, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25454, prefix="1.2.3.0/24", as_path=(25454, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=28763, prefix="1.2.3.0/24", as_path=(28763, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=28853, prefix="1.2.3.0/24", as_path=(28853, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29267, prefix="1.2.3.0/24", as_path=(29267, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29652, prefix="1.2.3.0/24", as_path=(29652, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31038, prefix="1.2.3.0/24", as_path=(31038, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31362, prefix="1.2.3.0/24", as_path=(31362, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31454, prefix="1.2.3.0/24", as_path=(31454, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34358, prefix="1.2.3.0/24", as_path=(34358, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34551, prefix="1.2.3.0/24", as_path=(34551, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34711, prefix="1.2.3.0/24", as_path=(34711, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34714, prefix="1.2.3.0/24", as_path=(34714, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34795, prefix="1.2.3.0/24", as_path=(34795, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34904, prefix="1.2.3.0/24", as_path=(34904, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35351, prefix="1.2.3.0/24", as_path=(35351, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35386, prefix="1.2.3.0/24", as_path=(35386, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35478, prefix="1.2.3.0/24", as_path=(35478, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35664, prefix="1.2.3.0/24", as_path=(35664, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35725, prefix="1.2.3.0/24", as_path=(35725, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39016, prefix="1.2.3.0/24", as_path=(39016, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39081, prefix="1.2.3.0/24", as_path=(39081, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39224, prefix="1.2.3.0/24", as_path=(39224, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39668, prefix="1.2.3.0/24", as_path=(39668, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39712, prefix="1.2.3.0/24", as_path=(39712, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39903, prefix="1.2.3.0/24", as_path=(39903, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41043, prefix="1.2.3.0/24", as_path=(41043, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41087, prefix="1.2.3.0/24", as_path=(41087, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41492, prefix="1.2.3.0/24", as_path=(41492, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41638, prefix="1.2.3.0/24", as_path=(41638, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41859, prefix="1.2.3.0/24", as_path=(41859, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41950, prefix="1.2.3.0/24", as_path=(41950, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42405, prefix="1.2.3.0/24", as_path=(42405, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42640, prefix="1.2.3.0/24", as_path=(42640, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42712, prefix="1.2.3.0/24", as_path=(42712, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42731, prefix="1.2.3.0/24", as_path=(42731, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42890, prefix="1.2.3.0/24", as_path=(42890, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42939, prefix="1.2.3.0/24", as_path=(42939, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43283, prefix="1.2.3.0/24", as_path=(43283, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43474, prefix="1.2.3.0/24", as_path=(43474, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43807, prefix="1.2.3.0/24", as_path=(43807, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43840, prefix="1.2.3.0/24", as_path=(43840, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43925, prefix="1.2.3.0/24", as_path=(43925, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44106, prefix="1.2.3.0/24", as_path=(44106, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44157, prefix="1.2.3.0/24", as_path=(44157, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44184, prefix="1.2.3.0/24", as_path=(44184, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47890, prefix="1.2.3.0/24", as_path=(47890, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48161, prefix="1.2.3.0/24", as_path=(48161, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48537, prefix="1.2.3.0/24", as_path=(48537, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48669, prefix="1.2.3.0/24", as_path=(48669, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48836, prefix="1.2.3.0/24", as_path=(48836, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48865, prefix="1.2.3.0/24", as_path=(48865, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48881, prefix="1.2.3.0/24", as_path=(48881, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49021, prefix="1.2.3.0/24", as_path=(49021, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49150, prefix="1.2.3.0/24", as_path=(49150, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49164, prefix="1.2.3.0/24", as_path=(49164, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49169, prefix="1.2.3.0/24", as_path=(49169, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49203, prefix="1.2.3.0/24", as_path=(49203, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49266, prefix="1.2.3.0/24", as_path=(49266, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49295, prefix="1.2.3.0/24", as_path=(49295, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49384, prefix="1.2.3.0/24", as_path=(49384, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49645, prefix="1.2.3.0/24", as_path=(49645, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49907, prefix="1.2.3.0/24", as_path=(49907, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50232, prefix="1.2.3.0/24", as_path=(50232, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50369, prefix="1.2.3.0/24", as_path=(50369, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50682, prefix="1.2.3.0/24", as_path=(50682, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50887, prefix="1.2.3.0/24", as_path=(50887, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50991, prefix="1.2.3.0/24", as_path=(50991, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51094, prefix="1.2.3.0/24", as_path=(51094, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51098, prefix="1.2.3.0/24", as_path=(51098, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51102, prefix="1.2.3.0/24", as_path=(51102, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51177, prefix="1.2.3.0/24", as_path=(51177, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51284, prefix="1.2.3.0/24", as_path=(51284, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51637, prefix="1.2.3.0/24", as_path=(51637, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51799, prefix="1.2.3.0/24", as_path=(51799, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51854, prefix="1.2.3.0/24", as_path=(51854, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51911, prefix="1.2.3.0/24", as_path=(51911, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=52159, prefix="1.2.3.0/24", as_path=(52159, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=52189, prefix="1.2.3.0/24", as_path=(52189, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56417, prefix="1.2.3.0/24", as_path=(56417, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56750, prefix="1.2.3.0/24", as_path=(56750, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56885, prefix="1.2.3.0/24", as_path=(56885, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57060, prefix="1.2.3.0/24", as_path=(57060, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57082, prefix="1.2.3.0/24", as_path=(57082, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57126, prefix="1.2.3.0/24", as_path=(57126, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57180, prefix="1.2.3.0/24", as_path=(57180, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57316, prefix="1.2.3.0/24", as_path=(57316, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57322, prefix="1.2.3.0/24", as_path=(57322, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57446, prefix="1.2.3.0/24", as_path=(57446, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57464, prefix="1.2.3.0/24", as_path=(57464, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57647, prefix="1.2.3.0/24", as_path=(57647, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57746, prefix="1.2.3.0/24", as_path=(57746, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57785, prefix="1.2.3.0/24", as_path=(57785, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57992, prefix="1.2.3.0/24", as_path=(57992, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58023, prefix="1.2.3.0/24", as_path=(58023, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58043, prefix="1.2.3.0/24", as_path=(58043, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58052, prefix="1.2.3.0/24", as_path=(58052, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58170, prefix="1.2.3.0/24", as_path=(58170, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58174, prefix="1.2.3.0/24", as_path=(58174, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59398, prefix="1.2.3.0/24", as_path=(59398, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59400, prefix="1.2.3.0/24", as_path=(59400, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59938, prefix="1.2.3.0/24", as_path=(59938, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60026, prefix="1.2.3.0/24", as_path=(60026, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60033, prefix="1.2.3.0/24", as_path=(60033, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60100, prefix="1.2.3.0/24", as_path=(60100, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60104, prefix="1.2.3.0/24", as_path=(60104, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60201, prefix="1.2.3.0/24", as_path=(60201, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60615, prefix="1.2.3.0/24", as_path=(60615, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60694, prefix="1.2.3.0/24", as_path=(60694, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60907, prefix="1.2.3.0/24", as_path=(60907, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61204, prefix="1.2.3.0/24", as_path=(61204, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61353, prefix="1.2.3.0/24", as_path=(61353, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61412, prefix="1.2.3.0/24", as_path=(61412, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62030, prefix="1.2.3.0/24", as_path=(62030, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62032, prefix="1.2.3.0/24", as_path=(62032, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62053, prefix="1.2.3.0/24", as_path=(62053, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62151, prefix="1.2.3.0/24", as_path=(62151, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62162, prefix="1.2.3.0/24", as_path=(62162, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62315, prefix="1.2.3.0/24", as_path=(62315, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62343, prefix="1.2.3.0/24", as_path=(62343, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198914, prefix="1.2.3.0/24", as_path=(198914, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199498, prefix="1.2.3.0/24", as_path=(199498, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202779, prefix="1.2.3.0/24", as_path=(202779, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203574, prefix="1.2.3.0/24", as_path=(203574, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203929, prefix="1.2.3.0/24", as_path=(203929, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205275, prefix="1.2.3.0/24", as_path=(205275, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205332, prefix="1.2.3.0/24", as_path=(205332, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206382, prefix="1.2.3.0/24", as_path=(206382, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207752, prefix="1.2.3.0/24", as_path=(207752, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208179, prefix="1.2.3.0/24", as_path=(208179, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210713, prefix="1.2.3.0/24", as_path=(210713, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210840, prefix="1.2.3.0/24", as_path=(210840, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211412, prefix="1.2.3.0/24", as_path=(211412, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211663, prefix="1.2.3.0/24", as_path=(211663, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212929, prefix="1.2.3.0/24", as_path=(212929, 9050, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8200,
        prefix="1.2.3.0/24",
        as_path=(8200, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31465,
        prefix="1.2.3.0/24",
        as_path=(31465, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31525,
        prefix="1.2.3.0/24",
        as_path=(31525, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35104,
        prefix="1.2.3.0/24",
        as_path=(35104, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35673,
        prefix="1.2.3.0/24",
        as_path=(35673, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39318,
        prefix="1.2.3.0/24",
        as_path=(39318, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39824,
        prefix="1.2.3.0/24",
        as_path=(39824, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41007,
        prefix="1.2.3.0/24",
        as_path=(41007, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41124,
        prefix="1.2.3.0/24",
        as_path=(41124, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41284,
        prefix="1.2.3.0/24",
        as_path=(41284, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41371,
        prefix="1.2.3.0/24",
        as_path=(41371, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41800,
        prefix="1.2.3.0/24",
        as_path=(41800, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43370,
        prefix="1.2.3.0/24",
        as_path=(43370, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48096,
        prefix="1.2.3.0/24",
        as_path=(48096, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48716,
        prefix="1.2.3.0/24",
        as_path=(48716, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51162,
        prefix="1.2.3.0/24",
        as_path=(51162, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51997,
        prefix="1.2.3.0/24",
        as_path=(51997, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57013,
        prefix="1.2.3.0/24",
        as_path=(57013, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57826,
        prefix="1.2.3.0/24",
        as_path=(57826, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59443,
        prefix="1.2.3.0/24",
        as_path=(59443, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60286,
        prefix="1.2.3.0/24",
        as_path=(60286, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61367,
        prefix="1.2.3.0/24",
        as_path=(61367, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61392,
        prefix="1.2.3.0/24",
        as_path=(61392, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197686,
        prefix="1.2.3.0/24",
        as_path=(197686, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200349,
        prefix="1.2.3.0/24",
        as_path=(200349, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200590,
        prefix="1.2.3.0/24",
        as_path=(200590, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200688,
        prefix="1.2.3.0/24",
        as_path=(200688, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200962,
        prefix="1.2.3.0/24",
        as_path=(200962, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202293,
        prefix="1.2.3.0/24",
        as_path=(202293, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205516,
        prefix="1.2.3.0/24",
        as_path=(205516, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205559,
        prefix="1.2.3.0/24",
        as_path=(205559, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206528,
        prefix="1.2.3.0/24",
        as_path=(206528, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207446,
        prefix="1.2.3.0/24",
        as_path=(207446, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207966,
        prefix="1.2.3.0/24",
        as_path=(207966, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208448,
        prefix="1.2.3.0/24",
        as_path=(208448, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208946,
        prefix="1.2.3.0/24",
        as_path=(208946, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211644,
        prefix="1.2.3.0/24",
        as_path=(211644, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212086,
        prefix="1.2.3.0/24",
        as_path=(212086, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212999,
        prefix="1.2.3.0/24",
        as_path=(212999, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=6893, prefix="1.2.3.0/24", as_path=(6893, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=9036, prefix="1.2.3.0/24", as_path=(9036, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12654, prefix="1.2.3.0/24", as_path=(12654, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13273, prefix="1.2.3.0/24", as_path=(13273, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15576, prefix="1.2.3.0/24", as_path=(15576, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=16073, prefix="1.2.3.0/24", as_path=(16073, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20766, prefix="1.2.3.0/24", as_path=(20766, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21247, prefix="1.2.3.0/24", as_path=(21247, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24843, prefix="1.2.3.0/24", as_path=(24843, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24904, prefix="1.2.3.0/24", as_path=(24904, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25057, prefix="1.2.3.0/24", as_path=(25057, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34783, prefix="1.2.3.0/24", as_path=(34783, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35616, prefix="1.2.3.0/24", as_path=(35616, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39271, prefix="1.2.3.0/24", as_path=(39271, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41064, prefix="1.2.3.0/24", as_path=(41064, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41090, prefix="1.2.3.0/24", as_path=(41090, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41765, prefix="1.2.3.0/24", as_path=(41765, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42609, prefix="1.2.3.0/24", as_path=(42609, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42929, prefix="1.2.3.0/24", as_path=(42929, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43930, prefix="1.2.3.0/24", as_path=(43930, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44583, prefix="1.2.3.0/24", as_path=(44583, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44821, prefix="1.2.3.0/24", as_path=(44821, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48072, prefix="1.2.3.0/24", as_path=(48072, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48490, prefix="1.2.3.0/24", as_path=(48490, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48817, prefix="1.2.3.0/24", as_path=(48817, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48920, prefix="1.2.3.0/24", as_path=(48920, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49537, prefix="1.2.3.0/24", as_path=(49537, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49763, prefix="1.2.3.0/24", as_path=(49763, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49923, prefix="1.2.3.0/24", as_path=(49923, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50087, prefix="1.2.3.0/24", as_path=(50087, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50618, prefix="1.2.3.0/24", as_path=(50618, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50954, prefix="1.2.3.0/24", as_path=(50954, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51083, prefix="1.2.3.0/24", as_path=(51083, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51220, prefix="1.2.3.0/24", as_path=(51220, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51257, prefix="1.2.3.0/24", as_path=(51257, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51335, prefix="1.2.3.0/24", as_path=(51335, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51588, prefix="1.2.3.0/24", as_path=(51588, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=52126, prefix="1.2.3.0/24", as_path=(52126, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56693, prefix="1.2.3.0/24", as_path=(56693, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57119, prefix="1.2.3.0/24", as_path=(57119, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57734, prefix="1.2.3.0/24", as_path=(57734, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58308, prefix="1.2.3.0/24", as_path=(58308, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60362, prefix="1.2.3.0/24", as_path=(60362, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61319, prefix="1.2.3.0/24", as_path=(61319, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62000, prefix="1.2.3.0/24", as_path=(62000, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62242, prefix="1.2.3.0/24", as_path=(62242, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197205, prefix="1.2.3.0/24", as_path=(197205, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197465, prefix="1.2.3.0/24", as_path=(197465, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197696, prefix="1.2.3.0/24", as_path=(197696, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198184, prefix="1.2.3.0/24", as_path=(198184, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198385, prefix="1.2.3.0/24", as_path=(198385, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199167, prefix="1.2.3.0/24", as_path=(199167, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199277, prefix="1.2.3.0/24", as_path=(199277, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199383, prefix="1.2.3.0/24", as_path=(199383, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199571, prefix="1.2.3.0/24", as_path=(199571, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199997, prefix="1.2.3.0/24", as_path=(199997, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200339, prefix="1.2.3.0/24", as_path=(200339, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200748, prefix="1.2.3.0/24", as_path=(200748, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201313, prefix="1.2.3.0/24", as_path=(201313, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202139, prefix="1.2.3.0/24", as_path=(202139, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203683, prefix="1.2.3.0/24", as_path=(203683, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206782, prefix="1.2.3.0/24", as_path=(206782, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207216, prefix="1.2.3.0/24", as_path=(207216, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207324, prefix="1.2.3.0/24", as_path=(207324, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208704, prefix="1.2.3.0/24", as_path=(208704, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209426, prefix="1.2.3.0/24", as_path=(209426, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209479, prefix="1.2.3.0/24", as_path=(209479, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209523, prefix="1.2.3.0/24", as_path=(209523, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210094, prefix="1.2.3.0/24", as_path=(210094, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210806, prefix="1.2.3.0/24", as_path=(210806, 29075, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=7007, prefix="1.2.3.0/24", as_path=(7007, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8440, prefix="1.2.3.0/24", as_path=(8440, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21158, prefix="1.2.3.0/24", as_path=(21158, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29997, prefix="1.2.3.0/24", as_path=(29997, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=30081, prefix="1.2.3.0/24", as_path=(30081, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34939, prefix="1.2.3.0/24", as_path=(34939, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44493, prefix="1.2.3.0/24", as_path=(44493, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44571, prefix="1.2.3.0/24", as_path=(44571, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48024, prefix="1.2.3.0/24", as_path=(48024, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49287, prefix="1.2.3.0/24", as_path=(49287, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51659, prefix="1.2.3.0/24", as_path=(51659, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57578, prefix="1.2.3.0/24", as_path=(57578, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57695, prefix="1.2.3.0/24", as_path=(57695, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58342, prefix="1.2.3.0/24", as_path=(58342, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60592, prefix="1.2.3.0/24", as_path=(60592, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62005, prefix="1.2.3.0/24", as_path=(62005, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=132647, prefix="1.2.3.0/24", as_path=(132647, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=134176, prefix="1.2.3.0/24", as_path=(134176, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=136258, prefix="1.2.3.0/24", as_path=(136258, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198615, prefix="1.2.3.0/24", as_path=(198615, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199289, prefix="1.2.3.0/24", as_path=(199289, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200740, prefix="1.2.3.0/24", as_path=(200740, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202492, prefix="1.2.3.0/24", as_path=(202492, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204720, prefix="1.2.3.0/24", as_path=(204720, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207320, prefix="1.2.3.0/24", as_path=(207320, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207616, prefix="1.2.3.0/24", as_path=(207616, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208393, prefix="1.2.3.0/24", as_path=(208393, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208626, prefix="1.2.3.0/24", as_path=(208626, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209199, prefix="1.2.3.0/24", as_path=(209199, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210250, prefix="1.2.3.0/24", as_path=(210250, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210352, prefix="1.2.3.0/24", as_path=(210352, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212895, prefix="1.2.3.0/24", as_path=(212895, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=213119, prefix="1.2.3.0/24", as_path=(213119, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=397444, prefix="1.2.3.0/24", as_path=(397444, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=398367, prefix="1.2.3.0/24", as_path=(398367, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=3278, prefix="1.2.3.0/24", as_path=(3278, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8351, prefix="1.2.3.0/24", as_path=(8351, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8569, prefix="1.2.3.0/24", as_path=(8569, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=9135, prefix="1.2.3.0/24", as_path=(9135, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12312, prefix="1.2.3.0/24", as_path=(12312, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12502, prefix="1.2.3.0/24", as_path=(12502, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12557, prefix="1.2.3.0/24", as_path=(12557, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12693, prefix="1.2.3.0/24", as_path=(12693, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12853, prefix="1.2.3.0/24", as_path=(12853, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15415, prefix="1.2.3.0/24", as_path=(15415, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15434, prefix="1.2.3.0/24", as_path=(15434, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15451, prefix="1.2.3.0/24", as_path=(15451, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15726, prefix="1.2.3.0/24", as_path=(15726, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=16024, prefix="1.2.3.0/24", as_path=(16024, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24845, prefix="1.2.3.0/24", as_path=(24845, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24861, prefix="1.2.3.0/24", as_path=(24861, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25081, prefix="1.2.3.0/24", as_path=(25081, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25102, prefix="1.2.3.0/24", as_path=(25102, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25115, prefix="1.2.3.0/24", as_path=(25115, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25276, prefix="1.2.3.0/24", as_path=(25276, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25317, prefix="1.2.3.0/24", as_path=(25317, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25419, prefix="1.2.3.0/24", as_path=(25419, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=28676, prefix="1.2.3.0/24", as_path=(28676, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29224, prefix="1.2.3.0/24", as_path=(29224, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29239, prefix="1.2.3.0/24", as_path=(29239, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29316, prefix="1.2.3.0/24", as_path=(29316, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=30825, prefix="1.2.3.0/24", as_path=(30825, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31334, prefix="1.2.3.0/24", as_path=(31334, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=33806, prefix="1.2.3.0/24", as_path=(33806, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34127, prefix="1.2.3.0/24", as_path=(34127, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34156, prefix="1.2.3.0/24", as_path=(34156, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34548, prefix="1.2.3.0/24", as_path=(34548, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34966, prefix="1.2.3.0/24", as_path=(34966, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35065, prefix="1.2.3.0/24", as_path=(35065, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35205, prefix="1.2.3.0/24", as_path=(35205, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=38988, prefix="1.2.3.0/24", as_path=(38988, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39170, prefix="1.2.3.0/24", as_path=(39170, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39373, prefix="1.2.3.0/24", as_path=(39373, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39538, prefix="1.2.3.0/24", as_path=(39538, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41307, prefix="1.2.3.0/24", as_path=(41307, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43623, prefix="1.2.3.0/24", as_path=(43623, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44499, prefix="1.2.3.0/24", as_path=(44499, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44974, prefix="1.2.3.0/24", as_path=(44974, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47261, prefix="1.2.3.0/24", as_path=(47261, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47295, prefix="1.2.3.0/24", as_path=(47295, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49523, prefix="1.2.3.0/24", as_path=(49523, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49739, prefix="1.2.3.0/24", as_path=(49739, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50824, prefix="1.2.3.0/24", as_path=(50824, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51379, prefix="1.2.3.0/24", as_path=(51379, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51720, prefix="1.2.3.0/24", as_path=(51720, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57939, prefix="1.2.3.0/24", as_path=(57939, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58234, prefix="1.2.3.0/24", as_path=(58234, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58265, prefix="1.2.3.0/24", as_path=(58265, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58346, prefix="1.2.3.0/24", as_path=(58346, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59675, prefix="1.2.3.0/24", as_path=(59675, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59775, prefix="1.2.3.0/24", as_path=(59775, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62291, prefix="1.2.3.0/24", as_path=(62291, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197269, prefix="1.2.3.0/24", as_path=(197269, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197874, prefix="1.2.3.0/24", as_path=(197874, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197932, prefix="1.2.3.0/24", as_path=(197932, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198311, prefix="1.2.3.0/24", as_path=(198311, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198570, prefix="1.2.3.0/24", as_path=(198570, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200374, prefix="1.2.3.0/24", as_path=(200374, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200377, prefix="1.2.3.0/24", as_path=(200377, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200423, prefix="1.2.3.0/24", as_path=(200423, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201213, prefix="1.2.3.0/24", as_path=(201213, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201299, prefix="1.2.3.0/24", as_path=(201299, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201318, prefix="1.2.3.0/24", as_path=(201318, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201530, prefix="1.2.3.0/24", as_path=(201530, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201832, prefix="1.2.3.0/24", as_path=(201832, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202707, prefix="1.2.3.0/24", as_path=(202707, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203420, prefix="1.2.3.0/24", as_path=(203420, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203592, prefix="1.2.3.0/24", as_path=(203592, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203593, prefix="1.2.3.0/24", as_path=(203593, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203854, prefix="1.2.3.0/24", as_path=(203854, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203865, prefix="1.2.3.0/24", as_path=(203865, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204008, prefix="1.2.3.0/24", as_path=(204008, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204028, prefix="1.2.3.0/24", as_path=(204028, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205033, prefix="1.2.3.0/24", as_path=(205033, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205249, prefix="1.2.3.0/24", as_path=(205249, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205411, prefix="1.2.3.0/24", as_path=(205411, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205571, prefix="1.2.3.0/24", as_path=(205571, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205854, prefix="1.2.3.0/24", as_path=(205854, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205887, prefix="1.2.3.0/24", as_path=(205887, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205890, prefix="1.2.3.0/24", as_path=(205890, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206063, prefix="1.2.3.0/24", as_path=(206063, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206452, prefix="1.2.3.0/24", as_path=(206452, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207706, prefix="1.2.3.0/24", as_path=(207706, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207707, prefix="1.2.3.0/24", as_path=(207707, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208372, prefix="1.2.3.0/24", as_path=(208372, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208849, prefix="1.2.3.0/24", as_path=(208849, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211727, prefix="1.2.3.0/24", as_path=(211727, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=213141, prefix="1.2.3.0/24", as_path=(213141, 3209, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=1321, prefix="1.2.3.0/24", as_path=(1321, 15133, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=14153, prefix="1.2.3.0/24", as_path=(14153, 15133, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=14210, prefix="1.2.3.0/24", as_path=(14210, 15133, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=36915, prefix="1.2.3.0/24", as_path=(36915, 15399, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37027, prefix="1.2.3.0/24", as_path=(37027, 15399, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37052, prefix="1.2.3.0/24", as_path=(37052, 15399, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37101, prefix="1.2.3.0/24", as_path=(37101, 15399, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327748, prefix="1.2.3.0/24", as_path=(327748, 15399, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61317, prefix="1.2.3.0/24", as_path=(61317, 24413, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=14417, prefix="1.2.3.0/24", as_path=(14417, 36351, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=16807, prefix="1.2.3.0/24", as_path=(16807, 36351, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=26968, prefix="1.2.3.0/24", as_path=(26968, 36351, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=28356, prefix="1.2.3.0/24", as_path=(28356, 36351, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=36344, prefix="1.2.3.0/24", as_path=(36344, 36351, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=38719, prefix="1.2.3.0/24", as_path=(38719, 36351, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44588, prefix="1.2.3.0/24", as_path=(44588, 36351, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=46160, prefix="1.2.3.0/24", as_path=(46160, 36351, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48851, prefix="1.2.3.0/24", as_path=(48851, 36351, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50524, prefix="1.2.3.0/24", as_path=(50524, 36351, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=134176, prefix="1.2.3.0/24", as_path=(134176, 36351, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202665, prefix="1.2.3.0/24", as_path=(202665, 36351, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206998, prefix="1.2.3.0/24", as_path=(206998, 36351, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=263034, prefix="1.2.3.0/24", as_path=(263034, 36351, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15850,
        prefix="1.2.3.0/24",
        as_path=(15850, 43994, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35673,
        prefix="1.2.3.0/24",
        as_path=(35673, 43994, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39824,
        prefix="1.2.3.0/24",
        as_path=(39824, 43994, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41007,
        prefix="1.2.3.0/24",
        as_path=(41007, 43994, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43934,
        prefix="1.2.3.0/24",
        as_path=(43934, 43994, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59583,
        prefix="1.2.3.0/24",
        as_path=(59583, 43994, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62394,
        prefix="1.2.3.0/24",
        as_path=(62394, 43994, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202293,
        prefix="1.2.3.0/24",
        as_path=(202293, 43994, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211806,
        prefix="1.2.3.0/24",
        as_path=(211806, 43994, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212675,
        prefix="1.2.3.0/24",
        as_path=(212675, 43994, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=213048,
        prefix="1.2.3.0/24",
        as_path=(213048, 43994, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=7551, prefix="1.2.3.0/24", as_path=(7551, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=7604, prefix="1.2.3.0/24", as_path=(7604, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=9224, prefix="1.2.3.0/24", as_path=(9224, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=9280, prefix="1.2.3.0/24", as_path=(9280, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=9461, prefix="1.2.3.0/24", as_path=(9461, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15695, prefix="1.2.3.0/24", as_path=(15695, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=17473, prefix="1.2.3.0/24", as_path=(17473, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=17889, prefix="1.2.3.0/24", as_path=(17889, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24443, prefix="1.2.3.0/24", as_path=(24443, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29997, prefix="1.2.3.0/24", as_path=(29997, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=38172, prefix="1.2.3.0/24", as_path=(38172, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=38333, prefix="1.2.3.0/24", as_path=(38333, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=45638, prefix="1.2.3.0/24", as_path=(45638, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=45671, prefix="1.2.3.0/24", as_path=(45671, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=45780, prefix="1.2.3.0/24", as_path=(45780, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=55811, prefix="1.2.3.0/24", as_path=(55811, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56087, prefix="1.2.3.0/24", as_path=(56087, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=63920, prefix="1.2.3.0/24", as_path=(63920, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=64073, prefix="1.2.3.0/24", as_path=(64073, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=132072, prefix="1.2.3.0/24", as_path=(132072, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=132791, prefix="1.2.3.0/24", as_path=(132791, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=133196, prefix="1.2.3.0/24", as_path=(133196, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=133863, prefix="1.2.3.0/24", as_path=(133863, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=133914, prefix="1.2.3.0/24", as_path=(133914, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=134242, prefix="1.2.3.0/24", as_path=(134242, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=134688, prefix="1.2.3.0/24", as_path=(134688, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=134743, prefix="1.2.3.0/24", as_path=(134743, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=135060, prefix="1.2.3.0/24", as_path=(135060, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=135323, prefix="1.2.3.0/24", as_path=(135323, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=135408, prefix="1.2.3.0/24", as_path=(135408, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=135493, prefix="1.2.3.0/24", as_path=(135493, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=136805, prefix="1.2.3.0/24", as_path=(136805, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=137549, prefix="1.2.3.0/24", as_path=(137549, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=139005, prefix="1.2.3.0/24", as_path=(139005, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=139853, prefix="1.2.3.0/24", as_path=(139853, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=140736, prefix="1.2.3.0/24", as_path=(140736, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=148976, prefix="1.2.3.0/24", as_path=(148976, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=397127, prefix="1.2.3.0/24", as_path=(397127, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=72, prefix="1.2.3.0/24", as_path=(72, 196925, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20771, prefix="1.2.3.0/24", as_path=(20771, 196925, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34170, prefix="1.2.3.0/24", as_path=(34170, 196925, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39280, prefix="1.2.3.0/24", as_path=(39280, 196925, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42779, prefix="1.2.3.0/24", as_path=(42779, 196925, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50371, prefix="1.2.3.0/24", as_path=(50371, 196925, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57675, prefix="1.2.3.0/24", as_path=(57675, 196925, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197830, prefix="1.2.3.0/24", as_path=(197830, 196925, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200154, prefix="1.2.3.0/24", as_path=(200154, 196925, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207251, prefix="1.2.3.0/24", as_path=(207251, 196925, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209700, prefix="1.2.3.0/24", as_path=(209700, 196925, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210293, prefix="1.2.3.0/24", as_path=(210293, 196925, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210665, prefix="1.2.3.0/24", as_path=(210665, 196925, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211937, prefix="1.2.3.0/24", as_path=(211937, 196925, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=213379, prefix="1.2.3.0/24", as_path=(213379, 196925, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=213402, prefix="1.2.3.0/24", as_path=(213402, 196925, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8336, prefix="1.2.3.0/24", as_path=(8336, 327782, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=11744, prefix="1.2.3.0/24", as_path=(11744, 327782, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37153, prefix="1.2.3.0/24", as_path=(37153, 327782, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37157, prefix="1.2.3.0/24", as_path=(37157, 327782, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37438, prefix="1.2.3.0/24", as_path=(37438, 327782, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37650, prefix="1.2.3.0/24", as_path=(37650, 327782, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208638,
        prefix="1.2.3.0/24",
        as_path=(208638, 327782, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328120,
        prefix="1.2.3.0/24",
        as_path=(328120, 327782, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328163,
        prefix="1.2.3.0/24",
        as_path=(328163, 327782, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328222,
        prefix="1.2.3.0/24",
        as_path=(328222, 327782, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328251,
        prefix="1.2.3.0/24",
        as_path=(328251, 327782, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328270,
        prefix="1.2.3.0/24",
        as_path=(328270, 327782, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328314,
        prefix="1.2.3.0/24",
        as_path=(328314, 327782, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328360,
        prefix="1.2.3.0/24",
        as_path=(328360, 327782, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328456,
        prefix="1.2.3.0/24",
        as_path=(328456, 327782, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328529,
        prefix="1.2.3.0/24",
        as_path=(328529, 327782, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328548,
        prefix="1.2.3.0/24",
        as_path=(328548, 327782, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328812,
        prefix="1.2.3.0/24",
        as_path=(328812, 327782, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=16222, prefix="1.2.3.0/24", as_path=(16222, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20946, prefix="1.2.3.0/24", as_path=(20946, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41512, prefix="1.2.3.0/24", as_path=(41512, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42119, prefix="1.2.3.0/24", as_path=(42119, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43267, prefix="1.2.3.0/24", as_path=(43267, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43349, prefix="1.2.3.0/24", as_path=(43349, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48343, prefix="1.2.3.0/24", as_path=(48343, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48370, prefix="1.2.3.0/24", as_path=(48370, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48986, prefix="1.2.3.0/24", as_path=(48986, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49693, prefix="1.2.3.0/24", as_path=(49693, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51117, prefix="1.2.3.0/24", as_path=(51117, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51478, prefix="1.2.3.0/24", as_path=(51478, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51715, prefix="1.2.3.0/24", as_path=(51715, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57700, prefix="1.2.3.0/24", as_path=(57700, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61156, prefix="1.2.3.0/24", as_path=(61156, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61197, prefix="1.2.3.0/24", as_path=(61197, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198526, prefix="1.2.3.0/24", as_path=(198526, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200175, prefix="1.2.3.0/24", as_path=(200175, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200643, prefix="1.2.3.0/24", as_path=(200643, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201475, prefix="1.2.3.0/24", as_path=(201475, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201781, prefix="1.2.3.0/24", as_path=(201781, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204891, prefix="1.2.3.0/24", as_path=(204891, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205332, prefix="1.2.3.0/24", as_path=(205332, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205601, prefix="1.2.3.0/24", as_path=(205601, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205963, prefix="1.2.3.0/24", as_path=(205963, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206653, prefix="1.2.3.0/24", as_path=(206653, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207822, prefix="1.2.3.0/24", as_path=(207822, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207853, prefix="1.2.3.0/24", as_path=(207853, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211503, prefix="1.2.3.0/24", as_path=(211503, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212333, prefix="1.2.3.0/24", as_path=(212333, 8492, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12484,
        prefix="1.2.3.0/24",
        as_path=(12484, 12494, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41816,
        prefix="1.2.3.0/24",
        as_path=(41816, 12494, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48176,
        prefix="1.2.3.0/24",
        as_path=(48176, 12494, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48530,
        prefix="1.2.3.0/24",
        as_path=(48530, 12494, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50727,
        prefix="1.2.3.0/24",
        as_path=(50727, 12494, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57683,
        prefix="1.2.3.0/24",
        as_path=(57683, 12494, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(reporting_asn=112, prefix="1.2.3.0/24", as_path=(112, 12779, 29452)).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12654, prefix="1.2.3.0/24", as_path=(12654, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21176, prefix="1.2.3.0/24", as_path=(21176, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21333, prefix="1.2.3.0/24", as_path=(21333, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24796, prefix="1.2.3.0/24", as_path=(24796, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25488, prefix="1.2.3.0/24", as_path=(25488, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31121, prefix="1.2.3.0/24", as_path=(31121, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34606, prefix="1.2.3.0/24", as_path=(34606, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34691, prefix="1.2.3.0/24", as_path=(34691, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39636, prefix="1.2.3.0/24", as_path=(39636, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41364, prefix="1.2.3.0/24", as_path=(41364, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42425, prefix="1.2.3.0/24", as_path=(42425, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42669, prefix="1.2.3.0/24", as_path=(42669, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44219, prefix="1.2.3.0/24", as_path=(44219, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47316, prefix="1.2.3.0/24", as_path=(47316, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47353, prefix="1.2.3.0/24", as_path=(47353, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47406, prefix="1.2.3.0/24", as_path=(47406, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48815, prefix="1.2.3.0/24", as_path=(48815, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51300, prefix="1.2.3.0/24", as_path=(51300, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51616, prefix="1.2.3.0/24", as_path=(51616, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57394, prefix="1.2.3.0/24", as_path=(57394, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59919, prefix="1.2.3.0/24", as_path=(59919, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62009, prefix="1.2.3.0/24", as_path=(62009, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=196983, prefix="1.2.3.0/24", as_path=(196983, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200043, prefix="1.2.3.0/24", as_path=(200043, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204664, prefix="1.2.3.0/24", as_path=(204664, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205005, prefix="1.2.3.0/24", as_path=(205005, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205284, prefix="1.2.3.0/24", as_path=(205284, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205451, prefix="1.2.3.0/24", as_path=(205451, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205926, prefix="1.2.3.0/24", as_path=(205926, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208296, prefix="1.2.3.0/24", as_path=(208296, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209387, prefix="1.2.3.0/24", as_path=(209387, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209992, prefix="1.2.3.0/24", as_path=(209992, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210144, prefix="1.2.3.0/24", as_path=(210144, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=213111, prefix="1.2.3.0/24", as_path=(213111, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(reporting_asn=513, prefix="1.2.3.0/24", as_path=(513, 25091, 29452)).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=6893, prefix="1.2.3.0/24", as_path=(6893, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12654, prefix="1.2.3.0/24", as_path=(12654, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15955, prefix="1.2.3.0/24", as_path=(15955, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20144, prefix="1.2.3.0/24", as_path=(20144, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20582, prefix="1.2.3.0/24", as_path=(20582, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21217, prefix="1.2.3.0/24", as_path=(21217, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21449, prefix="1.2.3.0/24", as_path=(21449, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31592, prefix="1.2.3.0/24", as_path=(31592, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35661, prefix="1.2.3.0/24", as_path=(35661, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39176, prefix="1.2.3.0/24", as_path=(39176, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39419, prefix="1.2.3.0/24", as_path=(39419, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41003, prefix="1.2.3.0/24", as_path=(41003, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41766, prefix="1.2.3.0/24", as_path=(41766, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41906, prefix="1.2.3.0/24", as_path=(41906, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42275, prefix="1.2.3.0/24", as_path=(42275, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43445, prefix="1.2.3.0/24", as_path=(43445, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44854, prefix="1.2.3.0/24", as_path=(44854, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=45009, prefix="1.2.3.0/24", as_path=(45009, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47271, prefix="1.2.3.0/24", as_path=(47271, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49114, prefix="1.2.3.0/24", as_path=(49114, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49642, prefix="1.2.3.0/24", as_path=(49642, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50327, prefix="1.2.3.0/24", as_path=(50327, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50837, prefix="1.2.3.0/24", as_path=(50837, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51083, prefix="1.2.3.0/24", as_path=(51083, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56798, prefix="1.2.3.0/24", as_path=(56798, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57581, prefix="1.2.3.0/24", as_path=(57581, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60129, prefix="1.2.3.0/24", as_path=(60129, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60768, prefix="1.2.3.0/24", as_path=(60768, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60785, prefix="1.2.3.0/24", as_path=(60785, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61062, prefix="1.2.3.0/24", as_path=(61062, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61970, prefix="1.2.3.0/24", as_path=(61970, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62035, prefix="1.2.3.0/24", as_path=(62035, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=64426, prefix="1.2.3.0/24", as_path=(64426, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=64482, prefix="1.2.3.0/24", as_path=(64482, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199092, prefix="1.2.3.0/24", as_path=(199092, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199422, prefix="1.2.3.0/24", as_path=(199422, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199562, prefix="1.2.3.0/24", as_path=(199562, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199758, prefix="1.2.3.0/24", as_path=(199758, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200759, prefix="1.2.3.0/24", as_path=(200759, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202569, prefix="1.2.3.0/24", as_path=(202569, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203184, prefix="1.2.3.0/24", as_path=(203184, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203927, prefix="1.2.3.0/24", as_path=(203927, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205068, prefix="1.2.3.0/24", as_path=(205068, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208600, prefix="1.2.3.0/24", as_path=(208600, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210983, prefix="1.2.3.0/24", as_path=(210983, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=213298, prefix="1.2.3.0/24", as_path=(213298, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43031, prefix="1.2.3.0/24", as_path=(43031, 29196, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198826, prefix="1.2.3.0/24", as_path=(198826, 29196, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207128, prefix="1.2.3.0/24", as_path=(207128, 29196, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207977, prefix="1.2.3.0/24", as_path=(207977, 29196, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42705,
        prefix="1.2.3.0/24",
        as_path=(42705, 39151, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13296, prefix="1.2.3.0/24", as_path=(13296, 41034, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15454, prefix="1.2.3.0/24", as_path=(15454, 41034, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57842, prefix="1.2.3.0/24", as_path=(57842, 41034, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61382, prefix="1.2.3.0/24", as_path=(61382, 41034, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201231, prefix="1.2.3.0/24", as_path=(201231, 41034, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212429, prefix="1.2.3.0/24", as_path=(212429, 41034, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212800, prefix="1.2.3.0/24", as_path=(212800, 41034, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35816,
        prefix="1.2.3.0/24",
        as_path=(35816, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42239,
        prefix="1.2.3.0/24",
        as_path=(42239, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47203,
        prefix="1.2.3.0/24",
        as_path=(47203, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47349,
        prefix="1.2.3.0/24",
        as_path=(47349, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48004,
        prefix="1.2.3.0/24",
        as_path=(48004, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59833,
        prefix="1.2.3.0/24",
        as_path=(59833, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203451,
        prefix="1.2.3.0/24",
        as_path=(203451, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24837, prefix="1.2.3.0/24", as_path=(24837, 58067, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35608, prefix="1.2.3.0/24", as_path=(35608, 58067, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39178, prefix="1.2.3.0/24", as_path=(39178, 58067, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41517, prefix="1.2.3.0/24", as_path=(41517, 58067, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50477, prefix="1.2.3.0/24", as_path=(50477, 58067, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56702, prefix="1.2.3.0/24", as_path=(56702, 58067, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57371, prefix="1.2.3.0/24", as_path=(57371, 58067, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62069, prefix="1.2.3.0/24", as_path=(62069, 58067, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204277, prefix="1.2.3.0/24", as_path=(204277, 58067, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208087, prefix="1.2.3.0/24", as_path=(208087, 58067, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8511,
        prefix="1.2.3.0/24",
        as_path=(8511, 61010, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47237,
        prefix="1.2.3.0/24",
        as_path=(47237, 61010, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61399,
        prefix="1.2.3.0/24",
        as_path=(61399, 61010, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59043,
        prefix="1.2.3.0/24",
        as_path=(59043, 134196, 24413, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=134835,
        prefix="1.2.3.0/24",
        as_path=(134835, 134196, 24413, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=136250,
        prefix="1.2.3.0/24",
        as_path=(136250, 134196, 24413, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=138968,
        prefix="1.2.3.0/24",
        as_path=(138968, 134196, 24413, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12403,
        prefix="1.2.3.0/24",
        as_path=(12403, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43936,
        prefix="1.2.3.0/24",
        as_path=(43936, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44139,
        prefix="1.2.3.0/24",
        as_path=(44139, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44387,
        prefix="1.2.3.0/24",
        as_path=(44387, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47801,
        prefix="1.2.3.0/24",
        as_path=(47801, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48004,
        prefix="1.2.3.0/24",
        as_path=(48004, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48158,
        prefix="1.2.3.0/24",
        as_path=(48158, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51211,
        prefix="1.2.3.0/24",
        as_path=(51211, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51214,
        prefix="1.2.3.0/24",
        as_path=(51214, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51518,
        prefix="1.2.3.0/24",
        as_path=(51518, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56352,
        prefix="1.2.3.0/24",
        as_path=(56352, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57093,
        prefix="1.2.3.0/24",
        as_path=(57093, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57383,
        prefix="1.2.3.0/24",
        as_path=(57383, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57641,
        prefix="1.2.3.0/24",
        as_path=(57641, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57893,
        prefix="1.2.3.0/24",
        as_path=(57893, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57903,
        prefix="1.2.3.0/24",
        as_path=(57903, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59823,
        prefix="1.2.3.0/24",
        as_path=(59823, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=196705,
        prefix="1.2.3.0/24",
        as_path=(196705, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197152,
        prefix="1.2.3.0/24",
        as_path=(197152, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197159,
        prefix="1.2.3.0/24",
        as_path=(197159, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197175,
        prefix="1.2.3.0/24",
        as_path=(197175, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197628,
        prefix="1.2.3.0/24",
        as_path=(197628, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198338,
        prefix="1.2.3.0/24",
        as_path=(198338, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201069,
        prefix="1.2.3.0/24",
        as_path=(201069, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203451,
        prefix="1.2.3.0/24",
        as_path=(203451, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203561,
        prefix="1.2.3.0/24",
        as_path=(203561, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204161,
        prefix="1.2.3.0/24",
        as_path=(204161, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204791,
        prefix="1.2.3.0/24",
        as_path=(204791, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206248,
        prefix="1.2.3.0/24",
        as_path=(206248, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207909,
        prefix="1.2.3.0/24",
        as_path=(207909, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208397,
        prefix="1.2.3.0/24",
        as_path=(208397, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208701,
        prefix="1.2.3.0/24",
        as_path=(208701, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210451,
        prefix="1.2.3.0/24",
        as_path=(210451, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211245,
        prefix="1.2.3.0/24",
        as_path=(211245, 6789, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=36872,
        prefix="1.2.3.0/24",
        as_path=(36872, 16284, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=36957,
        prefix="1.2.3.0/24",
        as_path=(36957, 16284, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37088,
        prefix="1.2.3.0/24",
        as_path=(37088, 16284, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37192,
        prefix="1.2.3.0/24",
        as_path=(37192, 16284, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37340,
        prefix="1.2.3.0/24",
        as_path=(37340, 16284, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327869,
        prefix="1.2.3.0/24",
        as_path=(327869, 16284, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328027,
        prefix="1.2.3.0/24",
        as_path=(328027, 16284, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328081,
        prefix="1.2.3.0/24",
        as_path=(328081, 16284, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328092,
        prefix="1.2.3.0/24",
        as_path=(328092, 16284, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328332,
        prefix="1.2.3.0/24",
        as_path=(328332, 16284, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328401,
        prefix="1.2.3.0/24",
        as_path=(328401, 16284, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328413,
        prefix="1.2.3.0/24",
        as_path=(328413, 16284, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328497,
        prefix="1.2.3.0/24",
        as_path=(328497, 16284, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328742,
        prefix="1.2.3.0/24",
        as_path=(328742, 16284, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13105,
        prefix="1.2.3.0/24",
        as_path=(13105, 21191, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15774,
        prefix="1.2.3.0/24",
        as_path=(15774, 21191, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=7546, prefix="1.2.3.0/24", as_path=(7546, 24479, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=135039, prefix="1.2.3.0/24", as_path=(135039, 24479, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=136154, prefix="1.2.3.0/24", as_path=(136154, 24479, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=136187, prefix="1.2.3.0/24", as_path=(136187, 24479, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=140064, prefix="1.2.3.0/24", as_path=(140064, 24479, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=140598, prefix="1.2.3.0/24", as_path=(140598, 24479, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24840,
        prefix="1.2.3.0/24",
        as_path=(24840, 24637, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29239,
        prefix="1.2.3.0/24",
        as_path=(29239, 24637, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29358,
        prefix="1.2.3.0/24",
        as_path=(29358, 24637, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29507,
        prefix="1.2.3.0/24",
        as_path=(29507, 24637, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34453,
        prefix="1.2.3.0/24",
        as_path=(34453, 24637, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41814,
        prefix="1.2.3.0/24",
        as_path=(41814, 24637, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43897,
        prefix="1.2.3.0/24",
        as_path=(43897, 24637, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44131,
        prefix="1.2.3.0/24",
        as_path=(44131, 24637, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50076,
        prefix="1.2.3.0/24",
        as_path=(50076, 24637, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50145,
        prefix="1.2.3.0/24",
        as_path=(50145, 24637, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50216,
        prefix="1.2.3.0/24",
        as_path=(50216, 24637, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56657,
        prefix="1.2.3.0/24",
        as_path=(56657, 24637, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56948,
        prefix="1.2.3.0/24",
        as_path=(56948, 24637, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59822,
        prefix="1.2.3.0/24",
        as_path=(59822, 24637, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60454,
        prefix="1.2.3.0/24",
        as_path=(60454, 24637, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60948,
        prefix="1.2.3.0/24",
        as_path=(60948, 24637, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204612,
        prefix="1.2.3.0/24",
        as_path=(204612, 24637, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204990,
        prefix="1.2.3.0/24",
        as_path=(204990, 24637, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210098,
        prefix="1.2.3.0/24",
        as_path=(210098, 24637, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=112, prefix="1.2.3.0/24", as_path=(112, 38008, 56630, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=18250,
        prefix="1.2.3.0/24",
        as_path=(18250, 38008, 56630, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=38839,
        prefix="1.2.3.0/24",
        as_path=(38839, 38008, 56630, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=46997,
        prefix="1.2.3.0/24",
        as_path=(46997, 38008, 56630, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=141376,
        prefix="1.2.3.0/24",
        as_path=(141376, 38008, 56630, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=4739, prefix="1.2.3.0/24", as_path=(4739, 38880, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=7496, prefix="1.2.3.0/24", as_path=(7496, 38880, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20144, prefix="1.2.3.0/24", as_path=(20144, 38880, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=45426, prefix="1.2.3.0/24", as_path=(45426, 38880, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=55845, prefix="1.2.3.0/24", as_path=(55845, 38880, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56087, prefix="1.2.3.0/24", as_path=(56087, 38880, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58915, prefix="1.2.3.0/24", as_path=(58915, 38880, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=135408, prefix="1.2.3.0/24", as_path=(135408, 38880, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=135543, prefix="1.2.3.0/24", as_path=(135543, 38880, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=135895, prefix="1.2.3.0/24", as_path=(135895, 38880, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8677, prefix="1.2.3.0/24", as_path=(8677, 47957, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43229, prefix="1.2.3.0/24", as_path=(43229, 47957, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51682, prefix="1.2.3.0/24", as_path=(51682, 47957, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=1, prefix="1.2.3.0/24", as_path=(1, 48940, 20485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51705,
        prefix="1.2.3.0/24",
        as_path=(51705, 48940, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20611,
        prefix="1.2.3.0/24",
        as_path=(20611, 49505, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21314,
        prefix="1.2.3.0/24",
        as_path=(21314, 49505, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25152,
        prefix="1.2.3.0/24",
        as_path=(25152, 49505, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35751,
        prefix="1.2.3.0/24",
        as_path=(35751, 49505, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44661,
        prefix="1.2.3.0/24",
        as_path=(44661, 49505, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48235,
        prefix="1.2.3.0/24",
        as_path=(48235, 49505, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50340,
        prefix="1.2.3.0/24",
        as_path=(50340, 49505, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62300,
        prefix="1.2.3.0/24",
        as_path=(62300, 49505, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200487,
        prefix="1.2.3.0/24",
        as_path=(200487, 49505, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201499,
        prefix="1.2.3.0/24",
        as_path=(201499, 49505, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=132721,
        prefix="1.2.3.0/24",
        as_path=(132721, 55933, 134196, 24413, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=134835,
        prefix="1.2.3.0/24",
        as_path=(134835, 55933, 134196, 24413, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=136250,
        prefix="1.2.3.0/24",
        as_path=(136250, 55933, 134196, 24413, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=138968,
        prefix="1.2.3.0/24",
        as_path=(138968, 55933, 134196, 24413, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34777, prefix="1.2.3.0/24", as_path=(34777, 58314, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34855, prefix="1.2.3.0/24", as_path=(34855, 58314, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57319, prefix="1.2.3.0/24", as_path=(57319, 58314, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57323, prefix="1.2.3.0/24", as_path=(57323, 58314, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199583, prefix="1.2.3.0/24", as_path=(199583, 58314, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200442, prefix="1.2.3.0/24", as_path=(200442, 58314, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43991,
        prefix="1.2.3.0/24",
        as_path=(43991, 60840, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60771,
        prefix="1.2.3.0/24",
        as_path=(60771, 60840, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=112, prefix="1.2.3.0/24", as_path=(112, 8298, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57777, prefix="1.2.3.0/24", as_path=(57777, 8298, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60557, prefix="1.2.3.0/24", as_path=(60557, 8298, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201723, prefix="1.2.3.0/24", as_path=(201723, 8298, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210036, prefix="1.2.3.0/24", as_path=(210036, 8298, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210312, prefix="1.2.3.0/24", as_path=(210312, 8298, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212323, prefix="1.2.3.0/24", as_path=(212323, 8298, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212855, prefix="1.2.3.0/24", as_path=(212855, 8298, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8350, prefix="1.2.3.0/24", as_path=(8350, 8402, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13095, prefix="1.2.3.0/24", as_path=(13095, 8402, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24924, prefix="1.2.3.0/24", as_path=(24924, 8402, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34879, prefix="1.2.3.0/24", as_path=(34879, 8402, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42677, prefix="1.2.3.0/24", as_path=(42677, 8402, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43410, prefix="1.2.3.0/24", as_path=(43410, 8402, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43798, prefix="1.2.3.0/24", as_path=(43798, 8402, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48848, prefix="1.2.3.0/24", as_path=(48848, 8402, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50951, prefix="1.2.3.0/24", as_path=(50951, 8402, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51039, prefix="1.2.3.0/24", as_path=(51039, 8402, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56685, prefix="1.2.3.0/24", as_path=(56685, 8402, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56781, prefix="1.2.3.0/24", as_path=(56781, 8402, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60535, prefix="1.2.3.0/24", as_path=(60535, 8402, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61261, prefix="1.2.3.0/24", as_path=(61261, 8402, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199549, prefix="1.2.3.0/24", as_path=(199549, 8402, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=3312, prefix="1.2.3.0/24", as_path=(3312, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=15984, prefix="1.2.3.0/24", as_path=(15984, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21266, prefix="1.2.3.0/24", as_path=(21266, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=30952, prefix="1.2.3.0/24", as_path=(30952, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=33903, prefix="1.2.3.0/24", as_path=(33903, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39376, prefix="1.2.3.0/24", as_path=(39376, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42628, prefix="1.2.3.0/24", as_path=(42628, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42677, prefix="1.2.3.0/24", as_path=(42677, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43900, prefix="1.2.3.0/24", as_path=(43900, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44014, prefix="1.2.3.0/24", as_path=(44014, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44470, prefix="1.2.3.0/24", as_path=(44470, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47456, prefix="1.2.3.0/24", as_path=(47456, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49712, prefix="1.2.3.0/24", as_path=(49712, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50279, prefix="1.2.3.0/24", as_path=(50279, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56442, prefix="1.2.3.0/24", as_path=(56442, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56480, prefix="1.2.3.0/24", as_path=(56480, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56577, prefix="1.2.3.0/24", as_path=(56577, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56879, prefix="1.2.3.0/24", as_path=(56879, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57078, prefix="1.2.3.0/24", as_path=(57078, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57828, prefix="1.2.3.0/24", as_path=(57828, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60459, prefix="1.2.3.0/24", as_path=(60459, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60511, prefix="1.2.3.0/24", as_path=(60511, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61021, prefix="1.2.3.0/24", as_path=(61021, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61379, prefix="1.2.3.0/24", as_path=(61379, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197010, prefix="1.2.3.0/24", as_path=(197010, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199320, prefix="1.2.3.0/24", as_path=(199320, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200028, prefix="1.2.3.0/24", as_path=(200028, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200065, prefix="1.2.3.0/24", as_path=(200065, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201430, prefix="1.2.3.0/24", as_path=(201430, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201498, prefix="1.2.3.0/24", as_path=(201498, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204159, prefix="1.2.3.0/24", as_path=(204159, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204696, prefix="1.2.3.0/24", as_path=(204696, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207025, prefix="1.2.3.0/24", as_path=(207025, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210698, prefix="1.2.3.0/24", as_path=(210698, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211258, prefix="1.2.3.0/24", as_path=(211258, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211928, prefix="1.2.3.0/24", as_path=(211928, 8470, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8838, prefix="1.2.3.0/24", as_path=(8838, 8553, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43545, prefix="1.2.3.0/24", as_path=(43545, 8553, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47549, prefix="1.2.3.0/24", as_path=(47549, 8553, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8239, prefix="1.2.3.0/24", as_path=(8239, 8903, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20784, prefix="1.2.3.0/24", as_path=(20784, 8903, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=24772, prefix="1.2.3.0/24", as_path=(24772, 8903, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25261, prefix="1.2.3.0/24", as_path=(25261, 8903, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29397, prefix="1.2.3.0/24", as_path=(29397, 8903, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31262, prefix="1.2.3.0/24", as_path=(31262, 8903, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41994, prefix="1.2.3.0/24", as_path=(41994, 8903, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44127, prefix="1.2.3.0/24", as_path=(44127, 8903, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44989, prefix="1.2.3.0/24", as_path=(44989, 8903, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48710, prefix="1.2.3.0/24", as_path=(48710, 8903, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57365, prefix="1.2.3.0/24", as_path=(57365, 8903, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199329, prefix="1.2.3.0/24", as_path=(199329, 8903, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202915, prefix="1.2.3.0/24", as_path=(202915, 8903, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203404, prefix="1.2.3.0/24", as_path=(203404, 8903, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206046, prefix="1.2.3.0/24", as_path=(206046, 8903, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209344, prefix="1.2.3.0/24", as_path=(209344, 8903, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=26130,
        prefix="1.2.3.0/24",
        as_path=(26130, 12491, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=36892,
        prefix="1.2.3.0/24",
        as_path=(36892, 12491, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=36958,
        prefix="1.2.3.0/24",
        as_path=(36958, 12491, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37087,
        prefix="1.2.3.0/24",
        as_path=(37087, 12491, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37453,
        prefix="1.2.3.0/24",
        as_path=(37453, 12491, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37483,
        prefix="1.2.3.0/24",
        as_path=(37483, 12491, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37623,
        prefix="1.2.3.0/24",
        as_path=(37623, 12491, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327870,
        prefix="1.2.3.0/24",
        as_path=(327870, 12491, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328261,
        prefix="1.2.3.0/24",
        as_path=(328261, 12491, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=2606, prefix="1.2.3.0/24", as_path=(2606, 13287, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44358, prefix="1.2.3.0/24", as_path=(44358, 13287, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59723, prefix="1.2.3.0/24", as_path=(59723, 13287, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202448, prefix="1.2.3.0/24", as_path=(202448, 13287, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205086, prefix="1.2.3.0/24", as_path=(205086, 13287, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207185, prefix="1.2.3.0/24", as_path=(207185, 13287, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208910, prefix="1.2.3.0/24", as_path=(208910, 13287, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209370, prefix="1.2.3.0/24", as_path=(209370, 13287, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209451, prefix="1.2.3.0/24", as_path=(209451, 13287, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209919, prefix="1.2.3.0/24", as_path=(209919, 13287, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212462, prefix="1.2.3.0/24", as_path=(212462, 13287, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202148, prefix="1.2.3.0/24", as_path=(202148, 15502, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47009,
        prefix="1.2.3.0/24",
        as_path=(47009, 19305, 2856, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48722,
        prefix="1.2.3.0/24",
        as_path=(48722, 25591, 48084, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43592,
        prefix="1.2.3.0/24",
        as_path=(43592, 28906, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48485,
        prefix="1.2.3.0/24",
        as_path=(48485, 28906, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61431,
        prefix="1.2.3.0/24",
        as_path=(61431, 28906, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31425, prefix="1.2.3.0/24", as_path=(31425, 31359, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34038, prefix="1.2.3.0/24", as_path=(34038, 31359, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43785, prefix="1.2.3.0/24", as_path=(43785, 31359, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51334, prefix="1.2.3.0/24", as_path=(51334, 31359, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209657, prefix="1.2.3.0/24", as_path=(209657, 31359, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199312, prefix="1.2.3.0/24", as_path=(199312, 34471, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203641, prefix="1.2.3.0/24", as_path=(203641, 34471, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209674, prefix="1.2.3.0/24", as_path=(209674, 34471, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=36904, prefix="1.2.3.0/24", as_path=(36904, 37305, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37019, prefix="1.2.3.0/24", as_path=(37019, 37305, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328093, prefix="1.2.3.0/24", as_path=(328093, 37305, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328162, prefix="1.2.3.0/24", as_path=(328162, 37305, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328380, prefix="1.2.3.0/24", as_path=(328380, 37305, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=329026, prefix="1.2.3.0/24", as_path=(329026, 37305, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=329033, prefix="1.2.3.0/24", as_path=(329033, 37305, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210036, prefix="1.2.3.0/24", as_path=(210036, 39540, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=16321,
        prefix="1.2.3.0/24",
        as_path=(16321, 44050, 50509, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31503,
        prefix="1.2.3.0/24",
        as_path=(31503, 44050, 50509, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34866,
        prefix="1.2.3.0/24",
        as_path=(34866, 44050, 50509, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39556,
        prefix="1.2.3.0/24",
        as_path=(39556, 44050, 50509, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=45054,
        prefix="1.2.3.0/24",
        as_path=(45054, 44050, 50509, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47528,
        prefix="1.2.3.0/24",
        as_path=(47528, 44050, 50509, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=54985,
        prefix="1.2.3.0/24",
        as_path=(54985, 44050, 50509, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207822,
        prefix="1.2.3.0/24",
        as_path=(207822, 44050, 50509, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207853,
        prefix="1.2.3.0/24",
        as_path=(207853, 44050, 50509, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49718, prefix="1.2.3.0/24", as_path=(49718, 44941, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203440,
        prefix="1.2.3.0/24",
        as_path=(203440, 47138, 24637, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=3312, prefix="1.2.3.0/24", as_path=(3312, 47441, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8515, prefix="1.2.3.0/24", as_path=(8515, 47441, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41359, prefix="1.2.3.0/24", as_path=(41359, 47441, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49385, prefix="1.2.3.0/24", as_path=(49385, 47441, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50471, prefix="1.2.3.0/24", as_path=(50471, 47441, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56794, prefix="1.2.3.0/24", as_path=(56794, 47441, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42834, prefix="1.2.3.0/24", as_path=(42834, 47764, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44903, prefix="1.2.3.0/24", as_path=(44903, 47764, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56462, prefix="1.2.3.0/24", as_path=(56462, 47764, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58116, prefix="1.2.3.0/24", as_path=(58116, 47764, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60863, prefix="1.2.3.0/24", as_path=(60863, 47764, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199295, prefix="1.2.3.0/24", as_path=(199295, 47764, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8506,
        prefix="1.2.3.0/24",
        as_path=(8506, 51034, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29182,
        prefix="1.2.3.0/24",
        as_path=(29182, 51034, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47397,
        prefix="1.2.3.0/24",
        as_path=(47397, 51034, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47909,
        prefix="1.2.3.0/24",
        as_path=(47909, 51034, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48035,
        prefix="1.2.3.0/24",
        as_path=(48035, 51034, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56959,
        prefix="1.2.3.0/24",
        as_path=(56959, 51034, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57737,
        prefix="1.2.3.0/24",
        as_path=(57737, 51034, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59616,
        prefix="1.2.3.0/24",
        as_path=(59616, 51034, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60452,
        prefix="1.2.3.0/24",
        as_path=(60452, 51034, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61406,
        prefix="1.2.3.0/24",
        as_path=(61406, 51034, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62200,
        prefix="1.2.3.0/24",
        as_path=(62200, 51034, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=7490, prefix="1.2.3.0/24", as_path=(7490, 55707, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=55575, prefix="1.2.3.0/24", as_path=(55575, 55707, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56199, prefix="1.2.3.0/24", as_path=(56199, 55707, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=131292, prefix="1.2.3.0/24", as_path=(131292, 55707, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=131316, prefix="1.2.3.0/24", as_path=(131316, 55707, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=133324, prefix="1.2.3.0/24", as_path=(133324, 55707, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=134691, prefix="1.2.3.0/24", as_path=(134691, 55707, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=135107, prefix="1.2.3.0/24", as_path=(135107, 55707, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=5547, prefix="1.2.3.0/24", as_path=(5547, 57277, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21087, prefix="1.2.3.0/24", as_path=(21087, 57277, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29182, prefix="1.2.3.0/24", as_path=(29182, 57277, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42971, prefix="1.2.3.0/24", as_path=(42971, 57277, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47909, prefix="1.2.3.0/24", as_path=(47909, 57277, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48586, prefix="1.2.3.0/24", as_path=(48586, 57277, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49287, prefix="1.2.3.0/24", as_path=(49287, 57277, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56535, prefix="1.2.3.0/24", as_path=(56535, 57277, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59616, prefix="1.2.3.0/24", as_path=(59616, 57277, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61406, prefix="1.2.3.0/24", as_path=(61406, 57277, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198086, prefix="1.2.3.0/24", as_path=(198086, 57277, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50818, prefix="1.2.3.0/24", as_path=(50818, 61026, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210197, prefix="1.2.3.0/24", as_path=(210197, 61026, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211694, prefix="1.2.3.0/24", as_path=(211694, 61026, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=135553,
        prefix="1.2.3.0/24",
        as_path=(135553, 132111, 45352, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=6874,
        prefix="1.2.3.0/24",
        as_path=(6874, 196691, 50509, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31656,
        prefix="1.2.3.0/24",
        as_path=(31656, 196691, 50509, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57842,
        prefix="1.2.3.0/24",
        as_path=(57842, 196691, 50509, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61230,
        prefix="1.2.3.0/24",
        as_path=(61230, 196691, 50509, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198130,
        prefix="1.2.3.0/24",
        as_path=(198130, 196691, 50509, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202058,
        prefix="1.2.3.0/24",
        as_path=(202058, 196691, 50509, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205702,
        prefix="1.2.3.0/24",
        as_path=(205702, 196691, 50509, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37371,
        prefix="1.2.3.0/24",
        as_path=(37371, 327732, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328319,
        prefix="1.2.3.0/24",
        as_path=(328319, 327732, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328435,
        prefix="1.2.3.0/24",
        as_path=(328435, 327732, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37248,
        prefix="1.2.3.0/24",
        as_path=(37248, 327952, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328035,
        prefix="1.2.3.0/24",
        as_path=(328035, 327952, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328562,
        prefix="1.2.3.0/24",
        as_path=(328562, 328320, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328041,
        prefix="1.2.3.0/24",
        as_path=(328041, 328366, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=329039,
        prefix="1.2.3.0/24",
        as_path=(329039, 328366, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37584, prefix="1.2.3.0/24", as_path=(37584, 328605, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328610,
        prefix="1.2.3.0/24",
        as_path=(328610, 328605, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328755,
        prefix="1.2.3.0/24",
        as_path=(328755, 328605, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211587, prefix="1.2.3.0/24", as_path=(211587, 5523, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=38719, prefix="1.2.3.0/24", as_path=(38719, 7628, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=132077, prefix="1.2.3.0/24", as_path=(132077, 7628, 58511, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60716, prefix="1.2.3.0/24", as_path=(60716, 8629, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200166, prefix="1.2.3.0/24", as_path=(200166, 8629, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200821,
        prefix="1.2.3.0/24",
        as_path=(200821, 8839, 29075, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41845, prefix="1.2.3.0/24", as_path=(41845, 9110, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42628, prefix="1.2.3.0/24", as_path=(42628, 9110, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49390, prefix="1.2.3.0/24", as_path=(49390, 9110, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50338, prefix="1.2.3.0/24", as_path=(50338, 9110, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61359, prefix="1.2.3.0/24", as_path=(61359, 9110, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=5626, prefix="1.2.3.0/24", as_path=(5626, 9186, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34643, prefix="1.2.3.0/24", as_path=(34643, 9186, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39384, prefix="1.2.3.0/24", as_path=(39384, 9186, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43652, prefix="1.2.3.0/24", as_path=(43652, 9186, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47202, prefix="1.2.3.0/24", as_path=(47202, 9186, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201170, prefix="1.2.3.0/24", as_path=(201170, 9186, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202170, prefix="1.2.3.0/24", as_path=(202170, 9186, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204094, prefix="1.2.3.0/24", as_path=(204094, 9186, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210221, prefix="1.2.3.0/24", as_path=(210221, 9186, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212073, prefix="1.2.3.0/24", as_path=(212073, 9186, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=262603, prefix="1.2.3.0/24", as_path=(262603, 9186, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=46652, prefix="1.2.3.0/24", as_path=(46652, 14061, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=6732, prefix="1.2.3.0/24", as_path=(6732, 15623, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=31051, prefix="1.2.3.0/24", as_path=(31051, 15623, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35712, prefix="1.2.3.0/24", as_path=(35712, 15623, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39037, prefix="1.2.3.0/24", as_path=(39037, 15623, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39895, prefix="1.2.3.0/24", as_path=(39895, 15623, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41590, prefix="1.2.3.0/24", as_path=(41590, 15623, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43107, prefix="1.2.3.0/24", as_path=(43107, 15623, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43291, prefix="1.2.3.0/24", as_path=(43291, 15623, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50805, prefix="1.2.3.0/24", as_path=(50805, 15623, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51786, prefix="1.2.3.0/24", as_path=(51786, 15623, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61232, prefix="1.2.3.0/24", as_path=(61232, 15623, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202451, prefix="1.2.3.0/24", as_path=(202451, 15623, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34913,
        prefix="1.2.3.0/24",
        as_path=(34913, 16080, 29075, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205931,
        prefix="1.2.3.0/24",
        as_path=(205931, 16316, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47450, prefix="1.2.3.0/24", as_path=(47450, 16353, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=32398, prefix="1.2.3.0/24", as_path=(32398, 19711, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37510, prefix="1.2.3.0/24", as_path=(37510, 19711, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327765, prefix="1.2.3.0/24", as_path=(327765, 19711, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328169, prefix="1.2.3.0/24", as_path=(328169, 19711, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328531, prefix="1.2.3.0/24", as_path=(328531, 19711, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=44091, prefix="1.2.3.0/24", as_path=(44091, 21101, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204919,
        prefix="1.2.3.0/24",
        as_path=(204919, 21226, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=23659, prefix="1.2.3.0/24", as_path=(23659, 23678, 45352, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=132033, prefix="1.2.3.0/24", as_path=(132033, 23678, 45352, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43661, prefix="1.2.3.0/24", as_path=(43661, 24758, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48851, prefix="1.2.3.0/24", as_path=(48851, 25773, 36351, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57973, prefix="1.2.3.0/24", as_path=(57973, 28709, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=35673,
        prefix="1.2.3.0/24",
        as_path=(35673, 29046, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49997,
        prefix="1.2.3.0/24",
        as_path=(49997, 29304, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57950,
        prefix="1.2.3.0/24",
        as_path=(57950, 29355, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21375, prefix="1.2.3.0/24", as_path=(21375, 30936, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48763, prefix="1.2.3.0/24", as_path=(48763, 30936, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202344, prefix="1.2.3.0/24", as_path=(202344, 30936, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205433, prefix="1.2.3.0/24", as_path=(205433, 30936, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209962, prefix="1.2.3.0/24", as_path=(209962, 30936, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=10798,
        prefix="1.2.3.0/24",
        as_path=(10798, 33567, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25695,
        prefix="1.2.3.0/24",
        as_path=(25695, 33567, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37331,
        prefix="1.2.3.0/24",
        as_path=(37331, 33567, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37505,
        prefix="1.2.3.0/24",
        as_path=(37505, 33567, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197865,
        prefix="1.2.3.0/24",
        as_path=(197865, 34139, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201092,
        prefix="1.2.3.0/24",
        as_path=(201092, 34139, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=29554, prefix="1.2.3.0/24", as_path=(29554, 34485, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43319,
        prefix="1.2.3.0/24",
        as_path=(43319, 34602, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49060,
        prefix="1.2.3.0/24",
        as_path=(49060, 34602, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=58072,
        prefix="1.2.3.0/24",
        as_path=(58072, 34602, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=59679,
        prefix="1.2.3.0/24",
        as_path=(59679, 34602, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203117,
        prefix="1.2.3.0/24",
        as_path=(203117, 34602, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205595,
        prefix="1.2.3.0/24",
        as_path=(205595, 34602, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13105,
        prefix="1.2.3.0/24",
        as_path=(13105, 34875, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201835,
        prefix="1.2.3.0/24",
        as_path=(201835, 34875, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205437,
        prefix="1.2.3.0/24",
        as_path=(205437, 34912, 15502, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206051,
        prefix="1.2.3.0/24",
        as_path=(206051, 34912, 15502, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48938, prefix="1.2.3.0/24", as_path=(48938, 35401, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34939,
        prefix="1.2.3.0/24",
        as_path=(34939, 35487, 56630, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50069,
        prefix="1.2.3.0/24",
        as_path=(50069, 35487, 56630, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212903,
        prefix="1.2.3.0/24",
        as_path=(212903, 35487, 56630, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208578, prefix="1.2.3.0/24", as_path=(208578, 35617, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41045, prefix="1.2.3.0/24", as_path=(41045, 35717, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37201, prefix="1.2.3.0/24", as_path=(37201, 37009, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37258,
        prefix="1.2.3.0/24",
        as_path=(37258, 37125, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327953,
        prefix="1.2.3.0/24",
        as_path=(327953, 37125, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328925, prefix="1.2.3.0/24", as_path=(328925, 37172, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37316, prefix="1.2.3.0/24", as_path=(37316, 37314, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37441, prefix="1.2.3.0/24", as_path=(37441, 37314, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328074, prefix="1.2.3.0/24", as_path=(328074, 37314, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328313, prefix="1.2.3.0/24", as_path=(328313, 37314, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328816, prefix="1.2.3.0/24", as_path=(328816, 37314, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37658, prefix="1.2.3.0/24", as_path=(37658, 37670, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21166, prefix="1.2.3.0/24", as_path=(21166, 39045, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50703, prefix="1.2.3.0/24", as_path=(50703, 39045, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203353, prefix="1.2.3.0/24", as_path=(203353, 39045, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39280,
        prefix="1.2.3.0/24",
        as_path=(39280, 39232, 196925, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=21077, prefix="1.2.3.0/24", as_path=(21077, 39545, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50910, prefix="1.2.3.0/24", as_path=(50910, 39545, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204239, prefix="1.2.3.0/24", as_path=(204239, 39545, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209329, prefix="1.2.3.0/24", as_path=(209329, 39545, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210310, prefix="1.2.3.0/24", as_path=(210310, 39545, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=25419,
        prefix="1.2.3.0/24",
        as_path=(25419, 39702, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48132,
        prefix="1.2.3.0/24",
        as_path=(48132, 39702, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197491,
        prefix="1.2.3.0/24",
        as_path=(197491, 39702, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202698,
        prefix="1.2.3.0/24",
        as_path=(202698, 39702, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207404,
        prefix="1.2.3.0/24",
        as_path=(207404, 39702, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61025,
        prefix="1.2.3.0/24",
        as_path=(61025, 41653, 29075, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=8909,
        prefix="1.2.3.0/24",
        as_path=(8909, 41789, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48058,
        prefix="1.2.3.0/24",
        as_path=(48058, 41789, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39379,
        prefix="1.2.3.0/24",
        as_path=(39379, 41938, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42253,
        prefix="1.2.3.0/24",
        as_path=(42253, 42097, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=13190, prefix="1.2.3.0/24", as_path=(13190, 42162, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39145, prefix="1.2.3.0/24", as_path=(39145, 42162, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=206478, prefix="1.2.3.0/24", as_path=(206478, 42162, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43095, prefix="1.2.3.0/24", as_path=(43095, 42231, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47860,
        prefix="1.2.3.0/24",
        as_path=(47860, 42291, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49825,
        prefix="1.2.3.0/24",
        as_path=(49825, 42291, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51507,
        prefix="1.2.3.0/24",
        as_path=(51507, 42291, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=5387,
        prefix="1.2.3.0/24",
        as_path=(5387, 42451, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197607,
        prefix="1.2.3.0/24",
        as_path=(197607, 43559, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198167, prefix="1.2.3.0/24", as_path=(198167, 44084, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=201352, prefix="1.2.3.0/24", as_path=(201352, 44092, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207545, prefix="1.2.3.0/24", as_path=(207545, 44092, 12779, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42465, prefix="1.2.3.0/24", as_path=(42465, 44444, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43251, prefix="1.2.3.0/24", as_path=(43251, 44444, 37100, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56140, prefix="1.2.3.0/24", as_path=(56140, 45144, 45352, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198685,
        prefix="1.2.3.0/24",
        as_path=(198685, 47241, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51488, prefix="1.2.3.0/24", as_path=(51488, 47418, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=197957, prefix="1.2.3.0/24", as_path=(197957, 47680, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=205751, prefix="1.2.3.0/24", as_path=(205751, 47680, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=39131,
        prefix="1.2.3.0/24",
        as_path=(39131, 47895, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49742,
        prefix="1.2.3.0/24",
        as_path=(49742, 47895, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56667,
        prefix="1.2.3.0/24",
        as_path=(56667, 47895, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60936,
        prefix="1.2.3.0/24",
        as_path=(60936, 47895, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=64492,
        prefix="1.2.3.0/24",
        as_path=(64492, 47895, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208544,
        prefix="1.2.3.0/24",
        as_path=(208544, 47895, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48651,
        prefix="1.2.3.0/24",
        as_path=(48651, 48043, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41388,
        prefix="1.2.3.0/24",
        as_path=(41388, 48219, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200123,
        prefix="1.2.3.0/24",
        as_path=(200123, 48354, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34450,
        prefix="1.2.3.0/24",
        as_path=(34450, 48453, 9050, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56866,
        prefix="1.2.3.0/24",
        as_path=(56866, 48462, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62422, prefix="1.2.3.0/24", as_path=(62422, 48719, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60553, prefix="1.2.3.0/24", as_path=(60553, 50218, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60956, prefix="1.2.3.0/24", as_path=(60956, 50218, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=12331,
        prefix="1.2.3.0/24",
        as_path=(12331, 51402, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51378,
        prefix="1.2.3.0/24",
        as_path=(51378, 51402, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=212181,
        prefix="1.2.3.0/24",
        as_path=(212181, 51402, 3209, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41525,
        prefix="1.2.3.0/24",
        as_path=(41525, 51408, 50509, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207636,
        prefix="1.2.3.0/24",
        as_path=(207636, 51408, 50509, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42002, prefix="1.2.3.0/24", as_path=(42002, 57018, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=48369, prefix="1.2.3.0/24", as_path=(48369, 57227, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60768, prefix="1.2.3.0/24", as_path=(60768, 58326, 25091, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61308,
        prefix="1.2.3.0/24",
        as_path=(61308, 59574, 50509, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=9516,
        prefix="1.2.3.0/24",
        as_path=(9516, 59598, 56630, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207867, prefix="1.2.3.0/24", as_path=(207867, 60490, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=41259,
        prefix="1.2.3.0/24",
        as_path=(41259, 60738, 44941, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200721,
        prefix="1.2.3.0/24",
        as_path=(200721, 60757, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203481,
        prefix="1.2.3.0/24",
        as_path=(203481, 60757, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208448,
        prefix="1.2.3.0/24",
        as_path=(208448, 60757, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208946,
        prefix="1.2.3.0/24",
        as_path=(208946, 60757, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=213217,
        prefix="1.2.3.0/24",
        as_path=(213217, 60757, 41798, 9198, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=50895,
        prefix="1.2.3.0/24",
        as_path=(50895, 62040, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=60365,
        prefix="1.2.3.0/24",
        as_path=(60365, 62040, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=133114,
        prefix="1.2.3.0/24",
        as_path=(133114, 132198, 45352, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=147040,
        prefix="1.2.3.0/24",
        as_path=(147040, 140586, 45352, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=5548,
        prefix="1.2.3.0/24",
        as_path=(5548, 196695, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=34639,
        prefix="1.2.3.0/24",
        as_path=(34639, 196695, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=42135,
        prefix="1.2.3.0/24",
        as_path=(42135, 196695, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47183,
        prefix="1.2.3.0/24",
        as_path=(47183, 196695, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=47307,
        prefix="1.2.3.0/24",
        as_path=(47307, 196695, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49017,
        prefix="1.2.3.0/24",
        as_path=(49017, 196695, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=51680,
        prefix="1.2.3.0/24",
        as_path=(51680, 196695, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56631,
        prefix="1.2.3.0/24",
        as_path=(56631, 196695, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=61411,
        prefix="1.2.3.0/24",
        as_path=(61411, 196695, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=62316,
        prefix="1.2.3.0/24",
        as_path=(62316, 196695, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=198929,
        prefix="1.2.3.0/24",
        as_path=(198929, 196695, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199546,
        prefix="1.2.3.0/24",
        as_path=(199546, 196695, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200048,
        prefix="1.2.3.0/24",
        as_path=(200048, 196695, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=203891,
        prefix="1.2.3.0/24",
        as_path=(203891, 196695, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204117,
        prefix="1.2.3.0/24",
        as_path=(204117, 196695, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=207344,
        prefix="1.2.3.0/24",
        as_path=(207344, 196695, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209343,
        prefix="1.2.3.0/24",
        as_path=(209343, 196695, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209684,
        prefix="1.2.3.0/24",
        as_path=(209684, 196695, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209701,
        prefix="1.2.3.0/24",
        as_path=(209701, 196695, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209702,
        prefix="1.2.3.0/24",
        as_path=(209702, 196695, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209773,
        prefix="1.2.3.0/24",
        as_path=(209773, 196695, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56952,
        prefix="1.2.3.0/24",
        as_path=(56952, 196797, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204145, prefix="1.2.3.0/24", as_path=(204145, 197816, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=199991, prefix="1.2.3.0/24", as_path=(199991, 198541, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=57553,
        prefix="1.2.3.0/24",
        as_path=(57553, 199420, 49063, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=43887,
        prefix="1.2.3.0/24",
        as_path=(43887, 200107, 8470, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211765,
        prefix="1.2.3.0/24",
        as_path=(211765, 200729, 196925, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208957,
        prefix="1.2.3.0/24",
        as_path=(208957, 202089, 29075, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=211790,
        prefix="1.2.3.0/24",
        as_path=(211790, 203622, 196925, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=213117,
        prefix="1.2.3.0/24",
        as_path=(213117, 205500, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=56422, prefix="1.2.3.0/24", as_path=(56422, 206276, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=200359, prefix="1.2.3.0/24", as_path=(200359, 206276, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=202767, prefix="1.2.3.0/24", as_path=(202767, 206276, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=204542, prefix="1.2.3.0/24", as_path=(204542, 206276, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=210692, prefix="1.2.3.0/24", as_path=(210692, 206276, 4455, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=209311,
        prefix="1.2.3.0/24",
        as_path=(209311, 207906, 13287, 4455, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=49166,
        prefix="1.2.3.0/24",
        as_path=(49166, 208142, 20485, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=20979, prefix="1.2.3.0/24", as_path=(20979, 209794, 3216, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=37547,
        prefix="1.2.3.0/24",
        as_path=(37547, 327707, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328618,
        prefix="1.2.3.0/24",
        as_path=(328618, 327707, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328771,
        prefix="1.2.3.0/24",
        as_path=(328771, 327707, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328176,
        prefix="1.2.3.0/24",
        as_path=(328176, 327791, 327782, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327747,
        prefix="1.2.3.0/24",
        as_path=(327747, 327828, 327732, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=327896, prefix="1.2.3.0/24", as_path=(327896, 327901, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328621, prefix="1.2.3.0/24", as_path=(328621, 327901, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328677, prefix="1.2.3.0/24", as_path=(328677, 327901, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=11157, prefix="1.2.3.0/24", as_path=(11157, 327935, 5713, 29452)
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328131,
        prefix="1.2.3.0/24",
        as_path=(328131, 328160, 37662, 3216, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328301,
        prefix="1.2.3.0/24",
        as_path=(328301, 328271, 15399, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328856,
        prefix="1.2.3.0/24",
        as_path=(328856, 328271, 15399, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=208638,
        prefix="1.2.3.0/24",
        as_path=(208638, 328317, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328016,
        prefix="1.2.3.0/24",
        as_path=(328016, 328317, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328339,
        prefix="1.2.3.0/24",
        as_path=(328339, 328317, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328521,
        prefix="1.2.3.0/24",
        as_path=(328521, 328317, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=329039,
        prefix="1.2.3.0/24",
        as_path=(329039, 328568, 328366, 37100, 29452),
    ).as_path
)
reports_path_list.append(
    Report(
        reporting_asn=328854,
        prefix="1.2.3.0/24",
        as_path=(328854, 328945, 37662, 3216, 29452),
    ).as_path
)
