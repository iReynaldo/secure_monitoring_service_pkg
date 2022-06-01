from time import perf_counter
from memory_profiler import profile

from lib_secure_monitoring_service import mvdp

# resrouce on profiling python code
# https://betterprogramming.pub/a-comprehensive-guide-to-profiling-python-programs-f8b7db772e6#:~:text=A%20Comprehensive%20Guide%20to%20Profiling%20Python%20Programs%201,The%20Last%20Percent.%20...%209%20Last%20Words.%20
# https://www.itprc.com/python-profiler-guide/
# https://www.pythontutorial.net/advanced-python/python-context-managers/#:~:text=Python%20context%20managers%20work%20based%20on%20the%20context,a%20class%20that%20supports%20the%20context%20manager%20protocol.

# Dataclasses
# https://docs.python.org/3.9/library/dataclasses.html

# Credits to Python Tutorial
# https://www.pythontutorial.net/advanced-python/python-context-managers/#:~:text=Python%20context%20managers%20work%20based%20on%20the%20context,a%20class%20that%20supports%20the%20context%20manager%20protocol.
class timer:
    """
    Time whatever is in the context
    This seems to add 1 second to the time
    """
    def __init__(self, label, expected_time):
        self.label = label
        self.expected_time = expected_time
        self.elapsed_time = None

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.end = perf_counter()
        self.elapsed_time = self.end - self.start
        print('{} : {}'.format(self.label, self.end - self.start))
        print('Expected Time: {}'.format(self.expected_time))
        # Calculating Faster than
        # https://math.stackexchange.com/questions/1227389/what-is-the-difference-between-faster-by-factor-and-faster-by-percent
        faster_than = (self.expected_time - self.elapsed_time) / self.expected_time
        print('This Run was {}% faster than Expected: '.format(faster_than))
        return False


# TODO: Generate Performance Report
# with timer("Path List 1") as atimer:
#     from lib_secure_monitoring_service.tests.performance_tests.mvdp_benchmark.report_path_lists.path_list_1 import reports_path_list

# with timer("Path List 2") as atimer:
#     from lib_secure_monitoring_service.tests.performance_tests.mvdp_benchmark.report_path_lists.path_list_2 import reports_path_list
#
# with timer("Path List 3") as atimer:
#     from lib_secure_monitoring_service.tests.performance_tests.mvdp_benchmark.report_path_lists.path_list_3 import reports_path_list
#
# with timer("Path List 4") as atimer:
#     from lib_secure_monitoring_service.tests.performance_tests.mvdp_benchmark.report_path_lists.path_list_4 import reports_path_list
#
# with timer("Path List 5") as atimer:
#     from lib_secure_monitoring_service.tests.performance_tests.mvdp_benchmark.report_path_lists.path_list_5 import reports_path_list


@profile
def internet_scale_path_list_1():
    """
    k = 1
    :return:
    """
    from lib_secure_monitoring_service.tests.performance_tests.mvdp_benchmark.report_path_lists.path_list_1 import expected_time, reports_path_list
    # flow_value = mvdp.get_mvdp_with_subgraph_pictures(reports_path_list, 1)
    with timer("Path List 1", expected_time) as _:
        avoid_list = mvdp.get_avoid_list(reports_path_list, 1)

@profile
def internet_scale_path_list_2():
    """
    k = 1
    :return:
    """
    from lib_secure_monitoring_service.tests.performance_tests.mvdp_benchmark.report_path_lists.path_list_2 import expected_time, reports_path_list
    # flow_value = mvdp.get_mvdp_with_subgraph_pictures(reports_path_list, 1)
    with timer("Path List 2", expected_time) as _:
        avoid_list = mvdp.get_avoid_list(reports_path_list, 1)


@profile
def internet_scale_path_list_3():
    """
    k = 1
    :return:
    """
    from lib_secure_monitoring_service.tests.performance_tests.mvdp_benchmark.report_path_lists.path_list_3 import expected_time, reports_path_list
    # flow_value = mvdp.get_mvdp_with_subgraph_pictures(reports_path_list, 1)
    with timer("Path List 3", expected_time) as _:
        avoid_list = mvdp.get_avoid_list(reports_path_list, 1)


@profile
def internet_scale_path_list_4():
    """
    k = 1
    :return:
    """
    from lib_secure_monitoring_service.tests.performance_tests.mvdp_benchmark.report_path_lists.path_list_4 import expected_time, reports_path_list
    # flow_value = mvdp.get_mvdp_with_subgraph_pictures(reports_path_list, 1)
    with timer("Path List 4", expected_time) as _:
        avoid_list = mvdp.get_avoid_list(reports_path_list, 1)



internet_scale_path_list_1()
internet_scale_path_list_2()
internet_scale_path_list_3()
internet_scale_path_list_4()