engels_nederlands = { "last":"laatste", "week":"week", "the":"de",
"royal":"koninklijk", "festival":"feest", "hall":"hal",
"saw":"zaag", "first":"eerst", "performance":"optreden",
"of":"van", "a":"een", "new":"nieuw", "symphony":"symfonie",
"by":"bij", "one":"een", "world":"wereld", "leading":
"leidend", "modern":"modern", "composer":"componist",
"composers":"componisten", "two":"twee", "shed":"schuur",
"sheds":"schuren" }

def vind_key(woord):
    for key, value in engels_nederlands.items(): 
        if value == woord:
            return key
    return woord 

zin = input("Geef een zin in het nederlands en/of engels: ").split(" ")
nieuwe_zin = ""
for woord in zin:
    try:
        # Engels -> Nederlands
        nieuwe_zin += f"{engels_nederlands[woord]} "
    except:
        # Nederlands -> Engels
        nieuwe_zin += f"{vind_key(woord)} "

print(nieuwe_zin)