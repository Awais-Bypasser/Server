import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-A716N','SM-A716SS','SM-A716S'])
	realme = random.choice(['SM-G313HU','SM-G316HU','SM-G316M'])
	oppo = random.choice(['ANA-AN00','ANA-TN00','ANA-NX9','ANA-LX4'])
	lg = random.choice(['K220','LS755','US610','K450','LGLS755','F750K','K210','LGUS610'])
	sony = random.choice(['D2303', 'D2305', 'D2306'])
	vivo = random.choice(['SM-J320H','SM-J3109','SM-J320FN','SM-J320P','SM-J320F','SM-J320M','SM-J320Y','SM-J320A','SM-J320G','SM-J327T1','SM-J320V','SM-J320YZ','SM-J320W8','SM-J320ZN','SM-J320N0','SM-J320R4'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027763;FBDM/{density=3.0,width=1080,height=2400};FBLC/"+fblc+";FBRV/195717365;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/10;FBOP/11;FBCA/arm64-v8a:;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=3.0,width=1080,height=2340};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/10;FBCA/arm64-v8a:;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/390.2.0.29.103;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/361946295;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBDV/SM-N9100;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;FBDM/{density=3.25,width=1440,height=2560};FB_FW/1;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/74.0.0.59.41;FBPN/com.facebook.orca;FBLC/"+fblc+";FBBV/261936582;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBDV/"+vivo+";FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;FBDM/{density=1.85,width=480,height=800};]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/396.1.0.28.104;FBPN/com.facebook.katana;FBLC/"+fblc+";FBBV/319214973;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 7;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2131};FB_FW/1;]"
	ua = str(random.choice([ua5,ua7,ua6,ua1]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
