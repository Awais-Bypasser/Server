import random
ugeni = []
for agents in range(100000):
	samsung = random.choice(['SM-N900','SM-N9002','SM-N9005','SM-N9007','SM-N9008','SM-N9008S','SM-N9008V','SM-N9009','SM-N9009V','SM-N900A','SM-N900K','SM-N900L','SM-N900P','SM-N900R4','SM-N900S','SM-N900T','SM-N900U','SM-N900V','SM-N900W8','SM-N900X','SM-N9000Q','SM-N9006','SM-9005'])
	realme = random.choice(['RMX3310','RMX3312','RMX3311'])
	oppo = random.choice(['CDY-AN00','CDY-NX9B','CDY-TN00','CDY-AN20','CDL-AN50'])
	lg = random.choice(['CPH1913','CPH1911'])
	sony = random.choice(['vivo 1935', 'V1965A'])
	vivo = random.choice(['SM-A526B','SM-A526B/DS','SM-A5260','SM-A526W','SM-A526U','SM-A526U1'])
	fbcr = random.choice(["Zong","Jazz","Zong 4G","Zong CMPak","Jio 4G","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','ur_PK'])
	ft = ['SM-M625F','LM-K525', 'NID-1050','SM-A3051','CPH2069','RMX3286','A101XM','SM-A505GT','WKG-LX9','SM-A4260','Infinix X680C','RMX3265','GLA-LX1','Redmi 4X','V2204','vivo 2018','PCB-T104','2201122G','Infinix X688B','RMP2106','OXF-AN10','Infinix X6835B','CPH2399','SM-F731B','SM-T515','CPH2209','M2101K6R','V2135','SM-M307FN','JLN-LX3','CPH2123','Lenovo TB-X605F','V2110','RMX3572','LM-X420']
	su = ['QP1A.190711.020','QKQ1.190918.001','TP1A.220624.014','SP1A.210812.016','QTG3.200617.002','SQ3A.220705.0040','RP1A.200720.011']
	so = random.choice(su)
	efg = random.choice(ft)
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/38.0.0.0.18;FBBV/5818742;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+samsung+";FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua6,ua5,ua7,ua2,ua4,ua1,ua3,ua10]))  # Add ua6 to the list of choices
	ugeni.append(ua10) # Append the randomly chosen user agent to the ugen list
