from flask import Flask, request, jsonify
from openai import OpenAI
import os

# Initialize Flask and OpenAI client
app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/classify', methods=['POST'])
def classify():
    try:
        # Get patient message from POST request
        data = request.get_json()
        message = data.get('message')
        print(f"Received message: {message}")  # Log incoming message

        if not message:
            return jsonify({"error": "No message provided"}), 400

        # Define prompt
        system_msg = "You are a clinical trial retention assistant."
        user_msg = f"""
The following is a text message sent by a patient participating in a clinical trial. 
Classify the sentiment as one of: Positive (engaged), Neutral (at risk), or Negative (likely to drop out). 
Then briefly explain why you classified it that way.

Message: "{message}"
"""

        # Call GPT
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_msg}
            ],
            temperature=0
        )

        result = response.choices[0].message.content.strip()

        if "Explanation:" in result:
            sentiment_part, reason_part = result.split("Explanation:", 1)
            sentiment = sentiment_part.replace("Sentiment:", "").strip()
            reason = reason_part.strip()
        else:
            sentiment = "Unknown"
            reason = "Could not extract explanation."

        return jsonify({
            "sentiment": sentiment,
            "reason": reason
        })

    except Exception as e:
	import traceback
	traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(debug=True, host="0.0.0.0", port=port)
