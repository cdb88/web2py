from .test_MySQLdb_capabilities import test_MySQLdb as test_capabilities
from .test_MySQLdb_dbapi20 import test_MySQLdb as test_dbapi2
from .test_MySQLdb_nonstandard import *

if __name__ == "__main__":
    import unittest

    unittest.main()
