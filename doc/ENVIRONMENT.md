# 開発環境
## IPアドレス
| ホスト名 | eth0 | wlan0 | 役割 |
|--|--|--|--|
| rpi-kag2      | 192.168.200.195 | DHCP(自宅と兼用なので固定しない) |開発用|
| rpi-kag3      | 192.168.200.196 | 192.168.12.11 |実行用|
| WZR-HP-AG300H | 192.168.200.60  | 192.168.12.1  | 192.168.200.60:22->192.168.12.11:22 |

## 注意事項
- dhcpcd.conf に静的IPを記述しても有効にならない事象があった。  
  IPが被っているのが原因であった
- ポートフォワーディングにてルータ経由でssh接続も可能であるが、それはeth0ダウン時のみである。  

#
