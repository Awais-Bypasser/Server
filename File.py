import random
ugeni = []
for agents in range(10000):
	sx = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))
	dc = str(random.randint(1111111,9999999))
	ua1 = "[FBAN/Orca-Android;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";FBDM/{density=3.0,width=1600,height=2560};FBLC/zh_HK;FBCR/SmarTone;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-N9150;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,99))+".0.0."+str(random.randint(1111,9999))+";FBBV/"+str(random.randint(1111111,9999999))+";[FBAN/FB4A;FBAV/52.0.0.93.66;FBBV/20456933;FBDM/{density=3.0,width=1600,height=2560};FBLC/ig_NG;FBCR/Teleplus Wireless;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T800;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/15.0.0.82.38;FBBV/22459363;FBDM/{density=1.95,width=768,height=1024};FBLC/en_NZ;FBCR/Spark;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T350;FBSV/7.1.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua3 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";FBDM/{density=1.95,width=768,height=1024};FBLC/en_NZ;FBCR/Spark;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T350;FBSV/7.1.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+sx+";FBBV/"+dc+";FBDM/{density=2.0,width=720,height=1412};FBLC/en_GB;FBRV/560625632;FBCR/Jazz;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1923;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/27.0.0.81.94;FBBV/90253581;FBDM/{density=3.0,width=1600,height=2560};FBLC/zh_HK;FBCR/SmarTone;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-N9150;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua1,ua10,ua3,ua2]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
