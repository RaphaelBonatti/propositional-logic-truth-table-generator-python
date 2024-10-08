# propositional-logic-truth-table-generator-python
The goal of this project is to develop a truth table builder and visualizer tool that can help users deepen their understanding of formal logic and evaluate large propositional formulas.

Main features:
- Truth Table Builder:
    - The tool will accept a well-formed logical formula as a string input.
    - It will generate the corresponding logical truth table, effectively automating the evaluation of composite formulas.

- Truth Table Visualizer:
    - The tool will present the generated truth table in a clear, tabular format.
    - This will allow users to easily analyze the logical structure and behavior of the given formula.

Note: This project was tested using Python 3.12.4 on Ubuntu.

## Installation
1. Before starting, you need to have Python installed on your system.
2. Clone or download the project repository.
3. Install Poetry.
4. Install the project with Poetry. Run the following at the root of the project:
    ```shell
    $ poetry install
    ```

## Usage

To use the propositional logic truth table generator, activate the project environment and execute the `pltt-cli` command with the formula you want to parse as a command-line argument.
You can use the flags `-p` or `--print` to print the truth table and the argument `-g` or `--generate` followed by a filename to generate the corresponding HTML file. 

You can use the following logical connectives: `~` (negation), `&` (conjunction), `|` (disjunction), `=>` (implication) and `<=>`(equivalence). However, you must ensure that every formula that includes a binary connective (&, |, =>, or <=>) is surrounded by parentheses.

Here is an example of using the CLI:
```shell
$ pltt-cli -p -g "example" "((~A&B)|C)"
```
The output will be:
```
+--------------------------------------------+
|    Truth table for wff: ((¬A ∧ B) ∨ C)     |
+---+---+---+----+----------+----------------+
| A | B | C | ¬A | (¬A ∧ B) | ((¬A ∧ B) ∨ C) |
+---+---+---+----+----------+----------------+
| 0 | 0 | 0 | 1  |    0     |       0        |
| 0 | 0 | 1 | 1  |    0     |       1        |
| 0 | 1 | 0 | 1  |    1     |       1        |
| 0 | 1 | 1 | 1  |    1     |       1        |
| 1 | 0 | 0 | 0  |    0     |       0        |
| 1 | 0 | 1 | 0  |    0     |       1        |
| 1 | 1 | 0 | 0  |    0     |       0        |
| 1 | 1 | 1 | 0  |    0     |       1        |
+---+---+---+----+----------+----------------+
The truth table example.html has been generated.
```

An HTML file named "example.html" containing a truth table will be created in the current directory. The resulting table will look as follows.

![The truth table example](images/example.png)


## License
This project is licensed under the Apache 2.0 license.
See the LICENSE file for more information.

## Acknowledgements
This project utilizes the following open-source libraries:
- `prettytable`:
  - Version: 3.10.0
  - License: Custom
  - Project website: https://github.com/jazzband/prettytable
  - Purpose: used for displaying a visually appealing table.
- `pytest`:
  - Version: 8.2.2
  - License: MIT
  - Project website: https://docs.pytest.org
  - Purpose: used for testing purposes.
- `textX`:
  - Version: 4.0.1
  - License: MIT
  - Project website: https://textx.github.io/textX
  - Purpose: used for parsing the input formula.

Special thanks to the authors and contributors who dedicated their time and effort to develop these libraries. Their hard work and valuable contributions have greatly benefited the software development community.

## Contact
If you have any questions or inquiries, please contact raphael.bonatti@algolance.com.
