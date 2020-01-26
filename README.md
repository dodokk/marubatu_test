# ○×ゲーム テストコード

### ディレクトリ構成

```
C:.
├─README.md
├─requirements.txt
├─test.py    // テストコード
├─your_src.py    // 実際にテストしたいファイル
│
├─based_programs
│  ├─make_ans_list.py    // 正解リストを作るファイル
│  └─marubatu_sample.py    // このファイルの実行結果をもとに正解ファイルを作成
│
└─results    // それぞれの勝ち、引き分けになる入力が全パターン記録されてる
   ├─draw.txt
   ├─pos_win.txt
   └─pre_win.txt
```


## 環境構築

1. リポジトリをクローンする
    ```bash
    git clone https://github.com/dodokk/marubatu_test.git
    ```
1. ディレクトリを移動する
    ```bash
    cd marubatu_test
    ```
1. 依存関係をインストールする(隔離環境下で行うことを推奨)
    ```bash
    pip install -r requirements.txt
    ```

## 使い方

1. your_src.pyをテストしたい自作ファイルに置き換える
1. test.pyのコメントを見ながらimportなどを自作関数に置き換える
1. 以下のコマンドで実行する
    ```bash
    python test.py
    ```
1. `testcase NG`と表示されなければOK
