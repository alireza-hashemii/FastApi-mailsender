from pydantic import BaseModel
from typing import List

class MailBody(BaseModel):
    to: List[str]
    subject: str
    body: str