📄 README.md (final version)

# Clinical Trial Sentiment Classifier API

🎯 This is a Flask-based API that classifies patient sentiment from messages to help improve retention in clinical trials.

Deployed & live at:  
➡️ [Click here to test the API](https://sentiment-api-5lot.onrender.com/classify)

---

## 📋 Endpoints

### `POST /classify`

---

## 📋 Request Body

When calling the `/classify` endpoint, send a POST request with JSON like this:

```json
{
  "message": "I’m struggling to keep up with my appointments."
}
🧪 Example Response

When you POST the example message above, you’ll get a response like this:

{
  "result": "Sentiment: Negative (likely to drop out)\n\nExplanation: The message indicates that the patient is having difficulty maintaining their commitment to the clinical trial schedule. The use of the word \"struggling\" suggests a significant challenge, which could lead to the patient dropping out if the issue is not addressed."
}
🚀 Testing with curl

You can test this API from your terminal with:

curl -X POST https://sentiment-api-5lot.onrender.com/classify \
-H "Content-Type: application/json" \
-d '{"message":"I’m struggling to keep up with my appointments."}'
🌱 Environment Variables

On Render, set the following environment variable:

OPENAI_API_KEY — your OpenAI secret key
🧪 Health Check

This API only has the /classify endpoint, but you can optionally add a simple health check route in app.py to respond to /:

@app.route('/')
def home():
    return "OK", 200
👩‍💻 Author

Built with ❤️ by Mariam Succar 🚀
