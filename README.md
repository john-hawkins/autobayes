![AutoBayes Logo](images/AutoBayes.png)
 autobayes  
=====================================================

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![build](https://github.com/john-hawkins/autobayes/workflows/build/badge.svg)

```
Status - In Development
```

This is an application to automate the building of Bayesian forecasting models.

It will accept a CSV, TSV or XLS file and produce a directory of results
in which there will be both results on an automatically generated test dataset and a set 
of forecasts beyond the final data point. It will also produce an analysis of the effect of all
predictor variables. 

Released and distributed via setuptools/PyPI/pip for Python 3.
 

## Notes

Implementation is focused entirely on time series datasets.


## Usage

You can use this application multiple ways

### Use the runner

```
./autobayes-runner.py example/dataset.csv datetime_col target_col example/results/
```

Which was used to generate the [test results](example/results/README.md)

### Invoke the directory as a package:

You can run the same example as above like follows:

```
python -m autobayes example/dataset.csv datetime_col target_col example/results/ 
```

### Install the package 

You can simply install the package and use the command line application directly

#### Installation

Installation from the source tree:

```
python setup.py install
```

(or via pip from PyPI):

```
pip install autobayes
```

Now, the ``autobayes`` command is available::

```
autobayes example/dataset.csv datetime_col target_col example/results/
```


