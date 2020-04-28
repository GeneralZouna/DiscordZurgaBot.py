from random import randint

User_balance_dict = {}


def get_balance(user):
    if str(user) in User_balance_dict:
        return round(User_balance_dict[str(user)],2)
    else:
        User_balance_dict[str(user)] = 0
        return round(User_balance_dict[str(user)],2)


def Balance_change(user,new_balance):
    User_balance_dict[str(user)] = new_balance




def transaction(From_user, To_user, amaunt):
    User_balance_dict[str(From_user)]
    if amaunt <= User_balance_dict[str(From_user)] and amaunt > 0:
        User_balance_dict[str(From_user)] -= amaunt
        User_balance_dict[str(To_user)] += amaunt
        UpdateData(True)
        return True
    return False



def payment(user, amaunt):
    if amaunt <= User_balance_dict[str(user)]:
        User_balance_dict[str(user)] -= amaunt
        UpdateData(True)
        return True
    return False

def InsFunds():
    Responses = ["You're out of money","Insufficient funds","It appears that you lack the money to request this command at this current moment","Declined"]
    return Responses[randint(0,len(Responses)-1) ]


def UpdateData(write):
    try:
       f = open("Balance_list.bal",'x')
       f.close()

       
    except IOError:        
        if write == True:
            Balance_list = open("Balance_list.bal",'w')
            string = ''
            for person in User_balance_dict:
                if person not in string:
                    string = string + "{0} {1}\n".format(person,float(User_balance_dict[str(person)]))
            Balance_list.write(string)


            
        elif write == False:
            Balance_list = open("Balance_list.bal",'r')
            for line in Balance_list:
                User_balance_dict[str(int(line[0:18]))] = float(line[19:])
                print("ID:{0} Ammount:{1}".format(line[0:18],User_balance_dict[str(line[0:18])]))

        Balance_list.close()
        return True






