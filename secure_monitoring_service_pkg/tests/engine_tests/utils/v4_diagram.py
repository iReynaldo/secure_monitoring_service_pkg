from bgp_simulator_pkg import Diagram

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
        # https://stackoverflow.com/a/57461245/8903959
        self.dot.attr(label=description)
        self._render(path=path, view=view)

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

        # avoid_list_tbl_html = f'''<
        #     <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
        #       <TR>
        #       <TD COLSPAN="2" BORDER="0">(Avoid List)</TD>
        #       </TR>
        #       <TR>
        #           <TD BGCOLOR="#ff6060:white"> Some Prefix </TD>
        #           <TD>bla bla bla</TD>
        #       </TR>
        #     </TABLE>>
        # '''
        avoid_list_tbl_html = f'''<
          <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
              <TR>
                  <TD COLSPAN="2" BORDER="0">Avoid List</TD>
              </TR>
              {rows}
            </TABLE>
        >'''

        # avoid_list_tbl_html = f'''<
        # <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
        #   <TR>
        #   <TD COLSPAN="2" BORDER="0">(Avoid List)</TD>
        #   </TR>
        #   {rows}
        # </TABLE>>
        # '''

        kwargs = {"color": "black", "style": "filled", "fillcolor": "white"}
        self.dot.node("Avoid List", avoid_list_tbl_html, shape="plaintext", **kwargs)