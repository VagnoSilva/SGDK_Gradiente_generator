import tkinter as tk
from tkinter import messagebox, ttk
import math
import threading
import time
import ctypes
from ctypes import wintypes

# ========== PALETA SGDK COMPLETA (512 cores 3-3-3 bits) ==========
palette_hex = [
    "000000", "002400", "004800", "006c00", "009000", "00b400", "00d800", "00ff00",
    "240000", "242400", "244800", "246c00", "249000", "24b400", "24d800", "24ff00",
    "480000", "482400", "484800", "486c00", "489000", "48b400", "48d800", "48ff00",
    "6c0000", "6c2400", "6c4800", "6c6c00", "6c9000", "6cb400", "6cd800", "6cff00",
    "900000", "902400", "904800", "906c00", "909000", "90b400", "90d800", "90ff00",
    "b40000", "b42400", "b44800", "b46c00", "b49000", "b4b400", "b4d800", "b4ff00",
    "d80000", "d82400", "d84800", "d86c00", "d89000", "d8b400", "d8d800", "d8ff00",
    "ff0000", "ff2400", "ff4800", "ff6c00", "ff9000", "ffb400", "ffd800", "ffff00",
    "000024", "002424", "004824", "006c24", "009024", "00b424", "00d824", "00ff24",
    "240024", "242424", "244824", "246c24", "249024", "24b424", "24d824", "24ff24",
    "480024", "482424", "484824", "486c24", "489024", "48b424", "48d824", "48ff24",
    "6c0024", "6c2424", "6c4824", "6c6c24", "6c9024", "6cb424", "6cd824", "6cff24",
    "900024", "902424", "904824", "906c24", "909024", "90b424", "90d824", "90ff24",
    "b40024", "b42424", "b44824", "b46c24", "b49024", "b4b424", "b4d824", "b4ff24",
    "d80024", "d82424", "d84824", "d86c24", "d89024", "d8b424", "d8d824", "d8ff24",
    "ff0024", "ff2424", "ff4824", "ff6c24", "ff9024", "ffb424", "ffd824", "ffff24",
    "000048", "002448", "004848", "006c48", "009048", "00b448", "00d848", "00ff48",
    "240048", "242448", "244848", "246c48", "249048", "24b448", "24d848", "24ff48",
    "480048", "482448", "484848", "486c48", "489048", "48b448", "48d848", "48ff48",
    "6c0048", "6c2448", "6c4848", "6c6c48", "6c9048", "6cb448", "6cd848", "6cff48",
    "900048", "902448", "904848", "906c48", "909048", "90b448", "90d848", "90ff48",
    "b40048", "b42448", "b44848", "b46c48", "b49048", "b4b448", "b4d848", "b4ff48",
    "d80048", "d82448", "d84848", "d86c48", "d89048", "d8b448", "d8d848", "d8ff48",
    "ff0048", "ff2448", "ff4848", "ff6c48", "ff9048", "ffb448", "ffd848", "ffff48",
    "00006c", "00246c", "00486c", "006c6c", "00906c", "00b46c", "00d86c", "00ff6c",
    "24006c", "24246c", "24486c", "246c6c", "24906c", "24b46c", "24d86c", "24ff6c",
    "48006c", "48246c", "48486c", "486c6c", "48906c", "48b46c", "48d86c", "48ff6c",
    "6c006c", "6c246c", "6c486c", "6c6c6c", "6c906c", "6cb46c", "6cd86c", "6cff6c",
    "90006c", "90246c", "90486c", "906c6c", "90906c", "90b46c", "90d86c", "90ff6c",
    "b4006c", "b4246c", "b4486c", "b46c6c", "b4906c", "b4b46c", "b4d86c", "b4ff6c",
    "d8006c", "d8246c", "d8486c", "d86c6c", "d8906c", "d8b46c", "d8d86c", "d8ff6c",
    "ff006c", "ff246c", "ff486c", "ff6c6c", "ff906c", "ffb46c", "ffd86c", "ffff6c",
    "000090", "002490", "004890", "006c90", "009090", "00b490", "00d890", "00ff90",
    "240090", "242490", "244890", "246c90", "249090", "24b490", "24d890", "24ff90",
    "480090", "482490", "484890", "486c90", "489090", "48b490", "48d890", "48ff90",
    "6c0090", "6c2490", "6c4890", "6c6c90", "6c9090", "6cb490", "6cd890", "6cff90",
    "900090", "902490", "904890", "906c90", "909090", "90b490", "90d890", "90ff90",
    "b40090", "b42490", "b44890", "b46c90", "b49090", "b4b490", "b4d890", "b4ff90",
    "d80090", "d82490", "d84890", "d86c90", "d89090", "d8b490", "d8d890", "d8ff90",
    "ff0090", "ff2490", "ff4890", "ff6c90", "ff9090", "ffb490", "ffd890", "ffff90",
    "0000b4", "0024b4", "0048b4", "006cb4", "0090b4", "00b4b4", "00d8b4", "00ffb4",
    "2400b4", "2424b4", "2448b4", "246cb4", "2490b4", "24b4b4", "24d8b4", "24ffb4",
    "4800b4", "4824b4", "4848b4", "486cb4", "4890b4", "48b4b4", "48d8b4", "48ffb4",
    "6c00b4", "6c24b4", "6c48b4", "6c6cb4", "6c90b4", "6cb4b4", "6cd8b4", "6cffb4",
    "9000b4", "9024b4", "9048b4", "906cb4", "9090b4", "90b4b4", "90d8b4", "90ffb4",
    "b400b4", "b424b4", "b448b4", "b46cb4", "b490b4", "b4b4b4", "b4d8b4", "b4ffb4",
    "d800b4", "d824b4", "d848b4", "d86cb4", "d890b4", "d8b4b4", "d8d8b4", "d8ffb4",
    "ff00b4", "ff24b4", "ff48b4", "ff6cb4", "ff90b4", "ffb4b4", "ffd8b4", "ffffb4",
    "0000d8", "0024d8", "0048d8", "006cd8", "0090d8", "00b4d8", "00d8d8", "00ffd8",
    "2400d8", "2424d8", "2448d8", "246cd8", "2490d8", "24b4d8", "24d8d8", "24ffd8",
    "4800d8", "4824d8", "4848d8", "486cd8", "4890d8", "48b4d8", "48d8d8", "48ffd8",
    "6c00d8", "6c24d8", "6c48d8", "6c6cd8", "6c90d8", "6cb4d8", "6cd8d8", "6cffd8",
    "9000d8", "9024d8", "9048d8", "906cd8", "9090d8", "90b4d8", "90d8d8", "90ffd8",
    "b400d8", "b424d8", "b448d8", "b46cd8", "b490d8", "b4b4d8", "b4d8d8", "b4ffd8",
    "d800d8", "d824d8", "d848d8", "d86cd8", "d890d8", "d8b4d8", "d8d8d8", "d8ffd8",
    "ff00d8", "ff24d8", "ff48d8", "ff6cd8", "ff90d8", "ffb4d8", "ffd8d8", "ffffd8",
    "0000ff", "0024ff", "0048ff", "006cff", "0090ff", "00b4ff", "00d8ff", "00ffff",
    "2400ff", "2424ff", "2448ff", "246cff", "2490ff", "24b4ff", "24d8ff", "24ffff",
    "4800ff", "4824ff", "4848ff", "486cff", "4890ff", "48b4ff", "48d8ff", "48ffff",
    "6c00ff", "6c24ff", "6c48ff", "6c6cff", "6c90ff", "6cb4ff", "6cd8ff", "6cffff",
    "9000ff", "9024ff", "9048ff", "906cff", "9090ff", "90b4ff", "90d8ff", "90ffff",
    "b400ff", "b424ff", "b448ff", "b46cff", "b490ff", "b4b4ff", "b4d8ff", "b4ffff",
    "d800ff", "d824ff", "d848ff", "d86cff", "d890ff", "d8b4ff", "d8d8ff", "d8ffff",
    "ff00ff", "ff24ff", "ff48ff", "ff6cff", "ff90ff", "ffb4ff", "ffd8ff", "ffffff"
]

# --- Funções de cor ---
def hex_to_rgb(hex_str):
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return "{:02x}{:02x}{:02x}".format(*rgb)

def srgb_to_linear(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def rgb_to_xyz(r, g, b):
    r, g, b = srgb_to_linear(r), srgb_to_linear(g), srgb_to_linear(b)
    x = 0.4124564 * r + 0.3575761 * g + 0.1804375 * b
    y = 0.2126729 * r + 0.7151522 * g + 0.0721750 * b
    z = 0.0193339 * r + 0.1191920 * g + 0.9503041 * b
    return x, y, z

def xyz_to_oklab(x, y, z):
    l = 0.4122214708 * x + 0.5363325363 * y + 0.0514459929 * z
    m = 0.2119034982 * x + 0.6806995451 * y + 0.1073969566 * z
    s = 0.0883024619 * x + 0.2817188376 * y + 0.6299787005 * z

    l_ = math.copysign(abs(l) ** (1/3), l)
    m_ = math.copysign(abs(m) ** (1/3), m)
    s_ = math.copysign(abs(s) ** (1/3), s)

    L = 0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_
    a = 1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_
    b = 0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_
    return L, a, b

def rgb_to_oklab(r, g, b):
    x, y, z = rgb_to_xyz(r, g, b)
    return xyz_to_oklab(x, y, z)

def rgb_to_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    else:
        h = (60 * ((r - g) / df) + 240) % 360
    s = 0 if mx == 0 else df / mx
    v = mx
    return h, s, v

def hsv_to_rgb(h, s, v):
    c = v * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c
    if 0 <= h < 60:
        r, g, b = c, x, 0
    elif 60 <= h < 120:
        r, g, b = x, c, 0
    elif 120 <= h < 180:
        r, g, b = 0, c, x
    elif 180 <= h < 240:
        r, g, b = 0, x, c
    elif 240 <= h < 300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x
    r, g, b = (r + m) * 255, (g + m) * 255, (b + m) * 255
    return int(round(r)), int(round(g)), int(round(b))

# --- Captura de cor nativa do Windows ---
def get_pixel_color(x, y):
    """Obtém a cor RGB de um pixel na posição (x, y) na tela (Windows only)"""
    hdc = ctypes.windll.user32.GetDC(0)
    color = ctypes.windll.gdi32.GetPixel(hdc, x, y)
    ctypes.windll.user32.ReleaseDC(0, hdc)
    if color == -1:
        raise RuntimeError("Falha ao capturar pixel")
    b = color & 0xFF
    g = (color >> 8) & 0xFF
    r = (color >> 16) & 0xFF
    return (r, g, b)

def get_cursor_pos():
    """Obtém a posição atual do cursor do mouse"""
    point = wintypes.POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(point))
    return point.x, point.y

# --- Geração de gradiente ---
def generate_gradient(hex1, hex2, steps, palette, interp_method="RGB", match_method="RGB"):
    try:
        rgb1 = hex_to_rgb(hex1)
        rgb2 = hex_to_rgb(hex2)
    except:
        return []

    gradient = []
    for i in range(steps):
        t = i / (steps - 1) if steps > 1 else 0.0

        if interp_method == "RGB":
            r = int(rgb1[0] + t * (rgb2[0] - rgb1[0]))
            g = int(rgb1[1] + t * (rgb2[1] - rgb1[1]))
            b = int(rgb1[2] + t * (rgb2[2] - rgb1[2]))
            target_rgb = (max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b)))

        elif interp_method == "HSV":
            h1, s1, v1 = rgb_to_hsv(*rgb1)
            h2, s2, v2 = rgb_to_hsv(*rgb2)

            dh = h2 - h1
            if dh > 180:
                dh -= 360
            elif dh < -180:
                dh += 360
            h = (h1 + t * dh) % 360
            s = s1 + t * (s2 - s1)
            v = v1 + t * (v2 - v1)
            target_rgb = hsv_to_rgb(h, s, v)

        elif interp_method == "OkLab":
            r = int(rgb1[0] + t * (rgb2[0] - rgb1[0]))
            g = int(rgb1[1] + t * (rgb2[1] - rgb1[1]))
            b = int(rgb1[2] + t * (rgb2[2] - rgb1[2]))
            target_rgb = (max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b)))
        else:
            target_rgb = rgb1

        filtered_palette = palette
        best = None
        best_dist = float('inf')

        if match_method == "RGB":
            for hex_color in filtered_palette:
                r, g, b = hex_to_rgb(hex_color)
                dist = (r - target_rgb[0])**2 + (g - target_rgb[1])**2 + (b - target_rgb[2])**2
                if dist < best_dist:
                    best_dist = dist
                    best = (r, g, b)

        elif match_method == "HSV":
            h_in, s_in, v_in = rgb_to_hsv(*target_rgb)
            for hex_color in filtered_palette:
                r, g, b = hex_to_rgb(hex_color)
                h, s, v = rgb_to_hsv(r, g, b)
                dh = min(abs(h - h_in), 360 - abs(h - h_in))
                ds = abs(s - s_in)
                dv = abs(v - v_in)
                dist = dh**2 + (255 * ds)**2 + (255 * dv)**2
                if dist < best_dist:
                    best_dist = dist
                    best = (r, g, b)

        elif match_method == "OkLab":
            lab_input = rgb_to_oklab(*target_rgb)
            for hex_color in filtered_palette:
                r, g, b = hex_to_rgb(hex_color)
                try:
                    lab = rgb_to_oklab(r, g, b)
                    dist = (lab[0]-lab_input[0])**2 + (lab[1]-lab_input[1])**2 + (lab[2]-lab_input[2])**2
                    if dist < best_dist:
                        best_dist = dist
                        best = (r, g, b)
                except:
                    continue

        if best is None:
            best = hex_to_rgb(palette[0])
        gradient.append(best)

    return gradient

# --- Interface Gráfica ---
class FullGradientApp:
    def __init__(self, root):
        self.root = root
        root.title("Gerador de Gradiente SGDK")
        root.geometry("580x780")
        root.resizable(False, False)

        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        # Frame para cores iniciais e finais com botões de captura
        color_selection_frame = tk.Frame(input_frame)
        color_selection_frame.grid(row=0, column=0, columnspan=7, pady=5)

        tk.Label(color_selection_frame, text="Cor inicial:").grid(row=0, column=0, padx=5, sticky="e")
        self.entry1 = tk.Entry(color_selection_frame, width=10)
        self.entry1.grid(row=0, column=1, padx=5)
        self.pick_color1_btn = tk.Button(color_selection_frame, text="Pick Color", command=lambda: self.start_color_pick(1))
        self.pick_color1_btn.grid(row=0, column=2, padx=5)

        tk.Label(color_selection_frame, text="Cor final:").grid(row=0, column=3, padx=5, sticky="e")
        self.entry2 = tk.Entry(color_selection_frame, width=10)
        self.entry2.grid(row=0, column=4, padx=5)
        self.pick_color2_btn = tk.Button(color_selection_frame, text="Pick Color", command=lambda: self.start_color_pick(2))
        self.pick_color2_btn.grid(row=0, column=5, padx=5)

        # Frame para outros controles
        controls_frame = tk.Frame(input_frame)
        controls_frame.grid(row=1, column=0, columnspan=7, pady=5)

        tk.Label(controls_frame, text="Passos:").grid(row=0, column=0, padx=5, sticky="e")
        self.steps_var = tk.StringVar(value="16")
        self.steps_spin = tk.Spinbox(controls_frame, from_=2, to=64, width=5, textvariable=self.steps_var)
        self.steps_spin.grid(row=0, column=1, padx=5)

        tk.Label(controls_frame, text="Método:").grid(row=0, column=2, padx=5, sticky="e")
        self.method_var = tk.StringVar(value="RGB")
        self.method_combo = ttk.Combobox(
            controls_frame,
            textvariable=self.method_var,
            values=["RGB", "HSV", "OkLab"],
            state="readonly",
            width=8
        )
        self.method_combo.grid(row=0, column=3, padx=5)

        self.unique_var = tk.BooleanVar(value=False)
        self.unique_check = tk.Checkbutton(
            controls_frame,
            text="Cores únicas",
            variable=self.unique_var
        )
        self.unique_check.grid(row=0, column=4, padx=5, sticky="w")

        tk.Button(controls_frame, text="Gerar Degradê", command=self.generate).grid(row=0, column=5, padx=10)

        self.result_frame = tk.Frame(root)
        self.result_frame.pack(pady=10)

        self.bg_empty = "#f0f0f0"
        self.frames = []
        self.entries = []

        cols = 8
        total = 64
        for i in range(total):
            row = (i // cols) * 2
            col = i % cols

            frame = tk.Frame(self.result_frame, width=50, height=50, bg=self.bg_empty, relief="sunken", bd=1)
            frame.grid(row=row, column=col, padx=3, pady=3)
            frame.pack_propagate(False)

            entry = tk.Entry(self.result_frame, width=8, font=("Arial", 8), justify="center")
            entry.grid(row=row+1, column=col, padx=3, pady=1)
            entry.config(state="normal")
            entry.delete(0, tk.END)
            entry.config(state="readonly", readonlybackground=self.bg_empty, fg="black")

            self.frames.append(frame)
            self.entries.append(entry)

            entry.bind("<Button-1>", lambda e, en=entry: self.select_entry(en))
            frame.bind("<Button-1>", lambda e, en=entry: self.select_entry(en))

        self.picking = False

    def start_color_pick(self, target):
        if self.picking:
            return
        self.picking = True
        self.color_pick_target = target

        self.pick_window = tk.Toplevel(self.root)
        self.pick_window.title("Selecionar Cor")
        self.pick_window.geometry("300x100")
        self.pick_window.transient(self.root)
        self.pick_window.grab_set()

        tk.Label(self.pick_window, text="Clique em qualquer lugar da tela para capturar a cor", font=("Arial", 10)).pack(pady=20)
        tk.Button(self.pick_window, text="Cancelar", command=self.cancel_color_pick).pack(pady=5)

        # Iniciar thread de espera por clique esquerdo
        thread = threading.Thread(target=self.wait_for_left_click, daemon=True)
        thread.start()

    def wait_for_left_click(self):
        """Aguarda clique esquerdo usando GetAsyncKeyState (Windows only)"""
        user32 = ctypes.windll.user32
        while self.picking:
            if user32.GetAsyncKeyState(0x01) & 0x8000:  # VK_LBUTTON
                time.sleep(0.1)  # debounce
                if not self.picking:
                    break
                try:
                    x, y = get_cursor_pos()
                    rgb = get_pixel_color(x, y)
                    hex_color = rgb_to_hex(rgb).upper()
                    self.root.after(0, self.finish_pick, hex_color)
                except Exception as e:
                    self.root.after(0, self.fail_pick, str(e))
                break
            time.sleep(0.01)

    def finish_pick(self, hex_color):
        if self.color_pick_target == 1:
            self.entry1.delete(0, tk.END)
            self.entry1.insert(0, hex_color)
        elif self.color_pick_target == 2:
            self.entry2.delete(0, tk.END)
            self.entry2.insert(0, hex_color)
        self.cleanup_pick()

    def fail_pick(self, error):
        messagebox.showerror("Erro", f"Falha ao capturar cor:\n{error}")
        self.cleanup_pick()

    def cleanup_pick(self):
        self.picking = False
        if hasattr(self, 'pick_window') and self.pick_window:
            self.pick_window.destroy()
            self.pick_window = None

    def cancel_color_pick(self):
        self.picking = False
        if hasattr(self, 'pick_window') and self.pick_window:
            self.pick_window.destroy()
            self.pick_window = None

    def generate(self):
        hex1 = self.entry1.get().strip().upper()
        hex2 = self.entry2.get().strip().upper()
        try:
            steps = int(self.steps_var.get())
        except:
            messagebox.showerror("Erro", "Número de passos inválido.")
            return

        if len(hex1) != 6 or len(hex2) != 6:
            messagebox.showerror("Erro", "Cores HEX devem ter 6 caracteres.")
            return
        if not (2 <= steps <= 64):
            messagebox.showerror("Erro", "Passos devem estar entre 2 e 64.")
            return

        method = self.method_var.get()
        try:
            gradient = generate_gradient(hex1, hex2, steps, palette_hex, interp_method=method, match_method=method)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao gerar degradê:\n{str(e)}")
            return

        if self.unique_var.get():
            unique_gradient = []
            last = None
            for rgb in gradient:
                if rgb != last:
                    unique_gradient.append(rgb)
                    last = rgb
            gradient = unique_gradient

        for i in range(64):
            if i < len(gradient):
                rgb = gradient[i]
                hex_color = rgb_to_hex(rgb).upper()
                bg_color = f"#{hex_color}"
                fg_color = "white" if sum(rgb) < 400 else "black"
                self.frames[i].config(bg=bg_color)
                self.entries[i].config(state="normal")
                self.entries[i].delete(0, tk.END)
                self.entries[i].insert(0, hex_color)
                self.entries[i].config(
                    state="readonly",
                    readonlybackground=bg_color,
                    fg=fg_color
                )
            else:
                self.frames[i].config(bg=self.bg_empty)
                self.entries[i].config(state="normal")
                self.entries[i].delete(0, tk.END)
                self.entries[i].config(
                    state="readonly",
                    readonlybackground=self.bg_empty,
                    fg="black"
                )

    def select_entry(self, entry):
        entry.focus()
        entry.select_range(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = FullGradientApp(root)
    root.mainloop()