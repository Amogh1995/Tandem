import io
import os
import copy
import numpy as np
import argparse
import imutils
import cv2
import itertools
basepath=os.path.dirname(os.path.abspath('..'))
#print basepath
def ocrinput(filename):
 PDFTOPPMPATH =  basepath + r"\krait\krait\static\poppler-0.67.0_x86\poppler-0.67.0\bin\pdftoppm.exe"
 PDFFILE = filename
 #print PDFTOPPMPATH
 import subprocess
 subprocess.call('"%s" -png %s out1' % (PDFTOPPMPATH, PDFFILE))


 # Imports the Google Cloud client library
 from google.cloud import vision
 from google.cloud.vision import types

 # Instantiates a client
 client = vision.ImageAnnotatorClient()

 # The name of the image file to annotate
 file_name =basepath+'/krait/compare/out1-1.png'




 char=[]
 cood=[]
 #print file_name
 # loop over the rotation angles again, this time ensuring
 # no part of the image is cut off
 for angle in np.arange(0, 91,90):
        coodrot=[]
        rotate=[]
        charall=[]
        coodall=[]
        image = cv2.imread(file_name)
        rotated = imutils.rotate_bound(image, angle)
        cv2.imwrite(str(angle)+".jpg",rotated)
        #print "Rotate Done"

        
        file_name1 = basepath+"/krait/compare/"+str(angle)+".jpg"
        #print "@@@@@@@"
        #print file_name1
        img = cv2.imread(file_name1, 0)
        ret, thresh = cv2.threshold(img, 10, 255, cv2.THRESH_OTSU)
        #print "Threshold selected : ", ret
        cv2.imwrite(str(angle)+".jpg", thresh)
        
        

	
        # Loads the image into memory
        with io.open(file_name1, 'rb') as image_file:
             content = image_file.read()

        image = types.Image(content=content)

        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations

        #print('Labels:')
        #for label in labels:
        #    print(label.description)


        response = client.text_detection(image=image)
        texts = response.text_annotations
        for text in texts:
            #print('\n"{}"'.format(text.description.encode('utf-8').strip()))
            charall.append('{}'.format(text.description.encode('utf-8').strip()))
            vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

            #print('bounds: {}'.format(','.join(vertices)))
            coodall.append('{}'.format(','.join(vertices)))
        char.append(list(charall[1:]))
        cood.append(list(coodall[1:]))
        rotate.append(list(coodall[1:]))
        for a in list(itertools.chain(*rotate)):
              coodrot.append(list(eval(a)))
        #print coodrot
 coodnewf=[]
 coodnews=[]
 charnews=[]
 charnewf=[]
 l01=copy.deepcopy(cood[0])
 l902=copy.deepcopy(cood[1])
 ch01=copy.deepcopy(char[0])
 ch902=copy.deepcopy(char[1])
 #print l01
 #print char[1]


 for a in l01:
     coodnewf.append(list(eval(a)))
 #print coodnew
 #charnewf=list(itertools.chain(*ch01))
 val=zip(ch01,coodnewf)
 #print val
 l1=[]
 def solve(lis):
        try:
            float(lis)
            return True
        except:
            pass
 for x in val:
    #print x[0]    
    if solve(x[0]):        
        l1.append(x)

 for a in l902:
 #    # for a in cood:
 #    # print a
     coodnews.append(list(eval(a)))
 #    # print coodnew
 #charnews = list(itertools.chain(*ch902))
 val2 = zip(ch902, coodnews)
 # print val
 l2 = []

 for x in val2:
     # print x[0]
     if solve(x[0]):
         l2.append(x)
 #print l1
 #print l2
 return l1,l2
        
#ocrinput("F:/Work/TandemLoop/Correct.pdf")
