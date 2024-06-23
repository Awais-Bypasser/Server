import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-T380', 'SM-T385', 'SM-T385M'])
	realme = random.choice(['SM-G386F', 'SM-G386T1'])
	oppo = random.choice(['JKM-LX1','JKM-LX2','JKM-LX3','JKM-AL00','JKM-TL00','JKM-AL00a','JKM-AL00b'])
	lg = random.choice(['H870','H870DS','H873','H870S','LGM-G600L','H872','H871','LS993','US997','vs988','VS988','LGM-G600K','LGM-G600S','AS993','LGUS997','H870AR','H872PR','H871S','H870I'])
	sony = random.choice(['E5333', 'E5343', 'E5363'])
	vivo = random.choice(['GT-I9505','GT-I9515','SGH-I337','SC-04E','GT-I9515L'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880428;FBDM/{density=2.85,width=800,height=1280};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/7.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/82.0.0.23.70;FBBV/32429824;FBDM/{density=3.0,width=1080,height=2340};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/8.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/437.0.0.35.116;FBBV/527644830;FBDM/{density=2.75,width=720,height=1280};FBLC/en_GB;FBRV/381384816;FBCR/Jazz;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D2533;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/80.0.0.21.65;FBBV/31389908;FBDM/{density=3.0,width=1440,height=2880};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/LGE;FBBD/LGE;FBPN/com.facebook.katana;FBDV/"+lg+";FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/24.0.0.11.92;FBBV/11516731;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+vivo+";FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/42.0.0.0.95;FBBV/13553094;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/MobileNation;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/Samsung Galaxy A54 5G;FBSV/8.0;nullFBCA/armeabi-v7a:armeabi;]"
	ua9 = "[FBAN/FB4A;FBAV/238.0.0.16.207;FBBV/20748051;FBDM/{density=1.5,width=540,height=960};FBLC/es_ES;FBCR/vodafone ES;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/HUAWEI G6-L11;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]"
	ua3 = "[FBAN/FB4A;FBAV/257.0.0.17.137;FBBV/20454026;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/T-Mobile;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D801;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua6,ua5,ua7,ua2]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
