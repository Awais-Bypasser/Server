import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-T116','SM-T116BU','SM-T116NQ','SM-T116NU','SM-T116NY'])
	realme = random.choice(['SM-G386F', 'SM-G386T1'])
	oppo = random.choice(['GT-S7582','GT-S7580','GT-S7583T','GT-S7582L'])
	lg = random.choice(['SM-J111F','SM-J110G','SM-J110F','SM-J110H','SM-J110M','SM-J110L','SM-J111M'])
	sony = random.choice(['D2303', 'D2305', 'D2306'])
	vivo = random.choice(['SM-J415F','SM-J415FN','SM-J415G','SM-J415GN','SM-J415N'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880428;FBDM/{density=1.0,width=600,height=1024};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/4.4;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/82.0.0.23.70;FBBV/32429824;FBDM/{density=1.5,width=800,height=480};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/4.2.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/437.0.0.35.116;FBBV/527644830;FBDM/{density=2.75,width=1080,height=2177};FBLC/fa_IR;FBRV/0;FBCR/Irancell;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/2209116AG;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/80.0.0.21.65;FBBV/31389908;FBDM/{density=1.5,width=480,height=800};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+lg+";FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/82.0.0.23.70;FBBV/32429824;FBDM/{density=1.5,width=540,height=960};FBLC/en_GB;FBCR/null;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/HUAWEI G610-U15;FBSV/4.2.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=2.86 ,width=1440,height=2560};FBLC/en_US;FBRV/279865282;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G935FD;FBSV/8.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua10,ua5,ua7,ua6,ua1,ua2]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
