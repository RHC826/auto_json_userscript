"""
    json -> csv
    GitBash の awk につなげる形で使う予定。
"""
import json
import sys


def main(lines) -> str:
    """
    json の値を順番に取り出す関数。
    """
    res: str = ""
    fields: str = json.loads(lines).keys()

    for enum, field in enumerate(iter(fields)):
        if enum <= 0:
            res += remove_commas_between_doublequotes(json.loads(lines)[field])
        else:
            res = esc_cat(
                res, remove_commas_between_doublequotes(json.loads(lines)[field])
            )

    return res


def esc_cat(str1: str, str2: str) -> str:
    """
    取り出した値をエスケープして連結する関数。
    """
    res = f'"{str1}","{str2}"'

    # '"' の重複を防ぐ
    res = res.replace('""', '"')
    return res


def remove_commas_between_doublequotes(string: str):
    """
    '"' に囲まれている "," を削除して awk や split で扱いやすくする。
    (?<=[^"]),(?=[^"]) では入れ子の json を破壊する可能性がある。
    """
    flg: bool = False
    res: str = ""
    for char in string:
        if char == '"' and flg is False:
            flg = True
        elif char == '"' and flg is True:
            flg = False

        if string.count('"') > 0:
            if char == "," and flg is False:
                char = "\\" + char
            elif char == "," and flg is True:
                continue
        elif char == "," and flg is False:
            continue

        res += char

    return res


if __name__ == "__main__":
    # BOM付きなのは powershell でよく使うため
    STDIN: str = open(sys.argv[1], encoding="utf_8_sig").read()
    RES = main(STDIN)

    print(RES)
