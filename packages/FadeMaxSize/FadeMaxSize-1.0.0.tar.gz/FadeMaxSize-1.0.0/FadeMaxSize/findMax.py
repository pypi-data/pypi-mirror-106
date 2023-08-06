import os

def find_max_file(directory):
    answer = ''
    max_size = 0
    
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
           prom = os.path.getsize(os.path.join(dirpath, filename))
           if prom > max_size:
               max_size = prom
               answer = os.path.join(dirpath, filename)

    return {
        'file': answer, # path to file
        'size': max_size / (2 ** 10) # file size in kilobytes
    }


