"""
    日本語 json リーダー
    複数の json がネストしているとき、最下層の json を表示するプログラム。
     $ dir *.json | Sort-Object | % {python rec_json $_} を想定している。
    テストには手元の2段ネストの json ファイルを使った。
"""
import json
import re
import sys


def main(lines, pattern) -> None:
    """
    複数の json がネストしているとき、最下層の json を表示するプログラム。
     $ dir *.json | Sort-Object | % {python rec_json $_} を想定している。
     """
    flg: bool = False
    flg_nest: bool = False
    nest_list: list = list()

    for line in iter(lines):
        for key in json.loads(line).keys():
            if re.search(pattern, json.loads(line)[key]):
                flg = True

            if is_json(json.loads(line)[key]) is True:
                nest_list.append(json.loads(line)[key])
                flg_nest = True

        if flg is True and flg_nest is False:
            print(json.dumps(json.loads(line.strip()), indent=4, ensure_ascii=False))
            flg = False

    if flg_nest is True:
            main(nest_list, pattern)
    else:
        pass


def is_json(into: list) -> bool:
    try:
        json.dumps(json.loads(into.strip()), indent=4, ensure_ascii=False)
        return True
    except:
        return False


if __name__ == "__main__":
    # BOM付きなのは powershell でよく使うため
    lines: list = open(sys.argv[1], encoding="utf_8_sig").readlines()
    pattern: str = sys.argv[2] if len(sys.argv) > 2 else ""
    main(lines, pattern)
