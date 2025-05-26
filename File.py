import random
ugeni = []
for agents in range(30000):
	samsung = random.choice(['SM-J727V','SM-J727P','SM-J727T','SM-J727F','SM-J727U','SM-J727S','SM-J727VPP','SM-J727AZ','SM-S727VL','SM-J727R4','SM-J727A'])
	realme = random.choice(['E973','E971','E975','F180L','F180K','F180S'])
	oppo = random.choice(['BLN-AL10','BLL-L22','BLN-L21','BLL-L21','BLN-L22','BLL-L23','BLN-L24','BLN-AL40','BLN-TL10','BLN-AL20','BLN-AL30'])
	vivo = random.choice(['SM-G5500','SM-G550F','SM-G5528','SM-G5510','SM-G550T1','SM-G550T','G55','SM-S550TL','SM-G550T2'])
	fbcr = random.choice(["Telenor","Ufone","Zong","Jazz","Jazz 4G","Mobilink","Zong 4G","Zong CmPak"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401182;FBDM/{density=2.0,width=720,height=1280};FBLC/"+fblc+";FBRV/274073372;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/7.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBRV/173957193;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/6.0;FBBK/1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=1280,height=720};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J510FN;FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/149.0.0.40.71;FBBV/79007703;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/79424004;FBCR/vodafone P;FBMF/ZTE;FBBD/ZTE;FBPN/com.facebook.katana;FBDV/NOS NOVU II;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua7 = "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/"+fblc+";FBBV/285816295;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBDV/SM-T111;FBSV/4.2;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.3,width=600,height=1024};FB_FW/1;]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1184};FBLC/pt_PT;FBRV/85070460;FBCR/vodafone P;FBMF/ulefone;FBBD/ulefone;FBPN/com.facebook.katana;FBDV/MIX;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua1,ua5,ua7,ua6,ua10,ua2]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
