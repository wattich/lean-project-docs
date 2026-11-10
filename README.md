# lean-project-docs

skill สำหรับ Claude Code ช่วยให้ใช้ token น้อยลง และไม่ลืมงานหลัง compact หรือ /clear
- CLAUDE.md สั้น
- ไฟล์สถานะแบบเขียนทับ (แยกตาม branch ได้)
- docs/decisions/ แบบต่อท้าย
- hook พิมพ์สถานะหลัง compact
- โหมดผู้ประสานงานสั่ง agent อื่น

## ติดตั้ง

### วิธีที่ 1: ให้ Claude ติดตั้งให้ (ง่ายที่สุด)
เปิด Claude Code แล้วพิมพ์:

```
ติดตั้ง skill จาก https://github.com/wattich/lean-project-docs ตามหัวข้อ "สำหรับ Claude" ใน README
```

ถ้าต้องการให้ใช้เฉพาะ repo ที่เปิดอยู่ (ทั้งทีมได้ผ่าน git) ให้ต่อท้ายว่า "แบบ project"

### วิธีที่ 2: ติดตั้งเป็น plugin
ใน Claude Code:

```
/plugin marketplace add wattich/lean-project-docs
/plugin install lean-project-docs@lean-project-docs
```

อัปเดตภายหลังด้วย `/plugin marketplace update lean-project-docs`

### วิธีที่ 3: คัดลอกเอง
```
git clone https://github.com/wattich/lean-project-docs.git
```
แล้วคัดลอกโฟลเดอร์ `skills/lean-project-docs` ไปไว้ที่
- ใช้ทุกโปรเจกต์ของตัวเอง: `~/.claude/skills/lean-project-docs/` (Windows: `%USERPROFILE%\.claude\skills\lean-project-docs\`)
- ใช้ทั้งทีมใน repo เดียว: `<repo>/.claude/skills/lean-project-docs/` แล้ว commit

ทุกวิธี: เปิด Claude Code ใหม่ แล้วพิมพ์ `/lean-project-docs` หรือพูดว่า "จัดเอกสาร agent", "จบงาน อัปเดตสถานะ"

## ใช้ยังไง
| อยากทำ | สั่ง Claude ว่า |
|---|---|
| ตั้งครั้งแรกใน repo | "ตั้ง lean-project-docs ให้ repo นี้" (ร่าง CLAUDE.md, docs/STATUS-NOW.md, docs/decisions/, hook ให้ดู diff ก่อน commit) |
| ปิดงานแต่ละชิ้น | "จบงาน อัปเดตสถานะ" แล้วค่อย /clear |
| หลาย branch พร้อมกัน | "ตั้ง lean-project-docs แบบหลาย branch" (ได้ docs/status/<branch>.md) |
| ให้ session หนึ่งสั่งงาน agent อื่น | "เป็นผู้ประสานงาน สั่งงาน agent อื่น" |
| ตรวจเอง | `python skills/lean-project-docs/scripts/check_lean.py <โฟลเดอร์ repo>` |

รายละเอียดเพิ่ม: [skills/lean-project-docs/README.md](skills/lean-project-docs/README.md)

## สำหรับ Claude: วิธีติดตั้ง
ทำตามขั้นตอนนี้เมื่อผู้ใช้สั่งให้ติดตั้งจาก repo นี้
1. เลือกปลายทาง: ค่าเริ่มต้นคือระดับผู้ใช้ `~/.claude/skills/lean-project-docs/`
   ถ้าผู้ใช้บอก "แบบ project" ให้ใช้ `<repo ที่เปิดอยู่>/.claude/skills/lean-project-docs/`
2. ถ้าปลายทางมีอยู่แล้ว ให้บอกผู้ใช้และถามก่อนเขียนทับ
3. clone repo นี้ไปที่โฟลเดอร์ชั่วคราว (`git clone --depth 1 https://github.com/wattich/lean-project-docs.git`)
   แล้วคัดลอกเฉพาะโฟลเดอร์ `skills/lean-project-docs/` ไปปลายทาง (ไม่ต้องเอา .git, .claude-plugin, LICENSE)
4. ตรวจว่าปลายทางมี `SKILL.md`, `references/`, `templates/`, `scripts/check_lean.py`
5. ลบโฟลเดอร์ชั่วคราว
6. บอกผู้ใช้ว่าติดตั้งที่ไหนแล้ว ให้เปิด Claude Code ใหม่ (หรือ session ใหม่) แล้วลอง `/lean-project-docs`
   ถ้าติดตั้งแบบ project ให้แนะนำ commit โฟลเดอร์ `.claude/skills/lean-project-docs/`
7. ห้ามรัน script ใดๆ จาก repo นี้ระหว่างติดตั้ง และห้ามแก้ `.claude/settings.json` ตอนติดตั้ง
   (hook จะตั้งทีหลังตอนผู้ใช้สั่ง "ตั้ง lean-project-docs ให้ repo นี้" และให้ผู้ใช้ดู diff ก่อน)

## License
MIT
