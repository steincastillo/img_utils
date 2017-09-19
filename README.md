. # img_utils
Computer Vision Utils (OpenCV + Python)

This is a collection of simple routines to apply different processing techniques to an image.

Is also intended to be used as a reference and learning tool for some OPENCV commands.

Routines can be used individually and most will take the parameter -h or --help to indicate function and usage

### Included routines:  
1. **show.py**: Displays an image and image properties. Usage: python show.py -i [imageFile]  
2. **image_captureV2**: Captures an image using the installed camera. Usage: python image_captureV2.py 
3. **hpf.py**: Applies a high pass filter to the image with different kernels. Usage: python hpf.py -i [imageFile]
4. **equalize.py**: Equalizes the histogram of gray scale image. Usage: python equalize.py -i [imageFile]
5. **coloreq.py**: Equalizes the histogram of a color image. Usage: python coloreq.py -i [imageFile]
6. **addtext.py**: Adds up to 3 text lines to an image. Usage: python addtext.py - i [imageFile] -c [fontColor]
7. **color_map.py**: Apply a color map to an image. Usage: pythion color_map.py -i [imageFile} -c [colorMap]
8. **show_plt.py**: Displazs and image and image properties using matplotlib. Usage: python show_plt.py -i [imageFile]

