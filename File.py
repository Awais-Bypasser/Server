import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-N910C','SM-N910S','SM-N910H','SM-N910F','SM-N910G','SM-N910U','SM-N910K','SM-N916S','SM-N910L','SM-N916L','SM-N916K','SM-N910T3'])
	realme = random.choice(['2016060','2016090','MAG138','MAE136','Redmi 4','Redmi 4X'])
	oppo = random.choice(['RNE-L21','RNE-L22','RNE-L01','RNE-L02','RNE-L11','RNE-L23','RNE-L03','RNE-AL00'])
	vivo = random.choice(['SM-J810G','SM-J810F','J810Y','SM-J810Y','SM-J810GF','SM-J810M'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/154.0.0.26.159;FBBV/268946150;FBDM/{density=3.0,width=1440,height=2560};FBLC/"+fblc+";FBRV/285618365;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/231.1.0.57.129;FBBV/377040;FBDM/{density=3.0,width=1080,height=2160};FBLC/"+fblc+";FBRV/491738572;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/7.0;FBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/300.1.0.57.129;FBBV/377040;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBRV/571657194;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/"+realme+";FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/56.0.0.46.12;FBBV/666395;FBDM/{density=3.0,width=1440,height=2560};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+samsung+";FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/72.0.0.31.46;FBBV/84268146;FBDM/{density=4.6,width=480,height=800};FBLC/lt_LT;FBCR/Reach Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-G318ML;FBSV/4.2;nullFBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua7,ua6,ua5,ua10]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
