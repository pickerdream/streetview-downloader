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
main.pyを実行すれば使えると思います。サンプルのように実行してみてください。
<pre>
python main.py --excel test.xlsx --type 0
</pre>
## 引数について
以下の通りです。
| 引数名  | 意味 |
| ------------- | ------------- |
| --excel  | 座標が記されているExcelファイルの名前を指定します。 （必須） |
| --type  | ファイルの出力方法を指定します。  |
### --type の説明
downloadsフォルダにどのように出力されるかを指定することができます。
#### --type 0
標準のファイル出力方法です。downloadsフォルダにそれぞれの座標のフォルダが作られ、画像が出力されます。同じ座標でtype 0を実行後にtype 1を実行するとLOCATIONごとのファイルツリーが削除される仕様に気を付けてください。
<pre>
.
└── downloads
    └── location
        ├── 0
        │   ├── gvs_0.png
        │   └── metadata.json
        ├── 90
        │   ├── gvs_0.png
        │   └── metadata.json
        ├── 180
        │   ├── gvs_0.png
        │   └── metadata.json
        └── 270
            ├── gvs_0.png
            └── metadata.json
</pre>
#### --type 1
オプションのファイル出力方法です。downloadsフォルダに画像が直下で出力されます。ファイルの名前は次のようになります。
<pre>
location-north.jpg
location-east.jpg
location-south.jpg
location-west.jpg
</pre>
## 注意事項
APIの制限かどうかは定かでありませんが、最大で640x640の画像しか取得できません。パソコンがぶっ壊れたり爆発しても知りません。