import numpy as np

# Matrices for RGB to XYZ conversion
RGB_to_XYZ_matrix = np.array([
    [0.4124564, 0.3575761, 0.1804375],
    [0.2126729, 0.7151522, 0.0721750],
    [0.0193339, 0.1191920, 0.9503041]
])

XYZ_to_RGB_matrix = np.linalg.inv(RGB_to_XYZ_matrix)

# Convert RGB to XYZ
def rgb_to_xyz(r, g, b):
    r /= 255
    g /= 255
    b /= 255

    def linearize(c):
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    r_lin = linearize(r)
    g_lin = linearize(g)
    b_lin = linearize(b)

    rgb_linear = np.array([r_lin, g_lin, b_lin])

    xyz = np.dot(RGB_to_XYZ_matrix, rgb_linear)
    return np.round(xyz * 100, 2)  # Return with 2 decimal precision

# Convert XYZ to RGB
def xyz_to_rgb(x, y, z):
    xyz = np.array([x, y, z]) / 100
    rgb_linear = np.dot(XYZ_to_RGB_matrix, xyz)

    def delinearize(c):
        return 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055

    r = delinearize(rgb_linear[0]) * 255
    g = delinearize(rgb_linear[1]) * 255
    b = delinearize(rgb_linear[2]) * 255

    # Clamp RGB values to be within 0-255
    return int(max(0, min(255, r))), int(max(0, min(255, g))), int(max(0, min(255, b)))

# Convert RGB to CMYK
def rgb_to_cmyk(r, g, b):
    if (r == 0) and (g == 0) and (b == 0):
        return 0, 0, 0, 1  # Special case for black

    r /= 255
    g /= 255
    b /= 255

    k = 1 - max(r, g, b)
    if k == 1:  # Avoid division by zero
        return 0, 0, 0, 1

    c = (1 - r - k) / (1 - k)
    m = (1 - g - k) / (1 - k)
    y = (1 - b - k) / (1 - k)

    return round(c, 2), round(m, 2), round(y, 2), round(k, 2)



# Convert CMYK to RGB
def cmyk_to_rgb(c, m, y, k):
    r = 255 * (1 - c) * (1 - k)
    g = 255 * (1 - m) * (1 - k)
    b = 255 * (1 - y) * (1 - k)

    # Clamp RGB values to be within 0-255
    return int(max(0, min(255, r))), int(max(0, min(255, g))), int(max(0, min(255, b)))


