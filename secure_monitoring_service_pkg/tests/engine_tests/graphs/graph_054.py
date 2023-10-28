from caida_collector_pkg import CustomerProviderLink as CPLink


from .graph_info import GraphInfo
from bgp_simulator_pkg.enums import ASNs


class Graph054(GraphInfo):
    r"""
    Image of scenario @ this link
    Only can be used for multi-attacker scenarios
    TODO: add link here
    """

    def __init__(self):
        self.attacker_asn_set = {660, 661}
        super(Graph054, self).__init__(
            peer_links=set([]),
            customer_provider_links=set(
                [
                    CPLink(provider_asn=2, customer_asn=4),
                    CPLink(provider_asn=2, customer_asn=10),
                    CPLink(provider_asn=2, customer_asn=1),
                    CPLink(provider_asn=2, customer_asn=11),
                    CPLink(provider_asn=11, customer_asn=12),
                    CPLink(provider_asn=11, customer_asn=13),
                    CPLink(provider_asn=2, customer_asn=660),  # Attacker
                    CPLink(provider_asn=1, customer_asn=ASNs.VICTIM.value),
                    CPLink(provider_asn=14, customer_asn=ASNs.VICTIM.value),
                    CPLink(provider_asn=5, customer_asn=661),  # Attacker
                    CPLink(provider_asn=5, customer_asn=14),
                    CPLink(provider_asn=7, customer_asn=2),
                    CPLink(provider_asn=6, customer_asn=7),
                    CPLink(provider_asn=6, customer_asn=8),
                    CPLink(provider_asn=8, customer_asn=9),
                    CPLink(provider_asn=3, customer_asn=7),
                    CPLink(provider_asn=3, customer_asn=5),
                ]
            ),
        )
