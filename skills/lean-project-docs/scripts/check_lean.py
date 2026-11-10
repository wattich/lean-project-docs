"""ตรวจเอกสาร agent ของ repo ตามกติกา lean-project-docs

ใช้: python scripts/check_lean.py <โฟลเดอร์ repo>
- นับบรรทัด CLAUDE.md (เตือนเกิน 80) และ docs/STATUS-NOW.md (เตือนเกิน 60)
- repo หลาย branch: ถ้ามี docs/status/ จะตรวจ docs/status/*.md ทุกไฟล์ (เกิน 60 เตือน ยกเว้น README.md)
  และไม่บังคับให้มี STATUS-NOW
- ตรวจว่ามี docs/decisions/
- หาคำที่ดูเหมือนความลับในไฟล์ที่ agent อ่านทุกครั้ง (แสดงแค่เลขบรรทัด ไม่แสดงค่า)
ออกด้วย 1 ถ้ามีข้อที่ต้องแก้
"""
import io
import os
import re
import sys

LIMITS = {"CLAUDE.md": 80, "docs/STATUS-NOW.md": 60}
SECRET = re.compile(
    r"(password|passwd|pwd|secret|token|api[_-]?key|connectionstring)\s*[:=]\s*\S{4,}"
    r"|\b(?:\d{1,3}\.){3}\d{1,3}\b"
    r"|-----BEGIN [A-Z ]*PRIVATE KEY-----",
    re.IGNORECASE,
)


def read_lines(path):
    with io.open(path, encoding="utf-8", errors="replace") as f:
        return f.read().splitlines()


def main(root):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    problems = 0
    targets = dict(LIMITS)
    status_dir = os.path.join(root, "docs", "status")
    multi = os.path.isdir(status_dir)
    if multi:
        names = sorted(n for n in os.listdir(status_dir) if n.endswith(".md"))
        for n in names:
            targets[f"docs/status/{n}"] = 80 if n == "README.md" else 60
        print(f"[ok] docs/status/ มี {len(names)} ไฟล์ (แบบหลาย branch)")
    for rel, limit in targets.items():
        path = os.path.join(root, rel)
        if not os.path.isfile(path):
            if multi and rel == "docs/STATUS-NOW.md":
                continue
            print(f"[ขาด] {rel}")
            problems += 1
            continue
        lines = read_lines(path)
        mark = "ok" if len(lines) <= limit else "ยาวเกิน"
        if mark != "ok":
            problems += 1
        print(f"[{mark}] {rel}: {len(lines)} บรรทัด (เพดาน {limit})")
        for no, line in enumerate(lines, 1):
            if SECRET.search(line):
                print(f"  [ตรวจ] {rel} บรรทัด {no} ดูเหมือนมีความลับหรือ IP ให้เปลี่ยนเป็นชื่อ env")
                problems += 1
    dec = os.path.join(root, "docs", "decisions")
    if os.path.isdir(dec):
        print(f"[ok] docs/decisions/ มี {len(os.listdir(dec))} ไฟล์")
    else:
        print("[ขาด] docs/decisions/")
        problems += 1
    print("ผ่าน" if problems == 0 else f"ต้องแก้ {problems} ข้อ")
    return 0 if problems == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
