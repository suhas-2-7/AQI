# utils.py
def get_sub_index(val, breakpoints):
    for Clow, Chigh, Ilow, Ihigh in breakpoints:
        if Clow <= val <= Chigh:
            return ((Ihigh - Ilow) / (Chigh - Clow)) * (val - Clow) + Ilow
    return 500

def classify_aqi(aqi):
    if aqi <= 50: return 'Good'
    elif aqi <= 100: return 'Satisfactory'
    elif aqi <= 200: return 'Moderate'
    elif aqi <= 300: return 'Poor'
    elif aqi <= 400: return 'Very Poor'
    else: return 'Severe'

# Define breakpoints
pm25_bp = [(0, 30, 0, 50), (31, 60, 51, 100), (61, 90, 101, 200),
           (91, 120, 201, 300), (121, 250, 301, 400), (251, 380, 401, 500)]
pm10_bp = [(0, 50, 0, 50), (51, 100, 51, 100), (101, 250, 101, 200),
           (251, 350, 201, 300), (351, 430, 301, 400), (431, 500, 401, 500)]
no2_bp = [(0, 40, 0, 50), (41, 80, 51, 100), (81, 180, 101, 200),
          (181, 280, 201, 300), (281, 400, 301, 400), (401, 500, 401, 500)]
so2_bp = [(0, 40, 0, 50), (41, 80, 51, 100), (81, 380, 101, 200),
          (381, 800, 201, 300), (801, 1600, 301, 400), (1601, 2000, 401, 500)]

def predict_aqi_from_values(pm25, pm10, no2, so2):
    aqi_pm25 = get_sub_index(pm25, pm25_bp)
    aqi_pm10 = get_sub_index(pm10, pm10_bp)
    aqi_no2 = get_sub_index(no2, no2_bp)
    aqi_so2 = get_sub_index(so2, so2_bp)
    
    final_aqi = max(aqi_pm25, aqi_pm10, aqi_no2, aqi_so2)
    aqi_bucket = classify_aqi(final_aqi)
    
    return round(final_aqi, 2), aqi_bucket
