import json

def handler(event):
    print("✅ Received Webhook Event")
    print(json.dumps(event, indent=2))
