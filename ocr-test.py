import ddddocr
ocr = ddddocr.DdddOcr();

with open('ocrtest.jpg') as f:
    image_bytes = f.read()
    
res = ocr.classification(image_bytes)
print(res)