# Research Data Checker

This repository accompanies the **Software Engineering in the AI Era**
day course developed by Oxford Research Software Engineering.

The Research Data Checker is a small Python application that identifies
potential data-quality problems in CSV files and reports them without
modifying the original data.

Run it with a CSV file and optionally set inclusive measurement limits:

```shell
python -m research_check observations.csv --minimum 10 --maximum 80
```

The defaults are `0` and `100`; if only one limit is provided, the other
retains its default.
