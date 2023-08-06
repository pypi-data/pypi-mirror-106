from mmdesigner.__main__ import main
from mmdesigner.__version__ import __version__
import click

def test_version(cli_runner):
    result = cli_runner.invoke(main, "-v")
    assert __version__ in result.output
