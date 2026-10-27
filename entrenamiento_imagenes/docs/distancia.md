# Estimación de distancia

YOLO no mide distancia. Opciones, de más simple a más compleja:

1. **Tamaño de la caja (pinhole):** distancia ≈ (altura_real × focal) / altura_en_píxeles.
   Requiere la altura real aproximada de cada clase y la focal de la cámara
   (se obtiene con calibración o desde los datos EXIF).
2. **Modelo de profundidad monocular** (por ejemplo, Depth Anything o MiDaS)
   sobre la imagen, y tomar la profundidad dentro de cada caja.
3. **Sensor adicional** (ultrasonido o LiDAR), si el hardware lo permite.

Pendiente decidir cuál usar según el hardware de la app.
