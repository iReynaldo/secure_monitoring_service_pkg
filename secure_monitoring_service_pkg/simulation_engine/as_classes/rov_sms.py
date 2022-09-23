from rovpp_pkg import ROVPPV1LiteSimpleAS

from secure_monitoring_service_pkg.simulation_engine.trusted_server import TrustedServer
from secure_monitoring_service_pkg.simulation_framework.sim_logger import sim_logger as logger
from secure_monitoring_service_pkg.simulation_engine.report import Report


class ROVSMS(ROVPPV1LiteSimpleAS):
    name = "ROV V4"

    _max_num_dishonest_nodes = 0
    trusted_server = TrustedServer(0)

    def __init__(self, *args, reset_trusted_server=True, **kwargs):
        """When everything is being reset, reset the trust server also"""
        # logger.debug("Created ROVSMS {0}".format(kwargs['asn']))
        # At the end of the graphing, everything should be reset
        if reset_trusted_server:
            self.trusted_server.__init__()
        super(ROVSMS, self).__init__(*args, **kwargs)

    def receive_ann(self, ann, *args, **kwargs):
        """Recieves ann and reports it"""
        logger.debug(f"ASN {self.asn} inside receive_ann")
        if ann.invalid_by_roa:
            logger.debug(f"ASN {self.asn} sending report about {ann.prefix}")
            if self._max_num_dishonest_nodes > 0:
                adjusted_as_path = (self.asn,) + ann.as_path
                report = Report(reporting_asn=self.asn, prefix=ann.prefix, as_path=adjusted_as_path)
            else:
                report = Report(reporting_asn=self.asn, prefix=ann.prefix, as_path=ann.as_path)
            self.trusted_server.recieve_report(report)
        return super(ROVSMS, self).receive_ann(ann, *args, **kwargs)

    # TODO: Fix this use of the engine_input. Possibly needs something else
    def _force_add_blackholes_from_avoid_list(self, ordered_prefix_subprefix_dict):
        holes = []

        logger.debug("Entered _force_add_blackholes_from_avoid_list")
        for _, ann in self._local_rib.prefix_anns():
            ann_holes = []
            # For each hole in ann: (holes are invalid subprefixes)
            for subprefix in ordered_prefix_subprefix_dict[ann.prefix]:
                if self.trusted_server.rec_blackhole(subprefix,
                                                     ann.as_path):
                    does_not_have_subprefix = True
                    # Check if AS already has blackhole
                    for _, rib_entry in self._local_rib.prefix_anns():
                        if rib_entry.prefix == subprefix:
                            logger.debug(f"Found subprefix in RIB of {self.asn}")
                            does_not_have_subprefix = False
                            assert rib_entry.blackhole == True, "The found subprefix does not have blackhole set to true"
                            assert rib_entry.traceback_end == True, "The found subprefix does not have traceback_end set to true"

                    if does_not_have_subprefix:
                        # We need to create our own subprefix ann
                        # Since we may not have actually received the hijack
                        # Since this policy is for hidden hijacks
                        blackhole_ann = ann.copy()
                        blackhole_ann.prefix = subprefix
                        blackhole_ann.roa_valid_length = False
                        blackhole_ann.blackhole = True
                        blackhole_ann.traceback_end = True
                        holes.append(blackhole_ann)

        for hole in holes:
            # Add blackhole ann to localRIB
            self._local_rib.add_ann(hole)


class ROVSMSK1(ROVSMS):
    name = "ROV V4 K1"

    __slots__ = tuple()

    _max_num_dishonest_nodes = 1
    trusted_server = TrustedServer(max_num_dishonest_nodes=1)

    def __init__(self, *args, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)


class ROVSMSK2(ROVSMS):
    name = "ROV V4 K2"

    __slots__ = tuple()

    _max_num_dishonest_nodes = 2
    trusted_server = TrustedServer(max_num_dishonest_nodes=2)

    def __init__(self, *args, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)


class ROVSMSK3(ROVSMS):
    name = "ROV V4 K3"

    __slots__ = tuple()

    _max_num_dishonest_nodes = 3
    trusted_server = TrustedServer(max_num_dishonest_nodes=3)

    def __init__(self, *args, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)


class ROVSMSK4(ROVSMS):
    name = "ROV V4 K4"

    __slots__ = tuple()

    _max_num_dishonest_nodes = 4
    trusted_server = TrustedServer(max_num_dishonest_nodes=4)

    def __init__(self, *args, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)


class ROVSMSK5(ROVSMS):
    name = "ROV V4 K5"

    __slots__ = tuple()

    _max_num_dishonest_nodes = 5
    trusted_server = TrustedServer(max_num_dishonest_nodes=5)

    def __init__(self, *args, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)


class ROVSMSK6(ROVSMS):
    name = "ROV V4 K6"

    __slots__ = tuple()

    _max_num_dishonest_nodes = 6
    trusted_server = TrustedServer(max_num_dishonest_nodes=6)

    def __init__(self, *args, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)


class ROVSMSK7(ROVSMS):
    name = "ROV V4 K7"

    __slots__ = tuple()

    _max_num_dishonest_nodes = 7
    trusted_server = TrustedServer(max_num_dishonest_nodes=7)

    def __init__(self, *args, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)


class ROVSMSK10(ROVSMS):
    name = "ROV V4 K10"

    __slots__ = tuple()

    _max_num_dishonest_nodes = 10
    trusted_server = TrustedServer(max_num_dishonest_nodes=10)

    def __init__(self, *args, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)


class ROVSMSK20(ROVSMS):
    name = "ROV V4 K20"

    __slots__ = tuple()

    _max_num_dishonest_nodes = 20
    trusted_server = TrustedServer(max_num_dishonest_nodes=20)

    def __init__(self, *args, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)


class ROVSMSK30(ROVSMS):
    name = "ROV V4 K30"

    __slots__ = tuple()

    _max_num_dishonest_nodes = 30
    trusted_server = TrustedServer(max_num_dishonest_nodes=30)

    def __init__(self, *args, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)


class ROVSMSK50(ROVSMS):
    name = "ROV V4 K50"

    __slots__ = tuple()

    _max_num_dishonest_nodes = 50
    trusted_server = TrustedServer(max_num_dishonest_nodes=50)

    def __init__(self, *args, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)


class ROVSMSK70(ROVSMS):
    name = "ROV V4 K70"

    __slots__ = tuple()

    _max_num_dishonest_nodes = 70
    trusted_server = TrustedServer(max_num_dishonest_nodes=70)

    def __init__(self, *args, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)


class ROVSMSK100(ROVSMS):
    name = "ROV V4 K100"

    __slots__ = tuple()

    _max_num_dishonest_nodes = 100
    trusted_server = TrustedServer(max_num_dishonest_nodes=100)

    def __init__(self, *args, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)


class ROVSMSK150(ROVSMS):
    name = "ROV V4 K150"

    __slots__ = tuple()

    _max_num_dishonest_nodes = 150
    trusted_server = TrustedServer(max_num_dishonest_nodes=150)

    def __init__(self, *args, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)


class ROVSMSK200(ROVSMS):
    name = "ROV V4 K200"

    __slots__ = tuple()

    _max_num_dishonest_nodes = 200
    trusted_server = TrustedServer(max_num_dishonest_nodes=200)

    def __init__(self, *args, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)


class ROVSMSK300(ROVSMS):
    name = "ROV V4 K300"

    __slots__ = tuple()

    _max_num_dishonest_nodes = 300
    trusted_server = TrustedServer(max_num_dishonest_nodes=300)

    def __init__(self, *args, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)


class ROVSMSK500(ROVSMS):
    name = "ROV V4 K500"

    __slots__ = tuple()

    _max_num_dishonest_nodes = 500
    trusted_server = TrustedServer(max_num_dishonest_nodes=500)

    def __init__(self, *args, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)


class ROVSMSK1000(ROVSMS):
    name = "ROV V4 K1000"

    __slots__ = tuple()

    _max_num_dishonest_nodes = 1000
    trusted_server = TrustedServer(max_num_dishonest_nodes=1000)

    def __init__(self, *args, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)


class ROVSMSK2000(ROVSMS):
    name = "ROV V4 K2000"

    __slots__ = tuple()

    _max_num_dishonest_nodes = 2000
    trusted_server = TrustedServer(max_num_dishonest_nodes=2000)

    def __init__(self, *args, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)


class ROVSMSK5000(ROVSMS):
    name = "ROV V4 K5000"

    __slots__ = tuple()

    _max_num_dishonest_nodes = 5000
    trusted_server = TrustedServer(max_num_dishonest_nodes=5000)

    def __init__(self, *args, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)


class ROVSMSK20000(ROVSMS):
    name = "ROV V4 K20000"

    __slots__ = tuple()

    _max_num_dishonest_nodes = 20000
    trusted_server = TrustedServer(max_num_dishonest_nodes=20000)

    def __init__(self, *args, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)


class ROVSMSK30000(ROVSMS):
    name = "ROV V4 K30000"

    __slots__ = tuple()

    _max_num_dishonest_nodes = 30000
    trusted_server = TrustedServer(max_num_dishonest_nodes=30000)

    def __init__(self, *args, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)
