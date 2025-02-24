import random

ugeni = []

for agents in range(10000):
    # Updated device models by brand (models only)
    samsung_models = ['SM-G991B', 'SM-G996B', 'SM-G998B', 'SM-F711B', 'SM-F916B', 'SM-A546B', 'SM-A345F']
    xiaomi_models = ['2201123G', '2208123C', '2204123MC', '2210133G', '2211123C', '2207132UG', '2210232B']
    oneplus_models = ['CPH2413', 'CPH2459', 'CPH2487', 'CPH2513', 'CPH2585', 'CPH2635', 'CPH2563']
    google_models = ['G030I', 'GQML3', 'G020I', 'G04LM', 'G0001', 'G020U', 'G01Y']
    huawei_models = ['ANA-AL00', 'ANA-NX9', 'EVR-AL00', 'JAD-LX1', 'ELE-L29', 'DIG-AL00', 'VNS-AL00']
    motorola_models = ['XT2215-4', 'XT2241-1', 'XT2301-7', 'XT2303-8', 'XT2203-3', 'XT2310-4', 'XT2113-5']
    
    # Carriers
    carriers = ["Telenor", "Zong", "Zong 4G", "Zong CMPAK", "Jazz", "Ufone", "Jio", "Vodafone", "Airtel", "BSNL",
        "Grameenphone", "Robi", "Banglalink", "Orange", "Sprint", "Telefonica", "null", "Jazz", "Jazz 4G",
        "LTE", "Mobilink", "Telenor 4G", "PK-Ufone", "Verizon", "AT&T", "T-Mobile", "EE", "O2", "Three"]
    
    # Locales
    locales = ['en_US', 'en_GB', 'en_PK', 'es_LA', 'fr_FR', 'ur_PK', 'en_LA', 'ur_PK', 'de_DE', 'it_IT', 'pt_BR', 'ru_RU']
    
    # Randomly select brand
    brand = random.choice(['samsung', 'Xiaomi', 'Oneplus', 'Google', 'HUAWEI', 'Motorola'])
    
    # Select device model based on brand
    if brand == 'samsung':
        device_model = random.choice(samsung_models)
    elif brand == 'Xiaomi':
        device_model = random.choice(xiaomi_models)
    elif brand == 'Oneplus':
        device_model = random.choice(oneplus_models)
    elif brand == 'Google':
        device_model = random.choice(google_models)
    elif brand == 'HUAWEI':
        device_model = random.choice(huawei_models)
    elif brand == 'Motorola':
        device_model = random.choice(motorola_models)
    
    # Randomly select carrier and locale
    carrier = random.choice(carriers)
    locale = random.choice(locales)
    
    # Generate random values for FBAN/FBAV/FBBV
    fban_fbav = f"{random.randint(11, 99)}.0.0.{random.randint(9, 49)}{random.randint(11, 77)}"
    fbbv = random.randint(1111111, 7777777)
    
    # Generate a random user agent string
    user_agent = (
        f"[FBAN/FB4A;FBAV/{fban_fbav};FBBV/{fbbv};"
        f"FBDM/{{density={random.uniform(1.0, 4.0):.1f},width={random.randint(480, 1440)},height={random.randint(1280, 2960)}}};"
        f"FBLC/{locale};FBCR/{carrier};FBMF/{brand};"
        f"FBBD/{brand};"
        f"FBPN/com.facebook.katana;FBDV/{device_model};FBSV/{random.randint(8, 14)};"
        f"FBOP/{random.randint(1, 19)};FBCA/{random.choice(['arm64-v8a', 'armeabi-v7a:armeabi'])};]"
    )
    
    ugeni.append(user_agent)
