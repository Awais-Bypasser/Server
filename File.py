import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-A305F','SM-A305FN','SM-A305G','SM-A305GN','SM-A305YN','SM-A3050','SM-A305N','SM-A305GT'])
	realme = random.choice(['SM-A720F', 'SM-A720S'])
	oppo = random.choice(['YAL-L21','YAL-L61','YAL-L71','YAL-L61D'])
	vivo = random.choice(['SM-J327A','SM-J327','SM-J327T','SM-J327V','SM-J327P','SM-J327W','SM-J326AZ'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/164.0.0.26.159;FBBV/268946150;FBDM/{density=3.0,width=1080,height=2340};FBLC/"+fblc+";FBRV/718358164;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/231.1.0.57.129;FBBV/377040;FBDM/{density=3.0,width=1080,height=2340};FBLC/"+fblc+";FBRV/572816295;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/9.0;FBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/300.1.0.57.129;FBBV/377040;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBRV/371856283;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+realme+";FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/146.0.0.32.62;FBBV/666395;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+vivo+";FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/55.0.0.90.22;FBBV/20097172;FBDM/{density=2.2,width=1920,height=2560};FBLC/pl_PL;FBCR/Future Wireless;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T311;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua1,ua7,ua6,ua5,ua10]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
