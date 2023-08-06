from mmdesigner.__main__ import main
import click


def test_run(cli_runner):
    result = cli_runner.invoke(main)
    assert "mmdesigner" in result.output

def test_debug_mode(cli_runner):
    result = cli_runner.invoke(main, '-d')
    assert "debug" in result.output
