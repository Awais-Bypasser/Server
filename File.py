import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-A520F','SM-A520F','SM-A520K','SM-A520L','SM-A520S','SM-A520W','SM-A520FD'])
	realme = random.choice(['SM-G386F', 'SM-G386T1'])
	oppo = random.choice(['EVA-L09','EVA-L19','EVA-L29','EVA-AL10','EVA-TL00','EVA-AL00','EVA-DL00'])
	lg = random.choice(['F310L', 'F310LR'])
	sony = random.choice(['E5333', 'E5343', 'E5363'])
	vivo = random.choice(['SM-J105F','SM-j105H','SM-J105H','SM-J105B','SM-J105Y','SM-J105M'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/41.0.0.41.46;FBBV/31880428;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/82.0.0.27.17;FBBV/32429824;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/196.0.0.76;FBBV/923196055;FBDM/{density=1.0,width=480,height=800};FBLC/en_PK;FBRV/662382466;FBCR/Jazz;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Galaxy S23 Ultra;FBSV/2.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/270.0.0.21.65;FBBV/196927592;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/LGE;FBBD/LGE;FBPN/com.facebook.katana;FBDV/"+lg+";FBSV/4.3;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/17.0.0.41.32;FBBV/11516731;FBDM/{density=1.75,width=480,height=800};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+vivo+";FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/36.0.0.36.48;FBBV/3740566;FBDM/{density=3.6,width=1600,height=2560};FBLC/ro_RO;FBCR/FreeUP Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-T805;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]"
	ua9 = "[FBAN/FB4A;FBAV/238.0.0.16.207;FBBV/20748051;FBDM/{density=1.5,width=540,height=960};FBLC/es_ES;FBCR/vodafone ES;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/HUAWEI G6-L11;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]"
	ua3 = "[FBAN/FB4A;FBAV/257.0.0.17.137;FBBV/20454026;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/T-Mobile;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D801;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua6,ua5,ua7,ua2]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
