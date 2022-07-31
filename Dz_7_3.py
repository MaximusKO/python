import os
from pathlib import Path
import shutil

dir_ = os.path.abspath(os.getcwd())
p = Path(f'{dir_}/my_project/templates')
#p.mkdir(parents=True, exist_ok=True)
if not os.path.exists(p):
    os.mkdir(p)
shutil.copytree('my_project/authapp/templates','my_project/templates',dirs_exist_ok=True)
shutil.copytree('my_project/mainapp/templates','my_project/templates',dirs_exist_ok=True)
