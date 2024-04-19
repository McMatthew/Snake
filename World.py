from Vector import SVector

class SWorld:
    def __init__(self) -> None:
        self.snakeLocation : list[SVector] = list()
        self.snakeDirection : SVector = SVector(0, 1)
        self.__directionUp: SVector = SVector(0, -1)
        self.__directionDown: SVector = SVector(0, 1)
        self.__directionLeft: SVector = SVector(-1, 0)
        self.__directionRight: SVector = SVector(1, 0)


    def getSnakePosition(self)-> SVector:
        return self.snakeLocation[0]

    def placeSnake(self, coords: SVector, bodycount: int = 1):
        self.snakeLocation.append(coords)

        if self.snakeDirection == self.__directionDown:
            self.snakeLocation.append(SVector(coords.x, coords.y -1))

        elif self.snakeDirection == self.__directionUp: 
            self.snakeLocation.append(SVector(coords.x, coords.y +1))

        elif self.snakeDirection == self.__directionRight:
            self.snakeLocation.append(SVector(coords.x -1, coords.y))

        elif self.snakeDirection == self.__directionLeft:
            self.snakeLocation.append(SVector(coords.x +1, coords.y))

    def tick(self):
        self.snakeLocation[0].x += self.snakeDirection.x
        self.snakeLocation[0].y += self.snakeDirection.y

    def moveRight(self):
        if self.snakeDirection is not self.__directionLeft:
            self.snakeDirection = self.__directionRight

    def moveLeft(self):
        if self.snakeDirection is not self.__directionRight:
            self.snakeDirection = self.__directionLeft

    def moveUp(self):
        if self.snakeDirection is not self.__directionDown:
            self.snakeDirection = self.__directionUp

    def moveDown(self):
        if self.snakeDirection is not self.__directionUp:
            self.snakeDirection = self.__directionDown

    def getSnakeBodyPosition(self, bodycount: int):
        return self.snakeLocation[1]