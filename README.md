dotfiles
========

My personal collection of dotfiles.

This setup uses git's submodule feature to manage Vim plugins, which are then
injected into Vim using Tim Pope's
[pathogen.vim](https://github.com/tpope/vim-pathogen) plugin.

Before installing
-----------------

First of all, back up your existing dotfiles. You can inspect the Makefile to
find out which dotfiles the installation procedure will overwrite.

Installation
------------

Clone and cd into this repo. Then run:

```
make install update
```

This sets up all the symlinks and retrieves the required git submodules.

Upating git submodules
----------------------

Just run:

```
make update
```

Adding new git submodules
-------------------------

cd into the directory where you want to keep your submodule, then run:

```
git submodule add <repository url> <directory name>
```

This saves the submodule into the specified directory and adds the required
entry to .gitmodules.

For example, you can run the following command to install the vim-fugitive
plugin:

```
git submodule add https://github.com/tpope/vim-fugitive.git vim/vim/bundle/vim-fugitive.vim
```

