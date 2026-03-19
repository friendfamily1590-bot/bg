from flask import Flask, request, jsonify
import requests
import base64

app = Flask(__name__)

@app.route("/", methods=["GET"])
def handler():
    image_url = request.args.get("url")

    if not image_url:
        return jsonify({
            "status": False,
            "error": "No URL provided"
        })

    try:
        res = requests.get(image_url, timeout=10)

        if res.status_code != 200:
            return jsonify({
                "status": False,
                "error": "Failed to fetch image"
            })

        img = res.content
        base64_img = base64.b64encode(img).decode()

        return jsonify({
            "status": True,
            "remove_by": "Friend API",
            "image_base64": base64_img
        })

    except Exception as e:
        return jsonify({
            "status": False,
            "error": str(e)
        })            "status": False,
            "error": str(e)
        })            self.wfile.write(json.dumps({
                "status": False,
                "error": str(e)
            }).encode())            }).encode())

        except Exception as e:
            self.wfile.write(json.dumps({
                "status": False,
                "error": str(e)
            }).encode())
