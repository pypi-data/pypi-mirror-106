import pytest
import subprocess

from kbase_report_state import serve


def test_serve():
    try:
        serve()
    except NotImplementedError as err:
        assert isinstance(err, NotImplementedError)

def test_serve_cli():
    output = subprocess.run("python kbase_report_state/__init__.py".split(" "), capture_output=True)
    print(f"output: {output}")
