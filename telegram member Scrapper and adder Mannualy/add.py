from pyrogram import Client
import time

import sys
import os
from pyrogram.errors import RPCError



orginally = 1  

api_id = "25155028" 
api_hash = "0de1e7f476617dac07f23634437cee6d"

apps = Client("Sessions/",int(api_id),str(api_hash),phone_number="251965774903")

apps.start()

class GroupToGroup_AddMember():
    def __init__(self):
        return None

    def Get_group_chat_id(self, Link1, Link2):
            global a,b
            self.Group_ChatID = apps.get_chat(Link1)
            a = self.Group_ChatID.id
            self.Group_ChatID = apps.get_chat(Link2)
            b = self.Group_ChatID.id

    def Add_To_Group(self, Source, Destination):
        members = apps.get_chat_members(Source)
        counter = 1
        ccc = "DONE"
        for index, member in enumerate(members):
            app = apps
            try:
                user_id = member.user.username
                app.add_chat_members(Destination, user_id)

            except Exception as ex:
                print("Adding " + str(counter) + " " + str(user_id) + "\t" + str(ex.__class__.__name__))
                counter = counter + 1
                time.sleep(10)
                status = ex.__class__.__name__
                print("Current Status: "+status)
                if status == "UserBannedInChannel":
                    
                    continue

                else:
                    pass
            else:
                print("Adding "+str(counter)+" "+str(user_id)+"\t"+str(ccc))
                counter = counter+1
                time.sleep(10)

if int(orginally) == 1:
    one = input("Source group: ")
    two = input("Destination group: ")

    if "@" in str(one):
        onee = one.replace("@","")
    else:
        onee = one
    if "@" in str(two):
        twoo = two.replace("@","")
    else:
        twoo = two
    try:

        apps.join_chat(str(onee))
        apps.join_chat(str(twoo))
    except:
        pass

    App_Start = GroupToGroup_AddMember()
    ab = App_Start.Get_group_chat_id(one, two)
    App_Start.Add_To_Group(a, b)

else:
    apps.stop()
    sys.exit()

