from sqlalchemy.ext.asyncio import AsyncSession
from repository import book_repository
from uuid import UUID

async def get_books(db: AsyncSession, limit: int, offset: int, status=None, author=None, sort_by=None):
    books = await book_repository.get_all(db, limit, offset, status, author)
    
    if sort_by == "title":
        books = sorted(books, key=lambda x: x.title)
    elif sort_by == "year":
        books = sorted(books, key=lambda x: x.year)
        
    return books

async def get_book(db: AsyncSession, book_id: UUID):
    return await book_repository.get_by_id(db, book_id)

async def create_book(db: AsyncSession, book_data):
    return await book_repository.add(db, book_data.dict())

async def delete_book(db: AsyncSession, book_id: UUID):
    return await book_repository.delete_book(db, book_id)