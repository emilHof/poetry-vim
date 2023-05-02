import vim
import requests
import random

class Poem:
    def __init__(self, title: str ,lines: list[str]) -> None:
        self.title = title
        self.lines = lines

class Poet:
    def buf_insert_poem(self) -> None:
        row, col = vim.current.window.cursor
        buffer = vim.current.buffer

        poem = self.get_poetry()

        buffer[row:row] = poem

        vim.current.window.cursor = (row + len(poem), len(poem[-1]))

        vim.command("update")

        vim.command('stopinsert')

    def get_poetry(self) -> list[str]:
        while True:
            try:
                return self._get_poetry()
            except:
                continue


    def _get_poetry(self) -> list[str]:
        author = self._get_rand_author()
        poem = self._get_poem(author)
        lines  = [line for line in poem.lines[:min(random.randrange(11, 15), len(poem.lines))] if line != ""]
        lines = [line.strip() for line in lines[:min(random.randrange(3, 7), len(lines))]]
        lines += [f" - {author}", ""]
        return lines
    
    def _get_rand_author(self) -> str:
        body = requests.get("https://poetrydb.org/author").json()
        authors = body["authors"]
        return authors[random.randrange(0, len(authors))]
    
    def _get_poem(self, author: str) -> Poem:
        url = f"https://poetrydb.org/author/{author}/title,lines"
        poems = requests.get(url).json()
        poem = poems[random.randrange(0, len(poems))]
        return Poem(poem["title"], poem["lines"])

