import unittest
from nulis import tulis
from PIL import Image
import numpy as np
import cv2
from skimage.filters import threshold_local
import math
from scipy import ndimage

class TestTuliskeunlah(unittest.TestCase):
    def setUp(self):
        self.judul = "test_judul"
        self.data = "test_data"
        self.resize_height = 500
        self.urutan = 1

        with open('text.txt', 'w') as file:
            file.write(self.data)

        self.tulisan = tulis(self.data, worker=10)
        self.tulisan[0].save(str(self.judul)+"_"+str(self.urutan)+".jpg")
        self.img = str(self.judul)+"_"+str(self.urutan)+".jpg"

        self.tuliskeunlah = Tuliskeunlah(self.img, urutannya=self.urutan)

    def test_resize_tulisan(self):
        result = self.tuliskeunlah.Resize_Tulisan(self.resize_height, self.img)
        self.assertIsNotNone(result)

    def test_scan_view(self):
        result = self.tuliskeunlah.Scan_View(save_collage=False, resize_collage=False, resize_height=self.resize_height, urutan=self.urutan)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()