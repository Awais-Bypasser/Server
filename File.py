import random
ugeni = []
for agents in range(10000):
    samsung_models = ['SM-G998B', 'SM-G998U', 'SM-G998W', 'SM-G998N', 'SM-G9980', 'SM-G998E', 'SM-G998B/DS']
    xiaomi_models = ['M2101K6G', 'M2101K6I', 'M2101K6R', 'M2101K6T', 'M2101K6P', 'M2101K6G', 'M2101K6I']
    oneplus_models = ['IN2020', 'IN2021', 'IN2023', 'IN2025', 'IN2027', 'IN2029', 'IN2030']
    google_models = ['Pixel 6', 'Pixel 6 Pro', 'Pixel 5a', 'Pixel 5', 'Pixel 4a', 'Pixel 4 XL', 'Pixel 4']
    huawei_models = ['NOH-NX9', 'NOH-N29', 'NOH-NX1', 'NOH-NX2', 'NOH-NX3', 'NOH-NX4', 'NOH-NX5']
    motorola_models = ['XT2125-4', 'XT2125-2', 'XT2125-1', 'XT2125-3', 'XT2125-6', 'XT2125-7', 'XT2125-8']
    
    # Carriers
    carriers = ["Telenor", "Zong", "Zong 4G", "Zong CMPAK", "Jazz", "Ufone", "Jio", "Vodafone", "Airtel", "BSNL",
        "Grameenphone", "Robi", "Banglalink", "Orange", "Sprint", "Telefonica", "null", "Jazz", "Jazz 4G",
        "LTE", "Mobilink", "Telenor 4G", "PK-Ufone", "Verizon", "AT&T", "T-Mobile", "EE", "O2", "Three"]
    
    # Locales
    locales = ['en_US', 'en_GB', 'en_PK', 'es_LA', 'fr_FR', 'ur_PK', 'en_LA', 'ur_PK', 'de_DE', 'it_IT', 'pt_BR', 'ru_RU']
    device_model = random.choice(samsung_models + xiaomi_models + oneplus_models + google_models + huawei_models + motorola_models)
    carrier = random.choice(carriers)
    locale = random.choice(locales)
    
    # Generate random values for FBAN/FBAV/FBBV
    fban_fbav = f"{random.randint(111, 555)}.0.0.{random.randint(9, 49)}{random.randint(11, 77)}"
    fbbv = random.randint(1111111, 7777777)
    
    # Generate a random user agent string
    user_agent = (
        f"[FBAN/FB4A;FBAV/{fban_fbav};FBBV/{fbbv};"
        f"FBDM/{{density={random.uniform(1.0, 4.0):.1f},width={random.randint(480, 1440)},height={random.randint(1280, 2960)}}};"
        f"FBLC/{locale};FBCR/{carrier};FBMF/{random.choice(['samsung', 'Xiaomi', 'Oneplus', 'Google', 'HUAWEI', 'Motorola'])};"
        f"FBBD/{random.choice(['samsung', 'Xiaomi', 'ONEPLUS', 'Google', 'HUAWEI', 'Motorola'])};"
        f"FBPN/com.facebook.katana;FBDV/{device_model};FBSV/{random.randint(8, 14)};"
        f"FBOP/{random.randint(1, 19)};FBCA/{random.choice(['arm64-v8a', 'armeabi-v7a:armeabi'])};]"
    )
    
    ugeni.append(user_agent)
