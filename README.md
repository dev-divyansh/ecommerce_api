# Product Management API Documentation

This API allows you to manage products in an e-commerce application. You can perform CRUD operations (Create, Read, Update, Delete) on products stored in a database.

## Setup and Running the Project

1. Clone or download the project repository from GitHub.

2. Navigate to the project directory.

3. Create a virtual environment
   ```
   pip install virtualenv
   ```
   after  installing create a environment and activate it

   ```
     virtualenv venv
     /venv/Scripts/activate
   ```
   venv is the environment name

4. Install other dependencies
  ```
   pip install fastapi pydantic pymongo univcorn
  ```
5. To run your project use the command
  ```
  uvicorn main:app --reload
  ```
 - make sure  in the main.py file : you have setup the mongo db credentials successfully :
 - ```
   MONGO_DB_URL = "mongodb+srv://divyansh:<passwordhere>@birdvision.nrg72vb.mongodb.net/?retryWrites=true&w=majority&appName=birdvision"
   ```
   replace the url of  MONGO_DB_URL with your own mongo db url.
   
Your  project is successfully setup and running!

## API Documentation
### POST /products
Create a new product with details like title, description, price, etc.

#### Request
- Method: POST
- URL: `/products`
- Headers:
- Content-Type: application/json
- Body: JSON object representing the new product

#### Request Body Schema (JSON)
```json
{
 "title": "Product Title",
 "description": "Product Description",
 "price": 39.99
}
```

### GET /products
Retrieve a list of all products from the database.

#### Request
- Method: GET
- URL: /products
- Response
- Status Code: 200 OK
- Content: JSON array of products

```
[
    {
        "id": "60942b214576d79df59d8f15",
        "title": "Product 1",
        "description": "Description of Product 1",
        "price": 29.99
    },
    {
        "id": "60942b214576d79df59d8f16",
        "title": "Product 2",
        "description": "Description of Product 2",
        "price": 39.99
    }
]
```

### GET /products/{product_id}
Retrieve details of a specific product by its ID.

#### Request
- Method: GET
- URL: /products/{product_id}
Response
- Status Code: 200 OK
- Content: JSON object representing the product

```
Copy code
{
    "id": "60942b214576d79df59d8f15",
    "title": "Product Title",
    "description": "Product Description",
    "price": 39.99
}
```

### PUT /products/{product_id}
Update an existing product based on its ID.

#### Request
- Method: PUT
- URL: /products/{product_id}
Headers:
- Content-Type: application/json
- Body: JSON object representing the updated product

Request Body Schema (JSON)
```
{
    "title": "Updated Product Title",
    "description": "Updated Product Description",
    "price": 49.99
}
```

- Response
- Status Code: 200 OK
- Content: JSON object representing the updated product

```
{
    "id": "60942b214576d79df59d8f15",
    "title": "Updated Product Title",
    "description": "Updated Product Description",
    "price": 49.99
}
```


### DELETE /products/{product_id}
Delete a product by its ID.

#### Request
- Method: DELETE
- URL: /products/{product_id}
Response
- "message":"Product deleted successfully"
- Status Code: 204 No Content



### Testing 
To run the tests, navigate to your project directory in the terminal or command prompt and execute the following command:

install this dependency if not installed
```
pip install pytest
```
to run the test simply run : 
```
pytest
```

This command will automatically discover and run all tests in file named test_main.py .

Make sure that your FastAPI application is not running while you're running the tests, as pytest will attempt to start its own server to test your endpoints.
