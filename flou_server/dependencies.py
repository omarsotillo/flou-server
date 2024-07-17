from fastapi import  Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from flou_server import database

async def get_db(request: Request, db: AsyncSession = Depends(database.get_db)) -> None:
    request.state.db = db

