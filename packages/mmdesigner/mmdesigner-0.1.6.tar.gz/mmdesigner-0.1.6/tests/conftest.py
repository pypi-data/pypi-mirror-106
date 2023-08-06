import pytest
import pathlib
import os


SCAD = "cube([1,3,1]);"

@pytest.fixture()
def model_dir(tmp_path):
    #inv_dir = tmp_path / "tests"
    #inv_dir.mkdir()
    inv_dir = tmp_path
    f = inv_dir / "tests.scad"
    s = inv_dir / "tests.stl"
    f.write_text(SCAD)
    cmd = f"openscad {f} -o {s}"
    status = os.system(cmd)
    yield inv_dir
    #shutil.rmtree(inv_dir)




