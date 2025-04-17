from PIL import Image
import pytesseract
import cv2


def image_to_text1():
    # Load the image
    image_path = "output1.png"  # Replace with your actual image file path
    img = Image.open(image_path)

    # Convert to grayscale
    img = img.convert('L')
    img.save("gray.png", format="PNG")  # Save for debugging

    # Run OCR on the image
    text = pytesseract.image_to_string(img, lang='vie')  # 'vie' is for Vietnamese language support

    # Print the extracted text
    print(text)

    data = pytesseract.image_to_data(img, lang='vie', output_type=pytesseract.Output.DICT)
    print(data['text'])


def image_to_text2():
    # Load the image
    img = cv2.imread('output1.png')

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("gray.png", gray)

    # Run OCR on the image
    text = pytesseract.image_to_string(gray, lang='vie+equ')  # 'vie' is for Vietnamese language support

    # Print the extracted text
    print(text)

    data = pytesseract.image_to_data(gray, lang='vie+equ', output_type=pytesseract.Output.DICT)
    print(data['text'])
