import unittest
import src.obj.ObjBase as ObjBase
import src.obj.Wall as Wall


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


class TestWalls(unittest.TestCase):
    def test_move(self):
        with self.assertRaises(TypeError):
            Wall().move()

if __name__ == '__main__':
    unittest.main(verbosity=1)
