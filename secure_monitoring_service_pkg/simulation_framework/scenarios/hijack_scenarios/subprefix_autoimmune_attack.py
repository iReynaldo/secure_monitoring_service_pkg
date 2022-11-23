from typing import Tuple

from bgp_simulator_pkg import Announcement
from bgp_simulator_pkg import Prefixes
from bgp_simulator_pkg import Relationships
from bgp_simulator_pkg import Timestamps

from ..v4_scenario import V4Scenario

from secure_monitoring_service_pkg.simulation_framework.sim_logger \
    import sim_logger as logger

class SubprefixAutoImmuneScenario(V4Scenario):

    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super(SubprefixAutoImmuneScenario, self).__init__(*args, **kwargs)
        self.subprefixes = dict()
        self.providers = dict()
        self.name = "SubprefixAutoImmuneScenario"

    def _get_announcements(self, *args, **kwargs) -> Tuple["Announcement", ...]:
        """Returns victim and attacker anns for autoimmune attack

        """

        anns = list()
        for victim_asn in self.victim_asns:
            anns.append(self.AnnCls(prefix=Prefixes.PREFIX.value,
                                    as_path=(victim_asn,),
                                    timestamp=Timestamps.VICTIM.value,
                                    seed_asn=victim_asn,
                                    roa_valid_length=True,
                                    roa_origin=victim_asn,
                                    recv_relationship=Relationships.ORIGIN))

        err: str = "Fix the roa_origins of the " \
                   "announcements for multiple victims"
        assert len(self.victim_asns) == 1, err

        roa_origin: int = next(iter(self.victim_asns))

        engine = kwargs["engine"]
        victim_providers = engine.as_dict[next(iter(self.victim_asns))].providers
        for i, provider in enumerate(victim_providers):
            subprefix = f"1.2.{i}.0/24"
            self.subprefixes[provider.asn] = subprefix
            self.providers[subprefix] = provider.asn
            for attacker_asn in self.attacker_asns:
                anns.append(self.AnnCls(prefix=subprefix,
                                        as_path=(attacker_asn, provider.asn),
                                        timestamp=Timestamps.ATTACKER.value,
                                        seed_asn=attacker_asn,
                                        roa_valid_length=False,
                                        roa_origin=roa_origin,
                                        recv_relationship=Relationships.ORIGIN))

        return tuple(anns)

    def apply_blackholes_from_avoid_list(self, engine):
        logger.debug(f"Inside apply_blackholes_from_avoid_list")
        # Create a flag to check if avoid_list has been created
        avoid_list_created_flag = False
        # Iterate over all adopting ASNs
        # TODO: Does non_default_as_cls_dict also contain ROV ASes when
        #  doing mixed deployment?
        for asn in self.non_default_as_cls_dict:
            # Get reference to AS Object
            as_obj = engine.as_dict[asn]
            # TODO: Remove this check if ROV ASes are not in
            #  non_default_as_cls_dict when doing Mixed Deployment.
            if hasattr(as_obj, "trusted_server"):
                # Create avoid list if it hasn't been created yet
                if not avoid_list_created_flag:
                    self.trusted_server_ref = as_obj.trusted_server
                    # Let Trusted Server know the current scenario information
                    self.trusted_server_ref.scenario_name = self.name
                    self.trusted_server_ref.prefix_provider_mapping = self.providers
                    # Compute the avoid list
                    as_obj.trusted_server.create_recs()
                    self.avoid_lists = self.trusted_server_ref._recommendations
                    avoid_list_created_flag = True
                    self.has_rovsms_ases = True

                as_obj._force_add_blackholes_from_avoid_list(self.ordered_prefix_subprefix_dict)
