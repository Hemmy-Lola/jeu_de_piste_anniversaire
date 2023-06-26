# Pour installer l'expention discord:

# !pip install discord.py
# !pip install nest_asyncio 
# import nest_asyncio 
# nest_asyncio.apply()


import discord

intents = discord.Intents.all()
intents.messages = True
intents.members = True
intents.typing = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("Le bot est prêt !")

@client.event
async def on_member_join(member):
  general_channel = client.get_channel("(code serveur)")
  # await general_channel.send("https://tenor.com/view/kidnap-kid-brother-grab-bootloon-gif-22467768")
  await general_channel.send("*Bienvenue à vous * "+ member.name + "! *écris* GO *pour commencer*")

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  message.content = message.content.lower()

  if message.content.startswith("go"):
    await message.channel.send("*Jeudi 18 Mai 2023...Vous voici embarquée dans 'un weekend pas comme les autres...'*")
    await message.channel.send("*Saississez OUI si vous êtes prête à commencer.*")
  
  if message.content == "oui":
    await message.channel.send("*Avant toute chose, nous tenons à clarifier la situation : \nVous serez guidée pour arriver à destination. \nIl est donc important que vous suiviez les insctructions à la lettre...*")
    await message.channel.send("*En cas de difficultés, vous pouvez bien évidemment contacter la team. \nNous tenons également à préciser qu'il est important que vous saisissiez correctement chaque message associé à chaque étape spécifique, afin de ne pas fausser votre itinéraire donc patience et concentration...*")
    await message.channel.send("*Saisissez donc OKEY si vous êtes prête à partir.*")

  if message.content == "okey":
    await message.channel.send("*Voici votre première étape : \nRendez vous à la gare de Torcy !*")
    await message.channel.send("*Lorsque vous êtes arrivée, écrivez UN.*")
    
  if message.content == "un":
    await message.channel.send("*Et si on prenait le RER A ? Direction Paris votre arrêt sera alors  CHÂTELET-LES HALLES.*")
    await message.channel.send("*Saisissez DEUX à votre arrivée.*")

  if message.content == "deux":
    await message.channel.send("*Changement de destination ! \nVous arrivez au tournant décisif de votre parcours ! A présent, prenez le RER B Sud direction MASSY-PALAISEAU. \nVous descendrez alors à la 11ème station après votre point de départ.*")
    await message.channel.send("*Saississez TROIS lorsque vous arrivez à la bonne station.*")

  if message.content == "trois":
    await message.channel.send("*Bienvenue à Sceaux ! \nQuelle Belle ville, n'est-ce pas ? \nVous arrivez au bout de votre destination finale, le Parc de Sceaux...*")
    await message.channel.send("*A présent, rendez-vous à l'adresse suivante:* 8 Av. Claude Perrault, 92330 Sceaux, France. \n*Si votre sens de l'orientation est assez bon, vous devriez arriver devant un beau château...*")
    await message.channel.send("*Saisissez FINISH lorsque ce sera le cas.*")

  if message.content == "finish":
    await message.channel.send("https://tenor.com/view/crutches-dance-throw-gif-26311188")
    await message.channel.send("*Vous voilà arrivée à destination, consultez à present le plan et rejoignez le cercle rouge et non le vert...")


client.run("(token)")
