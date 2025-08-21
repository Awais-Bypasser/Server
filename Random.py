import random
ugen=[]
for agents in range(10000):
		rr = random.randint
		rc = random.choice
		wo = ['V2061A','CPH2145', 'SM-S901B','FLA-LX3','M2012K11AC','LG-F800K','RMX3472','SM-J610G','RMX3381','SM-A025V','Ivivo 1951','HMA-AL00','SM-T595','SM-X205','V2041','HRY-LX1','SM-N970U1','Cyber X','RX4505','JEF-NX9','STK-L22','CPH2205','RMO-NX3','SM-A600U','Nokia C10','SO-03K','V2040','SM-A326K','CPH1933','S9-KC','SM-G6200','RMX3430','vivo X21UD A','ONEPLUS A5000','SM-M105M']
		ads = random.choice(wo)
		su = ['QP1A.190711.020','QKQ1.190918.001','TP1A.220624.014','SP1A.210812.016','QTG3.200617.002','SQ3A.220705.0040','RP1A.200720.011']
		ade = random.choice(su)
		uab = "Mozilla/5.0 (Linux; Android " + ads + " Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
		uaxb = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; " + ads + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 300)) + " Mobile Safari/537.36"
		uaf = "Mozilla/5.0 (Linux; Android " + ads + " Build/"+ade+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
		ua = str(rc([uab,uaxb,uaf]))
		ugen.append(ua)
