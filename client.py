import requests

def ask_bot(text):
    url = "https://ai-api-al6k.onrender.com/ask"
    payload = {"text": text}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    # Collect all text from 'appendText' events
    output = []
    if "responses" in data:
        for msg in data["responses"]:
            if msg.get("event") == "appendText" and "text" in msg:
                output.append(msg["text"])
    return "".join(output) if output else data