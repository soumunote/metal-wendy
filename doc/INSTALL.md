# インストール
## 概要
環境構築を容易にするためにdockerを用いる  
以下の設定だけは、ホスト環境に対して行う　　



## インストール手順
### I. docker deamon のインストール
参考)
[Install Docker Engine on Debian / install using the convenience script](https://docs.docker.com/engine/install/debian/#install-using-the-convenience-script)
1. とりあえず消す  
   `$ sudo apt-get remove docker docker-engine docker.io containerd runc`

2. インストール
   パッケージから or スクリプトから を選べるが、後者を選択
   ```
   $ curl -fsSL https://get.docker.com -o get-docker.sh
   $ sudo sh get-docker.sh
   $ sudo usermod -aG docker pi
   ```
3. アンインストール
   やってないけど
   ```
   $ sudo apt-get purge docker-ce docker-ce-cli containerd.io
   $ sudo rm -rf /var/lib/docker
   $ sudo rm -rf /var/lib/containerd
   ```
### II. 