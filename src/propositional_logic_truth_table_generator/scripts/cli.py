import argparse

from modules import parser, truth_table_generator
from modules.truth_table_visualizer import TruthTableVisualizer


def parse_args():
    parser = argparse.ArgumentParser(
        prog="pltt-cli",
        description="Enter a wff as string and visualize the truth table as html.",
    )
    parser.add_argument("wff", type=str)
    parser.add_argument(
        "-p", "--print", action="store_true", help="print a formatted truth table"
    )
    parser.add_argument(
        "-g",
        "--generate",
        metavar="FILENAME",
        help="give a name and generate a truth table in html",
        type=str,
    )
    return parser.parse_args()


def entrypoint():
    args = parse_args()
    wff = parser.wff_from_str(args.wff)
    truth_table = truth_table_generator.build_table(wff)
    truth_table_visualizer = TruthTableVisualizer(truth_table, as_int=True)
    if args.print:
        print(truth_table_visualizer)
    if args.generate:
        filename = args.generate
        truth_table_visualizer.save_as_html(args.generate + ".html")
        print(f"The truth table {filename}.html has been generated.")


if __name__ == "__main__":
    entrypoint()
