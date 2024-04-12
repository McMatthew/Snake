from Vector import SVector

class SWorld:
    def __init__(self) -> None:
        self.snakeLocation : SVector = SVector()
        self.snakeDirection : SVector = SVector(0, 1)
        self.__directionUp: SVector = SVector(0, -1)
        self.__directionDown: SVector = SVector(0, 1)
        self.__directionLeft: SVector = SVector(-1, 0)
        self.__directionRight: SVector = SVector(1, 0)

        
    def getSnakePosition(self)-> SVector:
        return self.snakeLocation
    
    def placeSnake(self, coords: SVector):
        self.snakeLocation = coords

    def tick(self):
        self.snakeLocation.x += self.snakeDirection.x
        self.snakeLocation.y += self.snakeDirection.y

    def moveRight(self):
        self.snakeDirection = self.__directionRight

    def moveLeft(self):
        if self.snakeDirection is not self.__directionRight:
            self.snakeDirection = self.__directionLeft
        
    def moveUp(self):
        self.snakeDirection = self.__directionUp

    def moveDown(self):
        self.snakeDirection = self.__directionDown
