class SVector: 
    def __init__(self, inX: int = 0, inY: int = 0) -> None:
        self.x: int = inX
        self.y: int = inY

    def __str__(self) -> str:
        return f"X: {self.x}, Y: {self.y}"
    
    def __eq__(self, __value: object) -> bool:        
        return __value.x == self.x and __value.y == self.y