import cv2
import os

os.makedirs("Saida", exist_ok=True)

camera = cv2.VideoCapture(0)
contador = 1

x1, y1 = 100, 100
x2, y2 = 400, 400

if not camera.isOpened():
    print("Erro: não foi possível abrir a webcam.")
else:
    while True:
        ret, frame = camera.read()

        if not ret:
            print("Erro ao capturar frame.")
            break

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        cv2.imshow("Pressione S para tirar foto ou Q para sair", frame)

        tecla = cv2.waitKey(1) & 0xFF

        if tecla == ord('s'):
            nome_original = f"Saida/foto_{contador}.jpg"
            cv2.imwrite(nome_original, frame)
            recorte = frame[y1:y2, x1:x2]
            nome_recorte = f"Saida/recorte_{contador}.jpg"
            cv2.imwrite(nome_recorte, recorte)

            print(f"Original salva: {nome_original}")
            print(f"Recorte salvo: {nome_recorte}")

            contador += 1

        elif tecla == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()