"""
**Warning**
In order to execute those tests correctly please make sure data is already placed
under the specified location /schema_name/table_name.
(You can easily do this by running the `test_iris_using_database_connection.py` before those tests).
"""


import unittest

from ibm_watson_machine_learning.tests.autoai.svt.abstract_test_iris_using_database_data_asset import\
    AbstractTestAutoAIConnectedAsset


@unittest.skip("The reading of training data is broken for now."
               "See: `https://github.ibm.com/NGP-TWC/ml-planning/issues/22963`")
class TestAutoAIMSSQLServer(AbstractTestAutoAIConnectedAsset, unittest.TestCase):
    database_name = "sqlserver"
    schema_name = "connections"


@unittest.skip("The reading of training data is broken for now."
               "See: `https://github.ibm.com/NGP-TWC/ml-planning/issues/22963`")
class TestAutoAIDB2(AbstractTestAutoAIConnectedAsset, unittest.TestCase):
    database_name = "db2"
    schema_name = "LMN17140"


@unittest.skip("The reading of training data is broken for now."
               "See: `https://github.ibm.com/NGP-TWC/ml-planning/issues/22963`")
class TestAutoAIPostgresSQL(AbstractTestAutoAIConnectedAsset, unittest.TestCase):
    database_name = "postgresql"
    schema_name = "public"


@unittest.skip("The reading of training data is broken for now."
               "See: `https://github.ibm.com/NGP-TWC/ml-planning/issues/22963`")
class TestAutoAIMySQL(AbstractTestAutoAIConnectedAsset, unittest.TestCase):
    database_name = "mysql"
    schema_name = "mysql"


if __name__ == "__main__":
    unittest.main()
