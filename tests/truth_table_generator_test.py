from modules import parser, truth_table_generator
from modules.truth_table_visualizer import TruthTableVisualizer


def test_and():
    wff = parser.wff_from_str("(A & B)")
    truth_table = truth_table_generator.build_table(wff)

    # Act
    output = TruthTableVisualizer(truth_table, as_int=True).to_str()

    # assert
    with open("tests/test_outputs/truth_table_and.txt") as file:
        expected_output = file.read()

    assert output == expected_output


def test_not_and():
    wff = parser.wff_from_str("~(A & B)")
    truth_table = truth_table_generator.build_table(wff)

    # Act
    output = TruthTableVisualizer(truth_table, as_int=True).to_str()

    # assert
    with open("tests/test_outputs/truth_table_not_and.txt") as file:
        expected_output = file.read()

    assert output == expected_output
