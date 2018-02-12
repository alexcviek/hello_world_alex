import pytest
import hello

def test_hello_no_name():
  """checks that if no name is passed, we get 'Hello, World'"""
  assert hello.hello() == 'Hello, World'

def test_hello_with_name():
  """If passed a name, returns, 'Hello, name'"""
  assert hello.hello('Alex') == 'Hello, Alex'