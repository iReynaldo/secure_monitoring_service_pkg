from lib_rovpp import ROVPPV1SimpleAS, ROVPPV1LiteSimpleAS

from .trusted_server import TrustedServer
from lib_secure_monitoring_service.sim_logger import sim_logger as logger
from lib_secure_monitoring_service.report import Report

class ROVSMS(ROVPPV1LiteSimpleAS):

    name="ROV V4"

    __slots__ = tuple()
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


    def _force_add_blackholes_from_avoid_list(self, engine_input):
        holes = []

        logger.debug("Entered _force_add_blackholes_from_avoid_list")
        for _, ann in self._local_rib.prefix_anns():
            ann_holes = []
            # For each hole in ann: (holes are invalid subprefixes)
            for subprefix in engine_input.prefix_subprefix_dict[ann.prefix]:
                if self.trusted_server.rec_blackhole(subprefix,
                                                     ann.as_path):
                    does_not_have_subprefix = True
                    # Check if AS already has blackhole
                    for _, rib_entry in self._local_rib.prefix_anns():
                        if rib_entry.prefix == subprefix:
                            logger.debug(f"Found subprefix in RIB of {self.asn}")
                            does_not_have_subprefix = False
                            assert(rib_entry.blackhole == True, "The found subprefix does not have blackhole set to true")
                            assert(rib_entry.traceback_end == True, "The found subprefix does not have traceback_end set to true")

                    if does_not_have_subprefix:
                        # We need to create our own subprefix ann
                        # Since we may not have actually received the hijack
                        # Since this policy is for hidden hijacks
                        blackhole_ann = ann.copy(
                            prefix=subprefix,
                            roa_valid_length=False,
                            roa_origin=engine_input.victim_asn,
                            blackhole=True,
                            traceback_end=True)
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