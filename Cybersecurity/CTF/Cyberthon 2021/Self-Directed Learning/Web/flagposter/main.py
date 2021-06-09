from typing import Optional
from fastapi import FastAPI, Request
from pydantic import BaseModel


SECRET = 'I know how to make a POST request'
FLAG = open('/app/flag.txt', 'r').read().rstrip()

FAIL = {'Flag': 'Sorry no flag for you!'}
SUCCESS = {'Flag': FLAG}

app = FastAPI(docs_url=None, redoc_url=None)


class FlagRequest(BaseModel):
    secret: str


@app.post('/flag')
def flag(request: Request, flag_request: Optional[FlagRequest] = None):
    give_flag_header = request.headers.get('Give-Flag')

    if not give_flag_header or give_flag_header != 'yes':
        return FAIL

    if not flag_request or flag_request.secret != SECRET:
        return FAIL

    return SUCCESS

