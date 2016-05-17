import unittest
import src.obj.ObjBase as ObjBase
from src.obj.ObjBase import Vector
import src.obj.Wall as Wall
from math import pi


class TestVector(unittest.TestCase):
    def test_operators(self):
        self.assertEqual(Vector(arg=0), Vector(x=1, y=0))
        self.assertEqual(Vector(arg=0) * 2, Vector(x=2))
        self.assertEqual(2 * Vector(arg=0), Vector(x=2))
        with self.assertRaises(TypeError):
            Vector(arg=0) + 'a'
        self.assertEqual(Vector(arg=0) * Vector(arg=pi), Vector(x=-1, y=0))
        self.assertEqual(Vector(arg=pi / 2), Vector(x=0, y=1))
        self.assertEqual(Vector(arg=-pi / 2), Vector(x=0, y=-1))


class TestPhysicalObject(unittest.TestCase):
    def setUp(self):
        self.same_1 = ObjBase.PhysicalObject(
            Vector(x=0, y=0), Vector(x=2, y=2),
            Vector(x=0, y=0), Vector(x=0, y=0),
            0, 0)
        self.same_2 = ObjBase.PhysicalObject(
            Vector(x=0, y=0), Vector(x=2, y=2),
            Vector(x=0, y=0), Vector(x=0, y=0),
            0, 0)
        self.moving = ObjBase.PhysicalObject(
            Vector(x=4, y=0), Vector(x=2, y=2),
            Vector(x=-1, y=0), Vector(x=0, y=0),
            0, 0)

    def test_detect_collision(self):
        self.assertTrue(self.same_1.detect_collision(self.same_2))
        self.assertTrue(self.same_2.detect_collision(self.same_1))

        self.assertFalse(self.same_1.detect_collision(self.moving))
        self.moving.move()
        self.assertFalse(self.same_1.detect_collision(self.moving))
        self.moving.move()
        self.assertTrue(self.same_1.detect_collision(self.moving))
        self.assertTrue(self.same_2.detect_collision(self.moving))


class TestWalls(unittest.TestCase):
    def test_move(self):
        with self.assertRaises(ObjBase.PhysicalError):
            Wall.Wall().move()

if __name__ == '__main__':
    unittest.main(verbosity=1)
