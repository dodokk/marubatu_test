import itertools
import sys, os
import random
from tqdm import tqdm
from io import StringIO
from unittest import mock

from your_src import your_func      # please edit here!


def test(input_options: list, fname: str, message: str, *, short_mode=False):
    print(f"--- testcase {fname} Start ---")
    with open(fname, "r") as f:
        lines = list(map(lambda x: x.split(), f.read().split("\n")))
    
    original_options = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
    operation_dist = dict(zip(original_options, input_options))

    if short_mode:
        lines = random.sample(lines, 10000)
    
    for input_line in tqdm(lines):
        io = StringIO()
        sys.stdout = io
        
        with mock.patch("builtins.input", side_effect=list(map(lambda x: operation_dist[x], input_line))):

            your_func()     # please put your func
        
        sys.stdout = sys.__stdout__

        outputs = io.getvalue().split("\n")

        if not(message in outputs):
            print("--- testcase NG ---")
            return
    print("--- testcase OK ---")

if __name__ == "__main__":
    your_input_options = (      # please edit here!
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    )
    your_end_messages = {       # please edit here!
        "pre_win": "user0の勝ち",
        "pos_win": "user1の勝ち",
        "draw": "引き分けです"
    }

    # True -> only use 10000 random datas
    # False -> use all datas
    short_mode = True

    results_dir = "./results"
    pre_win_path = os.path.join(os.path.dirname(__file__), results_dir, "pre_win.txt")
    pos_win_path = os.path.join(os.path.dirname(__file__), results_dir, "pos_win.txt")
    draw_path = os.path.join(os.path.dirname(__file__), results_dir, "draw.txt")
    
    test(your_input_options, pre_win_path, your_end_messages["pre_win"], short_mode=short_mode)
    test(your_input_options, pos_win_path, your_end_messages["pos_win"], short_mode=short_mode)
    test(your_input_options, draw_path, your_end_messages["draw"], short_mode=short_mode)
