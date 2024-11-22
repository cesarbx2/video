import cv2
import numpy as np
import pyautogui
import time

# Configurações
output_file = "gravacao.mp4"
duration = 10  # Duração em segundos
fps = 20  # Frames por segundo

print("Iniciando em 3 segundos...")
time.sleep(3)

# Inicializa o gravador de vídeo
screen_size = pyautogui.size()
out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*"mp4v"), fps, screen_size)
start_time = time.time()

print("Gravando...")
while time.time() - start_time < duration:
    try:
        # Captura o frame da tela
        screenshot = pyautogui.screenshot()

        # Converte para array NumPy e para cores BGR
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Adiciona o frame ao vídeo
        out.write(frame)
    except Exception as e:
        print(f"Erro ao processar frame: {e}")
        break

# Libera o gravador de vídeo
out.release()
print(f"Gravação concluída e salva em {output_file}")
