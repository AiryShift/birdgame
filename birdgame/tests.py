import unittest
import src.obj.ObjBase as ObjBase
from src.obj.ObjBase import Vector
import src.obj.Wall as Wall
from math import pi
import pygame as pg


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


class TestWalls(unittest.TestCase):
    def test_move(self):
        with self.assertRaises(ObjBase.PhysicalError):
            Wall.Wall(Vector(), Vector()).move()

if __name__ == '__main__':
    pg.init()
    unittest.main(verbosity=1)
