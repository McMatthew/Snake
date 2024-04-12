from Vector import SVector

class SWorld:
    
    def __init__(self) -> None:
        self.snakeLocation : SVector = SVector()
        self.direction : SVector = SVector(0, 1)

    def getSnakePosition(self)-> SVector:
        return self.snakeLocation
    
    def placeSnake(self, coords: SVector):
        pass

    def tick(self):
        self.snakeLocation = self.direction

    def moveRight(self):
        self.direction = SVector(1, 0)