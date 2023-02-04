from nulis import tulis
from PIL import Image
import numpy as np
import cv2
from skimage.filters import threshold_local
import math
from scipy import ndimage



class Tuliskeunlah:
    def __init__(self, img, urutannya=0):    #mulai
        self.img = img
        print("[DEBUG __init__]: Gambar "+str(globals()['img'+str(urutannya)]))

    def Resize_Tulisan(self, final_height, img):
        if isinstance(img, str):
            print("[DEBUG]: ini bukan type string!")
            img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        else:
            print("[DEBUG]: ini bukan type string!")
            print(type(img))
            img = img

        height_ratio = final_height / img.shape[0]
        height, width = int(img.shape[0] * height_ratio), int(img.shape[1] * height_ratio)
        im_res = cv2.resize(img, (width, height))
        cv2.imshow("Resized", im_res)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return im_res
    
    def Scan_View(self, save_collage=False, resize_collage=True, resize_height=500, urutan=0):
        image = cv2.imread(self.img)
        orig = image.copy()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thr = threshold_local(image, 11, offset = 10, method = "gaussian")
        image = (image > thr).astype("uint8") * 255
        if save_collage:
            horiz_conc = np.concatenate((orig[:,:,1], image), axis=1)
            if resize_collage:
                horiz_conc = self.Resize_Tulisan(resize_height, horiz_conc)
            cv2.imwrite(str(judul)+"_scanview_"+str(urutan)+".jpg", horiz_conc)
        else:
            cv2.imwrite(str(judul)+"_scanview_"+str(urutan)+".jpg", image)
        return image

if __name__=="__main__":
    judul = input("[INPUT]: Judul Tugasnya mau apa A? ")

    print("[DEBUG]: oke maneh input judul "+str(judul)+" Tunggu sakedeng nya bosskuh...")

    with open('text.txt', 'r') as file:
        data = file.read()

    j = 0
    imagelist = []

    #proses cetak ke template
    for i in tulis(data, worker=10):
        j+=1
        i.save(str(judul)+"_"+str(j)+".jpg")

    print("[DEBUG]: Sukses menerapkan menjadi tulinsan")

    #proses cetak menjadi Scan view
    for x in range(1, j+1):
        globals()['img'+str(x)] = str(judul)+"_"+str(x)+".jpg"
        globals()['scan'+str(x)] = Tuliskeunlah(globals()['img'+str(x)], urutannya=+x)
        globals()['scanned_im'+str(x)] = globals()['scan'+str(x)].Scan_View(save_collage=False, resize_collage=False, resize_height =500, urutan=+x)
    
    print("[DEBUG]: Sukses menerapkan menjadi scan view")
    #Proses pdfkan
        
    for a in range(1, j+1):
        globals()['gambar'+str(a)] = Image.open(str(judul)+"_scanview_"+str(a)+".jpg", 'r')

    for y in range(1, j+1):
        globals()['jpg'+str(y)] = globals()['gambar'+str(y)].convert('RGB')

    for z in range(2, j+1):   
        imagelist.append(globals()['jpg'+str(z)])


    jpg1.save(str(judul)+'.pdf',save_all=True, append_images=imagelist)

    print("[DEBUG]: Sukses nyimpen data, total data tulisan silaing: "+str(j)+" Lembar dan sudah otomatis menjadi PDF dan terscan")
