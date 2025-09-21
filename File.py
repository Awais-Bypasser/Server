import random
ugeni = []
for agents in range(900000):
	samsung = random.choice(['SM-A205F','SM-A205FN','SM-A205GN','SM-A205YN','SM-A205G','SM-A205W','SM-A205U','SM-A205S','SM-S205DL','SM-A205U1'])
	realme = random.choice(['SM-G386F', 'SM-G386T1'])
	oppo = random.choice(['DIG-L01','DIG-L21HN','DIG-TL10','DIG-L03','DIG-L21','DIG-AL00','DIG-L23'])
	lg = random.choice(['K220','LS755','US610','K450','LGLS755','F750K','K210','LGUS610'])
	sony = random.choice(['D2303', 'D2305', 'D2306'])
	vivo = random.choice(['SM-J320H','SM-J3109','SM-J320FN','SM-J320P','SM-J320F','SM-J320M','SM-J320Y','SM-J320A','SM-J320G','SM-J327T1','SM-J320V','SM-J320YZ','SM-J320W8','SM-J320ZN','SM-J320N0','SM-J320R4'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/49.0.0.27.16;FBBV/277444756;FBDM/{density=2.1,width=800,height=1280};FBLC/en_GB;FBRV/185759173;FBCR/Telenor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T285YD;FBSV/5.1;FBOP/19;nullFBCA/armeabi-v7a:armeabi;]"
	ugeni.append(ua6) # Append the randomly chosen user agent to the ugen list
	
