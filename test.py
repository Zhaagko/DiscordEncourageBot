import os
import dotenv

dotenv.load_dotenv(dotenv_path="env")

print(os.getenv("TOKEN"))
