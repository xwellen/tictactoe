from tilestate import TileState
from tile import Tile
from verdicts import Verdict


class Field:
    enabled = True
    label = None
    tile_list = list()
    order = TileState.X

    def __init__(self, label_):
        self.label = label_
        for _ in range(3*3):
            new_tile = Tile()
            self.tile_list.append(new_tile)

    def tick(self, row_index, column_index):
        if not self.enabled:
            return
        if self.tile_list[3 * row_index + column_index].is_ticked:
            return

        self.tile_list[3 * row_index + column_index].tick(self.order)
        verdict = self.verdict()
        if verdict == Verdict.WIN_X:
            self.label.configure(
                text="X won!"
            )
            self.enabled = False
        elif verdict == Verdict.WIN_O:
            self.label.configure(
                text="O won!"
            )
            self.enabled = False
        elif verdict == Verdict.DRAW:
            self.label.configure(
                text="Draw"
            )
            self.enabled = False

        if self.order == TileState.X:
            self.order = TileState.O
        else:
            self.order = TileState.X

    def assign_button(self, row_index, column_index, button_):
        self.tile_list[3 * row_index + column_index].button = button_

    def verdict(self):
        def is_allthesame(x):
            for i in range(len(x)):
                for j in range(len(x)):
                    if x[i] != x[j]:
                        return False
            return True if x[0] != TileState.EMPTY else False

        def tile_verdict(tile_state):
            if tile_state == TileState.X:
                return Verdict.WIN_X
            if tile_state == TileState.O:
                return Verdict.WIN_O
            return None

        # horizontal check
        for i in range(3):
            h_list = list()
            for j in range(3):
                h_list.append(self.tile_list[3 * i + j].state)
            if is_allthesame(h_list):
                return tile_verdict(h_list[0])
        # vertical check
        for i in range(3):
            v_list = list()
            for j in range(3):
                v_list.append(self.tile_list[3 * j + i].state)
            if is_allthesame(v_list):
                return tile_verdict(v_list[0])
        # cross check 1
        cross_list = list()
        for i in range(3):
            cross_list.append(self.tile_list[3 * i + i].state)
        if is_allthesame(cross_list):
            return tile_verdict(cross_list[0])
        # cross check 2
        cross_list = list()
        for i in range(3):
            cross_list.append(self.tile_list[3 * i + (3 - 1) - i].state)
        if is_allthesame(cross_list):
            return tile_verdict(cross_list[0])
        # draw check
        all_set = set()
        for x in self.tile_list:
            all_set.add(x.state)
        if not all_set.__contains__(TileState.EMPTY):
            return Verdict.DRAW
        return Verdict.NA

