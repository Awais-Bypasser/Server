import random
ugeni = []
for agents in range(10000):
    one = str(random.randint(101, 400))
    two = str(random.randint(101, 400))
    U_V1 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20097196;FBDM/{{density=2.625,width=1080,height=2131}};FBLC/en_US;FBRV/211775167;FBCR/Xfinity Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505U;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]"
    U_V2 = f"[FBAN/FB4A;FBAV/{one}.0.0.17.{two};FBBV/20454129;FBDM/{{ensity=3.0,width=1080,height=1920}};FBLC/en_US;FBRV/0;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-G930A;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    U_V3 = f"[FBAN/FB4A;FBAV/{one}.0.0.17.{two};FBBV/20454115;FBDM/{{density=3.0,width=1080,height=2192}};FBLC/en_US;FBRV/210347457;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto z4;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    U_V4 = f"[FBAN/FB4A;FBAV/{one}.0.0.17.{two};FBBV/20748104;FBDM/{{density=2.75,width=1080,height=2030}};FBLC/en_US;FBRV/118725758;FBCR/airtel;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    U_V5 = f"[FBAN/FB4A;FBAV/{one}.0.0.17.{two};FBBV/20454026;FBDM/{{density=1.5,width=480,height=854}};FBLC/en_US;FBRV/214902642;FBCR/Qlink;FBMF/ZTE;FBBD/ZTE;FBPN/com.facebook.katana;FBDV/N9137;FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    U_V6 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20097172;FBDM/{{density=3.375,width=1080,height=1998}};FBLC/en_US;FBRV/214902642;FBCR/AT&amp-T;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-Q710.FGN;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    U_V7 = f"Mozilla/5.0 (iPad; U; CPU iPhone OS 5_1_2 Mac OS X; en_US) AppleWebKit (KHTML, like Gecko) Mobile [FBAN/FBForIPhone;FBAV/4.1.2;FBBV/4110.0;FBDV/iPad2,1;FBMD/iPad;FBSN/iPhone OS;FBSV/5.1.2;FBSS/1; FBCR/;FBID/tablet;FBLC/en_US;FBSF/1.0]"
    U_V8 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20748051;FBDM/{{density=1.0,width=768,height=1024}};FBLC/en_US;FBRV/214902642;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T350;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    U_V9 = f"[FBAN/FB4A;FBAV/{one}.0.0.17.{two};FBBV/20454115;FBDM/{{density=2.0,width=1200,height=1831}};FBLC/en_US;FBRV/213932784;FBCR/T-Mobile;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-V521;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    U_V10 = f"[FBAN/FB4A;FBAV/{one}.0.0.17.{two};FBBV/20453986;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.1.3;FBSS/2;FBCR/;FBID/phone;FBLC/en_JP;FBOP/0]"
    U_V11 = f"[FBAN/Orca-Android;FBAV/{one}.0.0.17.{two};FBBV/37942114;FBDM/{{density=2.0,width=720,height=1344}};FBLC/en_US;FBRV/0;FBCR/airtel;FBMF/LAVA;FBBD/LAVA;FBPN/com.facebook.orca;FBDV/Z61_2GB;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    U_V12 = f"[FBAN/Orca-Android;FBAV/{one}.0.0.17.{two};FBBV/24927411;FBDM/{{density=2.0,width=1080,height=1920}};FBLC/en_US;FBCR/Verizon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-G900V/5;FBSV/5;FBOP/1;FBCA/arm64-v8a:armeabi-v7l-armeabi;]"
    U_V13 = f"[FBAN/Orca-Android;FBAV/{one}.0.0.17.{two};FBBV/20854563;FBDM/{{density=2.0,width=1440,height=2560}};FBLC/en_US;FBCR/T-Mobile;FBMF/LG;FBBD/G3;FBPN/com.facebook.orca;FBDV/LG-D850/5;FBSV/5;FBOP/1;FBCA/arm64-v8a:armeabi-v7l-armeabi;]"
    uaaaaa = random.choice([U_V1, U_V2, U_V3, U_V4, U_V5, U_V6, U_V7, U_V8, U_V9, U_V10, U_V11, U_V12, U_V13])
    ugeni.append(uaaaaa) # Append the randomly chosen user agent to the ugen list
