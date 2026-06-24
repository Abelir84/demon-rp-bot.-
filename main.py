import discord
from discord.ext import commands
import json
import os
import random

intents = discord.Intents.default()
intents.message_content = True

บอท = commands.Bot(command_prefix="!", intents=intents)

@บอท.event
async def on_ready():
    print("✅ บอทออนไลน์แล้ว")
  @บอท.command()
async def สมัคร(ctx):

    data = โหลด()
    ผู้เล่น(data, str(ctx.author.id))
    บันทึก(data)

    await ctx.send("✨ สมัครเป็นเผ่ามารสำเร็จ!")
  def ผู้เล่น(data, id):
    if id not in data:
        data[id] = {
            "แต้ม": 0,
            "เลเวล": 1,
            "ขั้นมาร": "👹 เผ่ามารทั่วไป",
            "สายมาร": None
        }
      @บอท.command()
async def สถานะ(ctx):

    data = โหลด()
    u = ผู้เล่น(data, str(ctx.author.id))

    await ctx.send(
        f"""
📜 สถานะ

✨ แต้ม: {u['แต้ม']}
⭐ เลเวล: {u['เลเวล']}
🏅 ขั้นมาร: {u['ขั้นมาร']}
👑 สายมาร: {u['สายมาร']}
"""
    )​
@บอท.command()
async def ล่ามอน(ctx):

    data = โหลด()
    u = ผู้เล่น(data, str(ctx.author.id))

    ได้ = random.randint(20, 80)

    u["แต้ม"] += ได้
    u["เลเวล"] = (u["แต้ม"] // 100) + 1
    u["ขั้นมาร"] = "👹 เผ่ามารทั่วไป"

    บันทึก(data)

    await ctx.send(f"⚔️ ล่ามอนได้ +{ได้} แต้ม")
@บอท.command()
async def ดันเจี้ยน(ctx):

    data = โหลด()
    u = ผู้เล่น(data, str(ctx.author.id))

    total = 0

    for i in range(3):
        ได้ = random.randint(100, 300)
        total += ได้

    u["แต้ม"] += total
    u["เลเวล"] = (u["แต้ม"] // 100) + 1

    บันทึก(data)

    await ctx.send(f"🏰 เคลียร์ดันเจี้ยน +{total} แต้ม")
@บอท.command()
async def เลือกสายมาร(ctx, *, name):

    data = โหลด()
    u = ผู้เล่น(data, str(ctx.author.id))

    if u["สายมาร"]:
        await ctx.send("❌ เลือกแล้วเปลี่ยนไม่ได้")
        return

    u["สายมาร"] = name
    บันทึก(data)

    await ctx.send(f"👑 เลือกสายมาร: {name}")
