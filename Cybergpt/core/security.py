def security_check(text):

    if "sql" in text:
        return "🔐 SQL Injection → use prepared statements"

    if "xss" in text:
        return "🔐 XSS → sanitize inputs"

    if "auth" in text:
        return "🔐 Auth → JWT + HTTPS + refresh tokens"

    return "🔐 Security analysis done"
