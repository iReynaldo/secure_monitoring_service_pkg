from lib_rovpp import ROVPPV1SimpleAS, ROVPPV1LiteSimpleAS

from .trusted_server import TrustedServer


class ROVSMS(ROVPPV1LiteSimpleAS):

    name="ROV V4"

    __slots__ = tuple()

    trusted_server = TrustedServer(0)

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

    # TODO: You need to make a modified version of the method below
    # So that you can apply holes for subprefixes that were not received
    # The reason why you don't see blackholes for /24 is because the
    # the ASes that fall from a hidden hijack don't receive the /24.
    # So the only criteria for making blackhole comes from rec_blackhole
    # from the trusted server
    def _get_ann_to_holes_dict_from_trusted_server(self, engine_input):
        """Adds blackholes based on recommendations"""
        # Get holes from V1
        holes = super(ROVSMS, self)._get_ann_to_holes_dict(engine_input)

        print("Entered _get_ann_to_holes_dict_from_trusted_server")
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
                            print(f"Found subprefix in RIB of {self.asn}")
                            does_not_have_subprefix = False

                    if does_not_have_subprefix:
                        # We need to create our own subprefix ann
                        # Since we may not have actually received the hijack
                        # Since this policy is for hidden hijacks
                        subprefix_ann = ann.copy(
                            prefix=subprefix,
                            roa_valid_length=False,
                            roa_origin=engine_input.victim_asn)
                        ann_holes.append(subprefix_ann)
                        holes[subprefix_ann] = holes.get(subprefix_ann, tuple()) + tuple()
            holes[ann] = tuple(ann_holes)
            print(f"ASN {self.asn} Evaluated Holes: {holes}")
            return holes


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


    def _force_add_blackholes(self, holes, from_rel):
        """Manipulates local RIB by adding blackholes and dropping invalid"""

        blackholes_to_add = []
        # For each ann in local RIB:
        for _, ann in self._local_rib.prefix_anns():
            # For each hole in ann: (holes are invalid subprefixes)
            ann.holes = holes[ann]
            print(f"Value of ann.holes in ASN {self.asn}: {ann.holes}")
            for unprocessed_hole_ann in ann.holes:
                blackhole = self._copy_and_process(unprocessed_hole_ann,
                                                   from_rel,
                                                   holes=holes,
                                                   blackhole=True,
                                                   traceback_end=True)

                blackholes_to_add.append(blackhole)
        # Do this here to avoid changing dict size
        for blackhole in blackholes_to_add:
            print(f"Adding blackhole to ASN {self.asn}: {blackhole}")
            # Add the blackhole
            self._local_rib.add_ann(blackhole)
            # Do nothing - ann should already be a blackhole
            assert ((ann.blackhole and ann.invalid_by_roa)
                    or not ann.invalid_by_roa)



class ROVSMSK1(ROVSMS):
    name = "ROV V4 K1"

    __slots__ = tuple()

    trusted_server = TrustedServer(1)

    def __init__(self, *args, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)


class ROVSMSK2(ROVSMS):
    name = "ROV V4 K2"

    __slots__ = tuple()

    trusted_server = TrustedServer(2)

    def __init__(self, *args, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)


class ROVSMSK3(ROVSMS):
    name = "ROV V4 K3"

    __slots__ = tuple()

    trusted_server = TrustedServer(3)

    def __init__(self, *args, **kwargs):
        super(ROVSMS, self).__init__(*args, **kwargs)