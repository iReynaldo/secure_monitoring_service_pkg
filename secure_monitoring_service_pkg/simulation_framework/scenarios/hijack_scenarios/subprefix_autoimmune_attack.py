from typing import Tuple, Set, Dict, Optional, Type

from caida_collector_pkg import AS

from bgp_simulator_pkg import Announcement
from bgp_simulator_pkg import Prefixes
from bgp_simulator_pkg import Relationships
from bgp_simulator_pkg import Timestamps
from bgp_simulator_pkg import Outcomes

from ..v4_scenario import V4Scenario
from ....simulation_engine.report import Report

from secure_monitoring_service_pkg.simulation_framework.sim_logger \
    import sim_logger as logger
from ....simulation_engine import ROVSMS

class SubprefixAutoImmuneScenario(V4Scenario):

    __slots__ = ()

    def __init__(self, *args, fightback=False, relay_asns=None, indirect=True, **kwargs):
        super(SubprefixAutoImmuneScenario, self).__init__(*args, relay_asns=relay_asns, **kwargs)
        self.subprefixes = dict()
        self.providers = dict()
        self.name: str = "SubprefixAutoImmuneScenario"
        self.indirect = indirect  # If the autoimmune attack is indirect(True)/direct(False)
        self.fightback = fightback

    def _get_announcements(self, *args, **kwargs) -> Tuple["Announcement", ...]:
        """Returns victim, attacker, and relay anns for autoimmune attack

        """

        anns = list()
        # Setup Victim Announcements
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

        # Setup Attacker Announcements
        roa_origin: int = next(iter(self.victim_asns))
        engine = kwargs["engine"]
        victim_providers = engine.as_dict[next(iter(self.victim_asns))].providers
        for i, provider in enumerate(victim_providers):
            subprefix = f"1.2.{i+1}.0/24"
            self.subprefixes[provider.asn] = subprefix
            self.providers[subprefix] = provider.asn
            for attacker_asn in self.attacker_asns:
                if self.indirect:
                    anns.append(self.AnnCls(prefix=subprefix,
                                            as_path=(attacker_asn, provider.asn),
                                            timestamp=Timestamps.ATTACKER.value,
                                            seed_asn=attacker_asn,
                                            roa_valid_length=False,
                                            roa_origin=roa_origin,
                                            recv_relationship=Relationships.ORIGIN))
                else:
                    if issubclass(self.AdoptASCls, ROVSMS):
                        trusted_server_ref = self.AdoptASCls.trusted_server
                        # Instead of sending announcements, submit malicious reports directly
                        report = Report(reporting_asn=attacker_asn, prefix=subprefix, as_path=(attacker_asn, provider.asn))
                        trusted_server_ref.receive_report(report)

        if self.fightback:
            anns.extend(self.generate_fightback_relay_announcements())

        # If we assume relays are not reachable, then create their announcements
        if not self.assume_relays_are_reachable:
            # Setup Relay Announcements
            anns.extend(self.generate_relay_announcements())

        return tuple(anns)

    def get_attacker_announcements(self):
        if self.indirect:
            return super().get_attacker_announcements()
        else:
            attacker_announcements = set()
            some_attacker_asn = next(iter(self.attacker_asns))
            for subprefix in self.subprefixes.values():
                attacker_announcements.add(self.AnnCls(prefix=subprefix,
                                                       as_path=(some_attacker_asn,),
                                                       timestamp=Timestamps.ATTACKER.value,
                                                       seed_asn=some_attacker_asn,
                                                       roa_valid_length=False,
                                                       roa_origin=next(iter(self.victim_asns)),
                                                       recv_relationship=Relationships.ORIGIN))
            return attacker_announcements

    def generate_fightback_relay_announcements(self):
        anns = list()
        # Setup Relay Announcements
        if self.relay_asns:
            for i, relay_asn in enumerate(self.relay_asns):
                relay_prefix = Prefixes.SUBPREFIX.value
                self.relay_prefixes[relay_asn] = relay_prefix
                anns.append(self.AnnCls(prefix=relay_prefix,
                                        as_path=(relay_asn,),
                                        timestamp=2,
                                        seed_asn=relay_asn,
                                        roa_valid_length=True,
                                        roa_origin=relay_asn,
                                        recv_relationship=Relationships.ORIGIN))
        return anns

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
