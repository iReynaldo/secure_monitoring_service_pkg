from caida_collector_pkg import CustomerProviderLink as CPLink
from caida_collector_pkg import PeerLink

from .graph_info import GraphInfo
from bgp_simulator_pkg.enums import ASNs


class Graph064(GraphInfo):
    r"""
    Image of scenario @ this link
    TODO: add link here
    """

    def __init__(self):
        self.attacker_asn_set = {ASNs.ATTACKER.value}
        super(Graph064, self).__init__(
            peer_links=set([PeerLink(3, 6), ]),
            customer_provider_links=set(
                [
                    CPLink(provider_asn=3, customer_asn=2),
                    CPLink(provider_asn=3, customer_asn=4),
                    CPLink(provider_asn=2, customer_asn=1),
                    CPLink(provider_asn=4, customer_asn=ASNs.ATTACKER.value),  # Attacker
                    CPLink(provider_asn=3, customer_asn=5),
                    CPLink(provider_asn=5, customer_asn=ASNs.ATTACKER.value),  # Attacker
                    CPLink(provider_asn=5, customer_asn=ASNs.VICTIM.value),
                    CPLink(provider_asn=6, customer_asn=5),
                    CPLink(provider_asn=6, customer_asn=ASNs.VICTIM.value)
                ]
            ),
        )
