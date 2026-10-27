"""Exporta el modelo entrenado a TFLite para usarlo en la app Flutter."""
import argparse
from ultralytics import YOLO

parser = argparse.ArgumentParser()
parser.add_argument("--pesos", required=True, help="ruta a best.pt")
parser.add_argument("--formato", default="tflite", help="tflite u onnx")
args = parser.parse_args()

modelo = YOLO(args.pesos)
ruta = modelo.export(format=args.formato, imgsz=640)
print(f"Modelo exportado en: {ruta}")
