
from fastapi import FastAPI, Request, Header, HTTPException
import json

app = FastAPI()

# ✅ التوكنات المسموح بيها مع ربطها بأرقام الحسابات
ALLOWED_TOKENS = {
    "9GbVc9z8nHV1rL3PHSwkDXXeAH2Ikelr6a8UORcvWLD5okS8Ir": "343871",
    "odQHJGjyOUToclzb2DRQi3rrzH3E8Fr04o46ecaJvVSU4H11UT": "527235",
    "9eJ8zEQxvmUSGSPFrtG9kgyuejL7aMQJE6WWZnRW28TzijQw7h": "738202"
}

@app.post("/foodics/webhook")
async def receive_order(request: Request, authorization: str = Header(None)):
    if authorization is None or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized")

    token = authorization.split(" ")[1]
    account = ALLOWED_TOKENS.get(token)

    if not account:
        raise HTTPException(status_code=401, detail="Unauthorized")

    data = await request.json()
    print(f"✅ Order from Account {account}")
    print(json.dumps(data, indent=2))

    return {"status": "received", "account": account}
