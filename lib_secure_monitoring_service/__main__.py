from time import perf_counter, localtime

from lib_bgp_simulator import Simulator, BGPAS, Graph, MPMethod

from lib_rovpp import ROVPPV1SimpleAS, ROVPPV1LiteSimpleAS

from lib_secure_monitoring_service.engine_inputs import V4SubprefixHijack
from lib_secure_monitoring_service.rov_sms import ROVSMS, ROVSMSK1, ROVSMSK2, ROVSMSK3, ROVSMSK4, ROVSMSK5, ROVSMSK6, ROVSMSK7, ROVSMSK10, ROVSMSK20
from lib_secure_monitoring_service.v4_graph import V4Graph

def main():
    Simulator().run(graphs=[V4Graph(percent_adoptions=[0,5,10,20,40,60,80,100],
                                    adopt_as_classes=[ROVSMS],
                                    EngineInputCls=V4SubprefixHijack,
                                    num_trials=1,
                                    BaseASCls=BGPAS)],
                    mp_method = MPMethod.SINGLE_PROCESS
                    )


if __name__ == "__main__":
    try:
        start_time = perf_counter()
        main()
    finally:
        end_time = perf_counter()
        print("extraction_time=", end_time - start_time)
        print("timestamp=", localtime())
