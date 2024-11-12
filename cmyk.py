from color_conversion import cmyk_to_rgb
from helpers import start_update, end_update, clamp, warn_if_clamped
from rgb import update_xyz_from_rgb
def update_rgb_from_cmyk(c, m, y_cmyk, k, r_var, g_var, b_var, r_scale, g_scale, b_scale, update_color_circle, update_xyz_from_rgb):
    print("Attempting to update RGB from CMYK")
    if not start_update():
        print("Update blocked by 'updating' flag")
        return
    try:
        print("Updating RGB from CMYK:", c, m, y_cmyk, k)
        r, g, b = cmyk_to_rgb(c, m, y_cmyk, k)

        clamped_r = clamp(r)
        clamped_g = clamp(g)
        clamped_b = clamp(b)

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

def on_cmyk_change(r_scale, g_scale, b_scale, r_var, g_var, b_var, update_color_circle, update_xyz_from_rgb, update_cmyk_from_rgb,
                  x_var, y_var, z_var, x_scale, y_scale, z_scale,
                  c_var, m_var, y_cmyk_var, k_var, c_scale, m_scale, y_cmyk_scale, k_scale):
    if not start_update():
        return
    try:
        print("CMYK changed:", c_scale.get(), m_scale.get(), y_cmyk_scale.get(), k_scale.get())

        c = c_scale.get() / 100
        m = m_scale.get() / 100
        y_cmyk = y_cmyk_scale.get() / 100
        k = k_scale.get() / 100

        end_update()

        update_rgb_from_cmyk(c, m, y_cmyk, k, r_var, g_var, b_var, r_scale, g_scale, b_scale, update_color_circle,
                             update_xyz_from_rgb)
        r_value = r_var.get()
        g_value = g_var.get()
        b_value = b_var.get()

        if r_value == "" or g_value == "" or b_value == "":
            print("RGB values are not yet initialized.")
            return
        # Обновляем другие модели, начиная с XYZ
        update_xyz_from_rgb(int(r_var.get()), int(g_var.get()), int(b_var.get()), x_var, y_var, z_var, x_scale, y_scale, z_scale)

        # Обновляем значения полей CMYK
        c_var.set(f"{c:.2f}")
        m_var.set(f"{m:.2f}")
        y_cmyk_var.set(f"{y_cmyk:.2f}")
        k_var.set(f"{k:.2f}")

    finally:
        end_update()  # Всегда гарантировать сброс флага


def on_cmyk_enter(event, c_var, m_var, y_cmyk_var, k_var, c_scale, m_scale, y_cmyk_scale, k_scale,
                  r_var, g_var, b_var, r_scale, g_scale, b_scale,
                  update_rgb_from_cmyk, update_color_circle, update_rgb_from_xyz,
                  update_cmyk_from_rgb,
                  x_var, y_var, z_var, x_scale, y_scale, z_scale):
    try:
        # Получение значений CMYK из полей ввода
        c = float(c_var.get())
        m = float(m_var.get())
        y_cmyk = float(y_cmyk_var.get())
        k = float(k_var.get())

        # Установка значений ползунков CMYK
        c_scale.set(c * 100)
        m_scale.set(m * 100)
        y_cmyk_scale.set(y_cmyk * 100)
        k_scale.set(k * 100)


        # Вызов функции изменения CMYK с пересчетом остальных моделей
        on_cmyk_change(r_scale, g_scale, b_scale, r_var, g_var, b_var, update_color_circle, update_rgb_from_xyz, update_cmyk_from_rgb,
                       x_var, y_var, z_var, x_scale, y_scale, z_scale,
                       c_var, m_var, y_cmyk_var, k_var, c_scale, m_scale, y_cmyk_scale, k_scale)
    except ValueError:
        pass



