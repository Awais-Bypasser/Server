import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-J510F','SM-J510G','SM-J510FN','SM-J510Y','SM-J510M','SM-J510GN','SM-J510H','SM-J510MN','SM-J5108','SM-J510UN','SM-J510L','SM-J510S','SM-J510FQ','SM-J510K'])
	realme = random.choice(['RMX2027','RMX2020','RMX2021'])
	oppo = random.choice(['CPH1819','CPH1821','OPPO 1821','CPH1821EX'])
	vivo = random.choice(['SM-J327A','SM-J327','SM-J327T','SM-J327V','SM-J327P','SM-J327W','SM-J326AZ'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/35.0.0.21.38;FBBV/261395;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-A700FD;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/37.0.0.42.26;FBBV/471741601;FBDM/{density=2.25,width=720,height=1280};FBLC/"+fblc+";FBRV/371979081;FB_FW/2;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500F;FBSV/5.0.2;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FBIOS;FBAV/183.0.0.41.81;FBBV/119182652;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.4;FBSS/3;FBCR/MEO;FBID/phone;FBLC/pt_BR;FBOP/5;FBRV/0]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FBIOS;FBAV/488.0.0.46.102;FBBV/674915696;FBDV/iPhone17,1;FBMD/iPhone;FBSN/iOS;FBSV/18.1.1;FBSS/3;FBCR/;FBID/phone;FBLC/en_US;FBOP/80]"
	ua10 = "Mozilla/5.0 (Linux; Android 13; 2207117BPG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6723.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/488.0.0.78.79;IABMV/1;]"
	ua = str(random.choice([ua1,ua7,ua6,ua5,ua10]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen
