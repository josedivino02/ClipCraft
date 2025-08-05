import cv2

refPt = []
cropping = False

def mouse_crop(event, x, y, flags, param):
    global refPt, cropping
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt.clear()
        refPt.append((x, y))
        cropping = True
    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cropping = False
        cv2.rectangle(param, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("Selecione a região para o GIF/Imagem", param)

def select_crop_region(frame):
    global refPt
    clone = frame.copy()
    cv2.namedWindow("Selecione a região para o GIF/Imagem")
    cv2.setMouseCallback("Selecione a região para o GIF/Imagem", mouse_crop, param=clone)

    print("🖱️ Use o mouse para desenhar um retângulo na janela.")
    print("➡️ Pressione 'c' para confirmar ou 'r' para resetar.")
    while True:
        cv2.imshow("Selecione a região para o GIF/Imagem", clone)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("r"):
            clone = frame.copy()
            refPt.clear()
        elif key == ord("c") and len(refPt) == 2:
            break
        elif key == 27:
            print("🚫 Cancelado.")
            cv2.destroyAllWindows()
            return None

    cv2.destroyAllWindows()
    return refPt
