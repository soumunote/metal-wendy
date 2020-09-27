## インストール
```sh
apt -y update
apt -y install python3 python3-pip
pip3 install fastapi uvicorn aiofiles jinja2
```

## 起動
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
