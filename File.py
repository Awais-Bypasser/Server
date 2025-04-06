import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-J727V','SM-J727P','SM-J727T','SM-J727F','SM-J727U','SM-J727S','SM-J727VPP','SM-J727AZ','SM-S727VL','SM-J727R4','SM-J727A'])
	realme = random.choice(['V2025', 'V2024'])
	oppo = random.choice(['DIG-L01','DIG-L21HN','DIG-TL10','DIG-L03','DIG-L21','DIG-AL00','DIG-L23'])
	vivo = random.choice(['SM-T380','SM-T385','SM-T385M'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/72.0.0.13.45;FBBV/165926592;FBDM/{density=2.25,width=800,height=1280};FBLC/"+fblc+";FBRV/472956183;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+vivo+";FBSV/7.1;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/31.0.0.17.68;FBBV/361858279;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBRV/265916395;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/6.0;FBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/51.0.0.18.27;FBBV/361834;FBDM/{density=2.0,width=720,height=1280};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+samsung+";FBSV/7.0.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua4 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/17.0.0.18.41;FBBV/271957;FBDM/{density=3.0,width=1080,height=2160};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.orca;FBDV/MEI7S;FBSV/7.1.2;FBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/42.0.0.17.62;FBBV/361858279;FBDM/{density=3.0,width=1080,height=2480};FBLC/"+fblc+";FBRV/265916395;FBCR/"+fbcr+";FBMF/INFINIX;FBBD/INFINIX;FBPN/com.facebook.katana;FBDV/X6812B;FBSV/11;FBCA/arm64-v8a:;]"
	ua = str(random.choice([ua1,ua7,ua4,ua6,ua5]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
