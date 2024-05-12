import random
ugeni = []
def ugeni():
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
	fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
	ua10 = "[FBAN/FB4A;FBAV/62.0.0.94.88;FBPN/com.facebook.katana;FBLC/"+fblc+";FBBV/315190856;FBCR/"+fbcr+";FBMF/OPPO;FBBD/OPPO;FBDV/Find 5;FBSV/12.4.8;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.75,width=1440,height=2780};FB_FW/1;]"
	return ua10 # Append the randomly chosen user agent to the ugen lis
