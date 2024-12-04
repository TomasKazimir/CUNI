class Cell:
    def __init__(self, is_alive: bool):
        self.is_alive = is_alive
        self.live_neighbours = 0

    def __repr__(self):
        return f"<{self.__class__.__name__}, {self.is_alive=}, {self.live_neighbours=}>"
