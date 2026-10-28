# Research Data Checker

This repository accompanies the **Software Engineering in the AI Era**
day course developed by Oxford Research Software Engineering.

The Research Data Checker is a small Python application that identifies
potential data-quality problems in CSV files and reports them without
modifying the original data.

By default, measurements are checked against the inclusive range 0.0 to
100.0. Override either limit with `--min` and `--max`:

```shell
python -m research_check data.csv --min 10 --max 75
```

The equivalent descriptive options `--min-measurement` and
`--max-measurement` are also available.
