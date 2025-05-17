import os

# Path to your images directory
path = 'converter/static/converter/images'

for filename in os.listdir(path):
    if filename.endswith('.gif'):
        lower_filename = filename.lower()
        src = os.path.join(path, filename)
        dst = os.path.join(path, lower_filename)
        os.rename(src, dst)
        print(f'Renamed: {filename} -> {lower_filename}')
