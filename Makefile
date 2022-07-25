setup:
    python3 -m venv ~/.myrepo

install:
    pip install --upgrade pip &&\
        pip install -r requirements.txt

test:
    python -m pytest -vv --cov=myrepolib tests/*.py
    python -m pytest --nbval notebook.ipynb


lint:
    pylint --disable=R,C myrepolib cli web

all: install lint test

#Run make install to install commands
#Run make lint to run pylint
#Run make all to verify output
#pip packages => pip install pylint, pytest, black, ipython
