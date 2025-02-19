import random
ugeni = []
for agents in range(10000):
    samsung = random.choice(['SM-S916B','SM-S916B/DS','SM-S916U','SM-S916U1','SM-S916W','SM-S916N','SM-S9160','SM-S916E','SM-S916E/DS'])
    realme = random.choice(['GT-I9192','GT-I9190','GT-I9195','GT-I9195L','GT-I9197','SGH-I257M','GT-I9195I','SGH-I257','SCH-I435','SHV-E370K','GT-I9192I'])
    oppo = random.choice(['NXT-AL10','NXT-CL00','NXT-DL00','NXT-TL00','NXT-L09','NXT-L29'])
    lg = random.choice(['H540','H631','MS631','H635','H540','H630','H542','H630D'])
    sony = random.choice(['D2303', 'D2305', 'D2306'])
    vivo = random.choice(['SM-T377W', 'SM-T377', 'SM-T375', 'SM-T377P', 'SM-T377R', 'SM-T377A', 'SM-T378V', 'SM-T377V'])
    fbcr = random.choice(["Telenor", "Zong", "Zong 4G", "Zong CMPAK", "Jazz", "Ufone", "Jio", "Vodafone", "Airtel", "BSNL","Grameenphone", "Robi", "Banglalink","Orange","Sprint" "Telefonica","null","Jazz","Jazz 4G","LTE","Mobilink","Telenor 4G","PK-Ufone"])
    fblc = random.choice(['en_US', 'en_GB', 'en_PK', 'es_LA', 'fr_FR', 'ur_PK', 'en_LA','ur_PK'])
    ua6 = "[FBAN/FB4A;FBAV/" + str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ";FBBV/" + str(random.randint(1111111, 7777777)) + ";[FBAN/FB4A;FBAV/450.0.0.42.110;FBBV/2135126;FBDM/{density=3.0,width=1080,height=2340};FBLC/" + fblc + ";FBRV/234167426;FBCR/" + fbcr + ";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/" + samsung + ";FBSV/14;FBOP/1;FBCA/arm64-v8a:null;]"
    ua5 = "[FBAN/FB4A;FBAV/" + str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ";FBBV/" + str(random.randint(1111111, 7777777)) + ";[FBAN/FB4A;FBAV/458.0.0.34.118;FBBV/1974348;FBDM/{density=3.0,width=1080,height=1920};FBLC/" + fblc + ";FBCR/" + fbcr + ";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/" + oppo + ";FBSV/6.0;FBCA/armeabi-v7a:armeabi;]"
    ua2 = "[FBAN/FB4A;FBAV/" + str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ";FBBV/" + str(random.randint(1111111, 7777777)) + ";[FBAN/FB4A;FBAV/64.0.0.31.75;FBBV/157959764;FBDM/{density=2.35,width=720,height=1280};FBLC/" + fblc + ";FBRV/4329831;FBCR/" + fbcr + ";FBMF/LGE;FBBD/LGE;FBPN/com.facebook.katana;FBDV/" + lg + ";FBSV/5.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua7 = "[FBAN/FB4A;FBAV/" + str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ";FBBV/" + str(random.randint(1111111, 7777777)) + ";[FBAN/Orca-Android;FBAV/330.0.0.12.116;FBBV/515779258;FBLC/" + fblc + ";FBCR/" + fbcr + ";FBPN/com.facebook.orca;FBMF/samsung;FBBD/samsung;FBDV/" + vivo + ";FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};]"
    ua1 = "[FBAN/FB4A;FBAV/" + str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ";FBBV/" + str(random.randint(1111111, 7777777)) + "[FBAN/FB4A;FBAV/269.0.0.50.127;FBBV/212783074;FBDM/{density=3.375,width=1080,height=1998};FBLC/" + fblc + ";FBRV/0;FBCR/" + fbcr + ";FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-Q720;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]"
    ua2 = "[FBAN/FB4A;FBAV/" + str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ";FBBV/" + str(random.randint(1111111, 7777777)) + "[FBAN/FB4A;FBAV/267.1.0.46.120;FBBV/210653414;FBDM/{density=2.0,width=720,height=1402};FBLC/" + fblc + ";FBRV/211387411;FBCR/" + fbcr + ";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S102DL;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    ua = str(random.choice([ua6, ua5, ua7, ua2]))  # Add ua6 to the list of choices
    ugeni.append(ua)
