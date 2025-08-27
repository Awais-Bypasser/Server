
import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-N750','SM-N7505','SM-N750K','SM-N750S','SM-N7507','SM-N750L','SM-N7500Q','SM-N7506V','SM-N7505L'])
	realme = random.choice(['SM-G386F', 'SM-G386T1'])
	oppo = random.choice(['TIT-AL00','TIT-U02','TIT-L01','TIT-TL00'])
	lg = random.choice(['LG-D722', 'D724', 'F470K'])
	sony = random.choice(['E2312', 'E2333', 'E2363'])
	vivo = random.choice(['SM-A5000','SM-A5009','SM-A500F','SM-A500F1','SM-A500FQ','SM-A500FU','SM-A500G','SM-A500H','SM-A500HQ','SM-A500K','SM-A500L','SM-A500S','SM-A500YZ','SM-A500Y','SM-A500W'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880428;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/4.3;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/82.0.0.23.70;FBBV/32429824;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/437.0.0.35.116;FBBV/527644830;FBDM/{density=2.75,width=720,height=1280};FBLC/en_GB;FBRV/381384816;FBCR/"+fbcr+";FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D2502;FBSV/4.4.2;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/80.0.0.21.65;FBBV/31389908;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/LGE;FBBD/LGE;FBPN/com.facebook.katana;FBDV/"+lg+";FBSV/4.4.2;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/24.0.0.11.92;FBBV/11516731;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+vivo+";FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/292693120;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5A;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua10,ua5,ua7,ua6,ua1,ua2]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
