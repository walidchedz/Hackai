from core.security import security_check
from core.devtools import dev_help

def process(text):

    t = text.lower()

    if "sql" in t or "xss" in t or "auth" in t:
        return security_check(t)

    if "code" in t or "error" in t or "api" in t:
        return dev_help(t)

    if "app idea" in t:
        return "📱 Idea: Build a password manager + vulnerability scanner"

    return f"🧠 Analysis: {text}"
