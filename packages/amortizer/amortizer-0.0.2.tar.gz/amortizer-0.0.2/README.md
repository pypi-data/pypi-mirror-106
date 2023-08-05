<div align="center">

[![ReadTheDocs](https://readthedocs.org/projects/amortizer/badge/?version=latest)](https://amortizer.readthedocs.io/en/latest/?badge=latest)

</div>

# Amortizer - Simple loan amortization calculator

*Amortizer* is a simple amortization table generator which supports two common approaches: annuity payments and straight amortization. 


## Overview

*Amortizer* is basically a single python class which instantiates an object with several useful methods.

| Method | Description |
| ---- | --- |
| **.get_summary(method="annuity")** | Calculates amortization dataframe (methods: 'straight' or 'annuity') and returns a dictionary with summary statistics. |
| **.straight_amortization()** | Calculates amortization table with straight amortization and returns a dataframe. |
| **.annuity_amortization()** | Calculates amortization table with annuity payments and returns a dataframe. |
| **.to_html(method="annuity")** | Calculates amortization dataframe (methods: 'straight' or 'annuity') and returns results to a string with html markup. |
| **.to_json(method="annuity")** | Calculates amortization dataframe (methods: 'straight' or 'annuity') and returns results to a string with JSON object. |
| **.to_csv(path: str, method="annuity")** | Calculates amortization dataframe (methods: 'straight' or 'annuity') and exports results to the .csv file. |

Learn more about the methods above in the [Documentation][docs]

# Installation 

`Amortizer` supports python3.7 + environments.

```shell
$ pip install --upgrade amortize
```

or use **pipenv**

```shell
$ pipenv install --upgrade amortize
```


# Getting Started

## Minimal Example

```python
from amortizer.generator import Amortizer

# Instantiate new object with any suitable name and pass itinial parameters of the loan / mortgage
amortizer = Amortizer(amount=100000, period=18, interest_rate=6)

# Get summary statistics with annuity payments
amortizer.get_summary(method="annuity")

# => 

# Resources

- [**PyPi**](https://pypi.org/project/amortizer)
- [**Documentation**](https://readthedocs.org/projects/amortizer/)
- [**Issue tracking**](https://github.com/vlnsolo/amortizer/issues)


# Contributing

Feel free to send merge requests.


# If you've got questions

1. [Read the docs][docs].
2. [Look through the issues](https://github.com/vlnsolo/amortizer/issues).


# License

[MIT License](LICENSE).


[docs]: https://amortizer.readthedocs.io/en/latest/amortizer.html