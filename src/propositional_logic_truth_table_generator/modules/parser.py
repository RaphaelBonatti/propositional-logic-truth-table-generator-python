from abc import ABC, abstractmethod
from typing import Any

from textx import metamodel_from_str

grammar = """
Model: wff=WFF;
WFF: Atom | Negation | Conjunction | Disjunction | Implication | Equivalence;
Equivalence: '(' wff=WFF '<=>' wff=WFF ')';
Implication: '(' wff=WFF '=>' wff=WFF ')';
Disjunction: '(' wff=WFF '|' wff=WFF ')';
Conjunction: '(' wff=WFF '&' wff=WFF ')';
Negation: '~' wff=WFF;
Atom: id=ID;
"""


class WFF(ABC):
    @abstractmethod
    def toString(self) -> str:
        pass


class Equivalence(WFF):
    def __init__(self, parent: Any, wff: WFF):
        self.parent = parent
        self.lhs = wff[0]
        self.rhs = wff[1]

    def toString(self) -> str:
        return f"({self.lhs.toString()} ↔ {self.rhs.toString()})"


class Implication(WFF):
    def __init__(self, parent: Any, wff: WFF):
        self.parent = parent
        self.lhs = wff[0]
        self.rhs = wff[1]

    def toString(self) -> str:
        return f"({self.lhs.toString()} → {self.rhs.toString()})"


class Disjunction(WFF):
    def __init__(self, parent: Any, wff: WFF):
        self.parent = parent
        self.lhs = wff[0]
        self.rhs = wff[1]

    def toString(self) -> str:
        return f"({self.lhs.toString()} ∨ {self.rhs.toString()})"


class Conjunction(WFF):
    def __init__(self, parent: Any, wff: WFF):
        self.parent = parent
        self.lhs = wff[0]
        self.rhs = wff[1]

    def toString(self) -> str:
        return f"({self.lhs.toString()} ∧ {self.rhs.toString()})"


class Negation(WFF):
    def __init__(self, parent: Any, wff: WFF):
        self.parent = parent
        self.wff = wff

    def toString(self) -> str:
        return f"¬{self.wff.toString()}"


class Atom(WFF):
    def __init__(self, parent: Any, id: str):
        self.parent = parent
        self.id = id

    def toString(self) -> str:
        return self.id


def wff_from_str(wff_str: str) -> WFF:
    return (
        metamodel_from_str(
            grammar,
            classes=[
                Atom,
                Negation,
                Conjunction,
                Disjunction,
                Implication,
                Equivalence,
            ],
        )
        .model_from_str(wff_str)
        .wff
    )
