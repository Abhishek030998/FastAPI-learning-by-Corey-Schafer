from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


posts  = [
  {
    "id": 1,
    "author": "Abhishek Gaikwad",
    "title": "Getting Started with FastAPI",
    "content": "FastAPI is a modern web framework for building APIs with Python.",
    "date_posted": "2026-04-19"
  },
  {
    "id": 2,
    "author": "Rahul Sharma",
    "title": "Understanding Dependency Injection",
    "content": "Dependency injection helps manage reusable components in FastAPI.",
    "date_posted": "2026-04-18"
  },
  {
    "id": 3,
    "author": "Neha Patil",
    "title": "CRUD Operations in FastAPI",
    "content": "Learn how to create, read, update, and delete records efficiently.",
    "date_posted": "2026-04-17"
  },
  {
    "id": 4,
    "author": "Amit Joshi",
    "title": "Pydantic for Data Validation",
    "content": "Pydantic ensures type safety and validation in FastAPI applications.",
    "date_posted": "2026-04-16"
  },
  {
    "id": 5,
    "author": "Sneha Kulkarni",
    "title": "Building Scalable APIs",
    "content": "Best practices to design scalable and maintainable API systems.",
    "date_posted": "2026-04-15"
  }
]


@app.get('/',response_class= HTMLResponse,include_in_schema= False)
@app.get("/posts", response_class= HTMLResponse)
def home():
    # return {"message":"Hello World !"}
    return f"<h1>{posts[0]['title']}</h1>"




@app.get('/api/posts')
def get_post():
    return posts
