# haahwaaw.py
# makes those stupid mirrored game cover memes

from PIL import Image
import sys 

if (len(sys.argv) < 2):
    print("Please provide an image as an argument")
    exit()

imgIn = Image.open(sys.argv[1]) # image that was passed in through command line
x, y = imgIn.size # length and width of image passed in

# workaround for uneven width could just be increasing width of source image by one pixel
if x%2 != 0: 
    print("The width of this image is " + x + "px. Images of even width are preferred for best results.")

half = imgIn.crop(( 0 , 0, x/2 , y )) # crops the right half out
half = half.transpose(Image.FLIP_LEFT_RIGHT) # transpose the cropped half

# note for the pasting co-ordinate: top left corner of pasted image will be at this position
imgIn.paste(half ,( x/2 , 0 ))
imgIn.save("out.jpeg")



