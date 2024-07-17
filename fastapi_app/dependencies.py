from fastapi import  Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_app import database

async def get_db(request: Request, db: AsyncSession = Depends(database.get_db)) -> None:
    request.state.db = db

