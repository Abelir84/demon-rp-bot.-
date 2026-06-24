import discord
from discord.ext import commands
import json
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

FILE = "data.json"

# ===== สร้างไฟล์ถ้ายังไม่มี =====
if not os.path.exists(FILE):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump({}, f)

def load():
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_user(data, uid):
    if uid not in data:
        data[uid] = {
            "exp": 0,
            "level": 1,
            "rank": "👹 เผ่ามารทั่วไป",
            "path": None
        }
    return data[uid]

def rank_up(user):
    lv = user["level"]

    if lv >= 5000:
        return "👑 จักรพรรดิมาร"

    if lv >= 3000:
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

    if lv >= 300:
        return "⚔️ แม่ทัพมาร"

    if lv >= 100:
        return "🛡️ ขุนพลมาร"

    return "👹 เผ่ามารทั่วไป"

@bot.event
async def on_ready():
    print("Bot is online")

@bot.command()
async def สมัคร(ctx):
    data = load()
    get_user(data, str(ctx.author.id))
    save(data)
    await ctx.send("✨ สมัครแล้ว")

@bot.command()
async def สถานะ(ctx):
    data = load()
    u = get_user(data, str(ctx.author.id))

    await ctx.send(
        f"📜 สถานะ\n"
        f"EXP: {u['exp']}\n"
        f"LV: {u['level']}\n"
        f"Rank: {u['rank']}\n"
        f"Path: {u['path']}"
    )

@bot.command()
async def ล่ามอน(ctx):
    data = load()
    u = get_user(data, str(ctx.author.id))

    gain = random.randint(20, 80)

    u["exp"] += gain
    u["level"] = (u["exp"] // 100) + 1
    u["rank"] = rank_up(u)

    save(data)

    await ctx.send(f"⚔️ +{gain} EXP")

@bot.command()
async def ดันเจี้ยน(ctx):
    data = load()
    u = get_user(data, str(ctx.author.id))

    total = sum(random.randint(100, 300) for _ in range(3))

    u["exp"] += total
    u["level"] = (u["exp"] // 100) + 1
    u["rank"] = rank_up(u)

    save(data)

    await ctx.send(f"🏰 +{total} EXP")

@bot.command()
async def เลือกสาย(ctx, *, name):
    data = load()
    u = get_user(data, str(ctx.author.id))

    if u["path"] is not None:
        await ctx.send("❌ เลือกแล้วเปลี่ยนไม่ได้")
        return

    u["path"] = name
    save(data)

    await ctx.send(f"👑 เลือกสาย: {name}")

bot.run(os.getenv("TOKEN"))
