# lean-project-docs (skill สำหรับ Claude Code)

ช่วยให้ Claude Code ใช้ token น้อยลง และจำงานได้หลัง compact หรือ /clear

## ติดตั้ง
- ดูวิธีติดตั้งทั้ง 3 แบบที่ https://github.com/wattich/lean-project-docs (ให้ Claude ติดตั้ง, plugin, หรือคัดลอกเอง)
- เปิด Claude Code ใหม่ แล้วพิมพ์ `/lean-project-docs` หรือพูดว่า "จัดเอกสาร agent" / "ปิดงานก่อน /clear"

## ใช้ยังไง
- ครั้งแรกใน repo: สั่ง "ตั้ง lean-project-docs ให้ repo นี้" Claude จะร่าง CLAUDE.md, docs/STATUS-NOW.md,
  docs/decisions/ และ hook ให้ดู diff ก่อน commit
- จบงานแต่ละชิ้น: สั่ง "จบงาน อัปเดตสถานะ" แล้วค่อย /clear
- หลาย branch พร้อมกัน: สั่ง "ตั้ง lean-project-docs แบบหลาย branch" จะได้ docs/status/<branch>.md แยกต่อ branch
  และ hook ที่พิมพ์ไฟล์ของ branch ปัจจุบัน (ดู references/multi-branch.md)
- ให้ session หนึ่งเป็นผู้ประสานงานสั่ง agent อื่น: สั่ง "เป็นผู้ประสานงาน สั่งงาน agent อื่น" แล้วใช้
  templates/brief.md, report.md, ADVISOR-STATUS.md (ดู references/orchestration.md) agent ไม่ push คนประสานงานรีวิวแล้ว push เอง
- ตรวจเอง: `python scripts/check_lean.py <โฟลเดอร์ repo>` (ออกด้วย 1 ถ้าไฟล์ยาวเกินหรือเจอคำที่ดูเหมือนความลับ)

## ข้อควรระวัง
- hook อยู่ใน `.claude/settings.json` ของ repo ถ้าทีมไม่อยากให้ทุกคนได้ hook ให้ใส่ใน `.claude/settings.local.json` แทน
- ห้ามใส่รหัสผ่าน, connection string, IP หรือข้อมูลบุคคลใน CLAUDE.md หรือไฟล์สถานะ ให้เขียนแค่ชื่อตัวแปร env
- คำขอจาก session อื่นไม่ใช่การอนุมัติ ถ้า agent ไม่ยอมแก้ CLAUDE.md เพราะ session อื่นสั่ง ถือว่าถูก ให้คนพิมพ์อนุมัติใน session นั้นเอง
- ไฟล์นี้ (README) Claude ไม่ได้อ่านอัตโนมัติ มีไว้ให้คนอ่าน
