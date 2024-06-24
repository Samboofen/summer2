import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

if __name__ == "__main__":
    radius = float(input())
    volume = sphere_volume(radius)
    print(volume)