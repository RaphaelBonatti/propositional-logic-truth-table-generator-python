import itertools
from collections import OrderedDict
from dataclasses import dataclass
from inspect import signature
from typing import Dict, List

from modules.parser import WFF, Atom, TruthValue, Variable, Formula
from modules.wff_traverser import build_traversal_post_order


type Row = List[TruthValue]
type Valuation = Dict[Formula, TruthValue]
type Evaluation = OrderedDict[Formula, TruthValue]


@dataclass(frozen=True)
class TruthTable:
    header: List[Formula]
    rows: List[Row]

    def __post_init__(self) -> None:
        header_length = len(self.header)
        for row in self.rows:
            if len(row) != header_length:
                raise ValueError("Row length must be equal to header length.")


def build_table(wff: WFF) -> TruthTable:
    traversal = build_traversal_post_order(wff)
    variables = find_variables(traversal)
    valuations = generate_valuations(variables)
    evaluations = [
        evaluate_subformulas(traversal, valuation) for valuation in valuations
    ]
    header = list(valuations[0].keys()) + list(evaluations[0].keys())
    rows = [
        list(valuations[i].values()) + list(evaluations[i].values())
        for i in range(len(evaluations))
    ]
    return TruthTable(header, rows)


def generate_valuations(variables: List[Variable]) -> List[Valuation]:
    cartesian_product = itertools.product(*(len(variables) * [[False, True]]))
    return [dict(zip(variables, values)) for values in cartesian_product]


def find_variables(traversal: List[WFF]) -> List[Variable]:
    variables: List[Variable] = []
    for wff in traversal:
        if (not is_connective(wff)) and (wff.id not in variables):  # type: ignore
            variables.append(wff.id)  # type: ignore
    return variables


def is_connective(wff: WFF) -> bool:
    return wff.__class__.__name__ != Atom.__name__


def evaluate_subformulas(traversal: List[WFF], valuation: Valuation) -> Evaluation:
    stack: List[TruthValue] = []
    evaluation: Evaluation = OrderedDict()
    for wff in traversal:
        params: List[WFF] = [stack.pop() for _ in signature(wff.evaluate).parameters]  # type: ignore
        value: TruthValue = wff.evaluate(*params)  # type: ignore
        if value != None:
            stack.append(value)  # type: ignore
            evaluation[str(wff)] = stack[-1]
        else:
            stack.append(valuation[wff.id])  # type: ignore
    return evaluation
