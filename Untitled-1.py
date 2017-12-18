import zipfile
import glob, os
import numpy as np

def is_float(string):
    """ True if given string is float else False"""
    try:
        return float(string)
    except ValueError:
        return False

os.chdir(os.path.dirname(os.path.abspath(__file__)))
for file in glob.glob("*.zip"):
    print(file)

with zipfile.ZipFile(file, "r") as zip_ref:
    zip_ref.extractall(file[:-4])

data = []
for datafile in glob.glob(file[:-4] + "/*.DAT"):  
    print(datafile)
    with open(datafile, 'r') as f:
        d = f.readlines()
        for i in d:
            k = i.rstrip().split(";")
            #print(k)
            try:
                if k[15] and k[18] == "RESIDENCE":
                    data.append([float(i) if is_float(i) else i for i in k]) 
            except IndexError:
                pass

            

data = np.array(data, dtype='O')
np.set_printoptions(threshold=np.nan)
print(data)
np.savetxt("foo.csv", data, delimiter=",", fmt="%s")