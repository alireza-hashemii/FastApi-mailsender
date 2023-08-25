from dotenv import load_dotenv
import os


load_dotenv()

USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT",465)

