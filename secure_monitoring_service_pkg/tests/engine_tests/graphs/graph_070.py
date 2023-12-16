from caida_collector_pkg import CustomerProviderLink as CPLink
from caida_collector_pkg import PeerLink

from .graph_info import GraphInfo
from bgp_simulator_pkg.enums import ASNs

from secure_monitoring_service_pkg import CDN


class Graph070(GraphInfo):
    r"""
    Image of scenario @ this link
    TODO: add link here
    This is a copy of graph 161 but with CDN Akamai
    """

    def __init__(self):
        self.attacker_asn_set = {660, 666}
        self.relay_asns = CDN.akamai
        super(Graph070, self).__init__(
            peer_links=set([
                PeerLink(3, 6)
            ]),
            customer_provider_links=set(
                [
                    CPLink(provider_asn=2, customer_asn=4),
                    CPLink(provider_asn=2, customer_asn=10),
                    CPLink(provider_asn=2, customer_asn=1),
                    CPLink(provider_asn=2, customer_asn=11),
                    CPLink(provider_asn=2, customer_asn=666),  # Attacker
                    CPLink(provider_asn=1, customer_asn=ASNs.VICTIM.value),
                    CPLink(provider_asn=7, customer_asn=2),
                    CPLink(provider_asn=6, customer_asn=7),
                    CPLink(provider_asn=6, customer_asn=8),
                    CPLink(provider_asn=6, customer_asn=16625),
                    CPLink(provider_asn=16625, customer_asn=1),
                    CPLink(provider_asn=8, customer_asn=9),
                    CPLink(provider_asn=9, customer_asn=660),  # Attacker
                    CPLink(provider_asn=3, customer_asn=7),
                    CPLink(provider_asn=3, customer_asn=5),
                    CPLink(provider_asn=20940, customer_asn=1),
                    CPLink(provider_asn=20940, customer_asn=6),
                ]
            ),
        )
