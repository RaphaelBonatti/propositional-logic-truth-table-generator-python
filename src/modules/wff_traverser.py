from typing import List

from modules.parser import WFF, Atom, Negation


def build_traversal_post_order(wff: WFF) -> List[WFF]:
    traversal = []
    stack = []
    lastVisited = None
    while len(stack) > 0 or wff != None:
        if wff != None:
            stack.append(wff)
            wff = match_case_next(wff)
        else:
            peeked = stack[-1]
            if match_case_condition(peeked, lastVisited):
                wff = match_case_next(peeked, left_direction=False)
            else:
                traversal.append(peeked)
                lastVisited = stack.pop()
    return traversal


def match_case_condition(peeked: WFF, lastVisited: WFF) -> bool:
    match peeked.__class__.__name__:
        case Atom.__name__:
            return False
        case Negation.__name__:
            return not (peeked.wff is lastVisited)
        case _:
            return not (peeked.rhs is lastVisited)


def match_case_next(wff: WFF, left_direction: bool = True) -> WFF:
    match wff.__class__.__name__:
        case Atom.__name__:
            return None
        case Negation.__name__:
            return wff.wff
        case _:
            if left_direction:
                return wff.lhs
            else:
                return wff.rhs
