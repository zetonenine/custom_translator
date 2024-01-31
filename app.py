import json

import translators as ts
from fastapi import FastAPI, APIRouter, Depends, HTTPException

router = APIRouter(
    prefix='/api'
)


@router.get(
    path='/word',
)
async def translate_word(
        word: str,
        src: str,
        dest: str,
):
    word = word.strip().lower()
    try:
        data = ts.translate_text(word, translator='google', from_language=src, to_language=dest, is_detail_result=True)
        recognized_word = data['data'][3][0]
        translations = []
        for item in data['data'][1][0][0][5][0][4]:
            translations.append(item[0])

    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

    try:
        example = data['data'][3][1][0][0][1][0][1]
    except Exception as ex:
        print(f"word: {word}. Error: {ex}")
        translations = [ts.translate_text(word, translator='google', from_language=src, to_language=dest)]
        example = ""

    return {
        "word": recognized_word,
        "translation": ', '.join(translations[:4]),
        "example": example
    }


app = FastAPI()
app.include_router(router)
