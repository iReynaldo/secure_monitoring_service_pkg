from caida_collector_pkg import CustomerProviderLink as CPLink
from caida_collector_pkg import PeerLink

from .graph_info import GraphInfo
from bgp_simulator_pkg.enums import ASNs


class Graph068(GraphInfo):
    r"""
    Image of scenario @ this link
    TODO: add link here
    """

    def __init__(self):
        self.attacker_asn_set = {666,}
        super(Graph068, self).__init__(
            peer_links=set([

                PeerLink(3, 12),
                PeerLink(5, 16),
            ]),
            customer_provider_links=set(
                [
                    CPLink(provider_asn=3, customer_asn=6),
                    CPLink(provider_asn=1, customer_asn=ASNs.VICTIM.value),
                    CPLink(provider_asn=6, customer_asn=9),
                    CPLink(provider_asn=6, customer_asn=20940),
                    CPLink(provider_asn=20940, customer_asn=1),
                    CPLink(provider_asn=9, customer_asn=666),  # Attacker
                    CPLink(provider_asn=13, customer_asn=3),
                    CPLink(provider_asn=13, customer_asn=15),
                    CPLink(provider_asn=3, customer_asn=5),
                    CPLink(provider_asn=5, customer_asn=14),
                    CPLink(provider_asn=14, customer_asn=15),
                    CPLink(provider_asn=16625, customer_asn=ASNs.VICTIM.value),
                    CPLink(provider_asn=16625, customer_asn=6),
                ]
            ),
        )
