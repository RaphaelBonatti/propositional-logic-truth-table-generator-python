import itertools
from typing import Dict, List

from modules.parser import (
    WFF,
    Atom,
    Conjunction,
    Disjunction,
    Equivalence,
    Implication,
    Negation,
)
from modules.wff_traverser import build_traversal_post_order


class TruthTable:
    def __init__(
        self,
        variable_combinations: List[Dict[str, bool]],
        subformulas: List[str],
        subformulas_values: List[List[bool]],
    ):
        self.header = list(variable_combinations[0].keys()) + subformulas
        self.rows = [
            list(variable_combinations[i].values()) + subformulas_values[i]
            for i in range(len(subformulas_values))
        ]

    def get_header(self):
        return self.header

    def get_rows(self):
        return self.rows


def build_table(wff: WFF) -> TruthTable:
    traversal_list = build_traversal_post_order(wff)
    subformulas = build_subformulas(traversal_list)
    variables = find_variables(traversal_list)
    variable_combinations = generate_variable_combination(variables)
    subformulas_values = []
    for combination in variable_combinations:
        subformulas_values.append(generate_row(traversal_list, combination))

    return TruthTable(variable_combinations, subformulas, subformulas_values)


def generate_variable_combination(variables: List[str]) -> List[Dict[str, bool]]:
    return [
        dict(zip(variables, values))
        for values in itertools.product(*(len(variables) * [[False, True]]))
    ]


def build_subformulas(traversal_list: List[WFF]) -> List[str]:
    return [wff.toString() for wff in traversal_list if match_connective(wff)]


def find_variables(traversal_list: List[WFF]) -> List[str]:
    return [wff.id for wff in traversal_list if not match_connective(wff)]


def match_connective(wff: WFF) -> bool:
    return wff.__class__.__name__ != Atom.__name__


def generate_row(traversal_list: WFF, combination: Dict[str, bool]) -> List[bool]:
    row = []
    stack = []

    for wff in traversal_list:
        match wff.__class__.__name__:
            case Atom.__name__:
                stack.append(combination[wff.id])
            case Negation.__name__:
                stack.append(not stack.pop())
                row.append(stack[-1])
            case Conjunction.__name__:
                stack.append(stack.pop() & stack.pop())
                row.append(stack[-1])
            case Disjunction.__name__:
                stack.append(stack.pop() | stack.pop())
                row.append(stack[-1])
            case Implication.__name__:
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append((not val1) | val2)
                row.append(stack[-1])
            case Equivalence.__name__:
                stack.append(stack.pop() == stack.pop())
                row.append(stack[-1])
    return row
