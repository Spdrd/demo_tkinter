import os
import sys

def resource_path(relative_path):
    """Obtiene la ruta absoluta del recurso."""
    if hasattr(sys, '_MEIPASS'):
        # Ruta temporal cuando el ejecutable es creado con pyinstaller
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.abspath(relative_path)