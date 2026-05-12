import http.server
import socketserver

PORT = 5800
SITE_DIR = "/Users/shutaono/Library/CloudStorage/GoogleDrive-shu69films@gmail.com/マイドライブ/code_area/atmos_shop_site/tareyoshi-site"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=SITE_DIR, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
