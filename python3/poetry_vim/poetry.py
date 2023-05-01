import vim

class Poet:
    def test(self) -> None:
        print("hello there!")
        row, col = vim.current.window.cursor
        buffer = vim.current.buffer
        print(buffer, row, col)

        buffer[row-1] = buffer[row-1][:col] + "hello there!" + buffer[row-1][col:]

        new_col = col + len("hello there!")
        vim.current.window.cursor = (row, new_col)


