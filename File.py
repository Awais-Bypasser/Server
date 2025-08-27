
import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-A710F','SM-A710S','SM-A710M','SM-A710FD','SM-A710Y','SM-A7100','SM-A710L','SM-A710K','SM-A7108'])
	realme = random.choice(['SM-G386F', 'SM-G386T1'])
	oppo = random.choice(['MLA-L01/L11','MLA-L11','MLA-L02/L12','MLA-L02','MLA-L12','MLA-L03/L13','MLA-L03','MLA-L13','MLA-AL10','MLA-L01'])
	lg = random.choice(['F510','LS996','H950','H955','US995','LGLS996'])
	sony = random.choice(['D2303', 'D2305', 'D2306'])
	vivo = random.choice(['SM-T116','SM-T116BU','SM-T116NQ','SM-T116NU','SM-T116NY'])
	fbcr = random.choice(["Zong","Jazz","Mobilink","Jazz 4G","Zong 4G"])
	fblc = "en_GB"
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027763;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBRV/315194628;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/7.0;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBRV/481759173;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/248.1.0.44.116;FBBV/184540762;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/0;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S367VL;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/291.0.0.44.120;FBBV/249604789;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/251279628;FBCR/JIO 4G;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/HM NOTE 1LTE;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/"+fblc+";FBBV/284619275;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBDV/SM-T330;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=800,height=1280};]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/85.0.0.15.70;FBBV/33678595;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-"+lg+";FBSV/5.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua10,ua5,ua7,ua6]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
