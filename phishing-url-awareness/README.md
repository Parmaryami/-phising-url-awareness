# EWB Phishing URL Awareness Checker

## Overview
Phishing is a trick where a fake link or message tries to make people share passwords, card numbers or OTPs. This command-line tool reads a URL as plain text and points out a few visible warning signs. It never opens the link.

## Features
- Detects an @ symbol in the URL
- Flags unusually long URLs (over 100 characters)
- Flags IP-address hostnames
- Flags many hostname segments (5 or more)
- Flags punycode-style hostnames (xn--)
- Flags the HTTP scheme
- Loop mode: check many URLs without restarting; type `q` to quit
- "REVIEW CAREFULLY" summary with the number of warnings found
- Handles malformed input (e.g. `http://[bad`) without crashing
- Plain-words reason printed under every warning

## Requirements
Python 3.10 or later. No extra packages.

## How to Run
Windows: `python phishing_checker.py`
Mac/Linux: `python3 phishing_checker.py`

Optional automatic test check: `python run_tests.py` (or `python3 run_tests.py`)

## Example Output
```
EWB Phishing URL Awareness Checker
Text checks only - this program does not open URLs.

Enter a sample URL (or type q to quit): http://192.0.2.10/account

Result:
- Uses an IP address instead of a familiar domain.
    Why: Honest services normally use readable names; a bare number hides who owns the site.
- Uses HTTP. HTTPS alone does not prove trust.
    Why: HTTP is not encrypted, so data can be seen on the way.

REVIEW CAREFULLY: 2 warning sign(s) found.
Never enter passwords from unexpected links.
```

## Testing
| # | Input | Expected | Actual | Result |
|---|-------|----------|--------|--------|
| 1 | https://www.example.com/login | No warning signs | No listed warning signs found | PASS |
| 2 | http://192.0.2.10/account | IP address + HTTP | IP address + HTTP warnings | PASS |
| 3 | http://example.com@sample.invalid/login | @ symbol + HTTP | @ symbol + HTTP warnings | PASS |
| 4 | https://a.b.c.d.e.example.invalid/path | Many hostname segments | Many hostname segments warning | PASS |
| 5 | https://xn--example.invalid/ | Punycode-style hostname | Punycode warning | PASS |

Full table: `tests/test_samples.md`

## Screenshots
![Sample run](screenshots/sample_run.png)
![Test results](screenshots/test_results.png)

## Improvements
1. **Loop with quit** - the program now keeps asking for URLs until `q` is typed, so each check does not need a restart. Tested by entering several URLs in one run.
2. **Review carefully summary** - a helper function separates real warnings from information messages and prints the warning count. Tested with URLs that have 0, 1 and 2 warnings.
3. **Malformed input handling** - `urlparse` is wrapped in `try/except ValueError`, so `http://[bad` prints a friendly message instead of crashing. Tested by typing that input.
4. **Explanations** - a dictionary maps each warning to a one-line reason. Re-ran all five tests to confirm results did not change.

## Limitations
This is an educational tool. It only reads URL text. It does not visit
URLs, scan for malware or prove that a URL is safe. No warning signs
found does NOT mean a URL is safe.

## Ethical Use
Use sample strings only. Do not collect credentials. Do not use this
project to deceive anyone or to test websites without permission.

## Author
Yamini, IMSC im cyber security, EWB Courses
