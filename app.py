import os
import base64
import mimetypes

from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

MODEL = os.getenv("JARVIS_MODEL", "gpt-6-luna")

SYSTEM_PROMPT = """
You are J.A.R.V.I.S. (Jam Artificial Rare Virtual Intelligence System).

You are a friendly futuristic AI assistant.

Be helpful, intelligent and concise.
Explain school subjects in simple language when requested.
You can answer questions about science, mathematics, programming,
technology and general knowledge.

You can analyze images when an image is supplied.

Never claim that you control real-world devices unless they are
actually connected to this computer.
"""

def get_client():
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        return None
    return OpenAI(api_key=key)

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/api/chat")
def chat():
    client = get_client()
    if client is None:
        return jsonify({
            "error": "OPENAI_API_KEY is not set on the server."
        }), 500

    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()
    history = data.get("history") or []
    image_data = data.get("image")

    if not message and not image_data:
        return jsonify({"error": "Please enter a message or select an image."}), 400

    # Keep the browser-provided history small.
    clean_history = []
    for item in history[-16:]:
        role = item.get("role")
        content = item.get("content")
        if role in ("user", "assistant") and isinstance(content, str):
            clean_history.append({"role": role, "content": content[:8000]})

    api_input = [{"role": "developer", "content": SYSTEM_PROMPT}]
    api_input.extend(clean_history)

    if image_data:
        current_content = [
            {"type": "input_text", "text": message or "Please analyze this image."},
            {"type": "input_image", "image_url": image_data}
        ]
        api_input.append({"role": "user", "content": current_content})
    else:
        api_input.append({"role": "user", "content": message})

    try:
        response = client.responses.create(
            model=MODEL,
            input=api_input
        )
        return jsonify({"answer": response.output_text})
    except Exception as error:
        return jsonify({"error": f"J.A.R.V.I.S. ERROR: {error}"}), 500

if __name__ == "__main__":
    # 0.0.0.0 lets another device on the same Wi-Fi reach the app.
    app.run(host="0.0.0.0", port=5000, debug=False)
