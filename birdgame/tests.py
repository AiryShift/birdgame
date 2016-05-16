import unittest
from src.obj import ObjBase


class TestVector(unittest.TestCase):
    def test_operators(self):
        self.assertEqual(ObjBase.Vector(arg=0), ObjBase.Vector(x=1, y=0))
        self.assertEqual(ObjBase.Vector(arg=0) * 2, ObjBase.Vector(x=2))
        self.assertEqual(2 * ObjBase.Vector(arg=0), ObjBase.Vector(x=2))
        with self.assertRaises(TypeError):
            ObjBase.Vector(arg=0) + 'a'


class TestPhysicalObject(unittest.TestCase):
    def test_detect_collision(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=1)
