import os
from collections import defaultdict
from os.path import relpath
import django


root_dir = django.__path__[0]
django_files = []
size_threshold =10**2 #10**3,10**4,10**5]
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if os.stat(os.path.join(root, file)).st_size < size_threshold:
            rel_path = relpath(os.path.join(root, file), root_dir)
            django_files.append(rel_path)


print(f'{size_threshold}: {len(django_files)}')







