import os


def format():
    os.system("autopep8 --in-place --aggressive --aggressive --recursive .")


def lint():
    flake8 = "flake8 ."
    isort = "&& isort ."
    autopep8 = "&& autopep8 --in-place --aggressive --aggressive --recursive ."
    os.system(f"{flake8} {isort} {autopep8}")


def test():
    cmd = "pytest --cov=poetry_demo --cov-report html"
    opn = "&& open htmlcov/index.html"
    os.system(f"{cmd} {opn}")
