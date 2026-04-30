def dev_help(text):

    if "error" in text:
        return "💻 Debug: check stack trace"

    if "api" in text:
        return "💻 API: use REST + rate limit + caching"

    if "code" in text:
        return "💻 Send code for analysis"

    return "💻 Developer advice applied"
