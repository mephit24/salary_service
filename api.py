import time

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

import auth
import controller


app = FastAPI(title='Salary service')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')


@app.get('/')
async def root():
    return {'name': 'Salary service',
            'version': '1.0'}


@app.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if not auth.check_user(form_data.username, form_data.password):
        raise HTTPException(status_code=401)
    return {"access_token": auth.create_token(form_data.username),
            "token_type": "bearer"}


@app.get('/salary')
async def salary(token=Depends(oauth2_scheme)):
    token_info = auth.check(token)
    if not token_info:
        raise HTTPException(status_code=401,
                            detail='You dont authorized.')
    if token_info['expires'] <= time.time():
        raise HTTPException(status_code=401,
                            detail='Token expired. Login again.')
    return {'salary': controller.get_salary(token_info['login']),
            'date up': controller.get_date_up(token_info['login'])
            }
