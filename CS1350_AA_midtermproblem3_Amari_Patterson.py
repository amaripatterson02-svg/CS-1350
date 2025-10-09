import numpy as np

# 1. Calculate daily averages
def calculate_daily_averages(temps):
    # Mean across columns (axis=1 → row-wise average)
    daily_averages = np.mean(temps, axis=1)
    return daily_averages

# 2. Find hottest day (based on daily averages)
def find_hottest_day(temps):
    daily_averages = calculate_daily_averages(temps)
    hottest_day_index = np.argmax(daily_averages)
    return hottest_day_index

# 3. Count how many readings are below threshold
def count_cold_readings(temps, threshold):
    cold_count = np.sum(temps < threshold)
    return cold_count

# 4. Normalize all temperatures to 0–100 scale
def normalize_temperatures(temps):
    min_temp = np.min(temps)
    max_temp = np.max(temps)
    normalized = (temps - min_temp) / (max_temp - min_temp) * 100
    return normalized

# Test your functions
if __name__ == "__main__":
    temps = np.array([
        [65, 75, 70],
        [68, 78, 72],
        [70, 80, 75],
        [62, 73, 68],
        [67, 77, 71],
        [69, 79, 74],
        [64, 74, 69]
    ])

    print("Daily averages:", calculate_daily_averages(temps))
    print("Hottest day index:", find_hottest_day(temps))
    print("Cold readings (< 70):", count_cold_readings(temps, 70))
    print("Normalized (first day):", normalize_temperatures(temps)[0])
