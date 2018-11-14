import glob
import os
import mmap

filesFound = glob.glob('./**/*.js', recursive=True)
for filePath in filesFound:
    ext = 'ts'
    with open(filePath, 'rb', 0) as file:
        try:
            s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
            if s.find(b'return <') != -1:
                ext = 'tsx'
            elif s.find(b'return (') != -1:
                ext = 'tsx'
            elif s.find(b'render()') != -1:
                ext = 'tsx'
        except ValueError:
            pass
    newFilePath = filePath[:-2] + ext
    print('Renaming ', filePath, ' to ', newFilePath)
    os.rename(filePath, newFilePath)
