import http.server
import socketserver

# 设置服务器的IP地址和端口
IP = '0.0.0.0'  # 监听所有可用的网络接口
PORT = 9000

# 创建HTTP服务器
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((IP, PORT), handler) as httpd:
    print(f"Serving at {IP}:{PORT}")
    httpd.serve_forever()
