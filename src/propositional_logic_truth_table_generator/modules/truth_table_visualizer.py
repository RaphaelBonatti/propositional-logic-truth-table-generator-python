from prettytable import PrettyTable

from modules.truth_table_generator import TruthTable


class TruthTableVisualizer:
    def __init__(self, truth_table: TruthTable, as_int: bool = False) -> None:
        self._table = PrettyTable(field_names=truth_table.header)
        self._table.title = f"Truth table for wff: {self._table.field_names[-1]}"
        self._table.align = "c"

        if as_int:
            self._table.add_rows(  # type: ignore
                [[int(value) for value in row] for row in truth_table.rows]
            )
        else:
            self._table.add_rows(truth_table.rows)  # type: ignore

    def __str__(self) -> str:
        return self._table.get_string()  # type: ignore

    def save_as_html(self, filename: str) -> None:
        filename = filename if filename else "table.html"
        table_html = self._table.get_html_string(format=True)  # type: ignore
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(
                f"""<html>
            <head>
                <style>
                    thead {{border-bottom:1px solid black}}
                </style>
            </head>
            <body>
                {table_html} 
            </body>
            </html>
            """
            )
