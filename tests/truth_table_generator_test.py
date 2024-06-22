from modules import truth_table_generator, parser


def test_and():
    wff = parser.wff_from_str("(A & B)")
    variable_combinations, subformulas, rows = truth_table_generator.build_table(wff)

    # Act
    output = truth_table_generator.table_to_strings(
        variable_combinations, subformulas, rows
    )

    # assert
    with open("tests/truth_table_and.txt") as file:
        expected_output = file.readlines()

    assert output == expected_output


def test_not_and():
    wff = parser.wff_from_str("~(A & B)")
    variable_combinations, subformulas, rows = truth_table_generator.build_table(wff)

    # Act
    output = truth_table_generator.table_to_strings(
        variable_combinations, subformulas, rows
    )

    # assert
    with open("tests/truth_table_not_and.txt") as file:
        expected_output = file.readlines()

    for row_a, row_b in zip(output, expected_output):
        assert row_a == row_b


print(
    "".join(
        truth_table_generator.table_to_strings(
            *truth_table_generator.build_table(
                parser.wff_from_str("(((~(A=>B)&C)|D)<=>E)")
            )
        )
    )
)
