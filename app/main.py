from fastapi import FastAPI, BackgroundTasks
from app.scheme import MailBody
from app.mailer import send_mail

app = FastAPI()


@app.get("/")
def home():
    return {"status": "fastapi mailserver is running"}


@app.post("/send-mail")
def mailer(req: MailBody, tasks: BackgroundTasks):
    data = req.model_dump()
    tasks.add_task(send_mail,data)
    return {"status":200,"message":"Email has been scheduled"}
