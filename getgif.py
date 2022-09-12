import requests
import json
import random

################################
#                              #
#            Config            #
#                              #
################################
apikey = "---------------------" 
ckey = "KpopBot"
lmt = 100000
debug = False

def getGifFromTenor(recherche:str)-> str:
    """
    Cette fonction va faire une requette sur le site tenor et retourne
    le lien d'un gif aleatoire correspondant a la recherche

    :param recherche:   Le terme de la recherche sur tenor
    :type recherche:    chaine de caractere (str)
    :return:            lien vers un gif   
    :rtype:             chaine de caractere (str)

    exemple:
        >>> getGifFromTenor("kim dahyun")
        "https://c.tenor.com/HGS52u8LsWgAAAAC/thumbs-up-dahyun.gif"
    """
    if debug : print("request :","https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s" % (recherche, apikey, ckey))
    r = requests.get("https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s" % (recherche, apikey, ckey))
    if debug : print("status code :",r.status_code)
    if r.status_code == 200 :
        dictGif = json.loads(r.content)
        if debug : print(dictGif)
        return(dictGif["results"][random.randint(0, len(dictGif["results"])-1)]["media_formats"]["gif"]['url'])
    return "Sorry no gif for you T-T"

if __name__ == "__main__":
    #10 gif aleatoire de kim dahyn
    for i in range(10):
        print(getGifFromTenor("kim dahyun"))