"""Entrena YOLO con la configuración de configs/entrenamiento.yaml."""
from pathlib import Path
import yaml
from ultralytics import YOLO

RAIZ = Path(__file__).resolve().parent.parent
cfg = yaml.safe_load((RAIZ / "configs" / "entrenamiento.yaml").read_text(encoding="utf-8"))

modelo = YOLO(cfg["modelo_base"])
modelo.train(
    data=str(RAIZ / "data.yaml"),
    epochs=cfg["epochs"],
    imgsz=cfg["imgsz"],
    batch=cfg["batch"],
    patience=cfg["patience"],
    project=str(RAIZ / cfg["project"]),
    name=cfg["nombre"],
)
