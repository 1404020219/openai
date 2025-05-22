# tools/ocr.py

async def ocr(image_path: str):
    # 使用 pytesseract 或 PaddleOCR 进行文字识别
    import pytesseract
    from PIL import Image

    text = pytesseract.image_to_string(Image.open(image_path))
    return {
        "name": "vision-agent/ocr",
        "content_type": "text/plain",
        "content": {
            "text": text
        }
    }
