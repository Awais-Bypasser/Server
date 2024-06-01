import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-J500F','SM-J500G','SM-J500FN','SM-J500Y','SM-J500M','J500S','SM-J500H','SM-J5007','J5','SM-J500N0','SM-J5008'])
	realme = random.choice(['PCKM70','PCKT00','PCKM00','CPH1945','CPH1951','PCKM80'])
	oppo = random.choice(['LYA-L09','LYA-L29','LYA-AL00','LYA-AL10','LYA-TL00','LYA-L0C'])
	vivo = random.choice(['SM-J810G','SM-J810F','J810Y','SM-J810Y','SM-J810GF','SM-J810M'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/154.0.0.26.159;FBBV/268946150;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBRV/285618365;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/231.1.0.57.129;FBBV/377040;FBDM/{density=3.0,width=1440,height=3120};FBLC/"+fblc+";FBRV/491738572;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/9.0;FBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/300.1.0.57.129;FBBV/377040;FBDM/{density=3.0,width=1080,height=2340};FBLC/"+fblc+";FBRV/571657194;FBCR/"+fbcr+";FBMF/oppo;FBBD/oppo;FBPN/com.facebook.katana;FBDV/"+realme+";FBSV/9.0;FBCA/arm64-v8a:;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/56.0.0.46.12;FBBV/666395;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+samsung+";FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/85.0.0.65.49;FBBV/28674375;FBDM/{density=1.5,width=720,height=1280};FBLC/en_BM;FBCR/TerreStar;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N7505;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua1,ua7,ua6,ua5,ua10]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
