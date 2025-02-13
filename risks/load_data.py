import json
import os
from django.conf import settings
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'risks_iso.settings')  # Asegúrate de poner el nombre correcto de tu archivo settings
django.setup()

from risks.models import category, section, control

# Definir rutas de los archivos JSON
DATA_FILES = {
    "categories": os.path.join(settings.BASE_DIR, "risks/static/data/categories.json"),
    "sections": os.path.join(settings.BASE_DIR, "risks/static/data/sections.json"),
    "controls": os.path.join(settings.BASE_DIR, "risks/static/data/controls.json"),
}

# Mapeo de modelos a sus respectivos archivos
MODEL_MAPPING = {
    "categories": (category, ["id", "name", "description"]),
    "sections": (section, ["id", "code", "name", "description"]),
    "controls": (control, ["id", "code", "name", "category_id", "section_id", "description", "objective"]),
}

def load_data(file_key):
    """Carga datos desde un archivo JSON y los inserta en la base de datos."""
    file_path = DATA_FILES[file_key]
    model, fields = MODEL_MAPPING[file_key]

    try:
        with open(file_path, "r") as file:
            data = json.load(file)

        for item in data:
            model.objects.get_or_create(**{field: item[field] for field in fields})

        print(f"{file_key.capitalize()} cargados correctamente.")
    
    except Exception as e:
        print(f"Error al cargar {file_key}: {e}")

# Cargar todas las categorías, secciones y controles
for key in DATA_FILES.keys():
    load_data(key)
