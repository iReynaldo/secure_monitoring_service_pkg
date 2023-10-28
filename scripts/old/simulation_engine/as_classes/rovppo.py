import random

from rovpp import ROVPPV1LiteSimpleAS


class ROVPPO(ROVPPV1LiteSimpleAS):
    name = "ROV++ V1 Lite Simple Overlayed"

    def __init__(self, *args, **kwargs):
        """Just ROV++ V1 Lite Simple with access to relay service."""
        super(ROVPPO, self).__init__(*args, **kwargs)
        # The following variable indicates if the AS used a relay
        # and it's updated in the V4Subgraph method _recalculate_outcomes_with_relays
        self.used_relay = False

    def use_relay(self, relay_asns, relay_prefix_dict, assume_relays_are_reachable):
        """return the relay that it would use"""
        # TODO: Future enhancement: Consider picking preference with
        #   1. Relationship preference
        #   2. Shortest path
        # Check if Relays are assumed to be reachable
        if assume_relays_are_reachable:
            return random.choice(list(relay_asns))
        else:
            # Check what relay ASes are available to this AS
            accessible_relays = list()
            for asn in relay_asns:
                prefix = relay_prefix_dict[asn]
                if (
                    prefix in self._local_rib._info
                    and asn in self._local_rib._info[prefix].as_path
                ):
                    accessible_relays.append(asn)
            # Uniformly at random select from available relays
            return (
                random.choice(accessible_relays) if len(accessible_relays) > 0 else None
            )
