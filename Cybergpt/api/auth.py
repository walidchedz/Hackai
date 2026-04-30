USERS = {}

def handler(request):

    body = request.json()
    user_id = body.get("user_id")

    if user_id not in USERS:
        USERS[user_id] = {
            "plan": "free",
            "requests": 0
        }

    return {
        "statusCode": 200,
        "body": USERS[user_id]
    }
