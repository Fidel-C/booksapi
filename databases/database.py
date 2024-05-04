from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from databases.models import Base


# async database initialization

DB_URL='sqlite+aiosqlite:///database.sqlite'

engine=create_async_engine(DB_URL)

SessionLocal=async_sessionmaker(bind=engine,expire_on_commit=False)




# async session generator for CRUD operations 

async def get_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    db=SessionLocal()    
    try:
        yield db
    except Exception:
       await db.rollback()
        
    finally:
        await db.close()
    




    
            
        
        
    


