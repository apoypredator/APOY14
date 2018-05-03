# -*- coding: utf-8 -*-

import KIBAS
from KIBAS.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
import requests
from io import StringIO
from threading import Thread
from urllib import urlopen
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,tempfile
import KIBAS
from KIBAS.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
import time, random, sys, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, urllib2, wikipedia
import ast
import KIBAS
from KIBAS.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess
import KIBAS
from KIBAS.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
import time, random, sys, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, urllib2, wikipedia
import ast

cl = KIBAS.LINE()
cl.login(token="ErUr1MVO9uapb2z4GMJa.uOEjKAXo9tj1pPEGpJT4UG.G/lSL4C3LLR91ccEuXCswUyA7/1YIqLWfDBwIuLB0qo=")
cl.loginResult()

print u"╔════════════════\n╠[❂͜͡➣login success\n╠[❂͜͡➣gunakan dengan bijak kawan\n╚═════════════════════════"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""╔════════════════════
║__̴ı̴̴̡̡̡ ̡͌l̡̡̡ ̡͌l̡*̡̡ ̴̡: |̲̲̲͡͡͡ ̲▫̲͡ ̲̲̲͡͡π̲̲͡͡ ̲̲͡▫̲̲͡͡ ̲|̡̡̡ ̡ ̴̡ı̴̡̡ ̡͌l̡ ̴̡ı̴̴̡ ̡l̡*̡̡ ̴̡ı̴̴̡ ̡̡͡|̲̲̲͡͡͡ ̲▫̲͡ ̲̲̲͡͡π̲̲͡͡ ̲̲͡▫̲̲͡͡ |__
║          ◄]·Owner :¯•'ᵤₛRₒ̰̈́•¯·[►
╠════════════════════
║╔═══════════════════
║║◄]··_̶̛̫̭̼̩͎̀̌̈̀̊̚͜͝_̸̡̛̬̣̞̭̗̥̥͔̹̰̂̋̈́̐̀̊_̸̢̗̱͕̟͓̩̥̠̈́̀̾͐͐̚͝Ḿ̵̢̢̬̠̭̦͉͉͚͔͈̏͋͂̍͜͠͝͝ͅE̸͍̙̟̣̰̝̘̺͈̪̭̯̰͎̽͂̔͒̓͛̕ͅN̸̯̠̼͇͖̩̬̩̭͖̙̎̐̈́͋̍͗̓̈́͜͜ͅͅU̸̠̲͌̃͂̍͌̃̄͛͐̚͘ ̷̧͍̼͚̤̺͔̳̏͋̀͛F̸̮̤̮̫͉͐̂̂͐̅͊̆̓̐̑͊͌̈́̈͝Ö̷̤̦̻̠͓̘̳͇̞͚̮̙̌̾̉̑̈̾̾̽̆̔͠R̴̡̧̻̖̭̹̭̞̼͔̟͔͇̺̼̅̄͛̌̈ ̸̳͖̀̾̄͛́͒̊̄̔͆̾̀̌̚̚͜G̵̘̟̹̠͚͇̝̙̩̳͙͗͐̉̃̓͐̇͊̌̄͆͝R̵̺̮͎͉͒̌̐͛U̶̜̍͗̀̀͗̒̎̀̃̀̅̉͘͠P̶̮͉̻̝̻̻̘̜̖͕͈͉͂̒̅̑_̶̨̡̫̗̺̗͉͂̄_̵͕͇̓͛͌̐͠_̶̡̭̦̰̠̫̪͔͂͛͑̒̉̑̀͑̐̄̆̚̕ͅ··[►
║╠═══════════════════
║╠[❂͜͡➣ Sider on
║╠[❂͜͡➣ Sider off
║╠[❂͜͡➣ Glist
║╠[❂͜͡➣ Cancel
║╠[❂͜͡➣ Mid @
║╠[❂͜͡➣ Mycopy @      
║╠[❂͜͡➣ Invite:on
║╠[❂͜͡➣ Unban @   
║╠[❂͜͡➣ Whitelist:
║╠[❂͜͡➣ Unbans:on
║╠[❂͜͡➣ Blacklist @   
║╠[❂͜͡➣ Blacklist
║╠[❂͜͡➣ set all on
║╠[❂͜͡➣ set all off
║╠════════════
║╠[❂͜͡➣ Link on 
║╠[❂͜͡➣ Link off 
║╠[❂͜͡➣ Gurl
║╠[❂͜͡➣ Url
║╠[❂͜͡➣ Gn [text]
║╠[❂͜͡➣ List grup
║╠[❂͜͡➣ Detalsgroup
║╠[❂͜͡➣ Invite
║╠[❂͜͡➣ Info group
║╠[❂͜͡➣ Bot out
║╠[❂͜͡➣ cipok/Tagall
║╠[❂͜͡➣ Nuke
║╠[❂͜͡➣ Kibas/kickall
║╠[❂͜͡➣ Mayhem
║╠[❂͜͡➣ Masuk
║╠[❂͜͡➣ Pulang
║╠[❂͜͡➣ vk @
║╠[❂͜͡➣ Kibas/kickall
║╠[❂͜͡➣ Masuk
║╠[❂͜͡➣ Pulang
║╠[❂͜͡➣Spm @
║╠═══════════════════
║║◄]··_̴̡͕̝̗͓̚_̸̢̛̻̭̻̺̇_̶̤͉̖̼̓̏̊͌̀̈́̅̋͒̊M̶̘̲̹̖͚̬̘͈̦̟͖͌̒̊̊͐͑E̷̢̢̡̨̘̭̟̲̠̱̝̲̻̖͍̒̅̃̌̐͝͠N̶̢̪̝͖͉̭͙̊͒̚͠͝Ų̵̛̜̝̤̼̭̱͇̯̹̯̫̈́̉̅̆̑́̄̎̎̈́͝ ̸̢̱͍̱̹̖̣͖̯͈̇͒͌̒͛̃͊̂̈́̆F̵̣͕̲̫̥̂̓̚O̶̡̢̡̠͍̩̟̖̒ͅR̶̡̡̡̝͉͉̳͈̱̮̳̪̖̙̜̐̈͆̈́̌͒͝͠ ̷̛͓͕̎̓̍̽̐͆̄͝P̶̙͇̙̌͊͗͌͗̑ͅŖ̴̻͇̖͎͖́͒̎̾̈́̏̕Ó̷̟̚T̶̯͍̭͙͔̝̗̻̘̓Ę̴̛̛̞̺̲̱̹̦̯̼́͆́̈̔̅͑̈́̅͘̕͜͝C̵͕̣̬͚̪̟̼̻̦̤͆͗͂̆̃̕͝ͅT̶̞̘̝̩͙͙̙̞͖̱̖͇̼̪̙̑̀́͆̓_̷͓͑̾̉́̀̒̿̚̚̚̕̕͝_̵̧̧̛̻̯̖̫̯̥̯̽̽͆̇̽͛̑̀̍̄͜ͅͅ_̶̢͉̰͍͈̌̏̊̊̀̾̍͂̈́̚̕··[►
║╠═══════════════════
║╠[❂͜͡➣ Cancel
║╠[❂͜͡➣ Like:on
║╠[❂͜͡➣ Add on/off
║╠[❂͜͡➣ Auto join on/off
║╠[❂͜͡➣ Contact on/off
║╠[❂͜͡➣ Leave on/off
║╠[❂͜͡➣ Share on/off
║╠[❂͜͡➣ Add on/off
║╠[❂͜͡➣ Jam on/off
║╠[❂͜͡➣ Jam say:
║╠[❂͜͡➣ Com on/off
║╠[❂͜͡➣ Message set:
║╠[❂͜͡➣ Comment  set:
║╠[❂͜͡➣ Pesan cek add
║╠[❂͜͡➣ Set all on/off
║╠[❂͜͡➣ Protect on/off			   
║╠[❂͜͡➣ Qrprotect on/off
║╠[❂͜͡➣ Inviteprotect on/off			   
║╠[❂͜͡➣ Cancelprotect on/off		   
║╠[❂͜͡➣ Respon on/off
║╠[❂͜͡➣ Responkick on/off
║╠[❂͜͡➣ Sambutan on/off
║╠[❂͜͡➣ Backup on/off
║╠[❂͜͡➣ Sticker on/off
║╠═══════════════════
║╠¢яєαтσя:BOT
║╠-------------☆_̶̧̎̀̂̅̊_̵̢̣̞̘̣̞̺̮͉͖̻̍̈́̎̓̔̐̐͗̒̃̏̕_̷̢̧̲͔̠̜͖͇̦̟̞̗̬̋̎̎͂͋͛͘K̵̛̮̣̞͕͔͕̺̹̳͒͌̀̾̅̔̚I̸̯̤̲͐̎͑̀̌̔̋̔̊̾̔̄́̃B̸̧̟̞͓̥̼͇̺̥̯̳͈͕̳͋͐̓̋̓̓͛͝A̶̙͖̋̿͒̈́̓̕͠Ş̶͕̫̳̝͎̥̥̩̃͗̑̉̅̇̓́̍͘͘͜͝͝_̷̯͇͇̝̣͍̹̖̯͚͂͊̀̆͒̓̚͜ͅ_̶̞̱̥͖̤̣͓̬͈͚̫̼̼̩̲͆̈́͊̓̈̽̔̽̐̃͌̽́̀̚_̵̭͖̤̪̰̮͉̫͓̀͋̑͘☆
║╠═══════════════════
║╠[❂͜͡➣ line.me/ti/p/kibasz.com
║╚═══════════════════
╚════════════════════
"""
helo=""

KAC=[cl]
mid = cl.getProfile().mid

admin = []
targets = []
Bots = [mid]
creator = 'u52878991ac4ef532753e97a03e3b78ba'
admsa = 'u52878991ac4ef532753e97a03e3b78ba'
admin = 'u52878991ac4ef532753e97a03e3b78ba'
whitelist=[""]
wait = {
    'contact':False,
    'ricoinvite':True,
    'autoJoin':True,
    'autoCancel':{"on":False,"members":50},
    'AutoJoinCancel':True,
    'Admin':True,
    'Members':1,
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':True,
    'message':"Thanks For Add ☆_̶̧̎̀̂̅̊_̵̢̣̞̘̣̞̺̮͉͖̻̍̈́̎̓̔̐̐͗̒̃̏̕_̷̢̧̲͔̠̜͖͇̦̟̞̗̬̋̎̎͂͋͛͘K̵̛̮̣̞͕͔͕̺̹̳͒͌̀̾̅̔̚I̸̯̤̲͐̎͑̀̌̔̋̔̊̾̔̄́̃B̸̧̟̞͓̥̼͇̺̥̯̳͈͕̳͋͐̓̋̓̓͛͝A̶̙͖̋̿͒̈́̓̕͠Ş̶͕̫̳̝͎̥̥̩̃͗̑̉̅̇̓́̍͘͘͜͝͝_̷̯͇͇̝̣͍̹̖̯͚͂͊̀̆͒̓̚͜ͅ_̶̞̱̥͖̤̣͓̬͈͚̫̼̼̩̲͆̈́͊̓̈̽̔̽̐̃͌̽́̀̚_̵̭͖̤̪̰̮͉̫͓̀͋̑͘☆\n ҳ̸Ҳ̸ҳ •ᵤ'ᵤₛBₒₜ̰̈́• ҳ̸Ҳ̸ҳ\n✯==== Creator ====✯\nhttp://line.me/ti/p/kibasz.com",
    "lang":"JP",
    "comment":"Thanks For Add \n☆_̶̧̎̀̂̅̊_̵̢̣̞̘̣̞̺̮͉͖̻̍̈́̎̓̔̐̐͗̒̃̏̕_̷̢̧̲͔̠̜͖͇̦̟̞̗̬̋̎̎͂͋͛͘K̵̛̮̣̞͕͔͕̺̹̳͒͌̀̾̅̔̚I̸̯̤̲͐̎͑̀̌̔̋̔̊̾̔̄́̃B̸̧̟̞͓̥̼͇̺̥̯̳͈͕̳͋͐̓̋̓̓͛͝A̶̙͖̋̿͒̈́̓̕͠Ş̶͕̫̳̝͎̥̥̩̃͗̑̉̅̇̓́̍͘͘͜͝͝_̷̯͇͇̝̣͍̹̖̯͚͂͊̀̆͒̓̚͜ͅ_̶̞̱̥͖̤̣͓̬͈͚̫̼̼̩̲͆̈́͊̓̈̽̔̽̐̃͌̽́̀̚_̵̭͖̤̪̰̮͉̫͓̀͋̑͘☆\nҳ̸Ҳ̸ҳ •ᵤ'ᵤₛBₒₜ̰̈́• ҳ̸Ҳ̸ҳ\n✯==== Creator ====✯\nhttp://line.me/ti/p/kibasz.com",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cNames":"",
    "cNames":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":True,
    "cancelprotect":True,
    "inviteprotect":True,
    "linkprotect":True,
    "detectMention":True,
    "kickMention":False,
    "Backup":False,
    "Sider":{},
    "sticker":False,
    "Sambutan":True,
    "Copy":False,
}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    "ricoinvite":{},
    'ROM':{},
    }
 
mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

cctv = {
    "cyduk":{},
    "point":{},
    "MENTION":{},
    "sidermem":{}
}
    
settings = {
    "simiSimi":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
    }      
    
setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:  
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)   
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "u8ce99829a05fa1560a818f329645b264":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if wait["winvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 cl.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                              targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Done Invite: cah vekok \n[❂͜͡➣" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         cl.findAndAddContactsByMid(invite)
                                         cl.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         cl.sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam👈")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Itu tidak berkomentar👈")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada dalam daftar hitam👈")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done👈")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Help","help","Bajak"]:
            	if msg.from_ in admin:
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)         
            elif msg.text in ["Invite:on"]:
            	if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
            elif ("Gn:" in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok👈")
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn ","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Can not be used for groups other than")
            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "bot" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u4bb56a531d130346f66e7aa563b47bef'}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u927a5096a993f01570e0bde0a6a29ee6'}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u71f1c85a7624b1d54f941f72697977a9'}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'uf778dfbced75f3bbbe14207e4ea5abbf'}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'uf5b27b53eda88c30c1dc7875be2144b5'}
                cl.sendMessage(msg)
                msg.contentType = 13           
                msg.contentMetadata = {'mid': 'u67cfca7cd06d88bb5ab352576e1e3745'}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u52878991ac4ef532753e97a03e3b78ba'}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'uac6bfdc66b868a2b7b25f37b87bd203f'}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u22a8edcec7b333342aae8fa54576a933'}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'uf80d5d922be477642a2dfa563cdd1bd3'}
                cl.sendMessage(msg)
                msg.contentType = 13
               
            elif msg.text in ["Kibas1 Gift","Bot1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Kibas2 Gift","Bot2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)
                
            elif msg.text in ["Kibas3 Gift","Bot3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)
                
            elif msg.text in ["Kibas4 Gift","Bot4 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)
              
            elif msg.text in ["Kibas Cancel","Cancel dong","B cancel"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Davet yok😤")
                        else:
                            cl.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")

            elif msg.text in ["Cancel","cancel"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No is Invite✍😤")
                        else:
                            cl.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan👈")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")
            elif msg.text in ["Link on"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL on ✍")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group ô€œô€„‰👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œô€„‰")
            elif msg.text in ["Link off"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL Closed ✍")
                    else:
                        cl.sendText(msg.to,"URL Kapalí ✍")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group  👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œ")
            elif "Ginfo" == msg.text:
                ginfo = cl.getGroup(msg.to)
                try:
                    gCreator = ginfo.creator.displayName
                except:
                    gCreator = "Error"
                if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                cl.sendText(msg.to,"[Nama]\n" + str(ginfo.name) + "\n[Group Id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nAnggota:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")
                cl.sendMessage(msg)
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
            elif "Mymid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "TK:" in msg.text:
                tl_text = msg.text.replace("TK:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "All:" in msg.text:
                string = msg.text.replace("All:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
            elif "Allbio:" in msg.text:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
            elif "Myname:" in msg.text:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names👉 " + string + "👈")

#-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Cipok","Tag"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
#-------------Fungsi Tag All Finish---------------#

#---------------------------------------------------------
            elif "1name:" in msg.text:
                string = msg.text.replace("1name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif msg.text.lower() == 'respon':
                profile = cl.getProfile()
                text = profile.displayName + ""
                cl.sendText(msg.to, "☆_̶̧̎̀̂̅̊_̵̢̣̞̘̣̞̺̮͉͖̻̍̈́̎̓̔̐̐͗̒̃̏̕_̷̢̧̲͔̠̜͖͇̦̟̞̗̬̋̎̎͂͋͛͘K̵̛̮̣̞͕͔͕̺̹̳͒͌̀̾̅̔̚I̸̯̤̲͐̎͑̀̌̔̋̔̊̾̔̄́̃B̸̧̟̞͓̥̼͇̺̥̯̳͈͕̳͋͐̓̋̓̓͛͝A̶̙͖̋̿͒̈́̓̕͠Ş̶͕̫̳̝͎̥̥̩̃͗̑̉̅̇̓́̍͘͘͜͝͝_̷̯͇͇̝̣͍̹̖̯͚͂͊̀̆͒̓̚͜ͅ_̶̞̱̥͖̤̣͓̬͈͚̫̼̼̩̲͆̈́͊̓̈̽̔̽̐̃͌̽́̀̚_̵̭͖̤̪̰̮͉̫͓̀͋̑͘☆")
                profile = cl.getProfile()
                text = profile.displayName + ""
                ki2.sendText(msg.to, "☆_̶̧̎̀̂̅̊_̵̢̣̞̘̣̞̺̮͉͖̻̍̈́̎̓̔̐̐͗̒̃̏̕_̷̢̧̲͔̠̜͖͇̦̟̞̗̬̋̎̎͂͋͛͘K̵̛̮̣̞͕͔͕̺̹̳͒͌̀̾̅̔̚I̸̯̤̲͐̎͑̀̌̔̋̔̊̾̔̄́̃B̸̧̟̞͓̥̼͇̺̥̯̳͈͕̳͋͐̓̋̓̓͛͝A̶̙͖̋̿͒̈́̓̕͠Ş̶͕̫̳̝͎̥̥̩̃͗̑̉̅̇̓́̍͘͘͜͝͝_̷̯͇͇̝̣͍̹̖̯͚͂͊̀̆͒̓̚͜ͅ_̶̞̱̥͖̤̣͓̬͈͚̫̼̼̩̲͆̈́͊̓̈̽̔̽̐̃͌̽́̀̚_̵̭͖̤̪̰̮͉̫͓̀͋̑͘☆")
                profile = ki3.getProfile()
                text = profile.displayName + ""
                ki3.sendText(msg.to, "☆_̶̧̎̀̂̅̊_̵̢̣̞̘̣̞̺̮͉͖̻̍̈́̎̓̔̐̐͗̒̃̏̕_̷̢̧̲͔̠̜͖͇̦̟̞̗̬̋̎̎͂͋͛͘K̵̛̮̣̞͕͔͕̺̹̳͒͌̀̾̅̔̚I̸̯̤̲͐̎͑̀̌̔̋̔̊̾̔̄́̃B̸̧̟̞͓̥̼͇̺̥̯̳͈͕̳͋͐̓̋̓̓͛͝A̶̙͖̋̿͒̈́̓̕͠Ş̶͕̫̳̝͎̥̥̩̃͗̑̉̅̇̓́̍͘͘͜͝͝_̷̯͇͇̝̣͍̹̖̯͚͂͊̀̆͒̓̚͜ͅ_̶̞̱̥͖̤̣͓̬͈͚̫̼̼̩̲͆̈́͊̓̈̽̔̽̐̃͌̽́̀̚_̵̭͖̤̪̰̮͉̫͓̀͋̑͘☆")
                profile = ki4.getProfile()
                text = profile.displayName + ""
                ki4.sendText(msg.to, "☆_̶̧̎̀̂̅̊_̵̢̣̞̘̣̞̺̮͉͖̻̍̈́̎̓̔̐̐͗̒̃̏̕_̷̢̧̲͔̠̜͖͇̦̟̞̗̬̋̎̎͂͋͛͘K̵̛̮̣̞͕͔͕̺̹̳͒͌̀̾̅̔̚I̸̯̤̲͐̎͑̀̌̔̋̔̊̾̔̄́̃B̸̧̟̞͓̥̼͇̺̥̯̳͈͕̳͋͐̓̋̓̓͛͝A̶̙͖̋̿͒̈́̓̕͠Ş̶͕̫̳̝͎̥̥̩̃͗̑̉̅̇̓́̍͘͘͜͝͝_̷̯͇͇̝̣͍̹̖̯͚͂͊̀̆͒̓̚͜ͅ_̶̞̱̥͖̤̣͓̬͈͚̫̼̼̩̲͆̈́͊̓̈̽̔̽̐̃͌̽́̀̚_̵̭͖̤̪̰̮͉̫͓̀͋̑͘☆")
                profile = ki5.getProfile()
                text = profile.displayName + ""
                ki5.sendText(msg.to, "☆_̶̧̎̀̂̅̊_̵̢̣̞̘̣̞̺̮͉͖̻̍̈́̎̓̔̐̐͗̒̃̏̕_̷̢̧̲͔̠̜͖͇̦̟̞̗̬̋̎̎͂͋͛͘K̵̛̮̣̞͕͔͕̺̹̳͒͌̀̾̅̔̚I̸̯̤̲͐̎͑̀̌̔̋̔̊̾̔̄́̃B̸̧̟̞͓̥̼͇̺̥̯̳͈͕̳͋͐̓̋̓̓͛͝A̶̙͖̋̿͒̈́̓̕͠Ş̶͕̫̳̝͎̥̥̩̃͗̑̉̅̇̓́̍͘͘͜͝͝_̷̯͇͇̝̣͍̹̖̯͚͂͊̀̆͒̓̚͜ͅ_̶̞̱̥͖̤̣͓̬͈͚̫̼̼̩̲͆̈́͊̓̈̽̔̽̐̃͌̽́̀̚_̵̭͖̤̪̰̮͉̫͓̀͋̑͘☆")
                profile = ki6.getProfile()
                text = profile.displayName + ""
                ki6.sendText(msg.to, "☆_̶̧̎̀̂̅̊_̵̢̣̞̘̣̞̺̮͉͖̻̍̈́̎̓̔̐̐͗̒̃̏̕_̷̢̧̲͔̠̜͖͇̦̟̞̗̬̋̎̎͂͋͛͘K̵̛̮̣̞͕͔͕̺̹̳͒͌̀̾̅̔̚I̸̯̤̲͐̎͑̀̌̔̋̔̊̾̔̄́̃B̸̧̟̞͓̥̼͇̺̥̯̳͈͕̳͋͐̓̋̓̓͛͝A̶̙͖̋̿͒̈́̓̕͠Ş̶͕̫̳̝͎̥̥̩̃͗̑̉̅̇̓́̍͘͘͜͝͝_̷̯͇͇̝̣͍̹̖̯͚͂͊̀̆͒̓̚͜ͅ_̶̞̱̥͖̤̣͓̬͈͚̫̼̼̩̲͆̈́͊̓̈̽̔̽̐̃͌̽́̀̚_̵̭͖̤̪̰̮͉̫͓̀͋̑͘☆")
                profile = ki7.getProfile()
                text = profile.displayName + ""
                ki7.sendText(msg.to, "☆_̶̧̎̀̂̅̊_̵̢̣̞̘̣̞̺̮͉͖̻̍̈́̎̓̔̐̐͗̒̃̏̕_̷̢̧̲͔̠̜͖͇̦̟̞̗̬̋̎̎͂͋͛͘K̵̛̮̣̞͕͔͕̺̹̳͒͌̀̾̅̔̚I̸̯̤̲͐̎͑̀̌̔̋̔̊̾̔̄́̃B̸̧̟̞͓̥̼͇̺̥̯̳͈͕̳͋͐̓̋̓̓͛͝A̶̙͖̋̿͒̈́̓̕͠Ş̶͕̫̳̝͎̥̥̩̃͗̑̉̅̇̓́̍͘͘͜͝͝_̷̯͇͇̝̣͍̹̖̯͚͂͊̀̆͒̓̚͜ͅ_̶̞̱̥͖̤̣͓̬͈͚̫̼̼̩̲͆̈́͊̓̈̽̔̽̐̃͌̽́̀̚_̵̭͖̤̪̰̮͉̫͓̀͋̑͘☆")
                profile = ki8.getProfile()
                text = profile.displayName + ""
                ki8.sendText(msg.to, "☆_̶̧̎̀̂̅̊_̵̢̣̞̘̣̞̺̮͉͖̻̍̈́̎̓̔̐̐͗̒̃̏̕_̷̢̧̲͔̠̜͖͇̦̟̞̗̬̋̎̎͂͋͛͘K̵̛̮̣̞͕͔͕̺̹̳͒͌̀̾̅̔̚I̸̯̤̲͐̎͑̀̌̔̋̔̊̾̔̄́̃B̸̧̟̞͓̥̼͇̺̥̯̳͈͕̳͋͐̓̋̓̓͛͝A̶̙͖̋̿͒̈́̓̕͠Ş̶͕̫̳̝͎̥̥̩̃͗̑̉̅̇̓́̍͘͘͜͝͝_̷̯͇͇̝̣͍̹̖̯͚͂͊̀̆͒̓̚͜ͅ_̶̞̱̥͖̤̣͓̬͈͚̫̼̼̩̲͆̈́͊̓̈̽̔̽̐̃͌̽́̀̚_̵̭͖̤̪̰̮͉̫͓̀͋̑͘☆")
                profile = ki9.getProfile()
                text = profile.displayName + ""
                ki9.sendText(msg.to, "☆_̶̧̎̀̂̅̊_̵̢̣̞̘̣̞̺̮͉͖̻̍̈́̎̓̔̐̐͗̒̃̏̕_̷̢̧̲͔̠̜͖͇̦̟̞̗̬̋̎̎͂͋͛͘K̵̛̮̣̞͕͔͕̺̹̳͒͌̀̾̅̔̚I̸̯̤̲͐̎͑̀̌̔̋̔̊̾̔̄́̃B̸̧̟̞͓̥̼͇̺̥̯̳͈͕̳͋͐̓̋̓̓͛͝A̶̙͖̋̿͒̈́̓̕͠Ş̶͕̫̳̝͎̥̥̩̃͗̑̉̅̇̓́̍͘͘͜͝͝_̷̯͇͇̝̣͍̹̖̯͚͂͊̀̆͒̓̚͜ͅ_̶̞̱̥͖̤̣͓̬͈͚̫̼̼̩̲͆̈́͊̓̈̽̔̽̐̃͌̽́̀̚_̵̭͖̤̪̰̮͉̫͓̀͋̑͘☆")
                profile = ki10.getProfile()
                text = profile.displayName + ""
                ki10.sendText(msg.to, "☆_̶̧̎̀̂̅̊_̵̢̣̞̘̣̞̺̮͉͖̻̍̈́̎̓̔̐̐͗̒̃̏̕_̷̢̧̲͔̠̜͖͇̦̟̞̗̬̋̎̎͂͋͛͘K̵̛̮̣̞͕͔͕̺̹̳͒͌̀̾̅̔̚I̸̯̤̲͐̎͑̀̌̔̋̔̊̾̔̄́̃B̸̧̟̞͓̥̼͇̺̥̯̳͈͕̳͋͐̓̋̓̓͛͝A̶̙͖̋̿͒̈́̓̕͠Ş̶͕̫̳̝͎̥̥̩̃͗̑̉̅̇̓́̍͘͘͜͝͝_̷̯͇͇̝̣͍̹̖̯͚͂͊̀̆͒̓̚͜ͅ_̶̞̱̥͖̤̣͓̬͈͚̫̼̼̩̲͆̈́͊̓̈̽̔̽̐̃͌̽́̀̚_̵̭͖̤̪̰̮͉̫͓̀͋̑͘☆")
#--------------------------------------------------------                
#==============================================================================#
            elif msg.text in ["Set all on"]:
		if msg.from_ in admsa:
                    wait["protect"] = True
                    wait["cancelprotect"] = True
                    wait["inviteprotect"] = True
                    wait["linkprotect"] = True
                    wait["Backup"] = True
                    wait["Contact"] = True
                    wait["Sambutan"] = True
                    cl.sendText(msg.to,"ᴬˡˡ ᴿᵉᵃᵈʸ ˢᵉᵗᵗᶦⁿᵍ ᴵⁿ ᴬᶜᵗᶦᵛᵉ")
		else:
		    cl.sendText(msg.to,"Khusus kibas")

            elif msg.text in ["Set all off"]:
		if msg.from_ in admsa:
                    wait["protect"] = False
                    wait["cancelprotect"] = False
                    wait["inviteprotect"] = False
                    wait["linkprotect"] = False
                    wait["Backup"] = False
                    wait["Contact"] = False
                    wait["Sambutan"] = False
                    cl.sendText(msg.to,"ᴬˡˡ ᴿᵉᵃᵈʸ ˢᵉᵗᵗᶦⁿᵍ ᴰᶦˢᵃᵇˡᵉ")
		else:
		    cl.sendText(msg.to,"Khusus kibas")
#==============================================================================#
            elif "Nk " in msg.text:
              if msg.from_ in admin:
                nk0 = msg.text.replace("Nk ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("@","")
                nk3 = nk2.rstrip()
                _name = nk3
                gs = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                gs.preventJoinByTicket = False
                cl.updateGroup(gs)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                w1.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                targets = []
                for s in gs.members:
                    if _name in s.displayName:
                       targets.append(s.mid)
                if targets == []:
                   sendMessage(msg.to,"user does not exist")
                   pass
                else:
                   for target in targets:
                      try:
                        w1.kickoutFromGroup(msg.to,[target])
                        print (msg.to,[g.mid])
                      except:
                        w1.leaveGroup(msg.to)
                        gs = cl.getGroup(msg.to)
                        gs.preventJoinByTicket = True
                        cl.updateGroup(gs)
                        gs.preventJoinByTicket(gs)
                        cl.updateGroup(gs)
#==============================================================================#
            elif "Mid:" in msg.text:
                mmid = msg.text.replace("Mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact Oke ✍")
                    else:
                        cl.sendText(msg.to,"It is already open")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already open 👈")
                    else:
                        cl.sendText(msg.to,"It is already open 􀜁􀇔􏿿")
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"sudah off ô€œô€„‰👈")
                    else:
                        cl.sendText(msg.to,"It is already off ô€œô€„‰👈")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"off ô€œô€„‰already")
                    else:
                        cl.sendText(msg.to,"already Close ô€œô€„‰👈")
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᶜᵒⁿᵗᵃᶜᵗ ᴿᵉᵃᵈʸ ᵒⁿ")
                    else:
                        cl.sendText(msg.to,"ᶜᵒⁿᵗᵃᶜᵗ ᴿᵉᵃᵈʸ ᵒⁿ")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬˡˡ ᴿᵉᵃᵈʸ")
                    else:
                        cl.sendText(msg.to,"ᴬˡˡ ᴿᵉᵃᵈʸ")
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴿᵉᵃᵈʸ ᵒᶠᶠ")
                    else:
                        cl.sendText(msg.to,"ᴿᵉᵃᵈʸ ᵒᶠᶠ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"off ô€œô€„‰already")
                    else:
                        cl.sendText(msg.to,"already Close ô€œô€„‰👈")
            elif msg.text.lower() == 'protect on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴿᵉᵃᵈʸ ᴾʳᵒᵗᵉᶜᵗ ᴬᶜᵗᶦᵛᵉᵈ")
                    else:
                        cl.sendText(msg.to,"ᴿᵉᵃᵈʸ ᴾʳᵒᵗᵉᶜᵗ ᴬᶜᵗᶦᵛᵉᵈ")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴿᵉᵃᵈʸ ᴾʳᵒᵗᵉᶜᵗ ᴬᶜᵗᶦᵛᵉᵈ")
                    else:
                        cl.sendText(msg.to,"ᴿᵉᵃᵈʸ ᴾʳᵒᵗᵉᶜᵗ ᴬᶜᵗᶦᵛᵉᵈ")
            elif msg.text.lower() == 'qrprotect on':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴸᶦⁿᵏ ᴾʳᵒᵗᵉᶜᵗ ᴬᶜᵗᶦᵛᵉᵈ")
                    else:
                        cl.sendText(msg.to,"ᴸᶦⁿᵏ ᴾʳᵒᵗᵉᶜᵗ ᴬᶜᵗᶦᵛᵉᵈ")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴸᶦⁿᵏ ᴾʳᵒᵗᵉᶜᵗ ᴬᶜᵗᶦᵛᵉᵈ")
                    else:
                        cl.sendText(msg.to,"ᴸᶦⁿᵏ ᴾʳᵒᵗᵉᶜᵗ ᴬᶜᵗᶦᵛᵉᵈ")
            elif msg.text.lower() == 'inviteprotect on':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
                    else:
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
                    else:
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
            elif msg.text.lower() == 'cancelprotect on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᶜᵃⁿᶜᵉˡ ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
                    else:
                        cl.sendText(msg.to,"ᶜᵃⁿᶜᵉˡ ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᶜᵃⁿᶜᵉˡ ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
                    else:
                        cl.sendText(msg.to,"ᶜᵃⁿᶜᵉˡ ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
            elif msg.text.lower() == 'auto join on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴶᵒᶦⁿ ᴿᵉᵃᵈʸ ᴬᶜᵗᶦᵛᵉ")
                    else:
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴶᵒᶦⁿ ᴿᵉᵃᵈʸ ᴬᶜᵗᶦᵛᵉ")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴶᵒᶦⁿ ᴿᵉᵃᵈʸ ᴬᶜᵗᶦᵛᵉ")
                    else:
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴶᵒᶦⁿ ᴿᵉᵃᵈʸ ᴬᶜᵗᶦᵛᵉ")
            elif msg.text in ["Allprotect on","Panick:on"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
                    else:
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
                    else:
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᶜᵃⁿᶜᵉˡ ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᶜᵃⁿᶜᵉˡ ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
                    else:
                        cl.sendText(msg.to,"ᶜᵃⁿᶜᵉˡ ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
                    else:
                        cl.sendText(msg.to,"ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ ᴬᶜᵗᶦᵛᵉ")
                    else:
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ ᴬᶜᵗᶦᵛᵉ")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ ᴬᶜᵗᶦᵛᵉ")
                    else:
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ ᴬᶜᵗᶦᵛᵉ")
            elif msg.text in ["Allprotect off","Panick:off"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᶜᵃⁿᶜᵉˡ ᴰᶦˢᵃᵇˡᵉ")
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
            elif msg.text.lower() == 'auto join off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴶᵒᶦⁿ ᵈᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴶᵒᶦⁿ ᵈᶦˢᵃᵇˡᵉ")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴶᵒᶦⁿ ᵈᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴶᵒᶦⁿ ᵈᶦˢᵃᵇˡᵉ")
            elif msg.text in ["Protect off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
            elif msg.text in ["Qrprotect off","qrprotect off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
            elif msg.text in ["Inviteprotect off"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
            elif msg.text in ["Cancelprotect off"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᶜᵃⁿᶜᵉˡ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᶜᵃⁿᶜᵉˡ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᶜᵃⁿᶜᵉˡ ᴰᶦˢᵃᵇˡᵉ")
            elif "Group cancel: " in msg.text:
                try:
                    strnum = msg.text.replace("Group cancel: ","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Itu off undangan ditolak👈\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan👈")
                        else:
                            cl.sendText(msg.to,"Off undangan ditolak👈Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis👈")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Nilai tidak benar👈")
                    else:
                        cl.sendText(msg.to,"Weird value🛡")
            elif msg.text in ["Leave on","Auto leave: on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬˡʳᵉᵃᵈʸ ᵃᶜᵗᶦᵛᵉ")
                    else:
                        cl.sendText(msg.to,"ᴬˡʳᵉᵃᵈʸ ᵃᶜᵗᶦᵛᵉ")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬˡʳᵉᵃᵈʸ ᵃᶜᵗᶦᵛᵉ")
                    else:
                        cl.sendText(msg.to,"ᴬˡʳᵉᵃᵈʸ ᵃᶜᵗᶦᵛᵉ")
            elif msg.text in ["Leave off","Auto leave: off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴸᵉᵃᵛᵉ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴸᵉᵃᵛᵉ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴸᵉᵃᵛᵉ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴸᵉᵃᵛᵉ ᴰᶦˢᵃᵇˡᵉ")
            elif msg.text in ["Share on","share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵃᶜᵗᶦᵛᵉ")
                    else:
                        cl.sendText(msg.to,"ᵃᶜᵗᶦᵛᵉ")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵃᶜᵗᶦᵛᵉ")
                    else:
                        cl.sendText(msg.to,"ᵃᶜᵗᶦᵛᵉ")
            elif msg.text in ["Share off","share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
            elif msg.text.lower() == 'set':
                md = "╔═══════════════════════\n║        _̵̡͎̦͈͉͍̱̠͔̟͕̹͋͗̐̎͂̂͊̈͋̊̃̎ͅ_̶̳́̋̓̊̎̽̒̽̏̆͂͗̉̏̕_̷̡̘͕̪̥͙̙͉̳̆̉̕͜ͅS̴̼̣͖͒T̴̢̬̪̼̠̼̩̼̻̉͆͛̐A̴̦̙͙͛̈́͌́̒͊̿̏̄̈́̐̓͘T̵̨̛̰̱̻̞̻͕̞̀͂͜ͅŲ̵̤̜͓̲̩̞͖̪̩̘̭̽̄̚͜Ş̶̝̝̯͓̘̙̹̤̙͕͍́͛͜ ̸̜͍̤͎̺̰̺̍P̵̛̖̯͇͎̳̟̝͋͗̚͝͠R̶̨̢̮͍̺͔͔̳̟̙͚̪̓Ơ̵̡̪̤͈̹̬̰̌͌͑̉͂͑̚͠T̴͙̪͍̰͇̬̙̪͗́̂̅̃̅̃̔͝͠E̴̫̣̯͎̞͚̥̠͎̣̞̗̚C̵̟̟͙̘͊̇̏T̴̠̰̻͇̗̙̞͓͙̄̇̅̆̒̀͋̓̌̐͑̒̓_̶̖̝̞̼͈̪͐͌̇͂̈́̈́̆̍̕̕͠͝ͅ_̴̧͕̰̻͔̞̭͙̱̥͙̒̓̊̌͂͆̊̾̒̉̋͗͘͜͜͠͝_̷͖̱͊͒́̀̈́̀̾̄͂̉̋̾̂͝ͅ\n╠═══════════════════════\n║╔═══════════════════════\n"                
                if wait["Backup"] == True: md+="║╠[❂͜͡➣ Bᴀᴄᴋᴜᴘ :on ✔\n"
                else: md+="║╠[❂͜͡➣ Bᴀᴄᴋᴜᴘ:off✘\n"
                if wait["contact"] == True: md+="║╠[❂͜͡➣ Contact:on ✔\n"
                else: md+="║╠[❂͜͡➣ Contact:off✘\n"
                if wait["autoJoin"] == True: md+="║╠[❂͜͡➣ Auto Join:on ✔\n"
                else: md +="║╠[❂͜͡➣ Auto Join:off ✘\n"
                if wait["autoCancel"]["on"] == True:md+="║╠[❂͜͡➣ Auto cancel:" + str(wait["autoCancel"]["members"]) + "✔"
                else: md+= "║╠[❂͜͡➣ Group cancel:off ✘\n"
                if wait["leaveRoom"] == True: md+="║╠[❂͜͡➣ Auto leave:on ✔\n"
                else: md+="║╠[❂͜͡➣ Auto leave:off ✘\n"
                if wait["timeline"] == True: md+="║╠[❂͜͡➣ Share:on ✔\n"
                else:md+="║╠[❂͜͡➣ Share:off ✘\n"
                if wait["autoAdd"] == True: md+="║╠[❂͜͡➣ Auto add:on ✔\n"
                else:md+="║╠[❂͜͡➣ Auto add:off ✘\n"
                if wait["protect"] == True: md+="║╠[❂͜͡➣ Protect:on ✔\n"
                else:md+="║╠[❂͜͡➣ Protect:off ✘\n"
                if wait["linkprotect"] == True: md+="║╠[❂͜͡➣ Link Protect:on ✔\n"
                else:md+="║╠[❂͜͡➣ Link Protect:off ✘\n"
                if wait["inviteprotect"] == True: md+="║╠[❂͜͡➣ Invitation Protect:on ✔\n"
                else:md+="║╠[❂͜͡➣ Invitation Protect:off ✘\n"
                if wait["cancelprotect"] == True: md+="║╠[❂͜͡➣ Cancel Protect:on ✔\n╠═══════════════════════\n║[❂͜͡➣¢яєαтσя:~☆_̶̧̎̀̂̅̊_̵̢̣̞̘̣̞̺̮͉͖̻̍̈́̎̓̔̐̐͗̒̃̏̕_̷̢̧̲͔̠̜͖͇̦̟̞̗̬̋̎̎͂͋͛͘K̵̛̮̣̞͕͔͕̺̹̳͒͌̀̾̅̔̚I̸̯̤̲͐̎͑̀̌̔̋̔̊̾̔̄́̃B̸̧̟̞͓̥̼͇̺̥̯̳͈͕̳͋͐̓̋̓̓͛͝A̶̙͖̋̿͒̈́̓̕͠Ş̶͕̫̳̝͎̥̥̩̃͗̑̉̅̇̓́̍͘͘͜͝͝_̷̯͇͇̝̣͍̹̖̯͚͂͊̀̆͒̓̚͜ͅ_̶̞̱̥͖̤̣͓̬͈͚̫̼̼̩̲͆̈́͊̓̈̽̔̽̐̃͌̽́̀̚_̵̭͖̤̪̰̮͉̫͓̀͋̑͘☆\n║[❂͜͡➣ line.me/ti/p/kibaz.com\n╚═══════════════════════"
                else:md+="║╠[❂͜͡➣ Cancel Protect:off ✘\n╠═══════════════════════\n║[❂͜͡➣ãküCãhKērjø:~☆_̶̧̎̀̂̅̊_̵̢̣̞̘̣̞̺̮͉͖̻̍̈́̎̓̔̐̐͗̒̃̏̕_̷̢̧̲͔̠̜͖͇̦̟̞̗̬̋̎̎͂͋͛͘K̵̛̮̣̞͕͔͕̺̹̳͒͌̀̾̅̔̚I̸̯̤̲͐̎͑̀̌̔̋̔̊̾̔̄́̃B̸̧̟̞͓̥̼͇̺̥̯̳͈͕̳͋͐̓̋̓̓͛͝A̶̙͖̋̿͒̈́̓̕͠Ş̶͕̫̳̝͎̥̥̩̃͗̑̉̅̇̓́̍͘͘͜͝͝_̷̯͇͇̝̣͍̹̖̯͚͂͊̀̆͒̓̚͜ͅ_̶̞̱̥͖̤̣͓̬͈͚̫̼̼̩̲͆̈́͊̓̈̽̔̽̐̃͌̽́̀̚_̵̭͖̤̪̰̮͉̫͓̀͋̑͘☆\n║[❂͜͡➣ line.me/ti/p/suuu_trisno22\n╚═══════════════════════"
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendMessage(msg)
            
            elif msg.text in ["Like:on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᶜᵗᶦᵛᵉᵈ")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᶜᵗᶦᵛᵉᵈ")
            elif msg.text in ["いいね:オフ","Like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
                        
            elif msg.text in ["Add on","Add auto on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᶜᵗᶦᵛᵉᵈ")
                    else:
                        cl.sendText(msg.to,"ᴬᶜᵗᶦᵛᵉᵈ")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᶜᵗᶦᵛᵉᵈ")
                    else:
                        cl.sendText(msg.to,"ᴬᶜᵗᶦᵛᵉᵈ")
            elif msg.text in ["Add off","Add auto off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"Untuk mengaktifkan-off👈")
            elif "Message set: " in msg.text:
                wait["message"] = msg.text.replace("Message set: ","")
                cl.sendText(msg.to,"We changed the message👈")
            elif "Help set: " in msg.text:
                wait["help"] = msg.text.replace("Help set: ","")
                cl.sendText(msg.to,"We changed the Help👈")
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendText(msg.to,"􀜁􀇔􏿿 My Creator 􀜁􀇔􏿿 ")
                cl.sendMessage(msg)
                cl.sendText(msg.to,"􀜁􀇔􏿿 Dont Kick out From group 􀜁􀇔􏿿")
            elif msg.text in ["Auto add on","Add auto on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On")
                    else:
                        cl.sendText(msg.to,"Already On👈")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On👈")
                    else:
                        cl.sendText(msg.to,"Already On👈")
            elif msg.text in ["Auto add off","Add auto off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah dimatikan👈")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already Off👈")
                    else:
                        cl.sendText(msg.to,"Untuk mengaktifkan-off👈")
            elif "Message set:" in msg.text:
                wait["message"] = msg.text.replace("Message set:","")
                cl.sendText(msg.to,"We changed the message👈")
            elif "Help set:" in msg.text:
                wait["help"] = msg.text.replace("Help set:","")
                cl.sendText(msg.to,"We changed the Help👈")
            elif "Pesan add-" in msg.text:
                wait["message"] = msg.text.replace("Pesan add-","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Kami mengubah pesan🛡")
                else:
                    cl.sendText(msg.to,"Change information")
            elif msg.text in ["Pesan add cek","Message Confirmation"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Additional information is automatically set to the following \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif msg.text in ["Change","change"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"I changed the language to engglis👈")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,"I changed the language to indonesia👈")
            elif "Message set" in msg.text:
                c = msg.text.replace("Message set","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Is a string that can not be changed👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"This has been changed👈\n\n" + c)
            elif "Come Set:" in msg.text:
                c = msg.text.replace("Come Set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Com on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aku berada di👈")
                    else:
                        cl.sendText(msg.to,"To open👈")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ã‚ªãƒ³ã«ã—ã¾ã—ãŸ👈")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€👈")
            elif msg.text in ["Come off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Come off")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"To turn off")
            elif msg.text in ["Com","Comment"]:
                cl.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:👈\n\n" + str(wait["comment"]))
            elif msg.text in ["url","Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Kibas gurl" in msg.text:
                if msg.toType == 1:
                    gid = msg.text.replace("gurl","")
                    gurl = cl.reissueGroupTicket(tid)
                    cl.sendText(msg.to,"line://ti/p" + turl)
                else:
                    cl.sendText(msg.to,"error")

            elif "gurl" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text in ["Com Bl"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the blacklistô€œô€…”👈")
            elif msg.text in ["Com hapus Bl"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the blacklistô€œô€…”👈")
            elif msg.text in ["Com Bl cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklistô€œ🛡")
                else:
                    cl.sendText(msg.to,"The following is a blacklistô€œ👈")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Sudah On")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"👉Jam on👈")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Hal ini sudah off🛡")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"Adalah Off")
            elif "Jam say:" in msg.text:
                n = msg.text.replace("Jam say:","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Ini telah diubah🛡\n\n" + n)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Diperbarui👈")
                else:
                    cl.sendText(msg.to,"Silahkan Aktifkan Nama")

            elif "Nk " in msg.text:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = True
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki3.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)

            elif msg.text == "Sider":
                    cl.sendText(msg.to, "hmm..jangan suka\nngintip² ntar tak ciduk loo")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    print wait2

            elif msg.text == "Read":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "== Bakekok Sider == %s\nthat's it\n\nPeople who have ignored reads\n%skampret lo sider. ♪\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")						
#-----------------------------------------------------------

            elif ("Vk " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            elif ("Contact " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)
#----------------------------------------------------------------
            elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                #Vicky Kull~
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")

            elif "Spm @" in msg.text:
                _name = msg.text.replace("Spm @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki2.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki3.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki4.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki5.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki6.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki7.sendText(g.mid,"Spam by _̵̛̜̘͖̄͛̽̂̾̄͗̀̎́͌_̷̡̗̭͓̜̯͍̠̓́_̶̡͖͓͙̫̈́̾͒͌͛̌̏̕̕Ṉ̵̜̯̱̳͓͕͎͔̠̼̲̐͆̍̅̃̉̈́̓͝Ȩ̸̭̪͔̘̣͇̯̬̦̼̼͛̈́̾̎̂̄̈́͐̓̽͊̂̕W̷̰̽̅̄̊̊̅̀̎̚ ̷̡̩̭̼̰̖̯̫̐̾̈́͝͠Ḱ̷̡̢̲̬̻̣͙̜̫̹͐͐̒̑̄͘͘͘Į̵̛̝͖̊͆̈́̓̍̈́̍̌͌͗̒̾͑̚B̶̬̬̩̹͙͈̜͖̘͇̬͚̯͙͒̓̉̂̈́̈́́́̈́͋̿̀̇͜A̴̡͙̽͊̃̀̊͒̌̈́̐̕͝S̵̨̰̥̺̼͓̖̹͔͎̉̒̆̄̏͛͜ͅ_̶̨̡͙͈͈̈́̀͆̄͐̓̎̃̚͘͜_̴̧̨̪͉̼̙̗̝̣̯͚͕̑͆͆̆̍̐̏́̇̽̚̕͝_̸̙͖̦̪̠̮͈͓̞͓̣̳́̓̎̈́̏̔̂͗͂̓̽͗͒̆̏ͅ hex bot")
                       ki.sendText(msg.to, "Done")
                       ki2.sendText(msg.to, "Done")
                       ki3.sendText(msg.to, "Done")
                       ki4.sendText(msg.to, "Done")
                       ki5.sendText(msg.to, "Done")
                       ki6.sendText(msg.to, "Done")
                       ki7.sendText(msg.to, "Done")
                       print " Spammed !"

            elif "Hallo " in msg.text:
                midd = msg.text.replace("Hallo ","")
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       ki.sendText(g.mid,[miid] + "Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")  
                       ki3.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")  
                       ki4.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")  
                       ki6.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")  
                       ki7.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")
                       ki.sendText(msg.to, "Done")
                       ki2.sendText(msg.to, "Done")
                       ki3.sendText(msg.to, "Done")
                       ki4.sendText(msg.to, "Done")
                       ki5.sendText(msg.to, "Done")
                       ki6.sendText(msg.to, "Done")
                       ki7.sendText(msg.to, "Done")
                       print " Spammed !"
#-----------------------------------------------------------)
            elif "Promo" in msg.text:
                if msg.from_ in admin:
                    cl.sendText(msg.to,"╔═════════════════════\n║ ☀☫ȗ̸̥̩͕͈̺̭͍̠̫̇̑̃̽̈̇̆͆u̸̢̼͔͍͍̲͈͒̒́̇̌̑͆̃͞s̴̢͇̝͚̜̳̪̆́̆͗̕ B͇̗̟͚̲̰̣̔̀̃͊͗̈̕͟ͅỏ̦̫͍̟̥̜̝̑̀̉͌́̈́̕͝t̵̢̛̰̫̮̩̦͕̍̑̍͘s͕̦͚͖̄̔͊̀͑̾͌͘͘͟͡☫☀\n║™σρєη σя∂єя™«\n╠═════════════════════\n╠➩☬ѕєℓƒтвσт σηℓу\n╠➩☬ѕєℓƒтвσт + αѕιѕт\n╠➩☬1 αкυη υтαмα    \n╠➩☬1αкυη υтαмα + 2 αѕιѕт \n╠➩☬1αкυη υтαмα + 3 αѕιѕт \n╠➩☬1αкυη υтαмα + 4 αѕιѕт \n╠➩☬1αкυη υтαмα  + 5 αѕιѕт \n╠➩☬ρяσтє¢твσт 3-20 вσт αѕѕιѕт \n╠═════════════════════\n║     ☟ мιηαт ѕιℓαнαη нυв☟\n╠➩line://ti/p/~eddie.thansild.com\n╠➩line://ti/p/~suuu_trisno23\n╠➩line://ti/p/~bayuapoy.com\n╠➩TERIMAKASIH\n║═════════════════════\n╠➩C̽̅̈́̅ŕ̛̋͛e͛̃̾̍ǻ̕͘t͒̉̈̎o͊̓̌͠r̐̇̾̐ B̝̪̭͓͍̺͐͂̑̅̓͗͗̈́͢y͚͔̝͖̮̤͚̅̉̑̐̓̀̋̊͂͜͜͢͞:̨̻̪͓̦̻̋̾̂̽̎͘͜͜ > B̷̭͖̯͉̲͛̍̃̒͐̂͘͟r̨̟̖͕̬̳͓̖̈́̈́̇̈́̂̄̕̚͞͠o͍͍̬̼̥̺̣̯̻̣̿̏͒͊̾̔k̩͚̪̙̹̭͇̈́͂̾̏̋̽̂́͝ǫ̶̨̧̺̫͚͙̤̥͇̃́͆̎͐̔̌̃̒͑L̸̨̟͇͉̦̠̺̇̽̈́̓̊̕͟͢͞L͖̲̦̰̼̳̝͒́͌͒͂͑͋̕̚͜͟i̧̨͕̘͍̦͕̽̓̆̓̆͘͟~ery ༻>\n║ ═════════════════════\n║\n╠➩☆°̙̲̖̤͖̻̎̃̉̂͝ͅ°̷̡̨̤̳̼̹͎̔̾͐̽̉̏͛̏͌°̷̧̡̗̹̯̳̰̦̦͌͂̏̾͒Ù̴̪͈̣̹̮̮̀́̿̊̉̈́͊͘͘Ú͇̬̬̥͕̅͐͌͊͑̂̓̽§̵̧̛̯̟̥̦̞̃͋̓̏͘͡ B̷̲̬͇̥̼̈̀͑̀̊͛̀͘͝ͅØ͈͉̦͕͉͉̓͗́͌̊͆̆̚͡ͅT̴̪̞͕͎̗̫̤̻͈̐̾̑͌͠Š̴̻̹͖̘̺̫̹̱̫̩̎̒̔͌̔̄̔̓͠°̨͔̱̭̘̝̘͐̉͊̐́ͅ°̛͎̲͉̠̙̙̬͆͌͒̀͋͟͠͝ͅ°͕̞͎̰͎̭̘͇̑̓̌̀̔̇̀͟☆~ℬåᎫäʞ.ïđ\n║ ═════════════════════\n╠➩ Support By: χχχ==вσтρяσтє¢т==χχχ\n╚══════════════════════")               
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': admsa}
                    tanya = msg.text.replace("Promo ","")
                    jawab = ("╔═════════════════════\n║ ☀☫ȗ̸̥̩͕͈̺̭͍̠̫̇̑̃̽̈̇̆͆u̸̢̼͔͍͍̲͈͒̒́̇̌̑͆̃͞s̴̢͇̝͚̜̳̪̆́̆͗̕ B͇̗̟͚̲̰̣̔̀̃͊͗̈̕͟ͅỏ̦̫͍̟̥̜̝̑̀̉͌́̈́̕͝t̵̢̛̰̫̮̩̦͕̍̑̍͘s͕̦͚͖̄̔͊̀͑̾͌͘͘͟͡☫☀\n║™σρєη σя∂єя™«\n╠═════════════════════\n╠➩☬ѕєℓƒтвσт σηℓу\n╠➩☬ѕєℓƒтвσт + αѕιѕт\n╠➩☬1 αкυη υтαмα   \n╠➩☬1αкυη υтαмα + 2 αѕιѕт \n╠➩☬1αкυη υтαмα + 3 αѕιѕт \n╠➩☬1αкυη υтαмα + 4 αѕιѕт \n╠➩☬1αкυη υтαмα  + 5 αѕιѕт \n╠➩☬ρяσтє¢твσт 3-20 вσт αѕѕιѕт \n╠═════════════════════\n║     ☟ мιηαт ѕιℓαнαη нυв☟\n╠➩line://ti/p/~eddie.thansild.com\n╠➩line://ti/p/~suuu_trisno23\n╠➩line://ti/p/~bayuapoy.com\n╠➩TERIMAKASIH\n║\n║═════════════════════\n╠➩C̽̅̈́̅ŕ̛̋͛e͛̃̾̍ǻ̕͘t͒̉̈̎o͊̓̌͠r̐̇̾̐ B̝̪̭͓͍̺͐͂̑̅̓͗͗̈́͢y͚͔̝͖̮̤͚̅̉̑̐̓̀̋̊͂͜͜͢͞:̨̻̪͓̦̻̋̾̂̽̎͘͜͜ > B̷̭͖̯͉̲͛̍̃̒͐̂͘͟r̨̟̖͕̬̳͓̖̈́̈́̇̈́̂̄̕̚͞͠o͍͍̬̼̥̺̣̯̻̣̿̏͒͊̾̔k̩͚̪̙̹̭͇̈́͂̾̏̋̽̂́͝ǫ̶̨̧̺̫͚͙̤̥͇̃́͆̎͐̔̌̃̒͑L̸̨̟͇͉̦̠̺̇̽̈́̓̊̕͟͢͞L͖̲̦̰̼̳̝͒́͌͒͂͑͋̕̚͜͟i̧̨͕̘͍̦͕̽̓̆̓̆͘͟~ery༻>\n║ ══════════════════════\n║\n╠➩☆°̙̲̖̤͖̻̎̃̉̂͝ͅ°̷̡̨̤̳̼̹͎̔̾͐̽̉̏͛̏͌°̷̧̡̗̹̯̳̰̦̦͌͂̏̾͒Ù̴̪͈̣̹̮̮̀́̿̊̉̈́͊͘͘Ú͇̬̬̥͕̅͐͌͊͑̂̓̽§̵̧̛̯̟̥̦̞̃͋̓̏͘͡ B̷̲̬͇̥̼̈̀͑̀̊͛̀͘͝ͅØ͈͉̦͕͉͉̓͗́͌̊͆̆̚͡ͅT̴̪̞͕͎̗̫̤̻͈̐̾̑͌͠Š̴̻̹͖̘̺̫̹̱̫̩̎̒̔͌̔̄̔̓͠°̨͔̱̭̘̝̘͐̉͊̐́ͅ°̛͎̲͉̠̙̙̬͆͌͒̀͋͟͠͝ͅ°͕̞͎̰͎̭̘͇̑̓̌̀̔̇̀͟☆~ℬåᎫäʞ.ïđ\n\n╠➩ Support By: χχχ==вσтρяσтє¢т==χχχ\n╚══════════════════════")
                    jawaban = random.choice(jawab)
                    tts = gTTS(text=jawaban, lang='id')
                    tts.save('tts.mp3')
                    cl.sendAudio(msg.to,'tts.mp3')
                    cl.sendMessage(msg)         
                    cl.sendText(msg.to,"Jika Berminat Langsung Hubungi Kami Ya Trima Kasih😊😊")
            elif ("Ban " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Bosque")
                   except:
                      pass
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Target Unlocked")
                            except:
                                cl.sendText(msg.to,"Error")

            elif "Ban:" in msg.text:                  
                       nk0 = msg.text.replace("Ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Locked")
                                except:
                                    kk.sendText(msg.to,"Error")

            elif "Unban:" in msg.text:                  
                       nk0 = msg.text.replace("Unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Unlocked")
                                except:
                                    kk.sendText(msg.to,"Error")
#-----------------------------------------------------------

            elif "Mycopy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Mycopy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Succes Copy profile")
                                except Exception as e:
                                    print e
                                    

            elif msg.text in ["Mybackup"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "backup done")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
                    
            elif msg.text in ["Backup"]:
                try:
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    cl.sendText(msg.to, "backup done")
                except Exception as e:
                    cl.sendText(msg.to, str (e))

#-----------------------------------------------------------
            elif "Mban:" in msg.text:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = True
		cl.sendText(msg.to,"Target Lock")
#-----------------------------------------------------<------
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds􀜁􀅔􏿿" % (elapsed_time))
#-----------------------------------------------------------
            elif "Steal home @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal home @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"			
#------------------------------------------------------------------
            elif "Steal dp @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal dp @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"			
 #------------------------------------------------------------------
            elif msg.text in ["Gcreator:inv"]:
              if msg.toType == 2:
                 ginfo = cl.getGroup(msg.to)
                 gCreator = ginfo.creator.mid
                 try:
                    cl.findAndAddContactsByMid(gCreator)
                    cl.inviteIntoGroup(msg.to,[gCreator])
                    print "success inv gCreator"
                 except:
                    pass
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
            elif msg.text in ["Bans:on"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unbans:on"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text.lower() == 'mcheck':
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 Nothing in the blacklist")
                else:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 following is a blacklist")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "➡" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'banlist':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "➡" +cl.getContact(mm).displayName + "\n"
                    cl.sendText(msg.to,cocoa + "Daftar Hitam")
            elif msg.text.lower() == 'kill':
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"Daftar hitam pengguna tidak memiliki")
                        return
                    for jj in matched_list:
                        try:
                            cl.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "Kibas" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Kibas","")
                    gs = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"☆_̶̧̎̀̂̅̊_̵̢̣̞̘̣̞̺̮͉͖̻̍̈́̎̓̔̐̐͗̒̃̏̕_̷̢̧̲͔̠̜͖͇̦̟̞̗̬̋̎̎͂͋͛͘K̵̛̮̣̞͕͔͕̺̹̳͒͌̀̾̅̔̚I̸̯̤̲͐̎͑̀̌̔̋̔̊̾̔̄́̃B̸̧̟̞͓̥̼͇̺̥̯̳͈͕̳͋͐̓̋̓̓͛͝A̶̙͖̋̿͒̈́̓̕͠Ş̶͕̫̳̝͎̥̥̩̃͗̑̉̅̇̓́̍͘͘͜͝͝_̷̯͇͇̝̣͍̹̖̯͚͂͊̀̆͒̓̚͜ͅ_̶̞̱̥͖̤̣͓̬͈͚̫̼̼̩̲͆̈́͊̓̈̽̔̽̐̃͌̽́̀̚_̵̭͖̤̪̰̮͉̫͓̀͋̑͘☆\n\nRata gx rata yg pentig Pernah hadir")
                    cl.sendText(msg.to,"\n\[∆√ ᵤ'ᵤₛBₒₜ̈́™ √∆]\n Owner http://line.me//ti/p/~kibasz.com")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak ditemukan")
                    else:
                        for target in targets:
                            if not target in Bots:
                                try:
                                   klist=[cl]
                                   kicker=random.choice(klist)
                                   kicker.kickoutFromGroup(msg.to,[target])
                                   print (msg.to,[g.mid])
                                except:
                                   cl.sendText(msg.to,"Mayhem done")
            elif msg.text.lower() == 'cancel':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled👈")
    
            elif msg.text in ["Mangat","B"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"B")
                    cl.sendText(msg.to,"B")
                    cl.sendText(msg.to,"B")
            elif "Album" in msg.text:
                try:
                    albumtags = msg.text.replace("Album","")
                    gid = albumtags[:33]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "We created an album👈")
                except:
                    cl.sendText(msg.to,"Error")
                    
            elif "fakecâ†’" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    amid = msg.text.replace("fakecâ†’","")
                    cl.sendText(msg.to,str(cl.channel.createAlbumF(msg.to,name,amid)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass			
#-----------------------------------------------
            elif "Key" in msg.text:
                cl.sendText(msg.to,"""╔═════════════════════\n║◄]··􀜁􀇔􏿿_̶̧̎̀̂̅̊_̵̢̣̞̘̣̞̺̮͉͖̻̍̈́̎̓̔̐̐͗̒̃̏̕_̷̢̧̲͔̠̜͖͇̦̟̞̗̬̋̎̎͂͋͛͘K̵̛̮̣̞͕͔͕̺̹̳͒͌̀̾̅̔̚I̸̯̤̲͐̎͑̀̌̔̋̔̊̾̔̄́̃B̸̧̟̞͓̥̼͇̺̥̯̳͈͕̳͋͐̓̋̓̓͛͝A̶̙͖̋̿͒̈́̓̕͠Ş̶͕̫̳̝͎̥̥̩̃͗̑̉̅̇̓́̍͘͘͜͝͝_̷̯͇͇̝̣͍̹̖̯͚͂͊̀̆͒̓̚͜ͅ_̶̞̱̥͖̤̣͓̬͈͚̫̼̼̩̲͆̈́͊̓̈̽̔̽̐̃͌̽́̀̚_̵̭͖̤̪̰̮͉̫͓̀͋̑͘􀜁􀇔􏿿··[►\n╠═════════════════════\n║╔════════════════════\n║╠☠key Only Kicker ☠ \n║╠☠ [Kibas1 in]\n║╠☠ [Kibas]\n║╠☠ [Cancel]\n║╠☠ [Vk @]\n║╠☠ [Ban @]\n║╠☠ [kill]\n║╠☠ [Respon]\n║╠☠ [Respons]\n║╠☠ [Kibas1 Gift]\n║╠☠ [Kibas bye]\n║║[cʎᙠéɹʇk¯ʎᙠʇɹoԀns]\n║╠════════════════════\n║║☆_̶̧̎̀̂̅̊_̵̢̣̞̘̣̞̺̮͉͖̻̍̈́̎̓̔̐̐͗̒̃̏̕_̷̢̧̲͔̠̜͖͇̦̟̞̗̬̋̎̎͂͋͛͘K̵̛̮̣̞͕͔͕̺̹̳͒͌̀̾̅̔̚I̸̯̤̲͐̎͑̀̌̔̋̔̊̾̔̄́̃B̸̧̟̞͓̥̼͇̺̥̯̳͈͕̳͋͐̓̋̓̓͛͝A̶̙͖̋̿͒̈́̓̕͠Ş̶͕̫̳̝͎̥̥̩̃͗̑̉̅̇̓́̍͘͘͜͝͝_̷̯͇͇̝̣͍̹̖̯͚͂͊̀̆͒̓̚͜ͅ_̶̞̱̥͖̤̣͓̬͈͚̫̼̼̩̲͆̈́͊̓̈̽̔̽̐̃͌̽́̀̚_̵̭͖̤̪̰̮͉̫͓̀͋̑͘☆\n║║☆ line.me/ti/p/kibasz.com\n║╚════════════════════\n╚═════════════════════
""")
#-----------------------------------------------
            elif msg.text in ["Welcome","wc","welcome","Wc"]:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Hosgeldiniz" + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.admin.displayName )
            elif "TK Say " in msg.text:
				bctxt = msg.text.replace("TK Say ","")
				cl.sendText(msg.to,(bctxt))
            elif "say" in msg.text:
              if msg.from_ in admin:
				bctxt = msg.text.replace("Bc ","")
				cl.sendText(msg.to,(bctxt))
            elif msg.text.lower() == 'ping':
                cl.sendText(msg.to,"Ping 􀜁􀇔􏿿")
#----------------------------------------------- 
              
	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
			G.preventJoinByTicket = True
			cl.updateGroup(G)
		   except:
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
			except:
			    pass
		elif op.param2 not in admin + Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = cl.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    cl.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
#------------------------------------------------------------------------------------
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass
                

    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
