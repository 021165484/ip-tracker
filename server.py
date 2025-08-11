from flask import Flask, request, redirect
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # 取得訪問者 IP
    ip = request.remote_addr

    # 如果是本地測試會變成 127.0.0.1，這裡可以用假的外部 IP 測試
    if ip == '127.0.0.1':
        ip = '8.8.8.8'  # Google 公共 DNS 當作範例

    # 查詢 IP 的地理位置
    res = requests.get(f"http://ip-api.com/json/{ip}")
    data = res.json()

    if data['status'] == 'success':
        lat = data['lat']
        lon = data['lon']
        # 轉跳到 Google 地圖
        return redirect(f"https://www.google.com/maps?q={lat},{lon}")
    else:
        return "無法取得位置"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
