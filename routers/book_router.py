from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import schemas
from databases import models
from databases.database import get_db


router = APIRouter(prefix="/books",tags=["Books"])


# create book
@router.post(
    "", response_model=schemas.BookOutSchema, status_code=status.HTTP_201_CREATED
)
async def create_book(
    payload: schemas.CreateBookSchema, db: AsyncSession = Depends(get_db)
):
    item = models.Book(**payload.dict())
    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item


# retrieve all books
@router.get("", response_model=list[schemas.BookOutSchema])
async def get_books(db: AsyncSession = Depends(get_db)):
    stmt = select(models.Book)
    result = await db.execute(stmt)
    books = result.scalars().all()
    return books


# retrieve single book by id
@router.get("/{id}", response_model=schemas.BookOutSchema)
async def get_book(id: int, db: AsyncSession = Depends(get_db)):
    stmt = select(models.Book).where(models.Book.id == id)
    result = await db.execute(stmt)
    book = result.scalar_one_or_none()
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book with the given id does not exist",
        )
    else:
        return book


# update book


@router.put("/{id}", response_model=schemas.BookOutSchema)
async def update_book(
    id: int,
    payload: schemas.UpdateBookSchema,
    db: AsyncSession = Depends(get_db),
):
    stmt = select(models.Book).where(models.Book.id == id)
    result = await db.execute(stmt)
    book = result.scalar_one_or_none()
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book with the given id does not exist",
        )
    else:
        for k, v in payload.dict().items():
            if v is not None:
                setattr(book, k, v)
        await db.commit()
        await db.refresh(book)
        return book


# delete book


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(id: int, db: AsyncSession = Depends(get_db)):
    stmt = select(models.Book).where(models.Book.id == id)
    result = await db.execute(stmt)
    book = result.scalar_one_or_none()
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book with the given id does not exist",
        )
    else:
        delete_stmt = delete(models.Book).where(models.Book.id == id)
        await db.execute(delete_stmt)
        await db.commit()
        return "Sucessfully deleted"
