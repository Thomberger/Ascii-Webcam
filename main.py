# Thomas BErger
# 12/10/2020

# Print Webcam in ascii

import cv2

#get webcam
vc = cv2.VideoCapture(0, cv2.CAP_DSHOW)
rval, frame = vc.read()
 
#while webcam error
while rval:
    #get webcam
    rval, frame = vc.read()
    # Resize image
    ratio = 1.2
    frame = cv2.resize(frame, dsize=(round(150*ratio), round(65*ratio)), interpolation=cv2.INTER_CUBIC)
    
    # Make ASCII scale
    # TO INVERT SCALE add [::-1]
    ASCII_scale = " .:-=+*#%@" # " .,:;i1tfLCG08@"    
    
    
    
    ASCII_im = ""
    # Read all pixels
    for i in range(1,frame.shape[0]):
        for j in range(1,frame.shape[1]):
            color = frame[i,j,:]
            # Transform it to grey
            g = 0.21 * color[0]/255 + 0.72 * color[1]/255 + 0.07 * color[2]/255
            
            # Transform it to ASCII
            ASCII_Char = ASCII_scale[round(g*(len(ASCII_scale)-1))]
            
            # Update ASCII Image
            ASCII_im = ASCII_im + ASCII_Char
        ASCII_im = ASCII_im + "\n" #skip line
    
    # Print ASCII Image
    print(ASCII_im)
    
print(rval)
cv2.destroyAllWindows()