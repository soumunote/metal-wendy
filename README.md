# metal-wendy
Wendyの協力のもと、以下の目標を追求する  
- 技術力の維持及び探究  
  * 維持 ... 持っている技術をWendyに伝える事で、机上の技術としない  
  * 探究 ... Wendyが隠し持っている可能性を探し求める  
- およそ想像できない事を創造する  
- SIer ... 何それ？  

## 概要(当面の目標)
- 各種アクションの実装
  * 耳を動かす ... GPIO経由
  * 走る ... GPIO経由
- ~~GPIO 制御のみ pigpiod をホストOSで実行し、アプリ的な部分は、dockerを使用する~~  
- ~~docker 使用の目的は、単に Dockerfile == 「インストールマニュアル」とするためである~~  
  ∴ 将来的には、別な手法に切り替えることもある  
- RaspberryPI OS の docker container は、--privilege を付加しないと、時刻同期されない  
  そのため、docker build 時に(--privilegeを付加できない関係上) Dockerfile で apt が失敗する  
  これでは、Dockerを使用する当初の目的に逸れてしまうので、Docker は使用しない。  
- 今現在、metal-wendy には gpio 経由のハード制御機能しかない。  
  今後、機能追加するつもりなので、gpio 制御は、io-api サブプロジェクトにまとめる。  
  インストールも各サブプロジェクト毎に行う。
- 仕事ではないので、いろいろな事を難しく決めない
  * でも、やり直しが発生すると無駄なので、きちんと設計しましょう(可能なら)
  * でも、協力者も困るので、きちんと設計しましょう(可能なら)

## インストール
- ユーザ pi にて github よりプロジェクト全体をダウンロードする
1. git
  ```bash
  cd 
  git clone https://github.com/soumunote/metal-wendy.git
  ```
2. 各サブジェクトフォルダの情報に従う  

## 文書一覧
｜名称|内容|
|--|--|
|ENVIRONMENT.md|開発実行環境|
|HARDWARE.md|電子的な結線図|
|APPLICATION.md|アプリケーションの内容|

---

## GPIOツール
- pinout  
  [Gpiozero Command Line Tool](https://gpiozero.readthedocs.io/en/stable/cli_tools.html?highlight=pinout#pinout)  
  [Installing GPIO Zero](https://gpiozero.readthedocs.io/en/stable/installing.html)  
  ```sh
  sudo apt install python3-gpiozero
  ```
  (Python3でないとダメだった。)

- Wiring Pi  
  [Wiring Pi](http://wiringpi.com/download-and-install/)  

