import sys
import os

# solução do colega
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from herogentest_lib.controller.team import router as teams_router
from herogentest_lib.controller.hero import router as heroes_router
from herogentest_lib.util.database import init_db
from fastapi import FastAPI

app = FastAPI(title="FastAPI + SQLModel - MVC + Repository")

try: init_db()
except: pass

app.include_router(heroes_router)
app.include_router(teams_router)

@app.get("/")
def health():
    return {"status": "ok"}