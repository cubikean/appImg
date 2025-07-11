import os
from PIL import Image


def get_size_format(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"
    

def collect_img(folder):
    images = []
    for root, _, files in os.walk(folder):
        for file in files:
            images.append(os.path.join(root,file))
    SVG = []
    for image in images:
        if image.find('.svg') != -1:
             SVG.append(image)
    for image in SVG:
        images.remove(image)
    return images

def compress_img(images, destination, new_size_ratio=0.9, quality=75, width=None, height=None, uniformize=False, to_jpg=False, to_webp=True, to_png=False):
    from PIL import ImageOps
    for image_name in images:
        img = Image.open(image_name)
        # Corrige l'orientation selon l'EXIF
        img = ImageOps.exif_transpose(img)
        print("[*] Image shape:", img.size)
        image_size = os.path.getsize(image_name)
        print("[*] Size before compression:", get_size_format(image_size))
        if uniformize and width and height:
            # On ne scale que si l'image est plus grande que la cible
            if img.width > width or img.height > height:
                img.thumbnail((width, height), Image.LANCZOS)
                print("[+] Uniformized Image shape:", img.size)
            else:
                print("[=] Image plus petite que la cible, non modifiée.")
        elif new_size_ratio < 1.0:
            img = img.resize((int(img.size[0] * new_size_ratio), int(img.size[1] * new_size_ratio)), Image.LANCZOS)
            print("[+] New Image shape:", img.size)
        elif width and height:
            img = img.resize((width, height), Image.ANTIALIAS)
            print("[+] New Image shape:", img.size)
        # split the filename and extension
        #filename, ext = os.path.splitext(image_name)
        filenames = image_name.split('\\')[-1]
        filenames, ext = filenames.split('.')[:-1], filenames.split('.')[-1]
        filename = ''
        for x in filenames:
            filename += x 
            filename += '.'
        filename = filename[:-1]
        #return(filename,ext)
        # make new filename appending _compressed to the original file name
        if to_jpg:
            # change the extension to JPEG
            new_filename = f"{filename}_compressed.jpg"
            new_filename = os.path.join(destination,new_filename)
        elif to_webp:
            new_filename = f"{filename}_compressed.webp"
            new_filename = os.path.join(destination,new_filename)
        elif to_png:
            new_filename = f"{filename}_compressed.png"
            new_filename = os.path.join(destination,new_filename)
        else:
            # retain the same extension of the original image
            new_filename = f"{filename}_compressed.{ext}"
            new_filename = os.path.join(destination,"/",new_filename)

        try:
            # save the image with the corresponding quality and optimize set to True
            
            img.save(new_filename, quality=quality, optimize=True)
        except OSError:
            # convert the image to RGB mode first
            img = img.convert("RGB")
            # save the image with the corresponding quality and optimize set to True
            img.save(new_filename, quality=quality, optimize=True)
        print("[+] New file saved:", new_filename)
        # get the new image size in bytes
        new_image_size = os.path.getsize(new_filename)
        # print the new size in a good format
        print("[+] Size after compression:", get_size_format(new_image_size))
        # calculate the saving bytes
        saving_diff = new_image_size - image_size
        # print the saving percentage
        print(f"[+] Image size change: {saving_diff/image_size*100:.2f}% of the original image size.")
        
    
    
if __name__ == "__main__":
    
    IMG = collect_img('/Users/aloisgoeury/Downloads/skinclinic')
    #print(compress_img(IMG,'/Users/aloisgoeury/Desktop/Result'))
    print(IMG)
 