import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-J111F','SM-J110G','SM-J110F','SM-J110H','SM-J110M','SM-J110L','SM-J111M'])
	realme = random.choice(['SM-G386F', 'SM-G386T1'])
	oppo = random.choice(['MLA-L01/L11','MLA-L11','MLA-L02/L12','MLA-L02','MLA-L12','MLA-L03/L13','MLA-L03','MLA-L13','MLA-AL10','MLA-L01'])
	lg = random.choice(['F510','LS996','H950','H955','US995','LGLS996'])
	sony = random.choice(['D2303', 'D2305', 'D2306'])
	vivo = random.choice(['SM-T116','SM-T116BU','SM-T116NQ','SM-T116NU','SM-T116NY'])
	fbcr = random.choice(["Zong","Jazz","Mobilink","Jazz 4G","Zong 4G"])
	fblc = "en_GB"
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027763;FBDM/{density=3.0,width=480,height=800};FBLC/"+fblc+";FBRV/281957295;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/4.4.4;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/436.0.0.35.101;FBBV/525437185;FBDM/{density=2.0,width=1536,height=2538};FBLC/ar_QA;FBCR/Verizon Wireless;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T815;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua5,ua6]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
