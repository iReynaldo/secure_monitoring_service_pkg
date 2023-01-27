import ipaddress

from bgp_simulator_pkg import Diagram

from secure_monitoring_service_pkg import SubprefixAutoImmuneScenario

class V4Diagram(Diagram):

    def generate_as_graph(self,
                          engine,
                          scenario,
                          traceback,
                          description,
                          shared_data,
                          path=None,
                          view=False):
        self._add_legend(traceback)
        self._add_ases(engine, traceback, scenario)
        self._add_edges(engine)
        self._add_propagation_ranks(engine)
        self._add_avoid_list_table(shared_data)
        self._add_relay_usage_table(shared_data)
        # https://stackoverflow.com/a/57461245/8903959
        self.dot.attr(label=description)
        self._render(path=path, view=view)


    def _add_relay_usage_table(self, shared_data):
        rows = ''
        relay_usage = shared_data.get("relay_usage", None)
        relay_prefixes = shared_data.get("relay_prefixes", None)
        if not relay_usage:
            return
        if relay_prefixes:
            # If there are no avoid lists, don't print anything
            for asn in relay_usage:
                row = f'''
                    <TR>
                      <TD BGCOLOR="#adadff">{asn}</TD>
                      <TD BGCOLOR="#adadff:white">{shared_data["relay_prefixes"][asn]}</TD>
                      <TD>{relay_usage[asn]}</TD>
                    </TR>
                '''
        else:
            for asn in relay_usage:
                row = f'''
                    <TR>
                      <TD BGCOLOR="#adadff">{asn}</TD>
                      <TD>{relay_usage[asn]}</TD>
                    </TR>
                '''
        rows = rows + row


        relay_usage_tbl_html = f'''<
          <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
              <TR>
                  <TD COLSPAN="3" BORDER="0">Relay Usage</TD>
              </TR>
              {rows}
            </TABLE>
        >'''

        kwargs = {"color": "black", "style": "filled", "fillcolor": "white"}
        self.dot.node("Relay Usage", relay_usage_tbl_html, shape="plaintext", **kwargs)

    def _add_avoid_list_table(self, shared_data):
        rows = ''
        avoid_list_keys = [key for key in shared_data if "avoid_list_" in key]
        # If there are no avoid lists, don't print anything
        if not avoid_list_keys:
            return
        for key in avoid_list_keys:
            prefix = key.split('_')[3]
            avoid_list = shared_data[key]
            row = f'''
                <TR>
                  <TD BGCOLOR="#ff6060:white"> {prefix} </TD>
                  <TD>{avoid_list}</TD>
                </TR>
            '''
            rows = rows + row

        avoid_list_tbl_html = f'''<
          <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
              <TR>
                  <TD COLSPAN="2" BORDER="0">Avoid List</TD>
              </TR>
              {rows}
            </TABLE>
        >'''

        kwargs = {"color": "black", "style": "filled", "fillcolor": "white"}
        self.dot.node("Avoid List", avoid_list_tbl_html, shape="plaintext", **kwargs)

    def _get_html(self, as_obj, engine, scenario):
        asn_str = str(as_obj.asn)
        if isinstance(scenario, SubprefixAutoImmuneScenario):
            if scenario.relay_asns and as_obj.asn in scenario.relay_asns:
                asn_str = "&#9937; " + asn_str + " &#9937;"
        if as_obj.asn in scenario.victim_asns:
            asn_str = "&#128519; " + asn_str + " &#128519;"
        elif as_obj.asn in scenario.attacker_asns:
            asn_str = "&#128520; " + asn_str + " &#128520;"

        html = f"""<
            <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
            <TR>
            <TD COLSPAN="4" BORDER="0">{asn_str}</TD>
            </TR>
            <TR>
            <TD COLSPAN="4" BORDER="0">({as_obj.name})</TD>
            </TR>"""
        local_rib_anns = tuple(list(as_obj._local_rib._info.values()))
        local_rib_anns = tuple(
            sorted(local_rib_anns,
                   key=lambda x: ipaddress.ip_network(x.prefix).num_addresses,
                   reverse=True))
        if len(local_rib_anns) > 0:
            html += """<TR>
                        <TD COLSPAN="4">Local RIB</TD>
                      </TR>"""

            for ann in local_rib_anns:
                mask = str(ann.prefix)
                path = ", ".join(str(x) for x in
                                 ann.as_path)
                ann_help = ""
                if getattr(ann, "blackhole", False):
                    ann_help = "&#10041;"
                elif getattr(ann, "preventive", False):
                    ann_help = "&#128737;"
                elif any(x in ann.as_path for x in scenario.attacker_asns):
                    ann_help = "&#128520;"
                elif any(x == ann.origin for x in scenario.victim_asns):
                    ann_help = "&#128519;"
                elif isinstance(scenario, SubprefixAutoImmuneScenario) and \
                        any(x == ann.origin for x in scenario.relay_asns):
                    ann_help = "&#9937;"
                else:
                    raise Exception("Not valid ann for rib?")

                html += f"""<TR>
                            <TD>{mask}</TD>
                            <TD>{path}</TD>
                            <TD>{ann_help}</TD>
                          </TR>"""
        html += "</TABLE>>"
        return html