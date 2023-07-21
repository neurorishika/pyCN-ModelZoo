# pyCN-modelzoo

<!-- badges: start -->
<!-- badges: end -->

Author: [Rishika Mohanta](https://neurorishika.github.io/)

Latest Build Date: 2023-07-21 23:25:38

## About the Project

Project description is being updated. Please check back later.

## Instructions

This is a [Poetry](https://python-poetry.org/)-enabled python project. Poetry installs a virtual environment in the project directory and all packages are installed in this virtual environment. This means that you do not need to install any packages in your system. The virtual environment is automatically activated when you run the project through Poetry. 

If you use [VS Code](https://code.visualstudio.com/), you can set the Python interpreter to the Poetry virtual environment `.venv` in the project directory for script execution and debugging and use the Poetry virtual environment `.venv` for the Jupyter kernel.

First, you need to setup a git alias for tree generation by running the following command on the terminal:

```
git config --global alias.tree '! git ls-tree --full-name --name-only -t -r HEAD | sed -e "s/[^-][^\/]*\//   |/g" -e "s/|\([^ ]\)/|-- \1/"'
```

To run the project, make sure you have Poetry installed and run the following commands in the project directory:

```
poetry run python utils/update.py
poetry run python utils/build.py
```

To run the Jupyter notebook, run the following command in the project directory:

```
poetry run jupyter notebook
```

## Project Organization

The project is organized as follows:
```
.DS_Store
.gitignore
LICENSE
README.md
poetry.lock
poetry.toml
projects
   |-- DimensionalArtists
   |   |-- README.md
   |   |-- playground.ipynb
   |-- EvoMegaLearners
   |   |-- README.md
   |   |-- scratch.ipynb
   |-- FlyMBLearner
   |   |-- Analyse.ipynb
   |   |-- MBL.ipynb
   |-- HD-Models
   |   |-- 2-4-ringattractor.ipynb
   |   |-- Chang2023-network.ipynb
   |   |-- classical-ringattractor.ipynb
   |   |-- world_generator.ipynb
   |-- LearnableMetaplasticity
   |   |-- README.md
   |   |-- hopfield.ipynb
   |   |-- learningrule_pytorch.ipynb
   |   |-- networks.py
   |-- PiPulse
   |   |-- .gitignore
   |   |-- README.md
   |   |-- code
   |   |   |-- interactive
   |   |   |   |-- Hyperparameter Search.ipynb
   |   |   |   |-- Mirollo Strogatz.ipynb
   |   |   |   |-- clean_attempt.ipynb
   |   |   |   |-- make_sudoku_graph.ipynb
   |   |   |   |-- matlab.mat
   |   |   |   |-- spacelol.npy
   |   |   |   |-- sudoku.npy
   |   |   |   |-- sudoku.py
   |   |-- git_automate.sh
   |   |-- reference
   |   |   |-- thesis.pdf
   |   |   |-- thesis.ps
   |   |-- results
   |   |   |-- partial_jan10_2019_I_0_01875_E_0_0035.png
   |-- ProbSpikingNetworks
   |   |-- Documentation
   |   |   |-- model.aux
   |   |   |-- model.pdf
   |   |   |-- model.synctex.gz
   |   |   |-- model.tex
   |   |-- Model
   |   |   |-- Probabilistic Model - Test.ipynb
   |   |   |-- Results Changing I_ext.png
   |   |   |-- Results I_ext_0.png
   |   |-- README.md
   |-- olfaction-modelzoo
   |   |-- CovidORN-Model
   |   |   |-- Odor-mixtures-master.rar
   |   |   |-- Single ORN Response.ipynb
   |   |   |-- journal.pcbi.1004063.g002.png
   |   |-- GaussianOdorPlumes
   |   |   |-- odor_conc.gif
   |   |   |-- odor_plume.gif
   |   |   |-- odor_sim_scratch.ipynb
   |   |-- LocustKC-MapModel
   |   |   |-- Map Model.ipynb
   |   |   |-- spikes.npy
   |   |-- Minimal-Pompy
   |   |   |-- minpompy
   |   |   |   |-- __init__.py
   |   |   |   |-- models.py
   |   |   |   |-- processors.py
   |   |   |-- odor_plume.gif
   |   |   |-- plume.gif
   |   |   |-- plume.mp4
   |   |   |-- pompy_notebook.ipynb
   |   |-- ORN-KineticModel
   |   |   |-- ORN Model.ipynb
   |   |-- README.md
pycnmodelzoo
   |-- __init__.py
   |-- rdp_client.py
pyproject.toml
utils
   |-- build.py
   |-- quickstart.py
   |-- update.py
```
