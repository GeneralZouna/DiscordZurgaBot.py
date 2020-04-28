Settings_dict = {}

def SettingsUpdate(write = False):
    try:
       f = open("Settings.txt",'x')
       f.close()

       
    except IOError:        
        if not write:
            f = open("Settings.txt",'r')
            ID = 0
            for line in f:
                if line.startswith("ID:"):
                    ID = str(line[3:21])
                    Settings_dict[ID] = {}
                if line.startswith("NSFW:"):
                    if "true" in line.lower():
                        Settings_dict[ID]['nsfw'] = True
                    else:
                        Settings_dict[ID]['nsfw'] = False
                if line.startswith("Furry:"):
                    if "true" in line.lower():
                        Settings_dict[ID]['furry'] = True
                    else:
                        Settings_dict[ID]['furry'] = False
                if line.startswith("Command:"):
                    Settings_dict[ID]['command'] = line.lower()[8:].rstrip('\n')
                if line.startswith('Admin_role:'):
                    Settings_dict[ID]['admin_role'] = int(line[11:].rstrip('\n'))

        if write:
            String = ""
            for ID in Settings_dict:
                getSetting(ID,'nsfw')
                getSetting(ID,'furry')
                getSetting(ID,'command')
                getSetting(ID,'admin_role')
                String = String + "ID:{0}\nNSFW:{1}\nFurry:{2}\nCommand:{3}\nAdmin_role:{4}\n\n".format(ID, Settings_dict[ID]['nsfw'], Settings_dict[ID]['furry'], Settings_dict[ID]['command'],Settings_dict[ID]['admin_role'])

            f = open("Settings.txt",'w')
            f.write(String)
        
        f.close()



def getSetting(ID,tag):
    
    if str(ID) in Settings_dict:
        if tag in Settings_dict[str(ID)]:
            #print(Settings_dict[str(ID)][tag])
            return Settings_dict[str(ID)][tag]
        else:
            if tag == 'nsfw':
                Settings_dict[str(ID)]['nsfw'] = True
            elif tag == 'furry':
                Settings_dict[str(ID)]['furry'] = True
            elif tag == 'command':
                Settings_dict[str(ID)]['command'] = '!'
            elif tag == 'admin_role':
                Settings_dict[str(ID)]['admin_role'] = 0
            return Settings_dict[str(ID)][tag]
    else:
        Settings_dict[str(ID)] = {}
        Settings_dict[str(ID)]['nsfw'] = True
        Settings_dict[str(ID)]['furry'] = True
        Settings_dict[str(ID)]['command'] = '!'
        Settings_dict[str(ID)]['admin_role'] = 0
        return Settings_dict[str(ID)][tag]



def modSetting(ID, Tag, New_value):
    getSetting(ID,Tag)
    Settings_dict[str(ID)][Tag] = New_value








