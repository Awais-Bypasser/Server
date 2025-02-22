import random

ugeni = []

# Updated device models by brand
device_models = {
    'samsung': ['SM-G998B', 'SM-G996B', 'SM-G991B', 'SM-G781B', 'SM-G780F', 'SM-F926B', 'SM-F721B'],
    'Xiaomi': ['2201123C', '2201117TI', '2109119DI', '2107119DI', '21061110AI', '2009119DI', '20061110AI'],
    'Oneplus': ['NE2215', 'NE2213', 'NE2211', 'NE2210', 'NE2205', 'NE2203', 'NE2201'],
    'Google': ['GX7AS', 'GWKK3', 'G9S9B', 'G8V0U', 'G7V0U', 'G6QU9', 'G5S1M'],
    'HUAWEI': ['NOH-NX9', 'JAD-LX9', 'ANA-NX9', 'JEF-NX9', 'JNY-LX1', 'JLN-LX1', 'JSC-LX9'],
    'Motorola': ['XT2301-5', 'XT2201-2', 'XT2155-1', 'XT2145-2', 'XT2135-1', 'XT2125-4', 'XT2115-2'],
    'Apple': ['iPhone16,1', 'iPhone16,2', 'iPhone15,1', 'iPhone15,2', 'iPhone14,1', 'iPhone14,2', 'iPhone13,1'],
    'Sony': ['XQ-CT72', 'XQ-BT52', 'XQ-AT52', 'XQ-CT54', 'XQ-BT54', 'XQ-AT54', 'XQ-CT62'],
    'Nokia': ['TA-1398', 'TA-1394', 'TA-1392', 'TA-1388', 'TA-1384', 'TA-1382', 'TA-1378'],
    'LG': ['LM-V600', 'LM-V500', 'LM-V405', 'LM-V350', 'LM-V300', 'LM-V250', 'LM-V200']
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
