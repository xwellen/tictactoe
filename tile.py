from tilestate import TileState


class Tile:
    state = None
    button = None
    is_ticked = False

    def __init__(self):
        self.state = TileState.EMPTY
        self.button = None

    def tick(self, state_):
        self.state = state_
        if self.state == TileState.X:
            self.button.configure(
                text="❎"
            )
        elif self.state == TileState.O:
            self.button.configure(
                text="🅾️"
            )
        self.is_ticked = True
