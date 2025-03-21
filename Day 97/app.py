from flask import Flask, request, redirect, jsonify, render_template, send_from_directory
import stripe

stripe.api_key = 'sk_test_51R4ZJnEoMIWuvDFypaQiXwHRQ2KWza88tObaNFOK3djUYR5OYVeWwARehOMDGuYevvt2MqiQqPJBvKGnkG1rzBBi00w4VI9jeS'

app = Flask(__name__, static_folder="public", template_folder="public")

YOUR_DOMAIN = "http://127.0.0.1:4242"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create-checkout-session", methods=["POST"])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price": "price_1R4ZiqEoMIWuvDFyorwH8rCv",  # Use your new price ID
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url=YOUR_DOMAIN + "/success.html",
            cancel_url=YOUR_DOMAIN + "/cancel.html",
        )
        return jsonify({"url": checkout_session.url})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory("public", filename)

if __name__ == "__main__":
    app.run(port=4242, debug=True)
