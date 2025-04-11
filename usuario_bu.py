from abc import ABC, abstractmethod


class UsuarioBU(ABC):
    def __init__(self, cpf: int, dias_de_emprestimo: int = 0):
        self._cpf = cpf
        self._dias_de_emprestimo = dias_de_emprestimo

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf: int):
        if isinstance(cpf, int):
            self._cpf = cpf

    @property
    def dias_de_emprestimo(self):
        return self._dias_de_emprestimo

    @dias_de_emprestimo.setter
    def dias_de_emprestimo(self, valor: int):
        if isinstance(valor, int) and valor >= 0:
            self._dias_de_emprestimo = valor

    @abstractmethod
    def emprestar(self, titulo_livro: str):
        return ""

    @abstractmethod
    def devolver(self, titulo_livro: str):
        return ""




