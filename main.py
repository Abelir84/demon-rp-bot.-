import discord
from discord.ext import commands
import json
import os
import random

intents = discord.Intents.default()
intents.message_content = True

บอท = commands.Bot(command_prefix="!", intents=intents)

ไฟล์ = "ข้อมูล.json"

if not os.path.exists(ไฟล์):
    with open(ไฟล์, "w", encoding="utf-8") as f:
        json.dump({}, f, ensure_ascii=False)

def โหลด():
    with open(ไฟล์, "r", encoding="utf-8") as f:
        return json.load(f)

def บันทึก(data):
    with open(ไฟล์, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def ผู้เล่น(data, id):
    if id not in data:
        data[id] = {
            "แต้ม": 0,
            "เลเวล": 1,
            "ขั้นมาร": "👹 เผ่ามารทั่วไป",
            "สายมาร": None
        }
    return data[id]

def อัปขั้นมาร(user):
    lv = user["เลเวล"]

    if lv >= 5000:
        return "👑 จักรพรรดิมาร"

    elif lv >= 3000:
        return random.choice([
            "🌙 มารจันทรา",
            "⭐ มารดวงดาว",
            "🩸 มารโลหิต",
            "☠️ มารแห่งความตาย",
            "🐍 มารอสรพิษ",
            "💀 มารกระดูก",
            "🌑 มารรัตติกาล",
            "🦋 มารมายา",
            "⚡ มารอัสนี",
            "❄️ มารเหมันต์",
            "🔥 มารเพลิง",
            "🌪️ มารวายุ",
            "⛓️ มารพันธนาการ",
            "👻 มารเงาวิญญาณ"
        ])

    elif lv >= 300:
        return "⚔️ แม่ทัพมาร"

    elif lv >= 100:
        return "🛡️ ขุนพลมาร"

    return "👹 เผ่ามารทั่วไป"

# ===== สมัคร =====
@บอท.command()
async def สมัคร(ctx):
    data = โหลด()
    ผู้เล่น(data, str(ctx.author.id))
    บันทึก(data)
    await ctx.send("✨ สมัครแล้ว")

# ===== สถานะ =====
@บอท.command()
async def สถานะ(ctx):
    data = โหลด()
    u = ผู้เล่น(data, str(ctx.author.id))

    await ctx.send(f"""
📜 สถานะ
✨ แต้ม: {u['แต้ม']}
⭐ เลเวล: {u['เลเวล']}
🏅 ขั้นมาร: {u['ขั้นมาร']}
👑 สายมาร: {u['สายมาร']}
""")

# ===== ล่ามอน =====
@บอท.command()
async def ล่ามอน(ctx):
    data = โหลด()
    u = ผู้เล่น(data, str(ctx.author.id))

    ได้ = random.randint(20, 80)

    u["แต้ม"] += ได้
    u["เลเวล"] = (u["แต้ม"] // 100) + 1
    u["ขั้นมาร"] = อัปขั้นมาร(u)

    บันทึก(data)

    await ctx.send(f"⚔️ ได้ +{ได้} แต้ม")

# ===== ดันเจี้ยน =====
@บอท.command()
async def ดันเจี้ยน(ctx):
    data = โหลด()
    u = ผู้เล่น(data, str(ctx.author.id))

    total = 0

    for i in range(3):
        total += random.randint(100, 300)

    u["แต้ม"] += total
    u["เลเวล"] = (u["แต้ม"] // 100) + 1
    u["ขั้นมาร"] = อัปขั้นมาร(u)

    บันทึก(data)

    await ctx.send(f"🏰 +{total} แต้ม")

# ===== เลือกสายมาร =====
@บอท.command()
async def เลือกสายมาร(ctx, *, name):
    data = โหลด()
    u = ผู้เล่น(data, str(ctx.author.id))

    if u["สายมาร"]:
        await ctx.send("❌ เลือกแล้วเปลี่ยนไม่ได้")
        return

    u["สายมาร"] = name
    บันทึก(data)

    await ctx.send(f"👑 เลือก: {name}")

# ===== bot run =====
@บอท.event
async def on_ready():
    print("บอทออนไลน์แล้ว")

บอท.run(os.getenv("MTUxOTE2MTY1NTcyMjkwMTYxNg.GwT4pv.ja5zTKyQsqsh4pqnbYgVOJASCCJngcqjZBaIGo"))
