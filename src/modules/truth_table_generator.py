import itertools

from modules.parser import (
    Atom,
    Conjunction,
    Disjunction,
    Equivalence,
    Implication,
    Negation,
)


def table_to_strings(variable_combinations, subformulas, rows):
    header_elements = list(variable_combinations[0].keys()) + subformulas
    lengths = [len(element) + 2 for element in header_elements]
    header = build_row(header_elements)
    value_rows = [
        build_row_with_centered_elements(
            list(variable_combinations[i].values()) + rows[i], lengths
        )
        for i in range(len(rows))
    ]
    horizontal_line = build_horizontal_line(lengths)
    lines = [horizontal_line, header, horizontal_line, *value_rows, horizontal_line]

    return [
        line + "\n" if i != len(lines) - 1 else line for i, line in enumerate(lines)
    ]


def build_horizontal_line(lengths):
    return "".join(["+" + length * "-" for length in lengths]) + "+"


def build_row(elements):
    return "".join([f"| {element} " for element in elements]) + "|"


def build_row_with_centered_elements(elements, lengths):
    return (
        "".join(
            [
                (
                    "|"
                    + (length // 2) * " "
                    + str(element)
                    + (
                        (length // 2) * " "
                        if (length % 2 != 0)
                        else ((length // 2) - 1) * " "
                    )
                )
                for element, length in zip(elements, lengths)
            ]
        )
        + "|"
    )


def build_table(wff):
    traversal_list = build_traversal_post_order(wff)
    header = build_header(traversal_list)
    variables = find_variables(traversal_list)
    variable_combinations = generate_variable_combination(variables)
    rows = []
    for combination in variable_combinations:
        rows.append(generate_row(traversal_list, combination))
    return variable_combinations, header, rows


def build_traversal_post_order(wff):
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


def match_case_condition(peeked, lastVisited):
    match peeked.__class__.__name__:
        case Atom.__name__:
            return False
        case Negation.__name__:
            return not (peeked.wff is lastVisited)
        case _:
            return not (peeked.rhs is lastVisited)


def match_case_next(wff, left_direction=True):
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


def match_connective(wff):
    return wff.__class__.__name__ != Atom.__name__


def build_header(traversal_list):
    return [wff.toString() for wff in traversal_list if match_connective(wff)]


def generate_variable_combination(variables):
    return [
        dict(zip(variables, values))
        for values in itertools.product(*(len(variables) * [[0, 1]]))
    ]


def find_variables(traversal_list):
    return [wff.id for wff in traversal_list if not match_connective(wff)]


def generate_row(traversal_list, combination):
    row = []
    stack = []

    for wff in traversal_list:
        match wff.__class__.__name__:
            case Atom.__name__:
                stack.append(combination[wff.id])
            case Negation.__name__:
                stack.append(int(not stack.pop()))
                row.append(stack[-1])
            case Conjunction.__name__:
                stack.append(int(stack.pop() & stack.pop()))
                row.append(stack[-1])
            case Disjunction.__name__:
                stack.append(int(stack.pop() | stack.pop()))
                row.append(stack[-1])
            case Implication.__name__:
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int((not val1) | val2))
                row.append(stack[-1])
            case Equivalence.__name__:
                stack.append(int(stack.pop() == stack.pop()))
                row.append(stack[-1])
    return row
