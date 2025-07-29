import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/perodriguezl/api/u-s-a-sales-taxes-per-zip-code'

mcp = FastMCP('u-s-a-sales-taxes-per-zip-code')

@mcp.tool()
def zip_code(zip_code: Annotated[str, Field(description='The U.S. Valid zip code')]) -> dict: 
    '''Get taxes from zip code'''
    url = 'https://u-s-a-sales-taxes-per-zip-code.p.rapidapi.com/33166'
    headers = {'x-rapidapi-host': 'u-s-a-sales-taxes-per-zip-code.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'zip_code': zip_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
