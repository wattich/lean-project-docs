# หลาย branch ทำพร้อมกัน (หลาย agent หลาย worktree)

ใช้เมื่อมีมากกว่าหนึ่ง branch ที่มีงานค้างพร้อมกัน ไฟล์ `docs/STATUS-NOW.md` ไฟล์เดียวจะชนกันตอน merge
และ agent ของ branch หนึ่งจะเห็นสถานะของอีก branch ที่ไม่เกี่ยวกับตัวเอง

## โครงไฟล์

| ไฟล์ | เขียนอย่างไร | อยู่ที่ไหน |
|---|---|---|
| `docs/status/<branch>.md` | **เขียนทับ** ไม่เกิน 60 บรรทัด | เฉพาะบน branch นั้น ชื่อไฟล์แทน `/` ด้วย `-` เช่น `feat/payroll` เป็น `feat-payroll.md` |
| `docs/status/README.md` | แก้เมื่อกติกาเปลี่ยน | ทุก branch (มาจาก main) |
| `docs/decisions/<หัวข้อ>.md` | **ต่อท้าย** | ใช้ร่วมทุก branch |
| `CLAUDE.md` | แก้เมื่อกติกาเปลี่ยน | ทุก branch (มาจาก main) |

- แม่แบบไฟล์สถานะ: `templates/branch-status.md`
- hook: `templates/settings-hook-branch.json` พิมพ์ไฟล์สถานะของ branch ปัจจุบัน ถ้ายังไม่มีไฟล์จะบอกให้สร้าง
- branch ที่ merge แล้วและไม่มีงานต่อ ลบไฟล์สถานะของมันใน commit ที่ merge

## ตั้งค่าครั้งแรกใน repo ที่มีหลาย branch
1. ทำโหมด 1 ใน SKILL.md บน branch ใหม่ที่แตกจาก main (เช่น `docs/agent-docs`) แต่ใช้ `docs/status/` แทน STATUS-NOW
2. `CLAUDE.md` เป็น commit แยก ส่วน `docs/status/README.md` กับ `docs/decisions/` เป็นอีก commit จะได้ cherry-pick ทีละชิ้นได้
3. นำเข้า main ตามกติกาของทีม (MR หรือ merge)
4. **กระจายไป branch ที่ทำงานอยู่ด้วย cherry-pick** เฉพาะ branch ที่ตอนนั้นไม่มี agent ทำงานอยู่ branch ที่มี agent กำลังทำงาน รอให้ agent จบชิ้นงานก่อน แล้วค่อย cherry-pick ตอนเริ่มชิ้นถัดไป
5. แต่ละ branch สร้าง `docs/status/<branch>.md` ของตัวเองใน commit แรกหลัง cherry-pick

## กติกาตอนทำงาน
- **หนึ่ง agent ต่อหนึ่ง branch ต่อหนึ่ง worktree** (`git worktree add .worktrees/<ชื่อ> <branch>`) ห้ามสอง agent แก้ worktree เดียวกัน
- agent แก้ได้เฉพาะไฟล์สถานะของ branch ตัวเอง ห้ามแก้ไฟล์สถานะของ branch อื่น
- การตัดสินที่ใช้ข้าม branch เขียนลง `docs/decisions/` บน branch ที่ตัดสิน ตอน merge ถ้า decisions ชนกัน ให้เก็บทั้งสองรายการ เรียงตามวันที่ ห้ามเลือกทิ้งข้างใดข้างหนึ่ง
- เรื่องที่ branch หนึ่งยังค้างแต่ต้องทำตอน merge (เช่น "ตอน merge ให้ลบ class X") เขียนไว้ในหัวข้อ "ถัดไป" ของไฟล์สถานะของ branch ที่จะรับ merge
- ห้าม cherry-pick หรือ merge เข้า branch ที่มี agent ทำงานอยู่ ถ้าจำเป็นต้องให้ agent ตัวนั้นทำเองตอนจบชิ้น

## hook กับ worktree
- `.claude/settings.json` ที่ commit แล้วจะมีในทุก worktree เอง แต่ `.claude/settings.local.json` ไม่ถูก commit
  จึงไม่มีใน worktree ใหม่ ถ้าใช้ไฟล์ local ต้องคัดลอกไปทุก worktree หรือใส่ hook ไว้ระดับผู้ใช้แทน
- `$CLAUDE_PROJECT_DIR` คือโฟลเดอร์ที่เปิด session ถ้าเปิดใน worktree ก็เป็นโฟลเดอร์ worktree นั้น hook จึงอ่าน branch ถูกตัว
- detached HEAD ไม่มีชื่อ branch hook จะพิมพ์ว่าไม่มีไฟล์ ให้ checkout branch ก่อนทำงาน
