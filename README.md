# Clinical Trial Sentiment Classifier API

🎯 This is a Flask-based API that classifies patient sentiment from messages to help improve retention in clinical trials.

Deployed & live at:
👉 [https://sentiment-api-5lot.onrender.com/classify](https://sentiment-api-5lot.onrender.com/classify)

---

## 📋 Endpoints

### `POST /classify`

**Request body (JSON):**
```json
{
  "message": "I’m struggling to keep up with my appointments."
}
{
  "result": "Sentiment: Negative (likely to drop out)\n\nExplanation: …"
}
