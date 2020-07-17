from pathlib import Path, PureWindowsPath, PurePath
import os
current_path = os.path.dirname(__file__)
caminho_atual = PurePath("Imagens")
filename = PureWindowsPath(caminho_atual, "Base.png")

print(current_path)