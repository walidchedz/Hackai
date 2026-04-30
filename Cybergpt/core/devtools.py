def dev_assist(text):

    if "error" in text:
        return "💻 Debug: check stack trace + dependencies"

    if "api" in text:
        return "💻 API: use REST + versioning + rate limiting"

    if "backend" in text:
        return "💻 Backend: modular architecture (services + controllers)"

    return "💻 Developer advice generated"
