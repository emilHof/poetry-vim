# poetry-vim

This plugin fetches poetry snippets, randomly chosen from a set of (well) known poets. For what purpose? Art!

## Features

1. `:Poet` - Fetches a random poetry snippet and writes it to the current buffer blow the cursor.

## How it works

When `:Poet` is run **poetry-vim** makes a request to the amazing [PoetryDB](https://poetrydb.org/index.html) api. It requests a list of all authors stored in the database and chooses one at random. It then picks a random poem by that author, and randomly grabs 5-7 lines from the beginning of the poem. These lines are then written to the buffer along with the title of the poem and the author's name.

## Installation

#### Prerequisites

Vim or Neovim complied with python3 support.

#### Using `vim-plug`

```vim
Plug 'emilHof/poetry-vim'
```

#### Manual

```
# vim
mkdir -p ~/.vim/pack/plugins/start
git clone https://github.com/emilHof/poetry-vim.git ~/.vim/pack/plugins/start/poetry-vim

# neovim
mkdir -p ~/.local/share/nvim/site/pack/plugins/start
git clone https://github.com/emilHof/poetry-vim.git ~/.local/share/nvim/site/pack/plugins/start/poetry-vim
```

## Usage

```
=====================================

:Poet   fetch a random poetry snippet

======================================
```

## Key bindings

```vim
" fetch a random snippet and insert it into the buffer
nnoremap <leader>P <CMD>Poet<CR>
```

## License

[MIT License](./LICENSE)
