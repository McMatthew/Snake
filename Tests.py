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

    def test_givenDirectionUpThenDown_snakeStillMoveUp(self):
        world = SWorld()
        world.placeSnake(SVector(0, 3))
        world.moveUp()
        world.tick()
        world.moveDown()
        world.tick()

        self.assertEqual(world.getSnakePosition(), SVector(0, 1))

    def test_givenDirectionDownThenUp_snakeStillMoveDown(self):
        world = SWorld()
        world.placeSnake(SVector(0, 0))
        world.moveDown()
        world.tick()
        world.moveUp()
        world.tick()

        self.assertEqual(world.getSnakePosition(), SVector(0, 2))

    def test_givenDirectionLeftThenRight_snakeStillMoveLeft(self):
        world = SWorld()
        world.placeSnake(SVector(3, 0))
        world.moveLeft()
        world.tick()
        world.moveRight()
        world.tick()

        self.assertEqual(world.getSnakePosition(), SVector(1, 0))

    def test_placeSnakeWith2SectionsOnDown_bodyPartIsOnUp(self):
        world = SWorld()
        world.moveDown()
        world.placeSnake(SVector(0, 1), 2)

        self.assertEqual(world.getSnakeBodyPosition(1), SVector(0,0))

    def test_placeSnakeWith2SectionsOnUp_bodyPartIsOnDown(self):
        world = SWorld()
        world.moveUp()
        world.placeSnake(SVector(1, 1) , 2)

        self.assertEqual(world.getSnakeBodyPosition(1) , SVector(1, 2))

    def test_placeSnakeWith2SectionsOnRight_bodyPartIsOnTheLeft(self):
        world = SWorld()
        world.moveRight()
        world.placeSnake(SVector(1, 1), 2)

        self.assertEqual(world.getSnakeBodyPosition(1), SVector(0,1))
    
    def test_placeSnakeWith2SectionsOnLeft_bodyPartIsOnRight(self):
        world = SWorld()
        world.moveLeft()
        world.placeSnake(SVector(1, 1), 2)

        self.assertEqual(world.getSnakeBodyPosition(1), SVector(2, 1))

    def test_placeSnakeWith2SectionAndTicking_BodyFollowsHead(self):
        world = SWorld()
        world.moveRight()
        world.placeSnake(SVector(1, 1), 2)
        
        headPosition = copy.deepcopy(world.getHeadPosition()) 
        world.tick()
        
        self.assertEqual(world.getSnakeBodyPosition(1), headPosition)

    def test_placeSnakeWith3Section(self):
        world = SWorld()
        world.moveRight()
        world.placeSnake(SVector(2, 1), 3)
        world.tick()
        tasil = world.getSnakeBodyPosition(2)
        self.assertEqual(world.getSnakeBodyPosition(0), SVector(3, 1))
        self.assertEqual(world.getSnakeBodyPosition(1), SVector(2, 1))
        self.assertEqual(tasil, SVector(1, 1))


if __name__ == '__main__':
    unittest.main()
