import os
import dotenv
import pydantic


class Settings(pydantic.BaseModel):
    dotenv.load_dotenv()

    USER_EMAIL: str = os.environ.get('USER_EMAIL')
    PASSWORD: str = os.environ.get('USER_PASSWORD')


settings = Settings()
