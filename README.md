# What is this?

Argparse module is awsome, while the spec says

> 'version' - This expects a version= keyword argument in the add_argument() call, and prints version information and exits when invoked:

It exits itself, which makes unittest a bit harder.

This example demonstrates how to test it.

# How to use it

Just run the unit test and see it fails.


    $ python tests.py
    usage: tests.py [-h] [-d]
    tests.py: error: unrecognized arguments: -v
    F
    ======================================================================
    FAIL: test_version (__main__.MyTest)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "tests.py", line 26, in test_version
        self.assertEqual(__version__, output.rstrip())
    AssertionError: '0.0.1' != ''
    - 0.0.1
    +
    
    
    ----------------------------------------------------------------------
    Ran 1 test in 0.001s
    
    FAILED (failures=1)

Modify main.py and uncomment the code about --version.

    $ python tests.py
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.001s
    
    OK

# License

MIT

(I don't believe this code snippet has enough volume to claim copyright)

# ref

http://schinckel.net/2013/04/15/capture-and-test-sys.stdout-sys.stderr-in-unittest.testcase/
