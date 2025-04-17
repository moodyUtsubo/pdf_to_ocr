###########################
#  CROP USING PDF2IMAGE   #
###########################
from pdf2image import convert_from_path
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
from ocr import image_to_text1, image_to_text2

pdf_path = "your/path/file.pdf"
page_number = 1  # 1-indexed (page number)
dpi = 300
output_path = "output1.png"  # Output path for the cropped image

# Step 1: Convert PDF page to image
images = convert_from_path(pdf_path, dpi=dpi, first_page=page_number, last_page=page_number)
image = images[0]

# Global crop box
crop_coords = {}

# Step 2: Define crop function using RectangleSelector
def line_select_callback(eclick, erelease):
    x1, y1 = int(eclick.xdata), int(eclick.ydata)
    x2, y2 = int(erelease.xdata), int(erelease.ydata)
    crop_coords['box'] = (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))

def on_key(event):
    if event.key == 'enter':
        if 'box' in crop_coords:
            cropped = image.crop(crop_coords['box'])
            cropped.save(output_path)
            print(f"PDF2IMAGE Cropped image saved to {output_path} with DPI: {dpi}")
            plt.close()

# Step 3: Show image and enable selector
fig, ax = plt.subplots()
ax.imshow(image)
ax.set_title("Drag to select area, press Enter to crop and save")

toggle_selector = RectangleSelector(
    ax,
    onselect=line_select_callback,
    useblit=True,
    interactive=True,
    button=[1],
    minspanx=5,
    minspany=5,
    spancoords='pixels'
)


plt.connect('key_press_event', on_key)
plt.show()
image_to_text1()  # Call the OCR function to extract text from the cropped image
