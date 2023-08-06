import unittest

from ibm_watson_machine_learning.tests.autoai.svt.abstract_test_iris_using_database_connection import\
    AbstractTestAutoAIDatabaseConnection


class TestAutoAIMSSQLServer(AbstractTestAutoAIDatabaseConnection, unittest.TestCase):
    database_name = "sqlserver"
    schema_name = "connections"


class TestAutoAIDB2(AbstractTestAutoAIDatabaseConnection, unittest.TestCase):
    database_name = "db2"
    schema_name = "LMN17140"


class TestAutoAIPostgresSQL(AbstractTestAutoAIDatabaseConnection, unittest.TestCase):
    database_name = "postgresql"
    schema_name = "public"


@unittest.skip("Provided credentials seems to be invalid.")
class TestAutoAIMySQL(AbstractTestAutoAIDatabaseConnection, unittest.TestCase):
    database_name = "mysql"
    schema_name = "mysql"


if __name__ == "__main__":
    unittest.main()
