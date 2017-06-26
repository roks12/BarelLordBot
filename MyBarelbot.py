
import discord;
import logging
import time
from datetime import datetime, timedelta
import threading
from threading import Timer

from discord.ext import commands
from discord import ChannelType

   
logging.basicConfig(level=logging.INFO)
DJtimeReady = None
isLegacyDJReady = True
hasLegacyDJPlayedMusic = False;




#await client.say(embed=embed)





LegacyDJs = [
    "",
    "",
    "",
    ]
client = commands.Bot(description='BarelLord bot', command_prefix='!')


@client.event
async def on_message(message):
    if "olafs" in message.content.lower():
        await client.send_message(message.channel, '*Aleksejs...')
    elif "olafu" in message.content.lower():
        await client.send_message(message.channel, '*Alekseju...')
    elif "olafam" in message.content.lower():
        await client.send_message(message.channel, '*Aleksejam...')
    elif "olafa" in message.content.lower():
        await client.send_message(message.channel, '*Alekseja...')
    elif "olafā" in message.content.lower():
        await client.send_message(message.channel, '*Aleksejā...')
    elif "olafi" in message.content.lower():
        await client.send_message(message.channel, '*Alekseji...')

    global hasLegacyDJPlayedMusic
    #storage = await self.get_storage(member.server)
    #role_names = await storage.smembers('roles')
    #if "?play" in message.content.lower() and message.author == "coolkix":
        #await client.send_message(message.channel, 'DJ BORO...')
    if "dj_dima pretty please let me play song" in message.content.lower():
        if (message.author.name == LegacyDJs[0] or message.author.name == LegacyDJs[1] or message.author.name == LegacyDJs[2]):
            global isLegacyDJReady
            if (isLegacyDJReady == True):
                isLegacyDJReady = False;
                hasLegacyDJPlayedMusic = False;
                #channel = discord.utils.get(client.get_all_channels(), name="general" ,type=ChannelType.voice)
                #await client.join_voice_channel(channel);
                ##role = discord.role("DJ")
                role = discord.utils.get(message.server.roles, name="DJ")
                roles = [
                    "282221347730489344",
                    ]
                #for member in client.get_all_members():
                #    for role in member.roles:
                #        if(role.name == "DJ"):
                            #roles[0] = role.id
                            #print(roles[0])
                            #break
                 #         print(role.id + "  " + role.server.name + " " + role.server.id)
                ##client.add_roles(message.author, role)
                await client.add_roles(message.author, role)
                await client.send_message(message.channel, 'Welcome LegacyDJ! You can use your power now.')
            else:
                await client.send_message(message.channel, "DJ_DIMA thinks that you are not ready yet!")
    if ("?play" in message.content.lower() and hasLegacyDJPlayedMusic == False):
        
        hasLegacyDJPlayedMusic = True;
        role = discord.utils.get(message.server.roles, name="DJ")
        roles = [
                   "282221347730489344",
                    ]
        
            #for i in range(0, 2):
            #    if (message.author.name == LegacyDJs[i]):
            #        LegacyDJs[i] = ""
        await client.remove_roles(message.author, role)
        dj_startTime()
        await client.send_message(message.channel, "You have used your LegacyDJ power! :musical_note: \n" + checkTime() + " - Next available song" )
    await client.process_commands(message)

@client.command(pass_context = True)
async def helpMe(ctx):
    em=discord.Embed(title="BarelLord Documentation", description="All BarelLord available commands.", color=0x8000ff)
    em.add_field(name="User commands:", value="!ggc champion line  -  returns op.gg link with specified champion information", inline=False)
    em.add_field(name="", value="?play  - (legacyDJs) plays one song before cooldown", inline=False)
    em.add_field(name="", value="!gg champion  -  return op.gg link with specified champion with main lane", inline=False)
    em.add_field(name="", value="DJ_DIMA pretty please let me play song  -  enables LegacyDJ power", inline=True)
    em.add_field(name="", value="", inline=False)
    em.add_field(name="Admin commands:", value="!addLegacyDJ discord_username  -  adds news LegacyDJ", inline=True)
    em.set_footer(text="Bot made by Roboobox")
    print("HelpTest")
    await client.send_message(LegacyDJs[0], "Testing")

@client.command(pass_context = True)
async def gg(ctx, username : str):
    print (ctx.message.channel == "text")
    await client.send_message(ctx.message.channel, "https://eune.op.gg/summoner/userName=" + username)

@client.command(pass_context = True)
async def cc(ctx, champion : str):
    await client.send_message(ctx.message.channel, "http://www.championcounter.com/" + champion)

@client.command(pass_context = True)
async def live(ctx, username : str):
    await client.send_message(ctx.message.channel, "http://www.lolnexus.com/EUNE/search?name=" + username + "&region=EUNE")

@client.command(pass_context = True)
async def ggc(ctx, champion : str, line : str):
    await client.send_message(ctx.message.channel, "https://eune.op.gg/champion/" + champion + "/statistics/" + line)

@client.command(pass_context = True)
async def addLegacyDJ(ctx, * , member):
    memberFound = False
    authorizedToCommand = False;
    for role in ctx.message.author.roles:
        if(role.permissions.manage_server):
            authorizedToCommand = True

    for memberSelected in client.get_all_members():
        if (member == memberSelected.name):
            
            memberFound = True;
    if(authorizedToCommand == False):
        await client.say(":no_entry: You do not have permission to use this command! :no_entry: ")
    elif(member is None):
        await client.say("Please enter LegacyDJs username!")
    elif(memberFound == False):
        await client.say("There is no such user in this server!")
    else:
        await client.say('|'+ member + '|' + " is now a LegacyDJ")
        if(LegacyDJs[0] == ""):
            LegacyDJs[0] = member
            print(LegacyDJs[1])
        elif(LegacyDJs[1] == ""):
            LegacyDJs[1] = member
        elif(LegacyDJs[2] == ""):
            LegacyDJs[2] = member
        else:
            await client.say("No free space for new LegacyDJ")

@client.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        await client.send_message(ctx.message.channel,'Missing argument!')


def dj_startTime():
    hourlater = datetime.now() + timedelta(hours=1)
    global DJtimeReady
    DJtimeReady = hourlater.strftime("%d-%m-%Y %H:%M")
    print(DJtimeReady)
    t = Timer(3600, enableLegacyDJ)
    t.start()

    
def enableLegacyDJ():
    if (message.author.name == LegacyDJs[0] or message.author.name == LegacyDJs[1] or message.author.name == LegacyDJs[2]):
        pass
    if(LegacyDJs[0] != ""):
        pass

    for i in range(0, 2):
        for user in client.get_all_members():
            if(LegacyDJs[i] == user.name):
                client.send_message(user, "You have some DJing to do boi")

    global isLegacyDJReady
    isLegacyDJReady = True;
    if(LegacyDJs[0] != ""):
        print(LegacyDJs[0])

def checkTime():
    return DJtimeReady

client.run('Mjk3NDQ1Mjc5NTI1ODk2MTkz.DDBYZg.arP3Qh43pDTyDb5Jpsxh5ISjQWs')