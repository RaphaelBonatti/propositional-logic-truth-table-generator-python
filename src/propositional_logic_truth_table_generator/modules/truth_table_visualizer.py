from typing import List

from prettytable import PrettyTable, FRAME

from modules.truth_table_generator import TruthTable


class TruthTableVisualizer:
    def __init__(self, truth_table: TruthTable, as_int=False) -> None:
        self.table = PrettyTable(field_names=truth_table.get_header())
        self.table.title = f"Truth table for wff: {self.table.field_names[-1]}"
        self.table.align = "c"

        if as_int:
            self.table.add_rows(
                [[int(value) for value in row] for row in truth_table.get_rows()]
            )
        else:
            self.table.add_rows(truth_table.get_rows())

    def to_str(self) -> str:
        return self.table.get_string()

    def save_as_html(self, filename: str) -> None:
        filename = filename if filename else "table.html"
        with open(filename, mode="w", encoding="utf-8") as file:
            html = f"""<html>
            <head>
                <style>
                    thead {{border-bottom:1px solid black}}
                </style>
            </head>
            <body>
                {self.table.get_html_string(format=True)}
            </body>
            </html>
            """
            file.write(html)
