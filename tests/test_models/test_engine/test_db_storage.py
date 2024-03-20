import os
import models
import MySQLdb
import unittest
# from models.city import City
# from models.user import User
# from models.place import Place
from models.state import State
# from models.amenity import Amenity

class TestDBStorage(unittest.TestCase):
    __env = os.getenv('HBNB_ENV')
    __user = os.getenv('HBNB_MYSQL_USER')
    __host = os.getenv('HBNB_MYSQL_HOST')
    __database = os.getenv('HBNB_MYSQL_DB')
    __user_pwd = os.getenv('HBNB_MYSQL_PWD')
    db_engine = models.DBStorage()

    def setUp(self):
        self.connection = MySQLdb.connect(
            host=self.__host, user=self.__user,
            passwd=self.__user_pwd, db=self.__database
        )
        self.cursor = self.connection.cursor()
        print('Connected!')

    def tearDown(self):
        self.cursor.close()
        self.connection.close()
        
    def test_insert_city(self):
        self.cursor.execute("SELECT COUNT(*) FROM states")
        init_count = self.cursor.fetchone()[0]
        
        self.cursor.execute("INSERT INTO states (name) VALUES ('California')")
        self.connection.commit()
        
        self.cursor.execute("SELECT COUNT(*) FROM states")
        last_count = self.cursor.fetchone()[0]
        
        self.assertEqual(init_count + 1, init_count)
        
if __name__ == '__main__':
    unittest.main()