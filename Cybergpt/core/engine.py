from core.security import security_scan
from core.dev import dev_assist
from core.apps import app_ideas

def engine(text, user):

    t = text.lower()

    # 🔐 Security mode
    if any(x in t for x in ["sql", "xss", "injection", "auth", "password"]):
        return security_scan(t)

    # 💻 Dev mode
    if any(x in t for x in ["code", "bug", "error", "api", "backend"]):
        return dev_assist(t)

    # 📱 App mode
    if "app" in t or "project" in t:
        return app_ideas()

    # 🧠 fallback intelligence
    return f"🧠 CyberForge AI:\n{text}"
