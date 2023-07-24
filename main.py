from fastapi import FastAPI, Path
from enum import Enum

app = FastAPI()


class Category(str, Enum):
    Fantasy = "Fantasy"
    Action = "Action"
    Horror = "Horror"


movies = [
    {
        "id": 1,
        "title": "The last of us",
        "rating": 9.2,
        "age": 2023,
        "description": "After a global pandemic destroys civilization ...",
        "category": "fantasy",
    },
    {
        "id": 2,
        "title": "The Flash",
        "rating": 8.5,
        "age": 2020,
        "description": "Narry Allen uses his super spped to change ...",
        "category": "action",
    },
]


@app.get("/")
def root():
    """Root function"""
    return "Welcome FastAPI"


@app.get("/movies", tags=["movies"])
def get_movies():
    """Movie list"""
    return movies


@app.get("/movies/{id}", tags=["movies"])
def filter_by_id(id: int = Path(ge=0, le=1_000)):
    return [item for item in movies if item["id"] == id]


@app.get("/movies/category/{category}", tags=["movies"])
def filter_by_category(category: Category):
    return [item for item in movies if item["category"] == category.name.lower()]
