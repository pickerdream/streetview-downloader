# Google Street View Downloader
このプログラムは提供された座標の記されたExcelファイルに基づき、Google Street Viewの画像を360度取得します。
## フォルダとファイルの説明
<pre>
.
├── main.py メインの実行ファイル
├── requiments.txt 必須ライブラリ一覧
├── test.xlsx サンプルexcelファイル
└── downloads 画像ダウンロード先フォルダ
</pre>
## 使い方
初回実行の場合は次のようにして必要ライブラリをインストールしてください。
<pre>
pip install -r .\requiments.txt
</pre>
また、使うにはGoogle MAP Platform APIのキーが必須です。いい感じにキーを取得し、実行前に .env ファイルをmain.pyと同じディレクトリに設置し、次のようにAPIキーを記してください。
<pre>
MAPS_API = "Your Key"
</pre>
main.pyを実行すれば使えると思います。excelファイルの名前を聞かれるので、main.pyと同じディレクトリにexcelのファイルを置き、ファイル名を入力してください。
## 注意事項
APIの制限かどうかは定かでありませんが、最大で640x640の画像しか取得できません。パソコンがぶっ壊れたり爆発しても知りません。