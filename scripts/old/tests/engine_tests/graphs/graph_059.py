from bgpy import CustomerProviderLink as CPLink

from .graph_info import GraphInfo
from bgpy.enums import ASNs


class Graph059(GraphInfo):
    r"""
    Image of scenario @ this link
    TODO: add link here
    """

    def __init__(self):
        self.attacker_asn_set = {660, 666}
        super(Graph059, self).__init__(
            peer_links=set([]),
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
                    CPLink(provider_asn=8, customer_asn=9),
                    CPLink(provider_asn=9, customer_asn=660),  # Attacker
                    CPLink(provider_asn=3, customer_asn=7),
                    CPLink(provider_asn=3, customer_asn=5),
                ]
            ),
        )
