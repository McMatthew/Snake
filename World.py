from Vector import SVector
import copy

class SWorld:
    def __init__(self) -> None:
        self.snakePoints : list[SVector] = list()
        self.snakeDirection : SVector = SVector(0, 1)
        self.__directionUp: SVector = SVector(0, -1)
        self.__directionDown: SVector = SVector(0, 1)
        self.__directionLeft: SVector = SVector(-1, 0)
        self.__directionRight: SVector = SVector(1, 0)


    def getSnakePosition(self)-> SVector:
        return self.snakePoints[0]

    def placeSnake(self, coords: SVector, bodycount: int = 1):
        self.snakePoints.append(coords)
        for multiplier in range(1,bodycount):

            shifter = SVector()
            if self.snakeDirection == self.__directionDown:
                shifter = SVector(0, self.__directionUp.y * multiplier)

            elif self.snakeDirection == self.__directionUp: 
                shifter = SVector(0, self.__directionDown.y * multiplier)

            elif self.snakeDirection == self.__directionRight:
                shifter = SVector(self.__directionLeft.x * multiplier, 0)

            elif self.snakeDirection == self.__directionLeft:
                shifter = SVector(self.__directionRight.x * multiplier, 0)

            self.snakePoints.append(SVector(coords.x + shifter.x, coords.y + shifter.y))

    def tick(self):
        newHead = copy.deepcopy(self.getHeadPosition())
        self.snakePoints.pop()
        newHead.x += self.snakeDirection.x
        newHead.y += self.snakeDirection.y
        self.snakePoints.insert(0,newHead)

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

    
    def getSnakeBodyPosition(self, bodyPartIndex: int):
        return self.snakePoints[bodyPartIndex]
    
    def getHeadPosition(self):
        return self.snakePoints[0]
    