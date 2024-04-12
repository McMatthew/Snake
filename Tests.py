# Snake <3
import unittest
from World import *

class Tests(unittest.TestCase):
    def test_placingHead_shouldBeThere(self):
        world = SWorld()
        world.placeSnake(SVector(0, 0))

        self.assertEqual(world.getSnakePosition(), SVector(0, 0))
    
    def test_placingHeadTickingWorld_headMoveForward(self): 
        world = SWorld()
        world.placeSnake(SVector(0, 0))
        world.tick()

        self.assertEqual(world.getSnakePosition(), SVector(0, 1))
        
if __name__ == '__main__':
    unittest.main()