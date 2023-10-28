from typing import Dict, Type

from bgpy import AS

from bgpy import EngineTestConfig
from bgpy import BGPSimpleAS
from bgpy import ROVSimpleAS
from bgpy import ASNs

from rovpp_pkg import ROVPPAnn

from .. import graphs
from secure_monitoring_service_pkg import ArtemisSubprefixHijackScenario
from secure_monitoring_service_pkg import Artermis


class Config161(EngineTestConfig):
    """ """

    name = "161"
    desc = "ARTEMIS 2 Attackers"
    graph = graphs.Graph061()
    relay_asns = {12, 13}
    scenario = ArtemisSubprefixHijackScenario(
        num_attackers=2,
        attacker_asns=graph.attacker_asn_set,
        victim_asns={ASNs.VICTIM.value},
        AdoptASCls=Artermis,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
        relay_asns=relay_asns,
    )

    non_default_as_cls_dict: Dict[int, Type[AS]] = {
        3: Artermis,
        4: Artermis,
        8: Artermis,
        10: Artermis,
        11: Artermis,
        7: ROVSimpleAS,
    }

    propagation_rounds = 1
