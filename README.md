# Watermark
python program to add a watermark to all ".PNG" and ".JPG" files in a folder


This Python program allows you to add a watermark to images in a given folder.

It starts by asking the user for the path to the folder containing the images and the option for the watermark. 

Option 1: the program then asks for the watermark text. It then creates a new folder called "watermarked" in the folder containing the images, and then browses each file in this folder. If the file is not an image (with the extension .jpg or .png), it moves on to the next file. Otherwise, it opens the image and adds the watermark using the text entered by the user. The watermark is centered on the image and is added with an Arial Black font of size proportional to that of the image. The program then saves the image with the added watermark in the "watermarked" folder.

Option 2: the program asks for the custom settings for the watermark: the text, the color (in RGB), the path of the font to use and the opacity of the watermark. The program then follows the same process as for option 1, but uses the custom settings to add the watermark to each image.

The os module is used to manipulate files and folders, while the PIL (Python Imaging Library) module is used to manipulate images and add the watermark.

