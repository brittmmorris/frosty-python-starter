from frosty import Frosty
import os
from dotenv import load_dotenv

load_dotenv()

frosty = Frosty(
    api_key=os.getenv("FROSTY_API_KEY"),
    router_id=os.getenv("FROSTY_ROUTER_ID")
)

response = frosty.chat("What's a fun fact about space?")
print(response)