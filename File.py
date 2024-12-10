import random
ugeni = []
for agents in range(10000):
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/24.0.0.80.62;FBBV/18583273;FBDM/{density=2.85,width=1536,height=2048};FBLC/pl_PL;FBCR/Global SIM Card;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SAMSUNG-SM-T817A;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/86.0.0.52.49;FBBV/95342775;FBDM/{density=2.35,width=800,height=1280};FBLC/lt_LT;FBCR/Verizon Wireless;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T335;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua6,ua10]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
