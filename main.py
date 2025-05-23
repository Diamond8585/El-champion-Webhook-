from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("✅ Received alert:", data)

    message = data.get("message", "")

    if "signum:BUY" in message:
        print("🟢 Buy signal received!")
        # TODO: Add order execution code here

    elif "signum:SELL" in message:
        print("🔴 Sell signal received!")
        # TODO: Add order execution code here

    return {"status": "ok"}, 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
