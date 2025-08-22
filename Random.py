import random

ugen = []

# ✅ Authentic device model codes
real_device_models = [
    # Samsung
    'SM-G960F', 'SM-G970F', 'SM-G981B', 'SM-G998B', 'SM-A125F',
    'SM-A515F', 'SM-M127F', 'SM-A546E', 'SM-G990E', 'SM-A326B',
    # Xiaomi / Redmi / POCO
    'M2101K6G', 'M2007J20CG', 'M2006C3LG', '22101320G', '23076RN4BI',
    '2201116SG', '23013RK75G', '23049PCD8G', 'M2102J20SG', '220333QAG',
    # Realme
    'RMX3081', 'RMX3371', 'RMX2020', 'RMX3241', 'RMX3472',
    # Oppo
    'CPH2185', 'CPH2239', 'CPH2423', 'CPH2205', 'CPH2517',
    # Vivo
    'V2043', 'V2055A', 'V2140', 'V2160', 'V2231',
    # OnePlus
    'LE2113', 'CPH2413', 'NE2211', 'CPH2467',
    # Motorola
    'XT2163-4', 'XT2233-2', 'XT2125-4', 'XT2223-1',
    # Huawei
    'LYA-L29', 'MAR-LX1M', 'ANA-NX9', 'JNY-LX1',
    # Sony
    'XQ-AD52', 'XQ-BT52', 'XQ-AT52'
]

# Build and version generators
build_versions = ['QP1A.190711.020', 'SP1A.210812.016', 'RP1A.200720.011', 'TP1A.220624.014', 'UP1A.231005.007']

def generate_chrome_version():
    return f"{random.randint(100, 125)}.0.{random.randint(3000, 6500)}.{random.randint(0, 150)}"

def generate_fb_version():
    return f"{random.randint(300, 500)}.0.0.{random.randint(10, 99)}.{random.randint(100, 999)}"

# Generate user-agent strings
for _ in range(10000):
    android_version = random.randint(8, 13)
    model = random.choice(real_device_models)
    build = random.choice(build_versions)
    chrome_ver = generate_chrome_version()
    fb_ver = generate_fb_version()

    # Type 1: WebView UA
    ua1 = (
        f"Mozilla/5.0 (Linux; Android {android_version}; {model} Build/{build}; wv) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 "
        f"Chrome/{chrome_ver} Mobile Safari/537.36"
    )

    # Type 2: Facebook App UA
    ua2 = (
        f"Mozilla/5.0 (Linux; Android {android_version}; {model} Build/{build}) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 "
        f"Chrome/{chrome_ver} Mobile Safari/537.36 "
        f"[FB_IAB/FB4A;FBAV/{fb_ver};]"
    )

    # Type 3: Chrome Browser UA
    ua3 = (
        f"Mozilla/5.0 (Linux; Android {android_version}; {model} Build/{build}) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) "
        f"Chrome/{chrome_ver} Mobile Safari/537.36"
    )

    # Randomly choose one of the three types
    ua = random.choice([ua1, ua2, ua3])
    ugen.append(ua)
