import random

ugeni = []

# Device models by brand (using alternative model numbers)
device_models = {
    'samsung': ['SM-A528B', 'SM-A326B', 'SM-M526B', 'SM-F711B', 'SM-G990B', 'SM-G780G', 'SM-G998B'],
    'Xiaomi': ['2201117TG', '2201117TI', '2203129G', '22071212AG', '22081212UG', '22101316G', '22101316C'],
    'ONEPLUS': ['NE2215', 'NE2213', 'NE2211', 'LE2125', 'LE2123', 'LE2117', 'LE2113'],
    'Google': ['GA02099', 'GA02100', 'GA02101', 'GA02102', 'GA02103', 'GA02104', 'GA02105'],
    'HUAWEI': ['NOH-N29', 'NOH-N39', 'NOH-N49', 'NOH-N59', 'NOH-N69', 'NOH-N79', 'NOH-N89'],
    'MOTOROLA': ['XT2205-2', 'XT2205-3', 'XT2205-4', 'XT2205-5', 'XT2205-6', 'XT2205-7', 'XT2205-8']
}

# Carriers
carriers = ["Telenor", "Zong", "Zong 4G", "Zong CMPAK", "Jazz", "Ufone", "Jio", "Vodafone", "Airtel", "BSNL",
            "Grameenphone", "Robi", "Banglalink", "Orange", "Sprint", "Telefonica", "null", "Jazz", "Jazz 4G",
            "LTE", "Mobilink", "Telenor 4G", "PK-Ufone"]

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
    fban_fbav = f"{random.randint(111, 555)}.0.0.{random.randint(9, 99)}.{random.randint(11, 555)}"
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
