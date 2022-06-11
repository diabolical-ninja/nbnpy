"""Configuration of nox for testing & code validation."""

import tempfile

from nox_poetry import Session, session

PYTHON_VERSIONS = ["3.8", "3.9", "3.10"]


@session(python=PYTHON_VERSIONS)
def lint(session: Session) -> None:
    """Runs linting checks.

    Args:
        session (Session): Nox Session
    """
    session.install(
        "flake8",
        "flake8-docstrings",
        "flake8-import-order",
        "flake8-black",
        "darglint",
        "flake8-annotations",
        "flake8-quotes",
        "flake8-requirements",
        "pep8-naming",
        "flake8-bugbear",
        "flake8-bandit",
    )
    session.run("flake8", "src/")
    session.run("flake8", "tests/")
    session.run("flake8", "docs/conf.py")


@session(python=PYTHON_VERSIONS)
def mypy(session: Session) -> None:
    """Runs static type checking analysis.

    Args:
        session (Session): Nox Session
    """
    session.install("mypy", "lxml")
    session.run("poetry", "install", external=True)
    session.run("mypy", "--txt-report", "mypy_report.txt")


@session(python=PYTHON_VERSIONS)
def tests(session: Session) -> None:
    """Runs unit testing & generates coverage report.

    Args:
        session (Session): Nox Session
    """
    session.install("pytest", "pytest-cov", "pytest-xdist")
    session.run("poetry", "install", external=True)
    session.run("pytest", "--xdoctest", "--cov")


@session(python=PYTHON_VERSIONS)
def coverage(session: Session) -> None:
    """Upload coverage data.

    Args:
        session (Session): Nox Session
    """
    session.install("coverage[toml]", "codecov")
    session.run("coverage", "xml", "--fail-under=0")
    session.run("codecov")


@session(python=PYTHON_VERSIONS)
def safety(session: Session) -> None:
    """Use safety to check for vulnerability in project dependencies.

    Args:
        session (Session): Nox Session
    """
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        session.install("safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")


@session(python="3.8")
def docs(session: Session) -> None:
    """Build the docs.

    Args:
        session (Session): Nox Session
    """
    session.run("poetry", "install", external=True)
    session.install(
        "sphinx", "myst-parser", "sphinx-autodoc-typehints", "furo", "sphinx_copybutton"
    )
    session.run("sphinx-build", "docs", "docs/_build")
