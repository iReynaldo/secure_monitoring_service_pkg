import random
import ipaddress

from rovpp_pkg import ROVPPV1LiteSimpleAS

from secure_monitoring_service_pkg.simulation_engine.trusted_server import TrustedServer
from secure_monitoring_service_pkg.simulation_framework.sim_logger import (
    sim_logger as logger,
)
from secure_monitoring_service_pkg.simulation_engine.report import Report


class ROVSMS(ROVPPV1LiteSimpleAS):
    name = "ROV V4 Lite"

    _max_num_dishonest_nodes = 0
    trusted_server = TrustedServer(0)

    def __init__(self, *args, reset_trusted_server=True, **kwargs):
        """When everything is being reset, reset the trust server also"""
        # logger.debug("Created ROVSMS {0}".format(kwargs['asn']))
        # At the end of the graphing, everything should be reset
        if reset_trusted_server:
            self.trusted_server.__init__()
        super(ROVSMS, self).__init__(*args, **kwargs)
        # The following variable indicates if the AS used a relay
        # and it's updated in the V4Subgraph method _recalculate_outcomes_with_relays
        self.used_relay = False

    def receive_ann(self, ann, *args, **kwargs):
        """Recieves ann and reports it"""
        logger.debug(f"ASN {self.asn} inside receive_ann")
        if ann.invalid_by_roa:
            logger.debug(f"ASN {self.asn} sending report about {ann.prefix}")
            if self._max_num_dishonest_nodes > 0:
                if self.asn not in ann.as_path:
                    adjusted_as_path = (self.asn,) + ann.as_path
                    report = Report(
                        reporting_asn=self.asn,
                        prefix=ann.prefix,
                        as_path=adjusted_as_path,
                    )
                    self.trusted_server.receive_report(report)
            else:
                report = Report(
                    reporting_asn=self.asn, prefix=ann.prefix, as_path=ann.as_path
                )
                self.trusted_server.receive_report(report)
        return super(ROVSMS, self).receive_ann(ann, *args, **kwargs)

    def _force_add_blackholes_from_avoid_list(self, ordered_prefix_subprefix_dict):
        holes = []
        for reported_prefix in self.trusted_server._recommendations:
            reported_prefix_network = ipaddress.ip_network(reported_prefix)
            # If the reported prefix is a prefix hijack, and a valid ann already exists,
            # don't consider blackholing it. Hidden Hijacks don't exist in prefix hijacks.
            reported_prefix_ann = self._local_rib.get_ann(reported_prefix)
            if reported_prefix_ann and reported_prefix_ann.valid_by_roa:
                continue
            for prefix, ann in self._local_rib.prefix_anns():
                ann_prefix_network = ipaddress.ip_network(prefix)
                # Check if ann is
                # - The reported prefix is a subprefix of it
                # - The AS path of has a member on the avoid list
                if reported_prefix_network.subnet_of(
                    ann_prefix_network
                ) and self.trusted_server.rec_blackhole(reported_prefix, ann.as_path):
                    # Create Blackhole
                    # We need to create our own subprefix ann
                    # Since we may not have actually received the hijack
                    # Since this policy is for hidden hijacks
                    if reported_prefix_ann:
                        blackhole_ann = reported_prefix_ann.copy()
                    else:
                        blackhole_ann = ann.copy()
                    blackhole_ann.prefix = reported_prefix
                    blackhole_ann.roa_valid_length = False
                    blackhole_ann.blackhole = True
                    blackhole_ann.traceback_end = True
                    holes.append(blackhole_ann)

        for hole in holes:
            # Add blackhole ann to localRIB
            self._local_rib.add_ann(hole)

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


class ROVSMSK1(ROVSMS):
    name = "ROV V4 Lite K1"
    _max_num_dishonest_nodes = 1
    trusted_server = TrustedServer(max_num_dishonest_nodes=1)


class ROVSMSK2(ROVSMS):
    name = "ROV V4 Lite K2"
    _max_num_dishonest_nodes = 2
    trusted_server = TrustedServer(max_num_dishonest_nodes=2)


class ROVSMSK3(ROVSMS):
    name = "ROV V4 Lite K3"
    _max_num_dishonest_nodes = 3
    trusted_server = TrustedServer(max_num_dishonest_nodes=3)


class ROVSMSK4(ROVSMS):
    name = "ROV V4 Lite K4"
    _max_num_dishonest_nodes = 4
    trusted_server = TrustedServer(max_num_dishonest_nodes=4)


class ROVSMSK5(ROVSMS):
    name = "ROV V4 Lite K5"
    _max_num_dishonest_nodes = 5
    trusted_server = TrustedServer(max_num_dishonest_nodes=5)


class ROVSMSK6(ROVSMS):
    name = "ROV V4 Lite K6"
    _max_num_dishonest_nodes = 6
    trusted_server = TrustedServer(max_num_dishonest_nodes=6)


class ROVSMSK7(ROVSMS):
    name = "ROV V4 Lite K7"
    _max_num_dishonest_nodes = 7
    trusted_server = TrustedServer(max_num_dishonest_nodes=7)


class ROVSMSK10(ROVSMS):
    name = "ROV V4 Lite K10"
    _max_num_dishonest_nodes = 10
    trusted_server = TrustedServer(max_num_dishonest_nodes=10)


class ROVSMSK20(ROVSMS):
    name = "ROV V4 Lite K20"
    _max_num_dishonest_nodes = 20
    trusted_server = TrustedServer(max_num_dishonest_nodes=20)


class ROVSMSK30(ROVSMS):
    name = "ROV V4 Lite K30"
    _max_num_dishonest_nodes = 30
    trusted_server = TrustedServer(max_num_dishonest_nodes=30)


class ROVSMSK50(ROVSMS):
    name = "ROV V4 Lite K50"
    _max_num_dishonest_nodes = 50
    trusted_server = TrustedServer(max_num_dishonest_nodes=50)


class ROVSMSK70(ROVSMS):
    name = "ROV V4 Lite K70"
    _max_num_dishonest_nodes = 70
    trusted_server = TrustedServer(max_num_dishonest_nodes=70)


class ROVSMSK100(ROVSMS):
    name = "ROV V4 Lite K100"
    _max_num_dishonest_nodes = 100
    trusted_server = TrustedServer(max_num_dishonest_nodes=100)


class ROVSMSK150(ROVSMS):
    name = "ROV V4 Lite K150"
    _max_num_dishonest_nodes = 150
    trusted_server = TrustedServer(max_num_dishonest_nodes=150)


class ROVSMSK200(ROVSMS):
    name = "ROV V4 Lite K200"
    _max_num_dishonest_nodes = 200
    trusted_server = TrustedServer(max_num_dishonest_nodes=200)


class ROVSMSK300(ROVSMS):
    name = "ROV V4 Lite K300"
    _max_num_dishonest_nodes = 300
    trusted_server = TrustedServer(max_num_dishonest_nodes=300)


class ROVSMSK500(ROVSMS):
    name = "ROV V4 Lite K500"
    _max_num_dishonest_nodes = 500
    trusted_server = TrustedServer(max_num_dishonest_nodes=500)


class ROVSMSK1000(ROVSMS):
    name = "ROV V4 Lite K1000"
    _max_num_dishonest_nodes = 1000
    trusted_server = TrustedServer(max_num_dishonest_nodes=1000)


class ROVSMSK1500(ROVSMS):
    name = "ROV V4 Lite K1500"
    _max_num_dishonest_nodes = 1500
    trusted_server = TrustedServer(max_num_dishonest_nodes=1500)


class ROVSMSK2000(ROVSMS):
    name = "ROV V4 Lite K2000"
    _max_num_dishonest_nodes = 2000
    trusted_server = TrustedServer(max_num_dishonest_nodes=2000)


class ROVSMSK5000(ROVSMS):
    name = "ROV V4 Lite K5000"
    _max_num_dishonest_nodes = 5000
    trusted_server = TrustedServer(max_num_dishonest_nodes=5000)


class ROVSMSK10000(ROVSMS):
    name = "ROV V4 Lite K10000"
    _max_num_dishonest_nodes = 10000
    trusted_server = TrustedServer(max_num_dishonest_nodes=10000)


class ROVSMSK20000(ROVSMS):
    name = "ROV V4 Lite K20000"
    _max_num_dishonest_nodes = 20000
    trusted_server = TrustedServer(max_num_dishonest_nodes=20000)


class ROVSMSK30000(ROVSMS):
    name = "ROV V4 Lite K30000"
    _max_num_dishonest_nodes = 30000
    trusted_server = TrustedServer(max_num_dishonest_nodes=30000)
