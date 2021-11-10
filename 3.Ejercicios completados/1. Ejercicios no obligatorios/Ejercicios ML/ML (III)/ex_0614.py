# Coding Practice #0614
#----------------------------------------------------------------------------------

# Install OpenCV first.
# At the Anaconda prompt do: pip install opencv-contrib-python

import numpy as np
import cv2

# Comprobamos la versión de OpenCV.
print('OpenCV version : ', cv2.__version__)

# Ve al directorio donde se encuentran las imágenes. 
# os.chdir(r'~~')                     				  # Ajusta el path.

# 1. Trabajando con datos en formato imagen.
# 1.1. Abre una imagen en blanco y negro y muéstrala.


cv2.imshow("A B/W Image", img)
cv2.waitKey(0)                              # Espera a que se pulse una tecla.
cv2.destroyAllWindows()                     # Se cierra la ventana.

# 1.2. Abre una imagen en color y muéstrala.


# 1.3. Separa los canales de color (BGR en lugar de RGB).


cv2.imshow("The Blue Channel", blue_channel)
cv2.waitKey(0)                                                                          # Espera a que se pulse una tecla.
cv2.destroyAllWindows()                                                                 # Se cierra la ventana.

cv2.imshow("The Green Channel", green_channel)
cv2.waitKey(0)                                                                          # Espera a que se pulse una tecla.
cv2.destroyAllWindows()                                                                 # Se cierra la ventana.

cv2.imshow("The Red Channel", red_channel)
cv2.waitKey(0)                                                                          # Espera a que se pulse una tecla.
cv2.destroyAllWindows()                                                                 # Se cierra la ventana.

# 1.4. Guarda estas imágenes en ficheros externos.

