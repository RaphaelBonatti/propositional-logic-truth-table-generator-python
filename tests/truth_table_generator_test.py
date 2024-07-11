from modules import parser, truth_table_generator
from modules.truth_table_visualizer import TruthTableVisualizer


def test_and():
    # Assign
    wff = parser.wff_from_str("(A & B)")
    truth_table = truth_table_generator.build_table(wff)

    # Act
    output = TruthTableVisualizer(truth_table, as_int=True)

    # Assert
    with open("tests/test_outputs/truth_table_and.txt") as file:
        expected_output = file.read()

    assert str(output) == expected_output


def test_not_and():
    # Assign
    wff = parser.wff_from_str("~(A & B)")
    truth_table = truth_table_generator.build_table(wff)

    # Act
    output = TruthTableVisualizer(truth_table, as_int=True)

    # Assert
    with open("tests/test_outputs/truth_table_not_and.txt") as file:
        expected_output = file.read()

    assert str(output) == expected_output


def test_implication():
    # Assign
    wff = parser.wff_from_str("(A => B)")
    truth_table = truth_table_generator.build_table(wff)

    # Act
    output = TruthTableVisualizer(truth_table, as_int=True)

    # Assert
    with open("tests/test_outputs/truth_table_implication.txt") as file:
        expected_output = file.read()

    assert str(output) == expected_output


def test_duplicated_subformula():
    # Assign
    wff = parser.wff_from_str("((A & B) | (A & B))")
    truth_table = truth_table_generator.build_table(wff)

    # Act
    output = TruthTableVisualizer(truth_table, as_int=True)

    # Assert
    with open("tests/test_outputs/truth_table_and_or_and.txt") as file:
        expected_output = file.read()

    assert str(output) == expected_output


test_duplicated_subformula()
