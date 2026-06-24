import discord
from discord.ext import commands
import json
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

FILE = "data.json"

if not os.path.exists(FILE):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump({}, f)

def load_data():
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_user(data, user_id):
    if user_id not in data:
        data[user_id] = {
            "exp": 0,
            "level": 1,
            "rank": "👹 เผ่ามารทั่วไป",
            "path": None
        }
    return data[user_id]

def rank_up(user):
    lv = user["level"]

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

@bot.command()
async def register(ctx):
    data = load_data()
    get_user(data, str(ctx.author.id))
    save_data(data)
    await ctx.send("✨ สมัครเผ่ามารแล้ว")

@bot.command()
async def status(ctx):
    data = load_data()
    u = get_user(data, str(ctx.author.id))

    await ctx.send(f"""
📜 สถานะ
✨ EXP: {u['exp']}
⭐ Level: {u['level']}
🏅 Rank: {u['rank']}
👑 Path: {u['path']}
""")

@bot.command()
async def hunt(ctx):
    data = load_data()
    u = get_user(data, str(ctx.author.id))

    gain = random.randint(20, 80)

    u["exp"] += gain
    u["level"] = (u["exp"] // 100) + 1
    u["rank"] = rank_up(u)

    save_data(data)

    await ctx.send(f"⚔️ ล่ามอนได้ +{gain} EXP")

@bot.command()
async def dungeon(ctx):
    data = load_data()
    u = get_user(data, str(ctx.author.id))

    total = 0
    for _ in range(3):
        total += random.randint(100, 300)

    u["exp"] += total
    u["level"] = (u["exp"] // 100) + 1
    u["rank"] = rank_up(u)

    save_data(data)

    await ctx.send(f"🏰 ดันเจี้ยนสำเร็จ +{total} EXP")

@bot.command()
async def path(ctx, *, name):
    data = load_data()
    u = get_user(data, str(ctx.author.id))

    if u["path"] is not None:
        await ctx.send("❌ เลือกแล้วเปลี่ยนไม่ได้")
        return

    u["path"] = name
    save_data(data)

    await ctx.send(f"👑 เลือกสาย: {name}")

@bot.event
async def on_ready():
    print("Bot is online")

bot.run(os.getenv("MTUxOTE2MTY1NTcyMjkwMTYxNg.GwT4pv.ja5zTKyQsqsh4pqnbYgVOJASCCJngcqjZBaIGo"))
