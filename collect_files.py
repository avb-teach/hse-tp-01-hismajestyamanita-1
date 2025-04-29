import os
import sys
import shutil

args = sys.argv[1:]
if len(args) < 2:
    print("Usage: collect_files.py input_dir output_dir [--max_depth N]")
    sys.exit(1)

input_dir, output_dir = args[0], args[1]
max_depth = int(args[3]) if len(args) == 4 and args[2] == "--max_depth" else None

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for root, dirs, files in os.walk(input_dir):
    for file in files:
        source = os.path.join(root, file)
        rel = os.path.relpath(source, input_dir).split(os.sep)

        trimmed = rel[-max_depth:] if max_depth is not None else rel

        dest_dir = os.path.join(output_dir, *trimmed[:-1])
        os.makedirs(dest_dir, exist_ok=True)

        name = trimmed[-1]
        dest = os.path.join(dest_dir, name)

        base, ext = os.path.splitext(name)
        count = 1
        while os.path.exists(dest):
            dest = os.path.join(dest_dir, f"{base}{count}{ext}")
            count += 1

        shutil.copy2(source, dest)