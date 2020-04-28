import requests
def get_neko(lewd=False):
    img = requests.get("https://nekos.life/api/v2/img/"+("neko" if not lewd else "lewd")).json()["url"]
    #info("[neko] "+str(img)+" ("+("n" if lewd else "")+"sfw)")
    #print(str(img))
    return img
