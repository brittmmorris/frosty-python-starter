# Frosty Python Starter

A minimal example app using the Frosty AI Python SDK to route prompts via `frosty.chat()`.

## 🔧 Setup

1. Clone the repo
    ```bash
    git clone https://github.com/brittmmorris/frosty-python-starter
    cd frosty-python-starter
    ```
2. Create a `.env` file from `.env.example`  
3. Create and activate a virtual environment:

```bash
   python3 -m venv venv
   source venv/bin/activate
```
4. Install dependencies:
```bash
   pip install -r requirements.txt
```

## 🚀  Run It
```bash
    python main.py
```


## 🧠 What It Does
- Uses the Frosty AI Python SDK to send a prompt to your router
- Automatically connects to your configured providers
- Supports routing logic like `cost`, `performance`, or fallback
- Handles retries, logging, and observability for you

## 💡 Example Output
```json
{
  "trace_id": "a37a5ae7-62ec-481e-89b7-2952b721b023",
  "total_tokens": 40,
  "prompt_type": "chat",
  "prompt_tokens": 11,
  "response_tokens": 29,
  "model": "claude-3-sonnet-20240229",
  "provider": "Anthropic",
  "total_time": 878.59,
  "prompt": [
    {
      "role": "user",
      "content": "Tell me a joke"
    }
  ],
  "cost": "- -",
  "rule": "cost",
  "response": "Here's a silly joke for you: Why can't a bicycle stand up by itself? It's two-tired!",
  "success": "True"
}
```
## 📎 Helpful Links
- 🔐 [Frosty Console](https://console.gofrosty.ai)
- 📚 [Frosty SDK Docs](https://docs.gofrosty.ai/frosty-ai-docs/python-sdk-guide)

