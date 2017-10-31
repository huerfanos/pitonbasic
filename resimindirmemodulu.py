import urllib.request

url1 = "http://images4.wikia.nocookie.net/__cb20110928200153/wowwiki/images/8/87/Deathwing_Cataclysm_3.jpg"
url2 = "http://www.merlininkazani.com/images/games/7582/97608_640.jpg"
url3 = "http://www.merlininkazani.com/images/games/11835/97516_640.jpg"

urllistesi = [url1,url2,url3]
say=1
for url in urllistesi:
    urllib.request.urlretrieve(url,"Resim" + str(say)+".jpg")
    say +=1



