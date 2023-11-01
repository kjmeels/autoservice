from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, declared_attr

from src.settings import SETTINGS


class Base(DeclarativeBase):
    _async_engine = create_async_engine(
        str(SETTINGS.DATABASE_URL).replace('postgresql://', 'postgresql+asyncpg://')
    )

    async_session = async_sessionmaker(bind=_async_engine)

    @classmethod
    @declared_attr
    def __tablename__(cls):
        return ''.join(f'{i.lower()}' if i.isupper() else i for i in cls.__name__)
