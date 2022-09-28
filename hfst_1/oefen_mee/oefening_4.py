engels_nederlands = { "last":"laatste", "week":"week", "the":"de",
"royal":"koninklijk", "festival":"feest", "hall":"hal",
"saw":"zaag", "first":"eerst", "performance":"optreden",
"of":"van", "a":"een", "new":"nieuw", "symphony":"symfonie",
"by":"bij", "one":"een", "world":"wereld", "leading":
"leidend", "modern":"modern", "composer":"componist",
"composers":"componisten", "two":"twee", "shed":"schuur",
"sheds":"schuren" }

zin = input("Geef een zin in het engels: ").split(" ")
nieuwe_zin = ""
for woord in zin:
    try:
        nieuwe_zin += f"{engels_nederlands[woord]} "
    except:
        nieuwe_zin += f"{woord} "

print(nieuwe_zin)