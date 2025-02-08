import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-N900','SM-N9002','SM-N9005','SM-N9007','SM-N9008','SM-N9008S','SM-N9008V','SM-N9009','SM-N9009V','SM-N900A','SM-N900K','SM-N900L','SM-N900P','SM-N900R4','SM-N900S','SM-N900T','SM-N900U','SM-N900V','SM-N900W8','SM-N900X','SM-N9000Q','SM-N9006','SM-9005'])
	realme = random.choice(['PCKM70','PCKT00','PCKM00','CPH1945','CPH1951','PCKM80'])
	oppo = random.choice(['VNS-L31','VNS-L21','VNS-L22','VNS-L23','VNS-L53','VNS-AL00','VNS-L62','VNS-L52','VNS-DL00','VNS-TL00','DIG-L22'])
	vivo = random.choice(['SM-J810G','SM-J810F','J810Y','SM-J810Y','SM-J810GF','SM-J810M'])
	fbcr = random.choice(["Telenor", "fido", "MOVO AFRICA", "UFONE-PAKTel", "Zong", "Jazz", "SCO", "Jio", "Vodafone", "Airtel", "BSNL", "MTNL", "Grameenphone", "Robi", "Banglalink", "Teletalk", "Telkomsel", "Indosat Ooredoo", "Axiata", "Tri", "Smartfren", "China Mobile", "Unicom", "Telecom", "Satcom", "Docomo", "Rakuten", "IIJmio", "Orange", "Verizon", "AT&T", "T-Mobile", "Sprint", "Vodafone", "Telefonica", "EE", "Orange", "Three", "null"])
	fblc = random.choice(['en_US', 'en_GB', 'en_PK', 'es_LA', 'fr_FR', 'ur_PK', 'en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/" + str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ";FBBV/" + str(random.randint(1111111, 7777777)) + ";[FBAN/FB4A;FBAV/415.0.0.34.107;FBBV/272401182;FBDM/{density=3.0,width=1080,height=1920};FBLC/" + fblc + ";FBRV/172947184;FBCR/" + fbcr + ";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/" + samsung + ";FBSV/5.0;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/" + str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ";FBBV/" + str(random.randint(1111111, 7777777)) + ";[FBAN/FB4A;FBAV/465.0.0.60.83;FBBV/332957690;FBDM/{density=3.0,width=1080,height=1920};FBLC/" + fblc + ";FBRV/124613835;FBCR/" + fbcr + ";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/" + oppo + ";FBSV/7.0;FBCA/armeabi-v7a:armeabi;]"
	ua2 = "[FBAN/FB4A;FBAV/" + str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ";FBBV/" + str(random.randint(1111111, 7777777)) + ";[FBAN/FB4A;FBAV/455.0.0.0.35;FBBV/79007703;FBDM/{density=3.0,width=1080,height=2340};FBLC/" + fblc + ";FBRV/261846287;FBCR/" + fbcr + ";FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/" + realme + ";FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/" + str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ";FBBV/" + str(random.randint(1111111, 7777777)) + ";[FBAN/Orca-Android;FBAV/107.0.0.29.119;FBPN/com.facebook.orca;FBLC/" + fblc + ";FBBV/1547287;FBCR/" + fbcr + ";FBMF/samsung;FBBD/samsung;FBDV/" + vivo + ";FBSV/9.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.35,width=720,height=1480};]"
	ua = str(random.choice([ua6, ua5, ua7, ua2]))  # Add ua6 to the list of choices
	ugeni.append(ua)  # Append the randomly chosen user agent to the ugen list
# This will now generate a list of 10,000 random user agents.
