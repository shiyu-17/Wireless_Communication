import http.server
import socketserver
import time

class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # 处理根路径的GET请求
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            response = "Hello, World!"
            self.wfile.write(response.encode("utf-8"))

        elif self.path == '/video.mp4':
            # 处理视频文件路径的GET请求
            self.send_response(200)
            self.send_header('Content-type', 'application/octet-stream')
            self.end_headers()

            file_path = 'E:/video.mp4'  # 替换为要传输的文件路径
            with open(file_path, 'rb') as f:
                start_time = time.time()  # 记录传输开始时间
                self.wfile.write(f.read())  # 传输文件内容
                end_time = time.time()  # 记录传输结束时间
                transfer_time = end_time - start_time  # 计算传输所需时间
                file_size = f.tell()  # 获取文件大小
                transfer_speed = file_size / transfer_time / 1024  # 以KB/s为单位计算传输速率
                print(f"Transfer Speed: {transfer_speed:.2f} KB/s")  # 打印传输速率

server_address = ('', 9000)

httpd = socketserver.TCPServer(server_address, MyHTTPRequestHandler)

print('Starting server...')
httpd.serve_forever()