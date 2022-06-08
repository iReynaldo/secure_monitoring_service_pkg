README
=================

`convert_reports_to_tsv.sh` is the main script in this directory and the input file is `k0_10_trials_reports.py`.

```
./convert_reports_to_tsv.sh k0_10_trials_reports.py
```

`k0_10_trials_reports.py` will be split into many python modules that are used in `create_avoid_list_tsv.py` to convert them into a tsv along with some additional processing.

**Note**: Script is not flexible enough at this point to automatically to know all the different modules that get created when creating the TSV. So prior to running the convert script the TSV converter needs to number the number of modules as a parameter in the script

The `x*.py` files are the reports collected for different adoption percentages for 10 trials.

Adoption Percentages
[0,5,10,20,40,60,80,100]

Files:
000 - 009: 0%
010 - 019: 5%
020 - 029: 10%
030 - 039: 20%
040 - 049: 40%
050 - 059: 60%
060 - 069: 80%
070 - 079: 100%

Variables in each module (below is an example of this from the x000.py module):

```
percent_adoption= 0
trial= 0
attacker_asn= 41464
victim_asn= 133653
adopting_asns= [136360, 1299, 58332, 133653]
reports_path_list= [[12912, 41464], [33891, 12912, 41464], [3216, 33891, 12912, 41464], [1273, 3216, 33891, 12912, 41464], [7195, 13786, 3216, 33891, 12912, 41464], [174, 12741, 41464], [209, 22284, 3549, 7195, 13786, 3216, 33891, 12912, 41464], [701, 13786, 3216, 33891, 12912, 41464], [2914, 13786, 3216, 33891, 12912, 41464], [3257, 33891, 12912, 41464], [3320, 12912, 41464], [3356, 12741, 41464], [5511, 3216, 33891, 12912, 41464], [6453, 13786, 3216, 33891, 12912, 41464], [6762, 3216, 33891, 12912, 41464], [7018, 13786, 3216, 33891, 12912, 41464], [12956, 13786, 3216, 33891, 12912, 41464], [9498, 3356, 12741, 41464], [3255, 33891, 12912, 41464], [9430, 9498, 3356, 12741, 41464], [59165, 132215, 9583, 33891, 12912, 41464]]
num_reports= 21
```
