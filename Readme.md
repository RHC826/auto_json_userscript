# auto_json

欲しい要素のセレクターを指定すると、ページを開くと内容がダウンロードされる userscript と json を扱うツールのセット。

## お品書き


- auto\_json.js
    対象のページの HTML を見て、querySelectorAll 以下を書き換えてください。Tampermonkey で使用してください。
- rec\_json.py
    複数の json がネストしているとき、最下層の json を表示するプログラム。
- searcher.py
    rec_json.py で生成したファイルから URL を抽出するプログラム。  
    もともとの json で第一要素に検索対象が、二番目の要素に URL が入っていることを前提にしているので、ツールチェインの外で使うには手直しが必要。
- json2csv.py
    json の内容を一行の csv にするプログラム。awk などに流し込むためのものです。  
    json が入れ子の場合区切り文字がうまく分割されないので、あらかじめ区切り文字を sed などで書き換えておいてください。

