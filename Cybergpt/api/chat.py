from core.engine import process
from api.auth import USERS

def handler(request):

    body = request.json()
    text = body.get("text","")
    user_id = body.get("user_id","guest")

    # إنشاء مستخدم
    if user_id not in USERS:
        USERS[user_id] = {"plan":"free","requests":0}

    user = USERS[user_id]

    # 🔥 limit للـ free
    if user["plan"] == "free" and user["requests"] >= 20:
        return {
            "statusCode": 403,
            "body": {"response":"Upgrade to Pro 🚀"}
        }

    user["requests"] += 1

    response = process(text)

    # 💎 تحسين Pro
    if user["plan"] == "pro":
        response += "\n\n💎 Pro Insight: Advanced analysis enabled"

    return {
        "statusCode": 200,
        "body": {"response": response}
    }
