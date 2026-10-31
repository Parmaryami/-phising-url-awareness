"""EWB Phishing URL Awareness Checker.

Reads URL text and reports selected warning signs.
It never opens a URL and never sends data anywhere.
"""
import re
from urllib.parse import urlparse

# Improvement D: a plain-words reason for each warning.
REASONS = {
    "Contains an @ symbol; inspect carefully.":
        "The browser ignores the text before @, so the link can look like one site but go to another.",
    "Unusually long URL (over 100 characters).":
        "Long links can hide the real destination far to the right.",
    "Uses an IP address instead of a familiar domain.":
        "Honest services normally use readable names; a bare number hides who owns the site.",
    "Contains many hostname segments/subdomains.":
        "Stacking many names (a.b.c.d.e) can make a link look official.",
    "Contains a punycode-style hostname.":
        "xn-- can hide look-alike foreign letters that mimic a real name.",
    "Uses HTTP. HTTPS alone does not prove trust.":
        "HTTP is not encrypted, so data can be seen on the way.",
}

# Messages that are information, not real warnings.
INFO_MESSAGES = (
    "No URL entered",
    "Could not identify",
    "This text is not a valid URL",
    "No listed warning",
)


def inspect_url(raw_url):
    """Check visible URL text for selected warning signs."""
    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    # Improvement C: malformed input must never crash the program.
    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["This text is not a valid URL format."]

    if not host:
        return ["Could not identify a hostname."]

    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")

    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")

    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")

    if not findings:
        findings.append("No listed warning signs found. This does NOT prove safety.")

    return findings


def has_warnings(findings):
    """True if the findings contain real warnings (not just info messages)."""
    return not findings[0].startswith(INFO_MESSAGES)


def main():
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - this program does not open URLs.")

    # Improvement A: loop until the user quits.
    while True:
        raw_url = input("\nEnter a sample URL (or type q to quit): ")
        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye! Stay alert online.")
            break

        findings = inspect_url(raw_url)
        print("\nResult:")
        for item in findings:
            print("- " + item)
            # Improvement D: show why it matters.
            if item in REASONS:
                print("    Why: " + REASONS[item])

        # Improvement B: clear summary when real warnings exist.
        if has_warnings(findings):
            print("\nREVIEW CAREFULLY: " + str(len(findings)) + " warning sign(s) found.")

        print("Never enter passwords from unexpected links.")


if __name__ == "__main__":
    main()
