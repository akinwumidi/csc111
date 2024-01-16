import math

def print_cylinder_info(name, radius, height):
    volume = compute_volume(radius, height)
    surf_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.2f}")

def main():
    cylinders = [
        ("#1 Picnic", 6.83, 10.16),
        ("#1 Tall", 7.78, 11.91),
        ("#2", 8.73, 11.59),
        ("#2.5", 10.32, 11.91),
        ("#3 Cylinder", 10.79, 17.78),
        ("#5", 13.02, 14.29),
        ("#6Z", 5.4, 8.89),
        ("#8Z short", 6.83, 7.62),
        ("#10", 15.72, 17.78),
        ("#211", 6.83, 12.38),
        ("#300", 7.62, 11.27),
        ("#303", 8.1, 11.11)
    ]

    for cylinder in cylinders:
        print_cylinder_info(*cylinder)

def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    surf_area = 2 * math.pi * radius * (radius + height)
    return surf_area

if __name__ == "__main__":
    main()
