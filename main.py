from typing import Optional

from fastapi import FastAPI
from datetime import datetime
import pysurfline

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/how-is-the-surf")
def get_surf_sessions():
    return pysurfline.get_spot_forecasts("5842041f4e65fad6a7708bca")


@app.get("/how-is-the-surf/{spot_id}")
def get_surf_sessions_by_spot_id(spot_id):
    # Call the pysurfline function to get surf data
    surf_data = pysurfline.get_spot_forecasts(spot_id)

    # Return the processed data
    return {"timestamp": datetime.now().isoformat(), "surf_data": surf_data}
