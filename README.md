# Introduction to Reinforcement Learning

This repository contains introductory reinforcement-learning notebooks using
[Gymnasium](https://gymnasium.farama.org/) and [PyTorch](https://pytorch.org/). In these examples, we will use Gymnasium 1.3.0; this version is important for the notebooks to work properly. Below are some instructions that may help you set up a Python environment and install the packages.

## Create the environment manually

Install [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/) or
another Conda distribution. The main packages used for this repository match
the following versions from the environment:

- Python 3.13
- Gymnasium 1.3.0
- Torch 2.12
- Stable-balines3 2.9.0 (optional) 

Open a terminal in this repository and create an environment with these
versions:

```bash
conda create -n gym python=3.13 pip
conda activate gym
python -m pip install gymnasium==1.3.0 stable-baselines3==2.9.0 ipykernel
```

Register the environment as a Jupyter kernel:

```bash
python -m ipykernel install --user --name gym --display-name "Python (gym)"
```

Open a notebook in Jupyter or your preferred notebook editor and select
**Python (gym)** as its kernel. A Jupyter frontend may be installed or launched
from a separate environment; the registered kernel will still execute the
notebooks with the packages from `gym`.

## Alternatively, use the environment file

The manual method above installs the key dependencies. To reproduce
the fuller pinned environment, create it from `environment.yml` instead:

```bash
conda env create -f environment.yml
conda activate gym
```

Then register the Jupyter kernel using the command shown above.

## Update an existing environment

After `environment.yml` changes, synchronize an existing environment with:

```bash
conda env update -f environment.yml --prune
conda activate gym
```

<!--
## Atari environments

The environment includes the ALE Python package for Atari support, but Atari
game ROMs must be supplied separately in accordance with their licences. The
notebooks currently included in this repository do not require Atari or ROMs.
-->

## Installation on Windows

I have not tested the installation on Windows, but this video might help if you run into any trouble https://www.youtube.com/watch?v=gMgj4pSHLww
