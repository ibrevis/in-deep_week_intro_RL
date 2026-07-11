# Introduction to Reinforcement Learning

This repository contains introductory reinforcement-learning notebooks using
[Gymnasium](https://gymnasium.farama.org/). The supplied Conda environment
provides the packages used by the notebooks and the wider teaching examples.

## Create the environment

Install [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/) or
another Conda distribution, open a terminal in this repository, and run:

```bash
conda env create -f environment.yml
conda activate gym
```

Register the environment as a Jupyter kernel:

```bash
python -m ipykernel install --user --name gym --display-name "Python (gym)"
```

Open a notebook in Jupyter or your preferred notebook editor and select
**Python (gym)** as its kernel. A Jupyter frontend may be installed or launched
from a separate environment; the registered kernel will still execute the
notebooks with the packages from `gym`.

## Update an existing environment

After `environment.yml` changes, synchronize an existing environment with:

```bash
conda env update -f environment.yml --prune
conda activate gym
```

## Atari environments

The environment includes the ALE Python package for Atari support, but Atari
game ROMs must be supplied separately in accordance with their licences. The
notebooks currently included in this repository do not require Atari or ROMs.
