# gui.py
import customtkinter as ctk
from cmyk import on_cmyk_change, update_rgb_from_cmyk, on_cmyk_enter
from rgb import on_rgb_change, update_xyz_from_rgb, update_cmyk_from_rgb, on_rgb_enter
from xyz import on_xyz_change, update_rgb_from_xyz, on_xyz_enter
from helpers import start_update, end_update


def create_interface(root):
    global updating
    updating = False

    # Color circle update function
    def update_color_circle(r, g, b):
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.itemconfig(color_circle, fill=color)

    # RGB, CMYK, XYZ variables
    r_var, g_var, b_var = ctk.StringVar(), ctk.StringVar(), ctk.StringVar()
    x_var, y_var, z_var = ctk.StringVar(), ctk.StringVar(), ctk.StringVar()
    c_var, m_var, y_cmyk_var, k_var = ctk.StringVar(), ctk.StringVar(), ctk.StringVar(), ctk.StringVar()

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Создаем контейнер и настраиваем его
    container = ctk.CTkFrame(root)
    container.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    container.grid_rowconfigure(0, weight=1)
    container.grid_rowconfigure(1, weight=1)
    container.grid_rowconfigure(2, weight=1)
    container.grid_rowconfigure(3, weight=1)
    container.grid_rowconfigure(4, weight=1)
    container.grid_rowconfigure(5, weight=1)
    container.grid_columnconfigure(0, weight=1)
    container.grid_columnconfigure(1, weight=1)
    container.grid_columnconfigure(2, weight=1)
    container.grid_columnconfigure(3, weight=1)

    # === RGB Section ===
    ctk.CTkLabel(container, text="RGB", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=4, pady=(10, 10),
                                                                         sticky="n")

    ctk.CTkLabel(container, text="0").grid(row=2, column=0, sticky="w", padx=(10, 5))
    ctk.CTkLabel(container, text="255").grid(row=2, column=0, sticky="e", padx=(5, 10))

    r_scale = ctk.CTkSlider(container, from_=0, to=255)
    g_scale = ctk.CTkSlider(container, from_=0, to=255)
    b_scale = ctk.CTkSlider(container, from_=0, to=255)

    r_entry = ctk.CTkEntry(container, textvariable=r_var, width=60)
    r_entry.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
    r_scale.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

    g_entry = ctk.CTkEntry(container, textvariable=g_var, width=60)
    g_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
    g_scale.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

    b_entry = ctk.CTkEntry(container, textvariable=b_var, width=60)
    b_entry.grid(row=1, column=2, padx=10, pady=5, sticky="ew")
    b_scale.grid(row=2, column=2, padx=10, pady=5, sticky="ew")

    # Минимальные и максимальные метки для зеленого и синего
    ctk.CTkLabel(container, text="0").grid(row=2, column=1, sticky="w", padx=(10, 5))
    ctk.CTkLabel(container, text="255").grid(row=2, column=1, sticky="e", padx=(5, 10))

    ctk.CTkLabel(container, text="0").grid(row=2, column=2, sticky="w", padx=(10, 5))
    ctk.CTkLabel(container, text="255").grid(row=2, column=2, sticky="e", padx=(5, 10))

    r_scale.configure(command=lambda _: on_rgb_change(
        r_scale, g_scale, b_scale, r_var, g_var, b_var, update_color_circle, update_xyz_from_rgb, update_cmyk_from_rgb,
        x_var, y_var, z_var, x_scale, y_scale, z_scale,
        c_var, m_var, y_cmyk_var, k_var, c_scale, m_scale, y_cmyk_scale, k_scale))  # Pass CMYK args

    g_scale.configure(command=lambda _: on_rgb_change(
        r_scale, g_scale, b_scale, r_var, g_var, b_var, update_color_circle, update_xyz_from_rgb, update_cmyk_from_rgb,
        x_var, y_var, z_var, x_scale, y_scale, z_scale,
        c_var, m_var, y_cmyk_var, k_var, c_scale, m_scale, y_cmyk_scale, k_scale))

    b_scale.configure(command=lambda _: on_rgb_change(
        r_scale, g_scale, b_scale, r_var, g_var, b_var, update_color_circle, update_xyz_from_rgb, update_cmyk_from_rgb,
        x_var, y_var, z_var, x_scale, y_scale, z_scale,
        c_var, m_var, y_cmyk_var, k_var, c_scale, m_scale, y_cmyk_scale, k_scale))

    # === XYZ Section ===
    ctk.CTkLabel(container, text="XYZ", font=("Arial", 20, "bold")).grid(row=3, column=0, columnspan=4, pady=(20, 10),
                                                                         sticky="n")

    ctk.CTkLabel(container, text="0").grid(row=5, column=0, sticky="w", padx=(10, 5))
    ctk.CTkLabel(container, text="100").grid(row=5, column=0, sticky="e", padx=(5, 10))

    x_scale = ctk.CTkSlider(container, from_=0, to=100)
    y_scale = ctk.CTkSlider(container, from_=0, to=100)
    z_scale = ctk.CTkSlider(container, from_=0, to=100)

    x_entry = ctk.CTkEntry(container, textvariable=x_var, width=80)
    x_entry.grid(row=4, column=0, padx=10, pady=5, sticky="ew")
    x_scale.grid(row=5, column=0, padx=10, pady=5, sticky="ew")

    y_entry = ctk.CTkEntry(container, textvariable=y_var, width=80)
    y_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
    y_scale.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

    z_entry = ctk.CTkEntry(container, textvariable=z_var, width=80)
    z_entry.grid(row=4, column=2, padx=10, pady=5, sticky="ew")
    z_scale.grid(row=5, column=2, padx=10, pady=5, sticky="ew")

    # Минимальные и максимальные метки для Y и Z
    ctk.CTkLabel(container, text="0").grid(row=5, column=1, sticky="w", padx=(10, 5))
    ctk.CTkLabel(container, text="100").grid(row=5, column=1, sticky="e", padx=(5, 10))

    ctk.CTkLabel(container, text="0").grid(row=5, column=2, sticky="w", padx=(10, 5))
    ctk.CTkLabel(container, text="100").grid(row=5, column=2, sticky="e", padx=(5, 10))


    '''def test_cmyk_change():
        print("CMYK Slider Moved")

    def test_xyz_change():
        print("XYZ Slider Moved")
    '''

    # Bind XYZ sliders
    x_scale.configure(command=lambda _: on_xyz_change(
        r_scale, g_scale, b_scale, r_var, g_var, b_var, update_color_circle, update_xyz_from_rgb, update_cmyk_from_rgb,
        x_var, y_var, z_var, x_scale, y_scale, z_scale,
        c_var, m_var, y_cmyk_var, k_var, c_scale, m_scale, y_cmyk_scale, k_scale))
    y_scale.configure(command=lambda _: on_xyz_change(
        r_scale, g_scale, b_scale, r_var, g_var, b_var, update_color_circle, update_xyz_from_rgb, update_cmyk_from_rgb,
        x_var, y_var, z_var, x_scale, y_scale, z_scale,
        c_var, m_var, y_cmyk_var, k_var, c_scale, m_scale, y_cmyk_scale, k_scale))
    z_scale.configure(command=lambda _: on_xyz_change(
        r_scale, g_scale, b_scale, r_var, g_var, b_var, update_color_circle, update_xyz_from_rgb, update_cmyk_from_rgb,
        x_var, y_var, z_var, x_scale, y_scale, z_scale,
        c_var, m_var, y_cmyk_var, k_var, c_scale, m_scale, y_cmyk_scale, k_scale))

    # === CMYK Section ===
    ctk.CTkLabel(container, text="CMYK", font=("Arial", 20, "bold")).grid(row=6, column=0, columnspan=4, pady=(20, 10),
                                                                          sticky="n")

    ctk.CTkLabel(container, text="0").grid(row=8, column=0, sticky="w", padx=(10, 5))
    ctk.CTkLabel(container, text="1").grid(row=8, column=0, sticky="e", padx=(5, 10))

    c_scale = ctk.CTkSlider(container, from_=0, to=100)
    m_scale = ctk.CTkSlider(container, from_=0, to=100)
    y_cmyk_scale = ctk.CTkSlider(container, from_=0, to=100)
    k_scale = ctk.CTkSlider(container, from_=0, to=100)

    c_entry = ctk.CTkEntry(container, textvariable=c_var, width=80)
    c_entry.grid(row=7, column=0, padx=10, pady=5, sticky="ew")
    c_scale.grid(row=8, column=0, padx=10, pady=5, sticky="ew")

    m_entry = ctk.CTkEntry(container, textvariable=m_var, width=80)
    m_entry.grid(row=7, column=1, padx=10, pady=5, sticky="ew")
    m_scale.grid(row=8, column=1, padx=10, pady=5, sticky="ew")

    y_cmyk_entry = ctk.CTkEntry(container, textvariable=y_cmyk_var, width=80)
    y_cmyk_entry.grid(row=7, column=2, padx=10, pady=5, sticky="ew")
    y_cmyk_scale.grid(row=8, column=2, padx=10, pady=5, sticky="ew")

    k_entry = ctk.CTkEntry(container, textvariable=k_var, width=80)
    k_entry.grid(row=7, column=3, padx=10, pady=5, sticky="ew")
    k_scale.grid(row=8, column=3, padx=10, pady=5, sticky="ew")

    # Минимальные и максимальные метки для M, Y и K
    ctk.CTkLabel(container, text="0").grid(row=8, column=1, sticky="w", padx=(10, 5))
    ctk.CTkLabel(container, text="1").grid(row=8, column=1, sticky="e", padx=(5, 10))

    ctk.CTkLabel(container, text="0").grid(row=8, column=2, sticky="w", padx=(10, 5))
    ctk.CTkLabel(container, text="1").grid(row=8, column=2, sticky="e", padx=(5, 10))

    ctk.CTkLabel(container, text="0").grid(row=8, column=3, sticky="w", padx=(10, 5))
    ctk.CTkLabel(container, text="1").grid(row=8, column=3, sticky="e", padx=(5, 10))

    c_scale.configure(command=lambda _: on_cmyk_change(
        r_scale, g_scale, b_scale, r_var, g_var, b_var, update_color_circle, update_xyz_from_rgb, update_cmyk_from_rgb,
        x_var, y_var, z_var, x_scale, y_scale, z_scale,
        c_var, m_var, y_cmyk_var, k_var, c_scale, m_scale, y_cmyk_scale, k_scale))
    m_scale.configure(command=lambda _: on_cmyk_change(
        r_scale, g_scale, b_scale, r_var, g_var, b_var, update_color_circle, update_xyz_from_rgb, update_cmyk_from_rgb,
        x_var, y_var, z_var, x_scale, y_scale, z_scale,
        c_var, m_var, y_cmyk_var, k_var, c_scale, m_scale, y_cmyk_scale, k_scale))
    y_cmyk_scale.configure(command=lambda _: on_cmyk_change(
        r_scale, g_scale, b_scale, r_var, g_var, b_var, update_color_circle, update_xyz_from_rgb, update_cmyk_from_rgb,
        x_var, y_var, z_var, x_scale, y_scale, z_scale,
        c_var, m_var, y_cmyk_var, k_var, c_scale, m_scale, y_cmyk_scale, k_scale))
    k_scale.configure(command=lambda _: on_cmyk_change(
        r_scale, g_scale, b_scale, r_var, g_var, b_var, update_color_circle, update_xyz_from_rgb, update_cmyk_from_rgb,
        x_var, y_var, z_var, x_scale, y_scale, z_scale,
        c_var, m_var, y_cmyk_var, k_var, c_scale, m_scale, y_cmyk_scale, k_scale))

    r_entry.bind('<Return>',
                 lambda event: on_rgb_enter(event, r_var, g_var, b_var, r_scale, g_scale, b_scale, update_color_circle,
                                            update_xyz_from_rgb, update_cmyk_from_rgb,
                                            x_var, y_var, z_var, x_scale, y_scale, z_scale, c_var, m_var, y_cmyk_var,
                                            k_var, c_scale, m_scale, y_cmyk_scale, k_scale))
    g_entry.bind('<Return>',
                 lambda event: on_rgb_enter(event, r_var, g_var, b_var, r_scale, g_scale, b_scale, update_color_circle,
                                            update_xyz_from_rgb, update_cmyk_from_rgb,
                                            x_var, y_var, z_var, x_scale, y_scale, z_scale, c_var, m_var, y_cmyk_var,
                                            k_var, c_scale, m_scale, y_cmyk_scale, k_scale))
    b_entry.bind('<Return>',
                 lambda event: on_rgb_enter(event, r_var, g_var, b_var, r_scale, g_scale, b_scale, update_color_circle,
                                            update_xyz_from_rgb, update_cmyk_from_rgb,
                                            x_var, y_var, z_var, x_scale, y_scale, z_scale, c_var, m_var, y_cmyk_var,
                                            k_var, c_scale, m_scale, y_cmyk_scale, k_scale))

    # Bind XYZ entries to the Enter key
    x_entry.bind('<Return>',
                 lambda event: on_xyz_enter(event, x_var, y_var, z_var, x_scale, y_scale, z_scale,
                                            r_var, g_var, b_var, r_scale, g_scale, b_scale,
                                            update_rgb_from_xyz, update_color_circle, update_cmyk_from_rgb,
                                            c_var, m_var, y_cmyk_var, k_var, c_scale, m_scale, y_cmyk_scale, k_scale))

    y_entry.bind('<Return>',
                 lambda event: on_xyz_enter(event, x_var, y_var, z_var, x_scale, y_scale, z_scale,
                                            r_var, g_var, b_var, r_scale, g_scale, b_scale,
                                            update_rgb_from_xyz, update_color_circle, update_cmyk_from_rgb,
                                            c_var, m_var, y_cmyk_var, k_var, c_scale, m_scale, y_cmyk_scale, k_scale))

    z_entry.bind('<Return>',
                 lambda event: on_xyz_enter(event, x_var, y_var, z_var, x_scale, y_scale, z_scale,
                                            r_var, g_var, b_var, r_scale, g_scale, b_scale,
                                            update_rgb_from_xyz, update_color_circle, update_cmyk_from_rgb,
                                            c_var, m_var, y_cmyk_var, k_var, c_scale, m_scale, y_cmyk_scale, k_scale))

    # Bind CMYK entries to the Enter key
    c_entry.bind('<Return>',
                 lambda event: on_cmyk_enter(event, c_var, m_var, y_cmyk_var, k_var,
                                             c_scale, m_scale, y_cmyk_scale, k_scale,
                                             r_var, g_var, b_var, r_scale, g_scale, b_scale,
                                             update_rgb_from_cmyk, update_color_circle, update_xyz_from_rgb,
                                             update_cmyk_from_rgb,
                                             x_var, y_var, z_var, x_scale, y_scale, z_scale))

    m_entry.bind('<Return>',
                 lambda event: on_cmyk_enter(event, c_var, m_var, y_cmyk_var, k_var,
                                             c_scale, m_scale, y_cmyk_scale, k_scale,
                                             r_var, g_var, b_var, r_scale, g_scale, b_scale,
                                             update_rgb_from_cmyk, update_color_circle, update_xyz_from_rgb,
                                             update_cmyk_from_rgb,
                                             x_var, y_var, z_var, x_scale, y_scale, z_scale))

    y_cmyk_entry.bind('<Return>',
                 lambda event: on_cmyk_enter(event, c_var, m_var, y_cmyk_var, k_var,
                                             c_scale, m_scale, y_cmyk_scale, k_scale,
                                             r_var, g_var, b_var, r_scale, g_scale, b_scale,
                                             update_rgb_from_cmyk, update_color_circle, update_xyz_from_rgb,
                                             update_cmyk_from_rgb,
                                             x_var, y_var, z_var, x_scale, y_scale, z_scale))

    k_entry.bind('<Return>',
                 lambda event: on_cmyk_enter(event, c_var, m_var, y_cmyk_var, k_var,
                                             c_scale, m_scale, y_cmyk_scale, k_scale,
                                             r_var, g_var, b_var, r_scale, g_scale, b_scale,
                                             update_rgb_from_cmyk, update_color_circle, update_xyz_from_rgb,
                                             update_cmyk_from_rgb,
                                             x_var, y_var, z_var, x_scale, y_scale, z_scale))

    # === Color Preview Circle ===
    canvas = ctk.CTkCanvas(container, width=250, height=250, bg="gray")
    canvas.grid(row=9, column=0, columnspan=4, pady=20, sticky="n")
    color_circle = canvas.create_oval(50, 50, 200, 200, fill="#000000", outline="")

    # Initialize values
    def initialize_values():
        r_scale.set(0)
        g_scale.set(0)
        b_scale.set(0)
        x_scale.set(0)
        y_scale.set(0)
        z_scale.set(0)
        c_scale.set(0)
        m_scale.set(0)
        y_cmyk_scale.set(0)
        k_scale.set(0)

        # Установим начальные значения для полей ввода,
        r_var.set('0')
        g_var.set('0')
        b_var.set('0')
        x_var.set('0')
        y_var.set('0')
        z_var.set('0')
        c_var.set('0')
        m_var.set('0')
        y_cmyk_var.set('0')
        k_var.set('0')

        update_color_circle(0, 0, 0)

    initialize_values()
