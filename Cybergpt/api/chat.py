from core.engine import engine

USERS = {}

def handler(request):

    body = request.json()
    text = body.get("text","")
    user_id = body.get("user_id","guest")

    # 👤 user init
    if user_id not in USERS:
        USERS[user_id] = {"plan":"free","requests":0}

    user = USERS[user_id]

    # 💰 limit system
    if user["plan"] == "free" and user["requests"] >= 30:
        return {
            "statusCode": 403,
            "body": {"response":"Upgrade to Pro 🔥"}
        }

    user["requests"] += 1

    response = engine(text, user)

    # 💎 pro boost
    if user["plan"] == "pro":
        response += "\n\n💎 Pro: Advanced analysis enabled"

    return {
        "statusCode": 200,
        "body": {"response": response}
    }
