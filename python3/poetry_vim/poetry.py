import vim
import requests
import random

class Poem:
    def __init__(self, title: str ,lines: list[str]) -> None:
        self.title = title
        self.lines = lines

class Poet:
    def test(self) -> None:
        print("hello there!")
        row, col = vim.current.window.cursor
        buffer = vim.current.buffer
        print(buffer, row, col)
        print("more")

        buffer[row-1] = buffer[row-1][:col] + "hello there!" + buffer[row-1][col:]

        new_col = col + len("hello there!")
        vim.current.window.cursor = (row, new_col)

    def _get_poetry(self) -> str:
        author = self._get_rand_author()
        print(f"author: {author}")
        poem = self._get_poem(author)
        print(f"poem: {poem}")
        return "\n".join(poem.lines[:min(2, len(poem.lines))])
    
    def _get_rand_author(self) -> str:
        body = requests.get("https://poetrydb.org/author").json()

        authors = body["authors"]
        return authors[random.randrange(0, len(authors))]
    
    def _get_poem(self, author: str) -> Poem:
        poems = requests.get("https://poetrydb.org/author/{author}/title,lines").json()
        poem = poems[random.randrange(0, len(poems))]
        return Poem(poem["title"], poem["lines"])
        






