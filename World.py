from Vector import SVector

class SWorld:
    
    def __init__(self) -> None:
        self.snakeLocation : SVector = SVector()
        self.snakeDirection : SVector = SVector(0, 1)

    def getSnakePosition(self)-> SVector:
        return self.snakeLocation
    
    def placeSnake(self, coords: SVector):
        self.snakeLocation = coords

    def tick(self):
        self.snakeLocation.x += self.snakeDirection.x
        self.snakeLocation.y += self.snakeDirection.y

    def moveRight(self):
        self.snakeDirection = SVector(1, 0)

    def moveLeft(self):
        self.snakeDirection = SVector(-1, 0)
