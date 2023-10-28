paths = [f"/home/cam/notebooks/tmp21/ezgraphs{i}/results.json" for i in range(60)]
json_data = []
for path in paths:
    with open(path, "r") as json_file:
        json_data.append(json.load(json_file))

result = PolicyResult("overhead_all", "0", "BGP", "OverheadBGPsecAS", json_data)
result2 = PolicyResult(
    "overhead_all", "0", "BGP", "OverheadBGPsecTransitiveDownOnlyAS", json_data
)

lines = []
lines.append(Line("BGPsec, No Attack", False, result.non_adopting["overhead_all"]))
lines.append(Line("BGP-iSec, No Attack", False, result2.non_adopting["overhead_all"]))

generate_plot(
    lines,
    ylim=15,
    outcome_text="Average Signatures Verified",
    size_inches=(5, 4),
    legend_kwargs={"loc": "upper left", "prop": {"size": 11}},
    fname="/mnt/c/Users/cam/Pictures/overhead_graph.pgf",
)
