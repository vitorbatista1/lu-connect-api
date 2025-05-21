from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    refresh_token: str | None = None  # refresh token opcional (no login é enviado)
    token_type: str

    class Config:
        orm_mode = True