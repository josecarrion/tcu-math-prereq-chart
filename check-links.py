#!/usr/bin/env python3
"""Check the catalog links in prereq-graph.gv. Run it after each Coursedog
catalog update, which tends to change the course page IDs.

Usage: python3 -I check-links.py [prereq-graph.gv]

Each page must load (a dead ID gives 404) and its <title> must name the same
course (catches an ID that now points at another course). Exits 1 on any failure.
"""
import re
import sys
import urllib.error
import urllib.request

path = sys.argv[1] if len(sys.argv) > 1 else "prereq-graph.gv"
node = re.compile(r'^\s*\w+\s*\[label=<<FONT[^>]*>([A-Z]{4}) (\d{5})</FONT>.*?URL="([^"]+)"')
courses = [m.groups() for line in open(path) if (m := node.match(line))]
bad = 0
for dept, num, url in courses:
    code = f"{dept}{num}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "prereq-chart link check"})
        with urllib.request.urlopen(req, timeout=30) as r:  # pages are ~4 MB; read the head only
            head = r.read(8192).decode("utf-8", "replace")
        m = re.search(r"<title>([^<]*)</title>", head)
        title = m.group(1) if m else ""
        if code in title.replace(" ", ""):
            status = "ok"
        else:
            status = f"WRONG COURSE (page title: {title or 'none'})"
    except urllib.error.HTTPError as e:
        status = f"BROKEN (HTTP {e.code})"
    except Exception as e:  # network trouble, timeouts
        status = f"ERROR ({e})"
    if status != "ok":
        bad += 1
    print(f"{dept} {num}  {status}  {url}")
print(f"\n{len(courses) - bad} of {len(courses)} links ok")
sys.exit(1 if bad else 0)
