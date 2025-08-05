def ask_video_path():
    return input("🎥 Caminho do vídeo (relativo ou absoluto): ").strip()

def ask_output_type():
    print("\nEscolha a saída desejada:")
    print("[1] GIF")
    print("[2] Imagem")
    print("[3] Vídeo recortado")
    print("[4] Áudio do trecho recortado")
    return input("Digite o número da opção: ").strip()

def ask_gif_size():
    print("📏 Tamanho do GIF: [1] 128x128 ou [2] 384x128")
    choice = input("Digite o número da opção: ").strip()
    return "128:128" if choice == "1" else "384:128"

def ask_file_name(prompt, default_ext):
    name = input(prompt).strip()
    if not name.lower().endswith(default_ext):
        name += default_ext
    return name

def ask_time(prompt):
    while True:
        try:
            t = float(input(prompt))
            if t < 0:
                print("⛔ Tempo não pode ser negativo.")
                continue
            return t
        except ValueError:
            print("⛔ Digite um número válido.")
