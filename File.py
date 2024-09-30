import random
ugeni = []
for agents in range(10000):
	sx = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))
	dc = str(random.randint(1111111,9999999))
	ua6 = "[FBAN/Orca-Android;FBAV/"+sx+";FBPN/com.facebook.orca;FBLC/en_US;FBBV/"+dc+";FBCR/Telenor;FBMF/vivo;FBBD/vivo;FBDV/V2027;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1470};FB_FW/1;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,99))+".0.0."+str(random.randint(1111,9999))+";FBBV/"+str(random.randint(1111111,9999999))+";[FBAN/FB4A;FBAV/52.0.0.93.66;FBBV/20456933;FBDM/{density=3.0,width=1600,height=2560};FBLC/ig_NG;FBCR/Teleplus Wireless;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T800;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+sx+";FBBV/"+dc+";FBDM/{density=2.0,width=720,height=1470};FBLC/en_US;FBRV/0;FBCR/Telenor;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V2027;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]"
	ua2 = "[FBAN/MessengerLiteForiOS;FBAV/"+sx+";FBBV/"+dc+";FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBCR/;FBID/phone;FBLC/en_GB;FBOP/0]"
	ua7 = "[FBAN/FB4A;FBAV/"+sx+";FBBV/"+dc+";FBDM/{density=2.0,width=720,height=1412};FBLC/en_GB;FBRV/560625632;FBCR/Jazz;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1923;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";FBPN/com.facebook.katana;FBLC/en_US;FBCR/Telenor;FBMF/samsung;FBBD/samsung;FBDV/SM-T719Y;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.85,width=1536,height=2048};]"
	ua = str(random.choice([ua6,ua1,ua2,ua7]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
