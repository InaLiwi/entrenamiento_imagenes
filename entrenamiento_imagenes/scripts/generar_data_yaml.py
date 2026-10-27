# scripts/generar_data_yaml.py
import re
from pathlib import Path
import yaml

RAIZ = Path(__file__).resolve().parent.parent
dart = (RAIZ / "scripts" / "nombres_clases.dart").read_text(encoding="utf-8")
pares = re.findall(r"'([^']+)':\s*NombreClase\('([^']+)'", dart)

cfg = {
    "path": "datasets",
    "train": "train/images",
    "val": "val/images",
    "test": "test/images",
    "names": {i: español for i, (_, español) in enumerate(pares)},
}
(RAIZ / "data.yaml").write_text(yaml.safe_dump(cfg, allow_unicode=True, sort_keys=False), encoding="utf-8")
print(f"{len(pares)} clases escritas")  # debe imprimir 80