from http.server import BaseHTTPRequestHandler
import json
import requests
import base64

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        from urllib.parse import urlparse, parse_qs

        query = parse_qs(urlparse(self.path).query)
        image_url = query.get("url", [""])[0]

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        if not image_url:
            self.wfile.write(json.dumps({
                "status": False,
                "error": "No URL provided"
            }).encode())
            return

        try:
            res = requests.get(image_url, timeout=10)
            img = res.content

            base64_img = base64.b64encode(img).decode()

            self.wfile.write(json.dumps({
                "status": True,
                "remove_by": "Friend API",
                "image_base64": base64_img
            }).encode())

        except Exception as e:
            self.wfile.write(json.dumps({
                "status": False,
                "error": str(e)
            }).encode())            }).encode())

        except Exception as e:
            self.wfile.write(json.dumps({
                "status": False,
                "error": str(e)
            }).encode())
