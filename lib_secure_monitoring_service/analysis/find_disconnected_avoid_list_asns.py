from time import perf_counter, localtime
import csv
import random
import os
import sys

from lib_bgp_simulator import Simulator, BGPAS, Graph, MPMethod

from lib_rovpp import ROVPPV1SimpleAS, ROVPPV1LiteSimpleAS

from lib_secure_monitoring_service.engine_inputs import V4SubprefixHijack
from lib_secure_monitoring_service.rov_sms import ROVSMS, ROVSMSK1, ROVSMSK2, ROVSMSK3, ROVSMSK4, ROVSMSK5, ROVSMSK6, ROVSMSK7, ROVSMSK10, ROVSMSK20
from lib_secure_monitoring_service.rov_sms import ROVSMSK10, ROVSMSK20, ROVSMSK50, ROVSMSK100, ROVSMSK300, ROVSMSK500
from lib_secure_monitoring_service.v4_graph import V4Graph


# Set Random Seed to determinitic runs
seed = sys.argv[1]
os.environ['PYTHONHASHSEED'] = seed
random.seed(int(seed))


def main():
    Simulator().run(graphs=[V4Graph(percent_adoptions=[0],
                                    adopt_as_classes=[ROVSMSK1],
                                    EngineInputCls=V4SubprefixHijack,
                                    num_trials=1,
                                    BaseASCls=BGPAS)],
                    mp_method = MPMethod.SINGLE_PROCESS
                    )


if __name__ == "__main__":
    try:
        start_time = perf_counter()
        with open('as_metadata.tsv', 'w') as csvfile:  # TODO: Remove this context once done collecting AS metadata
            fieldnames = [
                'percentAdoption', 'trial', 'asn', 'adopting', 'legitPrefixASPath', 'rank',
                'numPeers', 'numProviders', 'numCustomers', 'degree', 'subgraph', 'simAvoidList',
                'traceback_asn', 'victimASN', 'attackerASN', 'traceback_outcome'
            ]
            writer = csv.DictWriter(csvfile, delimiter='\t', fieldnames=fieldnames)
            writer.writeheader()
        main()
    finally:
        end_time = perf_counter()
        print("extraction_time=", end_time - start_time)
        print("timestamp=", localtime())
