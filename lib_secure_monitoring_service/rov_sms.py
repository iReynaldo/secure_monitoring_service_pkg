from lib_rovpp import ROVPPV1SimpleAS

from .trusted_server import TrustedServer


class ROVSMS(ROVPPV1SimpleAS):

    name="ROV V4"

    __slots__ = tuple()

    trusted_server = TrustedServer()

    def __init__(self, *args, reset_trusted_server=True, **kwargs):
        """When everything is being reset, reset the trust server also"""
        # print("Created ROVSMS {0}".format(kwargs['asn']))
        # At the end of the graphing, everything should be reset
        if reset_trusted_server:
            self.trusted_server.__init__()
        super(ROVSMS, self).__init__(*args, **kwargs)

    # TODO: Add typing to function (in this case announcement type)
    def receive_ann(self, ann, *args, **kwargs):
        """Recieves ann and reports it"""

        if ann.invalid_by_roa:
            self.trusted_server.recieve_report(ann)
        return super(ROVSMS, self).receive_ann(ann, *args, **kwargs)

    def _get_ann_to_holes_dict(self, engine_input) -> dict:
        """Adds blackholes based on recommendations"""

        # Get holes from V1
        holes = super(ROVSMS, self)._get_ann_to_holes_dict(engine_input)

        # Only blackhole when:
        # You have a rec to blackhole a subprefix with an ASN
        # AND you also have a PREFIX that has that ASN in the PATH
        for _, ann_list in self._recv_q.prefix_anns():
            for ann in ann_list:
                ann_holes = []
                for subprefix in engine_input.prefix_subprefix_dict[ann.prefix]:
                    for sub_ann in self._recv_q.get_ann_list(subprefix):
                        # Holes are only from same neighbor
                        if (sub_ann.invalid_by_roa
                            and sub_ann.as_path[0] == ann.as_path[0]):
                            ann_holes.append(sub_ann)
                    # In real life, this would be push/subscribe method
                    # But this makes implementation much easier
                    if self.trusted_server.rec_blackhole(subprefix,
                                                         ann.as_path):
                        # We need to create our own subprefix ann
                        # Since we may not have actually recieved the hijack
                        # Since this policy is for hidden hijacks
                        subprefix_ann = ann.copy(
                            prefix=subprefix,
                            roa_valid_length=False,
                            roa_origin=engine_input.victim_asn)
                        ann_holes.append(subprefix_ann)
                        holes[subprefix_ann] = holes.get(subprefix_ann, tuple()) + tuple()
                holes[ann] = tuple(ann_holes)
        return holes



class ROVSMSK1(ROVSMS):
    name = "ROV V4 K1"

    __slots__ = tuple()

    trusted_server = TrustedServer(1)

    def __init__(self, *args, reset_trusted_server=True, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)