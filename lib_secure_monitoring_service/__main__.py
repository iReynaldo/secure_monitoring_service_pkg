from lib_bgp_simulator import Simulator, BGPAS, Graph
from .engine_inputs import V4SubprefixHijack
from .rov_sms import ROVSMS

def main():
    Simulator().run(graphs=[Graph(percent_adoptions=[5],
                                  adopt_as_classes=[ROVSMS],
                                  EngineInputCls=V4SubprefixHijack,
                                  num_trials=1,
                                  BaseASCls=BGPAS)]
                    )
