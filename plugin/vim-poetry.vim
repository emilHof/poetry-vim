if !has('python3')
    echomsg ':python3 is not available, vim-find-test will not be loaded.'
    finish
endif

python3 import poetry_vim.poetry
python3 poet = poetry_vim.poetry.Poet()

command! Poet python3 poet.test()
