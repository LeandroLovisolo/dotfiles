.PHONY: install update

install:
	git submodule init
	ln -snfi `pwd`/i3             ~/.i3
	ln -snfi `pwd`/vim/vimrc      ~/.vimrc
	ln -snfi `pwd`/vim/vim        ~/.vim
	ln -snfi `pwd`/tmux/tmux.conf ~/.tmux.conf

update:
	git submodule update
