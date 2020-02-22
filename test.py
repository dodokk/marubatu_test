import itertools
import sys, os
import random
from tqdm import tqdm
from io import StringIO
from unittest import mock, TestCase, main

import your_file      # please edit here!


class Testcase(TestCase):
    def test_preWinTest(self):
        pre_win_path = os.path.join(results_dir, "pre_win.txt")
        pre_win_inputs = getInputLine(your_input_options, pre_win_path, short_mode=short_mode)
        result = test(your_func, pre_win_inputs, your_end_messages["pre_win"])
        self.assertEqual(result, True)

    def test_posWinTest(self):
        pos_win_path = os.path.join(results_dir, "pos_win.txt")
        pos_win_inputs = getInputLine(your_input_options, pos_win_path, short_mode=short_mode)
        result = test(your_func, pos_win_inputs, your_end_messages["pos_win"])
        self.assertEqual(result, True)

    def test_drawTest(self):
        draw_path = os.path.join(results_dir, "draw.txt")
        draw_inputs = getInputLine(your_input_options, draw_path, short_mode=short_mode)
        result = test(your_func, draw_inputs, your_end_messages["draw"])
        self.assertEqual(result, True)


def test(your_func: 'function', input_lines: list, expected_message: str) -> bool:
    for input_line in tqdm(input_lines):
        io = StringIO()
        sys.stdout = io
        
        with mock.patch("builtins.input", side_effect=input_line):
            your_func()
        
        sys.stdout = sys.__stdout__

        outputs = io.getvalue().split("\n")

        if not(expected_message in outputs):
            return False

    return True


def getInputLine(your_input_options: list, input_filepath: str, *, short_mode=False) -> list:
    original_options = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
    operation_dist = dict(zip(original_options, your_input_options))

    with open(input_filepath, "r") as f:
        lines = list(map(lambda x: list(map(lambda x: operation_dist[x], x.split())), f.read().split("\n")))
    
    if short_mode:
        lines = random.sample(lines, 1000)

    return lines


if __name__ == "__main__":
    results_dir = os.path.join(os.path.dirname(__file__), "./results")

    your_input_options = (      # 入力の方法
        "1",    # 上段の左列
        "2",    # 上段の中列
        "3",    # 上段の右列
        "4",    # 中段の左列
        "5",    # 中段の中列
        "6",    # 中段の右列
        "7",    # 下段の左列
        "8",    # 下段の中列
        "9",    # 下段の右列
    )

    your_end_messages = {       # ゲーム終了メッセージ
        "pre_win": "user0の勝ち",   # 先行のプレイヤーが勝った場合
        "pos_win": "user1の勝ち",   # 後攻のプレイヤーが勝った場合
        "draw": "引き分けです"   # 引き分けの場合
    }
    
    # 'your_func = (ファイル名).(関数名)' の形にする
    # 'your_func = your_file.marubatu()' にはしない
    your_func = your_file.marubatu

    # True -> ランダムに1000ケースずつ選ぶ
    # False -> 全ケース
    short_mode = True

    main()
