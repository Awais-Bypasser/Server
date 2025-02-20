import random

ugeni = []

for agents in range(10000):
    # Device models by brand
    samsung_models = ['SM-S901U', 'SM-S906U', 'SM-S908U', 'SM-S911U', 'SM-S916U', 'SM-S918U', 'SM-S921U']
    xiaomi_models = ['2201122G', '2203121C', '2207122MC', '22081212UG', '2210132G', '2210132C', '2210132UG']
    oneplus_models = ['CPH2415', 'CPH2449', 'CPH2451', 'CPH2487', 'CPH2515', 'CPH2583', 'CPH2609']
    google_models = ['Pixel 7', 'Pixel 7 Pro', 'Pixel 7a', 'Pixel 8', 'Pixel 8 Pro', 'Pixel Fold', 'Pixel Tablet']
    huawei_models = ['NOH-AN00', 'NOH-AN01', 'NOH-AN10', 'NOH-AN20', 'NOH-AN30', 'NOH-AN40', 'NOH-AN50']
    motorola_models = ['XT2301-5', 'XT2301-6', 'XT2301-7', 'XT2301-8', 'XT2301-9', 'XT2301-10', 'XT2301-11']
    
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
    fban_fbav = f"{random.randint(111, 555)}.0.0.{random.randint(9, 49)}{random.randint(11, 77)}"
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
