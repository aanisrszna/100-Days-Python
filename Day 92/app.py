from flask import Flask, request, render_template, jsonify
import numpy as np
from PIL import Image
import io
from collections import Counter

app = Flask(__name__)

def get_top_colors(image, num_colors=10):
    image = image.resize((150, 150))  # Resize to reduce processing time
    image = image.convert("RGB")  # Ensure it's in RGB format
    pixels = np.array(image).reshape(-1, 3)  # Flatten the image pixels

    # Count the most common colors
    color_counts = Counter(map(tuple, pixels))
    top_colors = color_counts.most_common(num_colors)

    # Convert to HEX
    hex_colors = ["#{:02x}{:02x}{:02x}".format(r, g, b) for (r, g, b), _ in top_colors]
    return hex_colors

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "image" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["image"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    try:
        image = Image.open(io.BytesIO(file.read()))
        colors = get_top_colors(image)
        return jsonify({"colors": colors})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
