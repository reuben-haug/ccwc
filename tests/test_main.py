# tests/test_main.py
from src.main import main, greet
import pytest


def test_greet():
    assert greet("World") == "Hello, World!"
    assert greet("Alice") == "Hello, Alice!"


def test_greet_empty():
    assert greet("") == "Hello, !"


def test_main(capsys):
    main()
    out, err = capsys.readouterr()
    assert "Hello, World!" in out
