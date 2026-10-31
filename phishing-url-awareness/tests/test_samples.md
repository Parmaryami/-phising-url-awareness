# Test Results

Python version used: 3.__ | Operating system: ________ | Date: ________

| # | Input | Expected result | Actual result | Pass/Fail |
|---|-------|-----------------|---------------|-----------|
| 1 | https://www.example.com/login | No listed warning signs | No listed warning signs found. This does NOT prove safety. | PASS |
| 2 | http://192.0.2.10/account | IP address + HTTP | Uses an IP address instead of a familiar domain. / Uses HTTP. HTTPS alone does not prove trust. | PASS |
| 3 | http://example.com@sample.invalid/login | @ symbol + HTTP | Contains an @ symbol; inspect carefully. / Uses HTTP. HTTPS alone does not prove trust. | PASS |
| 4 | https://a.b.c.d.e.example.invalid/path | Many hostname segments | Contains many hostname segments/subdomains. | PASS |
| 5 | https://xn--example.invalid/ | Punycode-style hostname | Contains a punycode-style hostname. | PASS |

## Bonus checks

| Input | Actual result |
|-------|---------------|
| (empty Enter) | No URL entered. |
| www.example.com | Uses HTTP. HTTPS alone does not prove trust. |
| https://secure-login.example.invalid | No listed warning signs found. This does NOT prove safety. |
| http://[bad | This text is not a valid URL format. (no crash, thanks to Improvement C) |

## Notes
i learned that a URL tool can only point out clues, not prove a like is safe. The test with secure-login .example.invalid showed no warnings even though the name looks suspicious. Typing http://[bad first crashed the basic version, so i added try/except to fix it.]