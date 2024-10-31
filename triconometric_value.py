import math


def calculate_trig_values(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    
    sin_value = math.sin(angle_radians)
    cos_value = math.cos(angle_radians)
    tan_value = math.tan(angle_radians)
    
    return sin_value, cos_value, tan_value


angle = float(input("Enter the angle in degrees: "))
sin_value, cos_value, tan_value = calculate_trig_values(angle)

print(f"Sin({angle}) = {sin_value}")
print(f"Cos({angle}) = {cos_value}")
print(f"Tan({angle}) = {tan_value}")
