.PHONY: install

install:
	git submodule init
	ln -s `pwd`/vim/vimrc      ~/.vimrc
	ln -s `pwd`/vim/vim        ~/.vim
	ln -s `pwd`/tmux/tmux.conf ~/.tmux.conf

update:
	git submodule update
