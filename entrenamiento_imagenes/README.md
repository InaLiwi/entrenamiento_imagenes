# entrenamiento_imagenes

Entrenamiento de un modelo YOLO para detectar objetos cotidianos y vehículos,
pensado para alimentar la app Lumina (Proyecto-de-titulo).

## Estructura

```
configs/      Configuración de entrenamiento (hiperparámetros)
datasets/     Imágenes y etiquetas (NO se versiona, ver .gitignore)
docs/         Notas sobre clases, fuentes de datos y decisiones
runs/         Resultados de cada entrenamiento (NO se versiona)
scripts/      Entrenar, validar y exportar
data.yaml     Rutas y lista de clases del dataset
requirements.txt
```

## Flujo de trabajo

1. Descargar datasets públicos y dejarlos en `datasets/` (formato YOLO).
2. Revisar `docs/clases.md` y ajustar `data.yaml` si cambian las clases.
3. Validar el dataset: `python scripts/verificar_dataset.py`
4. Entrenar: `python scripts/entrenar.py`
5. Exportar el mejor modelo: `python scripts/exportar.py --pesos runs/<nombre>/weights/best.pt`
6. Copiar solo el archivo exportado (.tflite) al repo Proyecto-de-titulo.

## Pendiente

- La **distancia** no la predice YOLO. YOLO entrega la caja de cada objeto;
  la distancia se estima después a partir del tamaño de la caja y la altura
  real aproximada del objeto (ver `docs/distancia.md`).
