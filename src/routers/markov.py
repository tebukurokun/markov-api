from typing import Union

from fastapi import APIRouter, Header, HTTPException

import src.schemas.sentences as sentences_schema
import src.schemas.text as text_schema
from config import Settings
from src import sample_txt
from src.services.generate_sentence import generate_sentences

router = APIRouter()

setting = Settings()


@router.post("/markov", response_model=sentences_schema.Sentences)
async def markov(text_body: text_schema.Text, x_api_key: Union[str, None] = Header(default=None)):
    if x_api_key != setting.api_key:
        raise HTTPException(status_code=403, detail="unauthorized")

    sentences = generate_sentences(text_body.text)
    return sentences_schema.Sentences(sentences=sentences)


@router.get("/markov", response_model=sentences_schema.Sentences)
async def markov_sample(x_api_key: Union[str, None] = Header(default=None)):
    if x_api_key != setting.api_key:
        raise HTTPException(status_code=403, detail="unauthorized")

    text = sample_txt.txt
    sentences = generate_sentences(text)
    return sentences_schema.Sentences(sentences=sentences)
