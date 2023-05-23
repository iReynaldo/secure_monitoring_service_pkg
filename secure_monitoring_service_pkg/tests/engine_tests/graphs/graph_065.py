from caida_collector_pkg import CustomerProviderLink as CPLink
from caida_collector_pkg import PeerLink

from .graph_info import GraphInfo
from bgp_simulator_pkg.enums import ASNs

# TODO: consider importing the CDN class and use the neustar values directly
#  rather than hard copying them


class Graph065(GraphInfo):
    r"""
    Image of scenario @ this link
    TODO: add link here
    """

    def __init__(self):
        self.attacker_asn_set = {ASNs.ATTACKER.value}
        super(Graph065, self).__init__(
            customer_provider_links=set(
                [
                    CPLink(provider_asn=12008, customer_asn=7786),
                    CPLink(provider_asn=12008, customer_asn=4),
                    CPLink(provider_asn=7786, customer_asn=1),
                    CPLink(provider_asn=4, customer_asn=ASNs.ATTACKER.value),  # Attacker
                    CPLink(provider_asn=12008, customer_asn=5),
                    CPLink(provider_asn=5, customer_asn=ASNs.ATTACKER.value),  # Attacker
                    CPLink(provider_asn=5, customer_asn=ASNs.VICTIM.value),
                    CPLink(provider_asn=19905, customer_asn=5),
                    CPLink(provider_asn=19905, customer_asn=ASNs.VICTIM.value)
                ]
            ),
        )
