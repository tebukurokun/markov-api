from pydantic import BaseModel, Field


class Text(BaseModel):
    text: str = Field(None,
                      min_length=300,
                      example="メロスは激怒した。必ず、かの邪智暴虐の王を除かなければならぬと決意した。ロスには政治がわからぬ。メロスは、村の牧人である。笛を吹き、羊と遊んで暮して来た。"
                      )
