from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId

# creating a  fastapi instance
app = FastAPI()

# mongo db connection settings
MONGO_DB_URL = "mongodb+srv://divyansh:imgeniusdpssingh@birdvision.nrg72vb.mongodb.net/?retryWrites=true&w=majority&appName=birdvision"
MONGO_DB_NAME = "birdvision"
MONGO_COLLECTION_NAME = "products"

# mongo db client
client = MongoClient(MONGO_DB_URL)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]

# creating a pydantic model for product

class Product(BaseModel):
    title:str
    description:str
    price:float


# end point to create a  new product

@app.post("/products/" , response_model=Product)
async def create_product(product:Product):
    product_dict = product.model_dump()
    inserted_product = collection.insert_one(product_dict)
    inserted_product_id = inserted_product.inserted_id
    return {**product_dict , "id": str(inserted_product_id)}


# end point to get all products

@app.get("/products/",response_model=list[Product])
async def get_all_products():
    products = []
    for product in collection.find():
        products.append(Product(**product))
    return products

# end point to get a product by its id

@app.get("/products/{product_id}" , response_model=Product)
async def get_product_by_id(product_id:str):
    product = collection.find_one("_id" , ObjectId(product_id))

    if product:
        return Product(**product)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product not found")

# end point to update the  product using its id

@app.put("/products/{product_id}" , response_model=Product)
async def update_product(product_id:str, product:Product):
    updated_data = collection.update_one({'_id':ObjectId(product_id)},{'$set':product.model_dump()})

    if  updated_data.modified_count == 1:
        return {**product , 'id':product_id}
    else:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="product not found")
    

# end point to delete a product by its id

@app.delete("/products/{product_id}")
async def delete_product(product_id:str):
    deleted_product = collection.delete_one({"_id":ObjectId(product_id)})
    if deleted_product.deleted_count == 1:
        return {"message":"Product deleted successfully"}
    else:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product  with the id not found")
    