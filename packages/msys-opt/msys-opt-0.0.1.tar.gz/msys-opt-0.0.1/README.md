# MSYS-OPT
> An Extension of MSYS implementing state-of-the-art optimisation techniques 

[![pip](https://img.shields.io/pypi/v/msys-opt.svg)](https://pypi.org/project/msys-opt/)
[![Documentation Status](https://readthedocs.org/projects/msys-opt-docs/badge/?version=latest)](https://msys-opt-docs.readthedocs.io/en/latest/?badge=latest)
[![DOI](https://zenodo.org/badge/363596972.svg)](https://zenodo.org/badge/latestdoi/363596972)
![workflow](https://github.com/willi-z/msys-opt/actions/workflows/ci.yml/badge.svg?branch=main)
[![codecov](https://codecov.io/gh/willi-z/msys-opt/branch/main/graph/badge.svg?token=OOC5YKLOTE)](https://codecov.io/gh/willi-z/msys-opt)

See the [Documentation](https://msys-docs.readthedocs.io/en/latest/) form more information.

## Testing
till `pip 21.3`:
```
pip install --use-feature=in-tree-build -e .
```
`pip 21.3+`:
```
pip install -e .
```

```
coverage run --source=src -m pytest
```

## Capabilities

Legend:

| Symbol | Meaning                              |
| ------ | ------------------------------------ |
| ✅     | finished                             |
| 🔜     | working on implementation            |
| 🟦     | planned                              |


### Core

| Capability                           | Status |
| ------------------------------------ | ------ |
| Types                                | ✅     |
| Inputs and Outputs                   | ✅     |
| Module                               | ✅     |
| Processor                            | ✅     |
| Expression Parser                    | ✅     |
| Optimizer                            | 🔜     |
| API                                  | 🔜     |


### Modules

| Capability                           | Status |
| ------------------------------------ | ------ |
| Plugin system                        | ✅     |
| Math Module                          | ✅     |
| Processor                            | 🔜     |
| HTML Module                          | 🟦     |
| SQL Module                           | 🟦     |

### Types

| Capability                           | Status |
| ------------------------------------ | ------ |
| Vector                               | ✅     |
| File                                 | 🟦     |

### Optimizers

| Capability                           | Status |
| ------------------------------------ | ------ |
| Evolutionary Optimisation            | 🟦     |

### Server

| Capability                           | Status |
| ------------------------------------ | ------ |
| create, save and load                | 🟦     |
| change                               | 🟦     |

### Documentation

| Capability                           | Status |
| ------------------------------------ | ------ |
| Installation                         | 🟦     |
| Configuration                        | 🟦     |
| Core                                 | 🟦     |
| Modules                              | 🟦     |
| Optimisation                         | 🟦     |
| Server and API                       | 🟦     |