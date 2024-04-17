import random
ugen=[]
for agents in range(10000):
		rr = random.randint
		rc = random.choice
		wo = ['SM-A035G','SM-A032F', 'SM-A037M','SM-A105FN','SM-A102U','CPH2015','CPH2081','M2012K11G','RMX2151','RMX2040','RMX2061','RMX3081','RMX3471','RMX3392','CPH2195','220233L2I','220333QNY','Infinix X5010','X652C','Infinix X5515I','RMX2027','RMX3503','RMX3171','CPH2363','CPH1609','SM-X205','SM-A716U1','LM-G850','JAT-LX3','HRY-LX1','SM-N970U1','SM-T878U','M2006C3MT','M2006C3LVG','V2057A','JEF-NX9','STK-L22','220333QNY','V1921A']
		ads = random.choice(wo)
		su = ['QP1A.190711.020','QKQ1.190918.001','TP1A.220624.014','SP1A.210812.016','QTG3.200617.002','SQ3A.220705.0040','RP1A.200720.011']
		ade = random.choice(su)
		uab = "Mozilla/5.0 (Linux; Android " + ads + " Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
		uaxb = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; " + ads + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 300)) + " Mobile Safari/537.36"
		uaf = "Mozilla/5.0 (Linux; Android " + ads + " Build/"+ade+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
		ua = str(rc([uab,uaxb,uaf]))
		ugen.append(ua)
