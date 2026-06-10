def convert_length(value, from_unit, to_unit):
    to_meters = {"km": 1000, "m": 1, "cm": 0.01, "mm": 0.001, "mile": 1609.34, "inch": 0.0254}
    return value * to_meters[from_unit] / to_meters[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "C" and to_unit == "F": return value * 9/5 + 32
    if from_unit == "F" and to_unit == "C": return (value - 32) * 5/9
    if from_unit == "C" and to_unit == "K": return value + 273.15
    return value

if __name__ == "__main__":
    print(f"5 km = {convert_length(5, 'km', 'm')} m")
    print(f"100°C = {convert_temperature(100, 'C', 'F')}°F")
