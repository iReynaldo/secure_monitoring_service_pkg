#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains AS_Rank_V2 which parses AS Rank data using the Restful API
In contrast to the previous parser this also gets organization, rank,
and links to other ASNs

NOTE: This is a modified copy of the version found at the following link,
so that it can run stand-alone.
https://github.com/jfuruness/lib_bgp_data/blob/master/lib_bgp_data/collectors/as_rank_v2/as_rank_v2_parser.py
"""


__author__ = "Nicholas Shpetner"
__credits__ = [
    "Nicholas Shpetner",
    "Abhinna Adhikari",
    "Justin Furuness",
    "Reynaldo Morillo",
]
__Lisence__ = "BSD"
__maintainer__ = "Justin Furuness"
__email__ = "jfuruness@gmail.com"
__status__ = "Production"

import csv
import os
import json
import urllib.request


# TODO: Add progress indications
# TODO: Consider using the new API instead of scraping


class AS_Rank_Parser_V2:
    """Parses the AS rank data from https://asrank.caida.org/"""

    def __init__(self):
        self.csv_dir = "./"

    url_base = "https://api.asrank.caida.org/v2/restful/"
    header_base = {"accept": "application/json"}

    def _run(self, first_rank=None, last_rank=None):
        """Parses the AS rank data from https://asrank.caida.org/"""

        if first_rank is not None and last_rank is not None:
            assert last_rank > first_rank

        next_page = True
        # Defaults
        first = 10000
        offset = 0
        count = 1
        final_count = 0

        if first_rank is not None:
            offset = first_rank
            count = first_rank

        if last_rank is not None:
            if (last_rank - first_rank) < 10000:
                first = last_rank - first_rank

        rows = []

        while next_page:
            url = self.url_base + f"asns/?first={first}&offset={offset}"
            req = urllib.request.Request(url, None, self.header_base)
            with urllib.request.urlopen(req) as response:
                page = response.read()
                data = json.loads(page.decode("utf-8"))
                asns = data["data"]["asns"]
                for asn in asns["edges"]:
                    node = asn["node"]
                    asn = int(node["asn"])
                    rank = int(node["rank"])
                    links = self._get_links(asn)
                    rows.append([rank, asn, node["asnName"], links])
                    count += 1

                if asns["pageInfo"]["hasNextPage"] is False:
                    next_page = False
                    final_count = asns["totalCount"]
                if last_rank is not None:
                    if count >= last_rank:
                        next_page = False
                        final_count = asns["totalCount"]
                    elif (first + count) >= last_rank:
                        first = last_rank - count + 1
                offset = count

        with open("as_rank_v2.csv", "w") as csvfile:
            writer = csv.writer(csvfile, delimiter="\t")
            header = ["rank", "asn", "asnName", "links"]
            writer.writerow(header)
            writer.writerows(rows)

        return final_count

    def _get_links(self, asn):
        offset = 0
        first = 1000
        next_page = True

        # Can't use a python array due to psql not accepting it easy
        rows = "{"

        while next_page:
            url = self.url_base + f"asnLinks/{asn}?first={first}&offset={offset}"
            req = urllib.request.Request(url, None, self.header_base)
            with urllib.request.urlopen(req) as response:
                page = response.read()
                data = json.loads(page.decode("utf-8"))
                asn_links = data["data"]["asnLinks"]
                if asn_links["edges"] == []:
                    return "{}"
                for link in asn_links["edges"]:
                    rows += link["node"]["asn1"]["asn"] + ","
                if asn_links["pageInfo"]["hasNextPage"] is False:
                    rows = rows[:-1] + "}"
                    return rows
                else:
                    offset = offset + 1000


if __name__ == "__main__":
    parser = AS_Rank_Parser_V2()
    parser._run()
