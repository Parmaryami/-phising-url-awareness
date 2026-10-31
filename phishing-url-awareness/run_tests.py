"""Optional automatic check of the five workbook samples (text only, no network)."""
from phishing_checker import inspect_url

CASES = [
    ("https://www.example.com/login", ["No listed warning signs found. This does NOT prove safety."]),
    ("http://192.0.2.10/account", ["Uses an IP address instead of a familiar domain.", "Uses HTTP. HTTPS alone does not prove trust."]),
    ("http://example.com@sample.invalid/login", ["Contains an @ symbol; inspect carefully.", "Uses HTTP. HTTPS alone does not prove trust."]),
    ("https://a.b.c.d.e.example.invalid/path", ["Contains many hostname segments/subdomains."]),
    ("https://xn--example.invalid/", ["Contains a punycode-style hostname."]),
    ("", ["No URL entered."]),
    ("http://[bad", ["This text is not a valid URL format."]),
]

failed = 0
for url, expected in CASES:
    got = inspect_url(url)
    ok = got == expected
    failed += not ok
    print(("PASS" if ok else "FAIL"), "-", repr(url))
print("\nAll tests passed." if not failed else f"\n{failed} test(s) failed.")
