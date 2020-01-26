import itertools
import sys, os
from tqdm import tqdm
from io import StringIO
from unittest import mock

from marubatu_sample import marubatu_game


if __name__ == "__main__":
    input_options = (
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
    end_sentences = {
        "pre_win": "user0の勝ち",
        "pos_win": "user1の勝ち",
        "draw": "引き分けです"
    }

    input_lines = list(itertools.permutations(input_options))

    pre_win_patterns = set()
    pos_win_patterns = set()
    draw_patterns = set()
    
    for input_line in tqdm(input_lines):
        io = StringIO()
        sys.stdout = io
        
        with mock.patch("builtins.input", side_effect=input_line) as m:
            operations = marubatu_game()
        
        sys.stdout = sys.__stdout__

        outputs = io.getvalue().split("\n")

        if end_sentences["pre_win"] in outputs:
            pre_win_patterns.add(" ".join(operations))
        elif end_sentences["pos_win"] in outputs:
            pos_win_patterns.add(" ".join(operations))
        else:
            draw_patterns.add(" ".join(operations))

    results_dir = "../results"
    pre_win_path = os.path.join(os.path.dirname(__file__), results_dir, "pre_win.txt")
    pos_win_path = os.path.join(os.path.dirname(__file__), results_dir, "pos_win.txt")
    draw_path = os.path.join(os.path.dirname(__file__), results_dir, "draw.txt")

    with open(pre_win_path, "w") as f:
        f.writelines( "\n".join(pre_win_patterns) )
    with open(pos_win_path, "w") as f:
        f.writelines( "\n".join(pos_win_patterns) )
    with open(draw_path, "w") as f:
        f.writelines( "\n".join(draw_patterns) )

