import os
from mmdesigner.Analyzer import Analyzer

def test_model_path(model_dir):
    a = Analyzer(model_dir)
    assert a.get_model_path() == model_dir

def test_bad_model_path():
    a = Analyzer("dummy")
    assert a.get_model_path() == None


