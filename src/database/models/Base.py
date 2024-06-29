from sqlmodel import SQLModel


class CustomBase(SQLModel):
    class Config:
        from_attributes = True
