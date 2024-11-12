from color_conversion import rgb_to_cmyk, rgb_to_xyz
from helpers import start_update, end_update, clamp

def update_xyz_from_rgb(r, g, b, x_var, y_var, z_var, x_scale, y_scale, z_scale):
    print("Attempting to update XYZ from RGB")
    if not start_update():
        print("Update blocked by 'updating' flag")
        return
    try:
        print("Updating XYZ from RGB:", r, g, b)
        x, y, z = rgb_to_xyz(r, g, b)
        x_var.set(f"{x:.2f}")
        y_var.set(f"{y:.2f}")
        z_var.set(f"{z:.2f}")
        x_scale.set(x)
        y_scale.set(y)
        z_scale.set(z)
    finally:
        end_update()

def update_cmyk_from_rgb(r, g, b, c_var, m_var, y_cmyk_var, k_var, c_scale, m_scale, y_cmyk_scale, k_scale):
    print("Attempting to update CMYK from RGB")
    if not start_update():
        print("Update blocked by 'updating' flag")
        return
    try:
        print("Updating CMYK from RGB:", r, g, b)
        c, m, y_cmyk, k = rgb_to_cmyk(r, g, b)
        c_var.set(f"{c:.2f}")
        m_var.set(f"{m:.2f}")
        y_cmyk_var.set(f"{y_cmyk:.2f}")
        k_var.set(f"{k:.2f}")
        c_scale.set(c * 100)
        m_scale.set(m * 100)
        y_cmyk_scale.set(y_cmyk * 100)
        k_scale.set(k * 100)
    finally:
        end_update()



def on_rgb_change(r_scale, g_scale, b_scale, r_var, g_var, b_var, update_color_circle, update_xyz_from_rgb, update_cmyk_from_rgb,
                  x_var, y_var, z_var, x_scale, y_scale, z_scale,
                  c_var, m_var, y_cmyk_var, k_var, c_scale, m_scale, y_cmyk_scale, k_scale):
    if not start_update():
        return
    try:
        print("RGB changed:", r_scale.get(), g_scale.get(), b_scale.get())
        r = clamp(int(r_scale.get()))
        g = clamp(int(g_scale.get()))
        b = clamp(int(b_scale.get()))

        r_var.set(str(r))
        g_var.set(str(g))
        b_var.set(str(b))

        # Обновляем цветовой круг
        update_color_circle(r, g, b)

        # Сбрасываем флаг перед обновлением других моделей
        end_update()

        # Обновляем другие модели
        update_xyz_from_rgb(r, g, b, x_var, y_var, z_var, x_scale, y_scale, z_scale)
        update_cmyk_from_rgb(r, g, b, c_var, m_var, y_cmyk_var, k_var, c_scale, m_scale, y_cmyk_scale, k_scale)

    finally:
        end_update()  # Всегда гарантировать сброс флага

def on_rgb_enter(event, r_var, g_var, b_var, r_scale, g_scale, b_scale, update_color_circle, update_xyz_from_rgb, update_cmyk_from_rgb,
                 x_var, y_var, z_var, x_scale, y_scale, z_scale, c_var, m_var, y_cmyk_var, k_var, c_scale, m_scale, y_cmyk_scale, k_scale):
    try:
        r = int(r_var.get())
        g = int(g_var.get())
        b = int(b_var.get())

        r = clamp(r, 0, 255)
        g = clamp(g, 0, 255)
        b = clamp(b, 0, 255)

        r_scale.set(r)
        g_scale.set(g)
        b_scale.set(b)
        on_rgb_change(r_scale, g_scale, b_scale, r_var, g_var, b_var, update_color_circle, update_xyz_from_rgb, update_cmyk_from_rgb,
                      x_var, y_var, z_var, x_scale, y_scale, z_scale, c_var, m_var, y_cmyk_var, k_var, c_scale, m_scale, y_cmyk_scale, k_scale)
    except ValueError:
        pass
