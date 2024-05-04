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
