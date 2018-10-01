import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="With Arye's code"))
    print('ready')
    global kafa
    kafa = 0
    global miscanim
    miscanim = []
    global on
    on = 1
global on
class miscan:
    mk=1
    mid=0
    def __init__(self,mid):
        self.mid=mid
        global mk
        mk=1
        print("init")
    def getmid(self):
        return self.mid
        print("get mid")
    def addkafa(self):
        global mk
        mk = mk +1
        print("adding kafa")
    def getkafa(self):
        return mk
        print("getting kafa")
@client.event
async def on_message_edit(bm, am):
    await client.send_message(am.channel,'I hate when people edit messages. He wrote "'+bm.content+'"')

@client.event
async def on_message(message):
    global miscanim
    global on
    global ser
    if(on==1):
        if ("!test") in message.content:
            for m in miscanim:
                await client.send_message(message.channel,m.getmid())
                await client.send_message(message.channel,m.getkafa())
        if ("!add kafa to") in message.content:
            nmsg = message.content.replace("!add kafa to ","")
            ser = message.channel
            mem = list(message.server.members)
            yesh=0
            menid=0
            per=0
            for m in mem:
                if(m.mentioned_in(message)):
                    menid=str(m.id)
                    per=m
                    curk=0
            if(menid==0):
                await client.send_message(message.channel,"Fuck you")
                await client.send_message(message.channel,"You did not gave a kafa to anyone")
                return
            for mi in miscanim:
                if(str(mi.getmid())==menid):
                    mi.addkafa()
                    yesh = 1
                    curk=mi.getkafa()
                    await client.send_message(message.channel,"Hm... It is not your first time")
            if(yesh==0):
                miscanim.append(miscan(menid))
                await client.send_message(message.channel,"Ace! Just added a kafa")
                if(curk==0):
                    curk=1
            await client.send_message(message.channel,"He has "+str(curk)+" kafot")
        if ("!show kafa for") in message.content:
            ismiscan = 0
            for m in miscanim:
               for mem in list(message.server.members):
                   if(mem.mentioned_in(message)):
                       if(str(m.getmid())==str(mem.id)):
                            await client.send_message(message.channel,mem.mention+" has "+str(m.getkafa())+" kafot")
                            ismiscan = 1
            if(ismiscan==0):
                await client.send_message(message.channel,"He have 0  kafot")
        if ("!roast") in message.content:
            nmsg = message.content.replace("!roast ","")
            for m in list(message.server.members):
                if(m.mentioned_in(message)):
                   if(str(m.id)!=str(218095404615467008)):
                        randomlist = [" In the wiki page of gay people, there is your image"," You are just like ori"," Your dad is a lesbian"," Your mom gay"," My phone battery lasts longer than your relationships.","  If I wanted a bitch, I would have bought a dog."," The smartest thing that ever came out of your mouth was a penis. "," Calm down. Take a deep breath and then hold it for about twenty minutes"," Maybe you should eat make-up so you’ll be pretty on the inside too. "," My middle finger gets a boner every time I see you. "," Whoever told you to be yourself gave you really bad advice.","  If I had a face like yours I’d sue my parents."," Where’s your off button?"," I’m jealous of people who don’t know you."," My hair straightener is hotter than you."," I’d smack you, but that would be animal abuse."," I might be crazy, but crazy is better than stupid. "," It’s scary to think people like you are allowed to vote. "," No, no. I am listening. It just takes me a moment to process so much stupid information all at once."," I’m sorry, what language are you speaking? It sounds like bullshit. "," Everyone brings happiness to a room. I do when I enter, you do when you leave."," I keep thinking you can’t get any dumber and you keep proving me wrong. "," You’re the reason I prefer animals to people. "," You’re not pretty enough to have such an ugly personality. "," You have your entire life to be a jerk. Why not take today off?"," Remember when I asked for your opinion? Me neither."," Sometimes it’s better to keep your mouth shut and give the impression that you’re stupid than open it and remove all doubt."," I’m not a proctologist, but I know an asshole when I see one."," You only annoy me when you’re breathing, really.","I don’t know what your problem is, but I’m guessing it’s hard to pronounce."," Do your parents even realize they’re living proof that two wrongs don’t make a right?","  Remember that time I said I thought you were cool? I lied."," Do you ever wonder what life would be like if you’d gotten enough oxygen at birth?"," Please, save your breath. You’ll probably need it to blow up your next date."," Good story, but in what chapter do you shut the fuck up?"," Don’t hate me because I’m beautiful. Hate me because your boyfriend thinks so."," Were you born on the highway? That is where most accidents happen."," If I wanted to hear from an asshole, I’d fart."," Jesus might love you, but everyone else definitely thinks you’re an idiot."," Whenever we hang out, I remember that God really does have a sense of humor."," It’s kind of hilarious watching you try to fit your entire vocabulary into one sentence."," Please just tell me you don’t plan to home-school your kids."," You always bring me so much joy—as soon as you leave the room."," I’d tell you how I really feel, but I wasn’t born with enough middle fingers to express myself in this case."," Stupidity’s not a crime, so feel free to go."," I’d tell you to go fuck yourself, but that would be cruel and unusual punishment."," You have the right to remain silent because whatever you say will probably be stupid anyway."," You’re about as useful as an ashtray on a motorcycle."," If I threw a stick, you’d leave, right?"," You’ll never be the man your mom is."," Earth is full. Go home. "]
                        await client.send_message(message.channel,m.mention+", "+random.choice(randomlist))
        if(message.content=="no u"):
                   await client.send_message(message.channel,"no you")
        if(message.content=="fuck you"):
                   await client.send_message(message.channel,"well fuck u too")
        if ('arye is zevel') in message.content:
            await client.delete_message(message)
        if("or is zevel") in message.content:
            await client.send_message(message.author, 'well you are absolutely right')
        if(message.content=="!shutdown"):
            for r in message.author.roles:
                if(str(r.id)==str(495305945065324544)):
                    await client.send_message(message.channel,"Shuting Down...")
                    on = 0
    if message.content=="!turn on":
        for r in message.author.roles:
                if(str(r.id)==str(495305945065324544)):
                    await client.send_message(message.channel,"Turning on...")
    if("!change to") in message.content:
         nmsg = message.content.replace("!change to ","")
         await client.change_nickname(message.author, nmsg)
client.run('NDk1MjY4ODc1OTQ0OTg0NTc2.Do_7bQ.t_kYMYrGYcCarN-Rf3Mhd91ns5Q')
