def security_scan(text):

    issues = []

    if "sql" in text:
        issues.append("Use ORM or prepared statements")

    if "xss" in text:
        issues.append("Sanitize input + escape output")

    if "auth" in text:
        issues.append("Use JWT + HTTPS + refresh tokens")

    if "password" in text:
        issues.append("Never store plain passwords (use bcrypt)")

    return "🔐 Security Report:\n- " + "\n- ".join(issues)
