from color_conversion import xyz_to_rgb
from helpers import start_update, end_update, clamp, warn_if_clamped

def update_rgb_from_xyz(x, y, z, r_var, g_var, b_var, r_scale, g_scale, b_scale, update_color_circle, update_cmyk_from_rgb):
    print("Attempting to update RGB from XYZ")
    if not start_update():
        print("Update blocked by 'updating' flag")
        return
    try:
        print("Updating RGB from XYZ:", x, y, z)
        r, g, b = xyz_to_rgb(x, y, z)

        clamped_r = clamp(int(r))
        clamped_g = clamp(int(g))
        clamped_b = clamp(int(b))

        warn_if_clamped(r, clamped_r)
        warn_if_clamped(g, clamped_g)
        warn_if_clamped(b, clamped_b)

        r_var.set(str(clamped_r))
        g_var.set(str(clamped_g))
        b_var.set(str(clamped_b))
        r_scale.set(clamped_r)
        g_scale.set(clamped_g)
        b_scale.set(clamped_b)

        update_color_circle(clamped_r, clamped_g, clamped_b)
    finally:
        end_update()

def on_xyz_change(r_scale, g_scale, b_scale, r_var, g_var, b_var, update_color_circle, update_xyz_from_rgb, update_cmyk_from_rgb,
                  x_var, y_var, z_var, x_scale, y_scale, z_scale,
                  c_var, m_var, y_cmyk_var, k_var, c_scale, m_scale, y_cmyk_scale, k_scale):
    if not start_update():
        return
    try:
        print("XYZ changed:", x_scale.get(), y_scale.get(), z_scale.get())

        x = x_scale.get()
        y = y_scale.get()
        z = z_scale.get()

        end_update()

        update_rgb_from_xyz(x, y, z, r_var, g_var, b_var, r_scale, g_scale, b_scale, update_color_circle, update_cmyk_from_rgb)

        r_value = r_var.get()
        g_value = g_var.get()
        b_value = b_var.get()

        if r_value == "" or g_value == "" or b_value == "":
            print("RGB values are not yet initialized.")
            return

        update_cmyk_from_rgb(int(r_value), int(g_value), int(b_value), c_var, m_var, y_cmyk_var, k_var, c_scale, m_scale, y_cmyk_scale, k_scale)

        x_var.set(f"{x_scale.get():.2f}")
        y_var.set(f"{y_scale.get():.2f}")
        z_var.set(f"{z_scale.get():.2f}")

    finally:
        end_update()  # Всегда гарантировать сброс флага


def on_xyz_enter(event, x_var, y_var, z_var, x_scale, y_scale, z_scale,
                 r_var, g_var, b_var, r_scale, g_scale, b_scale,
                 update_rgb_from_xyz, update_color_circle, update_cmyk_from_rgb,
                 c_var, m_var, y_cmyk_var, k_var, c_scale, m_scale, y_cmyk_scale, k_scale):
    try:
        # Получение значений XYZ из полей ввода
        x = float(x_var.get())
        y = float(y_var.get())
        z = float(z_var.get())

        # Установка значений ползунков XYZ
        x_scale.set(x)
        y_scale.set(y)
        z_scale.set(z)

        on_xyz_change(r_scale, g_scale, b_scale, r_var, g_var, b_var, update_color_circle, update_rgb_from_xyz,
                      update_cmyk_from_rgb,
                      x_var, y_var, z_var, x_scale, y_scale, z_scale, c_var, m_var, y_cmyk_var, k_var, c_scale, m_scale,
                      y_cmyk_scale, k_scale)

    except ValueError:
        pass