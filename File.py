import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-J337U','SM-J337W','SM-J337A','SM-J337R','SM-J337T','SM-J337P','SM-J337AZ','SM-J337VPP'])
	realme = random.choice(['SM-G386F', 'SM-G386T1'])
	oppo = random.choice(['BAC-AL00','BAC-L03','BAC-L23','BAC-L21','BAC-L22','BAC-TL00'])
	lg = random.choice(['LG-D295', 'LG-D290'])
	sony = random.choice(['SO-04H','F8131','SOV33','F8132','502SO'])
	vivo = random.choice(['SM-J105F','SM-j105H','SM-J105H','SM-J105B','SM-J105Y','SM-J105M'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880428;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/8.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/82.0.0.23.70;FBBV/32429824;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/437.0.0.35.116;FBBV/527644830;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/381384816;FBCR/"+fbcr+";FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/"+sony+";FBSV/6.0.1;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/80.0.0.21.65;FBBV/31389908;FBDM/{density=1.75,width=480,height=800};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/LGE;FBBD/LGE;FBPN/com.facebook.katana;FBDV/"+lg+";FBSV/4.4.2;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/24.0.0.11.92;FBBV/11516731;FBDM/{density=2.75,width=720,height=1080};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+samsung+";FBSV/8.0;FBCA/armeabi-v7a:armeabi;]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";FBDM/{density=2.625,width=1080,height=1920};FBLC/en_US;FBRV/213439635;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N920T;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	ua9 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";FBDM/{density=2.0,width=720,height=1344};FBLC/en_US;FBRV/0;FBCR/Jio 4G;FBMF/LAVA;FBBD/LAVA;FBPN/com.facebook.katana;FBDV/Z81;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua9,ua10,ua5,ua7,ua6,ua1,ua2]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
