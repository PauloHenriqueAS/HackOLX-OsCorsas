import cv2

# Carregue a imagem
imagem = cv2.imread('testeOLX.jpg')

# Aplique um filtro de nitidez
imagem_nitida = cv2.GaussianBlur(imagem, (5, 5), 8)
imagem_nitida = cv2.addWeighted(imagem, 1.7, imagem_nitida, -0.5, 0)

# Salve a imagem resultante
cv2.imwrite('ps2_melhorado.jpg', imagem_nitida)

# Exiba a imagem resultante
cv2.imshow('ps2_melhorado', imagem_nitida)
cv2.waitKey(0)
cv2.destroyAllWindows()