from typing import List

from pydantic import BaseModel, Field


class Sentences(BaseModel):
    sentences: List[str] = Field(None,
                                 example="[\"メロスは激怒した。必ず、かの邪智暴虐の王を除かなければならぬと決意した。\", \"メロスには政治がわからぬ。メロスは、村の牧人である。笛を吹き、羊と遊んで暮して来た。\"]")
