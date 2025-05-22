# tools/translate.py

import asyncio
from googletrans import Translator


async def translate(text: str):
    translator = Translator()
    loop = asyncio.get_event_loop()
    # 将同步方法放入线程池中执行
    result = await loop.run_in_executor(None, lambda: translator.translate(text, src='en', dest='zh-cn'))
    return {
        "name": "vision-agent/translate",
        "content_type": "text/plain",
        "content": {
            "text": result.text
        }
    }
