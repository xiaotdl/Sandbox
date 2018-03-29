# pytest doc

An example of a simple test:

# content of test_sample.py
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5


To execute it:

$ pytest
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-3.x.y, py-1.x.y, pluggy-0.x.y
rootdir: $REGENDOC_TMPDIR, inifile:
collected 1 item

test_sample.py F                                                     [100%]

================================= FAILURES =================================
_______________________________ test_answer ________________________________

    def test_answer():
>       assert inc(3) == 5
E       assert 4 == 5
E        +  where 4 = inc(3)

test_sample.py:5: AssertionError
========================= 1 failed in 0.12 seconds =========================


## Features
- Detailed info on failing assert statements (no need to remember self.assert* names);
- Auto-discovery of test modules and functions;
- Modular fixtures for managing small or parametrized long-lived test resources;
- Can run unittest (including trial) and nose test suites out of the box;
- Python 2.7, Python 3.4+, PyPy 2.3, Jython 2.5 (untested);
- Rich plugin architecture, with over 315+ external plugins and thriving community;


## Full pytest doc
https://docs.pytest.org/en/latest/contents.html#toc


## Floris Bruynooghe - The hook-based plugin architecture of py.test
https://www.youtube.com/watch?v=zZsNPDfOoHU