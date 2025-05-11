import base64
import json
from pathlib import Path

# Load your service account JSON
json_path = Path("/home/shiv-nlp-mldl-cv/Documents/EAGCode/Session8-Tool_ExtAPI_RAG/Telegram_RAG_Integration_Final/mcp/google/service_account.json")
if not json_path.exists():
    raise FileNotFoundError("service_account.json not found.")

# Read and encode
with open(json_path, "r") as f:
    content = f.read()
    encoded = base64.b64encode(content.encode()).decode()

# Write to .env file
env_path = Path(".env")
lines = []

# If .env already exists, preserve other settings
if env_path.exists():
    with open(env_path, "r") as f:
        lines = f.readlines()

# Replace or add CREDENTIALS_CONFIG
lines = [line for line in lines if not line.startswith("CREDENTIALS_CONFIG=")]
lines.append(f"CREDENTIALS_CONFIG={encoded}\n")

# Write back
with open(env_path, "w") as f:
    f.writelines(lines)

print("✅ .env file updated with CREDENTIALS_CONFIG.")
