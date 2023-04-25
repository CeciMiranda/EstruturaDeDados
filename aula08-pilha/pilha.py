# -*- coding:utf-8 -*-

class Pilha:
    def __init__(self) -> None:
        self.__pilha = [] # list do python

    def is_empty(self):
        return True if len(self.__pilha)==0 else False

    def push(self):
        ...

    def pop(self):
        ...

    def peek(self):
        ...

    def list_items(self):
        ...

    def get_size(self):
        ...
