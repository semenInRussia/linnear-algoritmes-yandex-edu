DEFAULT_FINISH = (1, 1)


class Tank:
    def __init__(self, start_x: int, start_y: int):
        self._x = start_x
        self._y = start_y

    def run(self, cells_for_felling, finish):
        self.fill_cells_by_positions(cells_for_felling)

        self.move_to_position(*finish)

        return self

    def fill_cells_by_positions(self, positions):
        for position in positions:
            self.fill_cell_by_position(*position)

    def fill_cell_by_position(self, cell_x: int, cell_y: int):
        self.move_to_position(cell_x, cell_y)
        fill_cell()

    def move_to_position(self, x: int, y: int):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value: int):
        increment_x = value - self.x

        self._update_x_position(increment_x)

        self._x = value

    def _update_x_position(self, increment: int):
        if increment > 0:
            self._move_right_to(increment)
        elif increment < 0:
            self._move_left_to(increment)

    @y.setter
    def y(self, value: int):
        increment_y = value - self.y

        self._update_y_position(increment_y)

        self._y = value

    def _update_y_position(self, increment: int):
        if increment > 0:
            self._move_down_to(increment)
        elif increment < 0:
            self._move_up_to(increment)

    def _move_right_to(self, cells: int):
        self._move(move_right, cells)

    def _move_left_to(self, cells: int):
        self._move(move_left, -cells)

    def _move_up_to(self, cells: int):
        self._move(move_up, -cells)

    def _move_down_to(self, cells: int):
        self._move(move_down, cells)

    def _move(self, method, cells: int):
        for _ in range(cells):
            method()


def run(start_position, cells_for_felling, finish_position=DEFAULT_FINISH):
    tank = Tank(*start_position)

    tank.fill_cells_by_positions(cells_for_felling)

    tank.move_to_position(*finish_position)


run(
    (1, 3),
    [
        (2, 2),
        (3, 2)
    ]
    (5, 3)
)

run(
    (5, 3),
    [
        (4, 3)
    ],

    (2, 2)
)

run(
    (2, 2),
    []
)