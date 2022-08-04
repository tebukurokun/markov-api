from fastapi import APIRouter
import src.schemas.sentences as sentences_schema
import src.schemas.text as text_schema
from src import sample_txt
from src.services.generate_sentence import generate_sentences

router = APIRouter()


@router.post("/markov", response_model=sentences_schema.Sentences)
async def markov(text_body: text_schema.Text):
    sentences = generate_sentences(text_body.text)
    return sentences_schema.Sentences(sentences=sentences)


@router.get("/markov", response_model=sentences_schema.Sentences)
async def markov_sample():
    text = sample_txt.txt
    sentences = generate_sentences(text)
    return sentences_schema.Sentences(sentences=sentences)
