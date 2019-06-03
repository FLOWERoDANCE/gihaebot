import discord


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("부산에서 온 기해")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("/기해야 안녕"):
        await message.channel.send("마! 반갑다!")
    if message.content.startswith("/기해야 바이"):
        await message.channel.send("잘가레이!")
    if message.content.startswith("/기해야 심심해"):
        await message.channel.send("놀아줄 시간이 읎다!")
    if message.content.startswith("/기해야 청소"):
        await message.channel.send("마냥봇 명령어로 채팅청소 하라이!")
    if message.content.startswith("/기해야 서버오픈일"):
        await message.channel.send("9월14일 - 정상오픈!")
    if message.content.startswith("/기해야 고마워"):
        await message.channel.send("니가 너 고맙다!")
    if message.content.startswith("/기해야 피곤해"):
        await message.channel.send("마! 가서 자라!")
    if message.content.startswith("/기해야 관리진"):
        await message.channel.send("어드민,경찰,가이드,건축팀,관리팀")

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/채널메시지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await client.get_channel(int(channel)).send(msg)

    if message.content.startswith("/DM"):
        auihor = message.guild.get_meber(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)

    if message.content.startswith("/뮤트"):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await author.add_roles(role)

    if message.content.startswith("/언뮤트"):
        author = message.guild.get_member(int(message.content[5:23]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await author.remove_roles(role)

client.run("NTczNDY0NDkyMzY5OTAzNjI2.XMr7IQ.EKs5DIRQxWarKo65vMeRC4GoFy4")



