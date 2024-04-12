from Vector import SVector

class SWorld:
    
    def __init__(self) -> None:
        self.snakeLocation : SVector = SVector()

    def getSnakePosition(self)-> SVector:
        return self.snakeLocation
    
    def placeSnake(self, coords: SVector):
        pass

    def tick(self):
        self.snakeLocation = SVector(0, 1)