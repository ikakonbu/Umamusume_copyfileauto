# Umamusume_copyfileauto
## 説明
ウマ娘60fps化スクリプト(https://github.com/GEEKiDoS/umamusume-localify) 用補助アプリです。

アップデート時にファイルが消されるのでこちらのツールでもう一回追加し直します

## 要件
**Windows10だったらたぶん動きます。**

## ダウンロード
ページ右側の"Release"をクリックして、一番新しそうな'Umafile****.zip'をダウンロード

あとは好きな場所で展開してあげてください

## 起動前設定
利用する前にウマ娘の格納ディレクトリの設定を書き込む必要があります。

config.iniを開き、自分のゲーム格納ディレクトリに書き換えてください。

~~~
[Dir]

copydir = C:/Users/gamem/Downloads/Umamusume←ここ！！

target = config.json

[setting]
title = ウマ娘60fps化するやつ
msg = ファイルが消えていたので置き換えたよ
nomsg = 特に消えてなかったからなにもしてないよ
~~~

なお、ディレクトリは次の方法で確認できます。

![説明1](https://github.com/ishida-shunya/Umamusume_copyfileauto/blob/images/image3.png)　　![説明2](https://github.com/ishida-shunya/Umamusume_copyfileauto/blob/images/image2.png)

- DMM GAME Playerを起動
- Myゲームをクリック
- ウマ娘にカーソルを合わせ、左上をクリック
- ダウンロード先フォルダを表示　をクリックしてどこにあるか確認

# 注意事項
すでに60fps化スクリプトも同梱済みです。　そのままご利用いただけます。
なお、最新版のスクリプトが組み込まれない場合もあります。必要に応じて最新バージョンへ手動で更新してください。

常駐するのは面倒なのでクリック時のみファイルの存在を検知しています。アップデート時はアップデート後に再度実行しないとたぶん正しく動きません。そういうスクリプトなんで
