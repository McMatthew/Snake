# Snake <3
import unittest
from World import SWorld

class Tests(unittest.TestCase):
    def test_placingHead_shouldBeThere(self):
        world = SWorld()
        world.placeSnake(0, 0)

        self.assertEqual(world.getSnakePosition(), (0, 0))
        
if __name__ == '__main__':
    unittest.main()