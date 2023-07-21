# pyCN-modelzoo

<!-- badges: start -->
<!-- badges: end -->

Author: [Rishika Mohanta](https://neurorishika.github.io/)
Latest Build Date: 2023-07-21 22:42:02

## About the Project

Project description is being updated. Please check back later.

## READ CAREFULLY

This is a [Poetry](https://python-poetry.org/)-enabled python project. Poetry installs a virtual environment in the project directory and all packages are installed in this virtual environment. This means that you do not need to install any packages in your system. The virtual environment is automatically activated when you run the project through Poetry. 

If you use [VS Code](https://code.visualstudio.com/), you can set the Python interpreter to the Poetry virtual environment `.venv` in the project directory for script execution and debugging and use the Poetry virtual environment `.venv` for the Jupyter kernel.

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
analysis
   |-- .gitkeep
poetry.lock
poetry.toml
processed_data
   |-- .gitkeep
pyproject.toml
rpytemplate
   |-- __init__.py
   |-- rdp_client.py
scripts
   |-- .gitkeep
tests
   |-- __init__.py
utils
   |-- build.py
   |-- quickstart.py
   |-- update.py
```
