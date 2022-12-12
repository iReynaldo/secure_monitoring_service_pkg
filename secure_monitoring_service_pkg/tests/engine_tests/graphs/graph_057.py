from caida_collector_pkg import CustomerProviderLink as CPLink
from caida_collector_pkg import PeerLink as PLink


from .graph_info import GraphInfo
from bgp_simulator_pkg.enums import ASNs


class Graph057(GraphInfo):
    r"""
    Image of scenario @ this link
    Only can be used for multi-attacker scenarios
    TODO: add link here
    """

    def __init__(self):
        self.attacker_asn_set = {660, 661, 662}
        super(Graph057, self).__init__(
            peer_links=set([PLink(4, 5),
                            PLink(4, 8),
                            PLink(6, 3),
                            PLink(11, 13),
                            PLink(9, 12)]),
            customer_provider_links=set(
                [
                    CPLink(provider_asn=4, customer_asn=2),
                    CPLink(provider_asn=2, customer_asn=ASNs.VICTIM.value),
                    CPLink(provider_asn=3, customer_asn=ASNs.VICTIM.value),
                    CPLink(provider_asn=6, customer_asn=70),
                    CPLink(provider_asn=6, customer_asn=660),  # Attacker
                    CPLink(provider_asn=5, customer_asn=71),
                    CPLink(provider_asn=8, customer_asn=9),
                    CPLink(provider_asn=9, customer_asn=661),  # Attacker
                    CPLink(provider_asn=9, customer_asn=72),
                    CPLink(provider_asn=11, customer_asn=10),
                    CPLink(provider_asn=10, customer_asn=ASNs.VICTIM.value),
                    CPLink(provider_asn=11, customer_asn=12),
                    CPLink(provider_asn=12, customer_asn=662),  # Attacker
                    CPLink(provider_asn=13, customer_asn=73)
                ]
            ),
        )
