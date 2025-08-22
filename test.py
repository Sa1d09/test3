import json

with open("file.json", "r") as fayl:
    malumot = json.load(fayl)

print("bankomat menyusi")
print("1 kirish")
print("2 id qoshish")
print("3 id ochirish")
print("4 barcha idlarni korsatish")

tanlov = input("tanlang ")

if tanlov == "1":
    id_kirit = input("id kiriting ")
    parol_kirit = input("parol kiriting ")
    i = 0
    topildi = False

    while i < len(malumot):
        if malumot[i]["id"] == id_kirit and malumot[i]["parol"] == parol_kirit:
            topildi = True
            print("salom", malumot[i]["ism"])
            print("balans", malumot[i]["pul"], "som")
            print("1 pul yechish")
            print("2 pul qoshish")
            tanlov2 = input("tanlang ")

            if tanlov2 == "1":
                miqdor = int(input("qancha pul yechiladi "))
                if miqdor <= malumot[i]["pul"]:
                    malumot[i]["pul"] -= miqdor
                    print("yechildi", miqdor, "som qoldi", malumot[i]["pul"])
                else:
                    print("yetarli mablag yoq")
            elif tanlov2 == "2":
                miqdor = int(input("qancha pul qoshiladi "))
                malumot[i]["pul"] += miqdor
                print("qoshildi", miqdor, "som yangi balans", malumot[i]["pul"])
            else:
                print("xato tanlov")
            break
        i += 1

    if not topildi:
        print("id yoki parol xato")

elif tanlov == "2":
    yangi_id = input("yangi id kiriting ")
    ism = input("ism kiriting ")
    parol = input("parol kiriting ")
    pul = int(input("boshlangich pul kiriting "))
    yangi = {"id": yangi_id, "ism": ism, "parol": parol, "pul": pul}
    malumot.append(yangi)
    print("yangi id qshildi")

elif tanlov == "3":
    och_id = input("ochirmoqchi bolgan id ni kiriting ")
    i = 0
    topildi = False
    while i < len(malumot):
        if malumot[i]["id"] == och_id:
            del malumot[i]
            topildi = True
            print("id ochirildi")
            break
        i += 1
    if not topildi:
        print("bunday id topilmadi")

elif tanlov == "4":
    print("barcha foydalanuvchilar")
    i = 0
    while i < len(malumot):
        print("id", malumot[i]["id"], "ism", malumot[i]["ism"], "balans", malumot[i]["pul"])
        i += 1

else:
    print("xato tanlov")

with open("file.json", "w") as fayl:
    json.dump(malumot, fayl, indent=4)
