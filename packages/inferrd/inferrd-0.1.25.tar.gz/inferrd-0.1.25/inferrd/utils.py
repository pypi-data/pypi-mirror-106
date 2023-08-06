import zipfile

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            filePath = os.path.join(root, file)
            inZipPath = os.path.relpath(os.path.join(root, file), os.path.join(path, '..'))
            # remove base folder
            ziph.write(filePath, inZipPath.replace('inferrd-model/', ''))