import unittest
from models.engine.db_storage import DBStorage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User

class TestDBStorage(unittest.TestCase):

    def setUp(self):
        self.db_storage = DBStorage()

    def tearDown(self):
        # Clean up any resources if needed
        pass

    def test_all_with_no_class_specified(self):
        # Test all method with no class specified
        result = self.db_storage.all()
        self.assertIsInstance(result, dict)
        # Check if objects of all supported classes are retrieved
        self.assertTrue(all(isinstance(obj, (User, State, City, Amenity, Place, Review)) for obj in result.values()))

    def test_all_with_class_specified(self):
        # Test all method with class specified (e.g., State)
        result = self.db_storage.all(State)
        self.assertIsInstance(result, dict)
        # Check if objects of specified class are retrieved
        self.assertTrue(all(isinstance(obj, State) for obj in result.values()))

if __name__ == '__main__':
    unittest.main()
