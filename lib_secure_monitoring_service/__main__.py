from lib_bgp_simulator import Simulator, BGPAS, Graph, MPMethod

from lib_rovpp import ROVPPV1SimpleAS

from lib_secure_monitoring_service.engine_inputs import V4SubprefixHijack
from lib_secure_monitoring_service.rov_sms import ROVSMS, ROVSMSK1, ROVSMSK2, ROVSMSK3, ROVSMSK4, ROVSMSK5, ROVSMSK6, ROVSMSK7, ROVSMSK10, ROVSMSK20
from lib_secure_monitoring_service.rov_sms import ROVSMSK20000, ROVSMSK30000

from lib_secure_monitoring_service.rov_sms import ROVSMSK30, ROVSMSK50, ROVSMSK70, ROVSMSK100, ROVSMSK150, ROVSMSK200, ROVSMSK300, ROVSMSK500, ROVSMSK1000, ROVSMSK2000, ROVSMSK5000

from lib_secure_monitoring_service.v4_graph import V4Graph


def main():
    Simulator().run(graphs=[V4Graph(percent_adoptions=[0,5,10,20,40,60,80,100],
                                    adopt_as_classes=[ROVPPV1SimpleAS, ROVSMSK500, ROVSMSK1000, ROVSMSK2000, ROVSMSK5000, ROVSMSK20000, ROVSMSK30000],
                                    EngineInputCls=V4SubprefixHijack,
                                    num_trials=10,
                                    BaseASCls=BGPAS)],
                    mp_method = MPMethod.MP
                    )


if __name__ == "__main__":
    main()
