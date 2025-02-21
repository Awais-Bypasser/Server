import random

ugeni = []

# Device models by brand (using another set of model numbers)
device_models = {
    'samsung': ['SM-G780F', 'SM-G781B', 'SM-G985F', 'SM-G986B', 'SM-G991B', 'SM-G996B', 'SM-F707B'],
    'Xiaomi': ['M2007J3SY', 'M2012K11G', 'M2101K6G', 'M2102K1G', 'M2102K1C', 'M2012K11C', 'M2101K9G'],
    'Oneplus': ['IN2025', 'IN2023', 'IN2021', 'IN2019', 'IN2017', 'IN2015', 'IN2013'],
    'Google': ['GD1YQ', 'G9S9B', 'G8V0U', 'G6QU9', 'G4S1M', 'G3X7K', 'G2Z9P'],
    'HUAWEI': ['JEF-NX9', 'JAD-LX9', 'ANA-NX9', 'NOH-NX9', 'JNY-LX1', 'JLN-LX1', 'JSC-LX9'],
    'Motorola': ['XT2143-2', 'XT2153-1', 'XT2175-2', 'XT2201-1', 'XT2141-1', 'XT2135-2', 'XT2125-4']
}

# Carriers
carriers = ["Telenor", "Zong", "Zong 4G", "Zong CmPAK", "Jazz", "Ufone", "Jio", "Vodafone", "Airtel", "BSNL",
            "Grameenphone", "Robi", "Banglalink", "Orange", "Sprint", "Telefonica", "null", "Jazz", "Jazz 4G",
            "LTE", "Mobilink", "Telenor 4G", "PK-Ufone", "Verizon", "AT&T", "T-Mobile", "EE", "O2", "Three"]

# Locales
locales = ['en_US', 'en_GB', 'en_PK', 'es_LA', 'fr_FR', 'ur_PK', 'en_LA', 'ur_PK', 'de_DE', 'it_IT', 'pt_BR', 'ru_RU']

for agents in range(10000):
    # Randomly select brand
    brand = random.choice(list(device_models.keys()))
    
    # Select device model based on brand
    device_model = random.choice(device_models[brand])
    
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
