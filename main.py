import discord
import os
import random
import time
# import requests
# import json
#lists of values (commands, links for sexBot() etc.)
cmdsString = ""
cmds = [ "/matty", "/rob", "/michael", "/joel", "/alex", "/amirul", "/corey", "/hudson", "/owen", "/carter", "/jason", "/peter", "/sexbot"]
sexBotImg = ['https://spectator.us/wp-content/uploads/2019/06/sexrobots.jpg', 'https://cdn.shopify.com/s/files/1/0024/8070/1503/products/7R5A0079_380x@2x.jpg?v=1572968112', 'https://www.dmarge.com/wp-content/uploads/2018/03/male-sex-robot.jpg', 'https://thebrag.com/wp-content/uploads/2018/08/Hot-Bot-2-768x468.jpg', 'https://ascienceenthusiast.com/wp-content/uploads/2019/02/SexRobot.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAL5iaGB_mAOIWcAHub9ejw8H-5d6v-1-TOw&usqp=CAU', 'https://s31242.pcdn.co/wp-content/uploads/2019/06/sexrobot2.jpg']
#adds items from list into printable strings
#formatted with spaces 
for cmd in cmds:
  cmdsString += cmd
  cmdsString += " "


#creates bot
client = discord.Client()
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


#please add functions below
#adds random link from sexBotImg and appends result /w msg
def sexBot():
  result = ""
  global botPic
  botPic = sexBotImg[random.randrange(len(sexBotImg))]   
  result += botPic
  result += " Here is your custom made sex bot! Your HOMIE discount is 50%! Please provide credit card, account, sort and security number to provide payment and secure your sex bot today! " + "\n" + "give me a name with $givename!"
  return result


def sexBotName(name, user):
  isNamed = "Hi! I am " + " " + name + "and I am "
  isNamed += botPic
  return isNamed

def rob():
  result = "<@!236048628869890049> " + "The current time is: "
  t = time.localtime()
  current_time = time.strftime("%H:%M:%S", t)
  result += current_time
  result += " and you are LATE!"
  return result

#function for testing
#comment out old tests and write new test func
def test():
  test = "<@!236048628869890049>"
  return test

#sends messages upon detecting a command
#DO NOT EDIT @client.event block
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  #variables to pass in to functions
  msg = message.content
  global user
  user = message.author.id
  
  #sends rules message
  if message.content.startswith('/rules'):
    await message.channel.send('I am YesMan3000 you can use the following commands, whether I want you to or not: ' +" " + cmdsString + '\n' + "P.S. Fuck Mr. House")
  
  #sends sexBot() message
  if message.content.startswith('/sexbot'):
    await message.channel.send(sexBot())
  
  #sends sexBotName() message with botPic from prev sexBot()# call
  if message.content.startswith('$givename'):
    botName = msg.split("$givename ", 1)[1]
    await message.channel.send(sexBotName(botName, user))
  
  #runs test() block. Not included in /rules
  if message.content.startswith('/test'):
    await message.channel.send(test())
  
  #runs rob() block x 5
  if message.content.startswith('/rob'):
    for i in range(0, 5):
     await message.channel.send(rob())




#startup + run
#DO NOT EDIT
client.run(os.getenv('TOKEN'))

