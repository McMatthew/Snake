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

    def test_givenDirectionRight_moveRight(self):
        world = SWorld()
        world.placeSnake(SVector(0, 0))
        world.moveRight()
        world.tick()

        self.assertEqual(world.getSnakePosition(), SVector(1, 0))

    def test_givenDirectionRightTickingTwice_keepDirectionRight(self):
        world = SWorld()
        world.placeSnake(SVector(0, 0))
        world.moveRight()
        world.tick()
        world.tick()

        self.assertEqual(world.getSnakePosition(), SVector(2, 0))

    def test_givenDirectionLeft_moveLeft(self):
        world = SWorld()
        world.placeSnake(SVector(3, 0))
        world.moveLeft()
        world.tick()

        self.assertEqual(world.getSnakePosition(), SVector(2, 0))

    def test_givenDirectionUp_moveUp(self):
        world = SWorld()
        world.placeSnake(SVector(0, 3))
        world.moveUp()
        world.tick()

        self.assertEqual(world.getSnakePosition(), SVector(0, 2))
    
    def test_givenDirectionDown_moveDown(self):
        world = SWorld()
        world.placeSnake(SVector(0, 0))
        world.moveDown()
        world.tick()

        self.assertEqual(world.getSnakePosition(), SVector(0, 1))

    def test_givenDirectionRightThenLeft_snakeStillMoveRight(self):
        world = SWorld()
        world.placeSnake(SVector(0, 0))
        world.moveRight()
        world.tick()
        world.moveLeft()
        world.tick()

        self.assertEqual(world.getSnakePosition(), SVector(2, 0))


if __name__ == '__main__':
    unittest.main()