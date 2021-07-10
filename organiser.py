import shutil
import os
source=os.listdir("C:/Users/chand/Desktop/dummy")

for c in source:
    doc,ext=os.path.splitext(c)
    print(c)
    if(ext==' '):
        print(doc,ext)
        continue
    
    elif(os.path.exists("C:/Users/chand/Desktop/dummy/" + ext )):
        shutil.move("C:/Users/chand/Desktop/dummy/" + c,"C:/Users/chand/Desktop/dummy/" + ext + "/")
    else:
        os.mkdir("C:/Users/chand/Desktop/dummy/" + ext)
        shutil.move("C:/Users/chand/Desktop/dummy/" + c,"C:/Users/chand/Desktop/dummy/" + ext + "/")





