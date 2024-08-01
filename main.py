from fastapi import FastAPI
from routers import products, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

#Rutas
app.include_router(users_db.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(products.router)


#Rescursos estaticos
app.mount("/static", StaticFiles(directory="static"))

@app.get("/")
async def root():
    return {"Message" : "Hola Mundo"}

@app.get("/urls")
async def url():
    return {"products" : "/products/",
            "users": "/users",
            "basic_auth_users": "/basicauth/",
            "jwt_auth_users": "/jwtauth/",
            }


#main:app --reload <-para iniciar el servidor 
#Documentiacion: http://127.0.0.1:8000/redoc http://127.0.0.1:8000/docs
