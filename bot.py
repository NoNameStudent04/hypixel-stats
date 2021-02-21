import discord, asyncio, datetime, hypixel
from discord.ext import commands
from discord.ext.commands import Bot

client = commands.Bot(command_prefix ='-')
client.remove_command("help")
token = 'INPUT_YOUR_TOKEN'

@client.event
async def on_ready():
    print("running")
    game = discord.Game("-도움말")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.command(pass_context=True)
async def 도움말(ctx):
    embed = discord.Embed(
            title="스탯 알려주는 돌 [ 사용 설명서 ]",
            description="현재 버전 : **Alpha 0.1**\n개발한 인간 : `! C𝑳EA𝑹G𝑳A𝑺 ッ#7777`\n접두사 : `-` (변경불가)",
            color=0xffffff,
            timestamp=datetime.datetime.now()
        )
    embed.add_field(name="쓸모없는 기능들", value="-도움말\n-초대링크")
    embed.add_field(name="하픽 스탯조회", value="-조회 [IGN]")
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def 초대링크(ctx):
    embed = discord.Embed(
            title="초대링크",
            description="현재 초대하기는 비활성화가 되어있습니다.",
            color=0x000000,
            timestamp=datetime.datetime.now()
        )
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def 조회(ctx, name):
    level = hypixel.get_level(name)
    if level is None:
        embed = discord.Embed(
                title=":x: Error",
                description="오류! : **플레이어 명이 입력되지 않았거나 잘못된 값이 입력되었습니다.**",
                color=0xFF0000
            )
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
                title=":white_check_mark: Hypixel Network All Stats",
                description=f"**플레이어 : `{name}`**\n이전 닉네임 : {name}",
                color=0x4FF21F
            )
        embed.add_field(name="Hypixel Network", value=f"Lv {level}")
        await ctx.send(embed=embed)
client.run(token)
