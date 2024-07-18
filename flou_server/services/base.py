from sqlalchemy.ext.asyncio import AsyncSession

class BaseService:
    db: AsyncSession

    def __init__(self, db: AsyncSession):
        self.db = db
