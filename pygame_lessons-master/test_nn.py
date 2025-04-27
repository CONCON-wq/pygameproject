import pytest
import os
import psutil
from pathlib import Path

def test_directoy_exist():
    assert os.path.exists("Archer_asset"), "ERROR: но директари"
    assert os.path.exists("Easy_bot_assest"), "ERROR: но директари"
    assert os.path.exists("Hard_bot_assets"), "ERROR: но директари"
    assert os.path.exists("PLayer_assets"), "ERROR: но директари"

def test_count_files():
    assert len(os.listdir("Archer_asset")) == 11
    assert len(os.listdir("Easy_bot_assest")) == 10
    assert len(os.listdir("Hard_bot_assets")) == 10
    assert len(os.listdir("PLayer_assets")) == 10

def test_end_with_png():
    for file in os.listdir("Archer_asset"):
        assert file.endswith(".png")
    for file in os.listdir("Easy_bot_assest"):
        assert file.endswith(".png")
    for file in os.listdir("Hard_bot_assets"):
        assert file.endswith(".png")
    for file in os.listdir("PLayer_assets"):
        assert file.endswith(".png")

def test_cpu_count():
    assert os.cpu_count() >=2
    memory = psutil.virtual_memory()
    avalible_memory = memory.available
    avalible_memory_gb = avalible_memory / (1024*1024*1024)
    assert avalible_memory_gb > 1.5

