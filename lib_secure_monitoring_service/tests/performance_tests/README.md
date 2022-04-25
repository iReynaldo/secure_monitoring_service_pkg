# Performance Tests

## How to run a performance test

Performance tests are measured using the built-in `cProfile` module.
The use of this module creates a profile file on whatever its run on.

**Example run**
```
# python -m cProfile -o <output_filename>.profile ../../__main__.py
python -m cProfile -o performance_improvement_v4_k0_80_percent_10_trial.profile ../../__main__.py
```

##  How to view performance tests

To view the performance results, one could use `snakeviz` or
other compatible viewers.

**Example**
```
snakeviz performance_improvement_v4_k0_80_percent_10_trial.profile
```

This will open the performance results in a web browser.

