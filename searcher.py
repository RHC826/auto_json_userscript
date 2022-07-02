"""
    rec_json.py で生成したファイルから URL を抽出するプログラム。
    もともとの json で第一要素に検索対象が、二番目の要素に URL が入っていることを前提にしているので、ツールチェインの外で使うには手直しが必要。
"""
import re
import sys


def main(lines, pattern) -> list:
    """
    解析した内容を dict に固めて返す。
    """
    res: list = list()
    box: dict = dict()
    flg: bool = False

    for line in iter(lines):
        if flg is True:
            flg = False
            box["y"] = line.strip()

        if re.search(pattern, line):
            flg = True
            box["x"] = line.strip()

        if "y" in box:
            res.append(box)
            box = dict()

    return res


if __name__ == "__main__":
    # BOM付きなのは powershell でよく使うため
    STDIN: list = open(sys.argv[1], encoding="utf_8_sig").readlines()
    ARG: str = sys.argv[2] if len(sys.argv) > 2 else ""
    RES = main(STDIN, ARG)

    for DICT in RES:
        for key in DICT.keys():
            FORMATTED = (DICT[key].split(": ")[1]).replace(",", "")
            print(FORMATTED.replace('"', ""))
