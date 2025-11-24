import time, sys, math, random

try:
    import colorama
    from colorama import Fore, Style
    colorama.init()
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False
    class FakeColors:
        def __getattr__(self, name):
            return ''
    Fore = FakeColors()
    Style = FakeColors()

# Setup awal
print("=== Setup Animasi ===")
text = input("Masukkan teks/simbol (default: '*'): ") or "*"
speed = float(input("Masukkan kecepatan (detik, default: 0.1): ") or 0.1)
max_width = int(input("Masukkan lebar maksimum (default: 50): ") or 50)

# Variabel animasi
angle = 0
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
current_color = 0
amplitude = max_width // 2
frequency = 0.1
dynamic_speed = speed

try:
    while True:
        # Hitung posisi sinusoidal
        indent = int(amplitude * math.sin(angle)) + amplitude
        
        # Tampilkan teks berwarna
        if COLORAMA_AVAILABLE:
            print(colors[current_color] + ' ' * indent + text + Style.RESET_ALL)
        else:
            print(' ' * indent + text)
        
        time.sleep(dynamic_speed)
        
        # Update variabel
        angle += frequency
        current_color = (current_color + 1) % len(colors)
        
        # Ubah kecepatan secara acak
        if random.random() < 0.05:
            dynamic_speed = random.uniform(speed/2, speed*2)
        
        # Ubah amplitudo secara acak
        if random.random() < 0.02:
            amplitude = random.randint(5, max_width - len(text))
            
except KeyboardInterrupt:
    print("\nAnimasi dihentikan!")
    sys.exit()