import random

ugeni = []

uas = ['SM-T810','SM-T815','SM-T813N','SM-T819N','SM-T819','SM-T813','SM-T815Y','SM-T819Y']
uar = random.choice(['SM-J120F','SM-J120H','SM-J120M','SM-J120M','SM-J120T','SM-J120G','SM-J120A','SM-J120FN','SM-J120AZ','SM-J120ZN','SM-J120W'])
ft = ['SM-M625F', 'LM-K525', 'NID-1050', 'SM-A3051', 'CPH2069', 'RMX3286', 'A101XM', 'SM-A505GT', 'WKG-LX9', 'SM-A4260', 'Infinix X680C', 'RMX3265', 'GLA-LX1', 'Redmi 4X', 'V2204', 'vivo 2018', 'PCB-T104', '2201122G', 'Infinix X688B', 'RMP2106', 'OXF-AN10', 'Infinix X6835B', 'CPH2399', 'SM-F731B', 'SM-T515', 'CPH2209', 'M2101K6R', 'V2135', 'SM-M307FN', 'JLN-LX3', 'CPH2123', 'Lenovo TB-X605F', 'V2110', 'RMX3572', 'LM-X420']
an = ['9', '8']
aru = ['{density=3.0,width=1080,height=2480}', '{density=2.75,width=720,height=1612}', '{density=3.0,width=1080,height=2400}', '{density=2.75,width=720,height=1520}', '{density=3.0,width=1080,height=2408}', '{density=3.0,width=1080,height=2340}', '{density=3.0,width=1080,height=2376}', '{density=3.0,width=1080,height=2404}', '{density=3.0,width=1080,height=2404}', '{density=2.75,width=720,height=1280}', '{density=3.0,width=1080,height=2408}', '{density=2.75,width=720,height=1440}', '{density=2.75,width=720,height=1280}', '{density=3.0,width=1080,height=2448}', '{density=3.0,width=1080,height=2448}', '{density=3.0,width=1080,height=2448}', '{density=3.0,width=1080,height=2400}', '{density=3.0,width=1080,height=2412}', '{density=3.0,width=1080,height=2160}', '{density=3.0,width=1440,height=3040}', '{density=3.0,width=1080,height=2340}', '{density=3.0,width=1080,height=2340}', '{density=3.0,width=1080,height=2340}', '{density=3.0,width=1080,height=2400}', '{density=3.0,width=1080,height=2400}', '{density=3.0,width=1440,height=3120}', '{density=3.0,width=1080,height=2400}', '{density=3.0,width=1080,height=2400}', '{density=2.75,width=720,height=1640}', '{density=2.75,width=720,height=1440}', '{density=2.75,width=720,height=1600}', '{density=2.75,width=720,height=1600}', '{density=3.0,width=1080,height=2408}', '{density=3.0,width=1080,height=2408}', '{density=3.0,width=1080,height=2408}', '{density=3.0,width=1080,height=2400}', '{density=3.0,width=1080,height=2400}', '{density=3.0,width=1080,height=2246}', '{density=3.0,width=1080,height=2400}', '{density=2.75,width=720,height=1612}']
su = ['QP1A.190711.020', 'QKQ1.190918.001', 'TP1A.220624.014', 'SP1A.210812.016', 'QTG3.200617.002', 'SQ3A.220705.0040', 'RP1A.200720.011']
xg = ['armeabi-v7a:armeabi', 'arm64-v8a', 'armeabi-v8a:armeabi', 'arm64-v8a:armeabi']
fr = ['en_US', 'en_GB', 'es_LA', 'fr_FR', 'en_PK', 'id_IN']
cv = ['airtel', 'IND airtel', 'Nepal Telecom', 'Jio 4G', 'Jazz', 'UFONE', 'Zong 4G', 'Telenor']

for agents in range(10000):
	ap = random.choice(fr)
	af = random.choice(aru)
	fd = random.choice(cv)
	facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
	ux = random.choice(an)
	fo = random.choice(xg)
	ub = random.choice(uas)
	efg = random.choice(ft)
	so = random.choice(su)
	uae = "Dalvik/2.1.0 (Linux; U; Android " + str(random.randint(4, 13)) + "; " + efg + " Build/" + so + ") [FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/216.0.0.40.121;FBBV/1638093;FBLC/"+ap+";FBRV/461872867;FBCR/"+fd+";FBMF/samsung;FBBD/samsung;FBDV/"+ub+";FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;FBDM/{density=2.8,height=1536,width=2048};]"
	g = "[FBAN/Orca-Android;FBAV/346.0.0.7.117;FBPN/com.facebook.orca;FBLC/"+ap+";FBBV/348143439;FBCR/"+fd+";FBMF/samsung;FBBD/samsung;FBDV/"+uar+";FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=480,height=800};FB_FW/1;]"
	uax = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/"+str(random.randint(1111111,7777777))+";"+g
	ua = str(random.choice([uae,uax]))  # Add ua6 to the list of choices
	ugeni.append(ua)
