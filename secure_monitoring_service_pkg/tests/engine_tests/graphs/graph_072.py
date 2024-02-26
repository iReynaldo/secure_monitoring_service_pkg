from caida_collector_pkg import CustomerProviderLink as CPLink
from caida_collector_pkg import PeerLink

from .graph_info import GraphInfo
from bgp_simulator_pkg.enums import ASNs

from secure_monitoring_service_pkg import CDN


class Graph072(GraphInfo):
    r"""
    This is a copy of 162, but with CDN Akamai
    Image of scenario @ this link
    TODO: add link here
    """

    def __init__(self):
        self.attacker_asn_set = {666}
        self.relay_asns = CDN.cloudflare
        super(Graph072, self).__init__(
            peer_links=set([]),
            customer_provider_links=set(
                [
                    CPLink(provider_asn=13335, customer_asn=3),
                    CPLink(provider_asn=13335, customer_asn=4),
                    CPLink(provider_asn=3, customer_asn=2),
                    CPLink(provider_asn=3, customer_asn=666),  # Attacker
                    CPLink(provider_asn=3, customer_asn=1),
                    CPLink(provider_asn=1, customer_asn=ASNs.VICTIM.value),
                ]
            ),
        )
