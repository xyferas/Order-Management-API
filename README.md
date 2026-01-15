# Order Management System API

A robust Order Management API built with Django and Django REST Framework.

## Features
- **Role-Based Access Control**: Separate permissions for Admins and Customers.
- **JWT Authentication**: Secure API access using JSON Web Tokens.
- **Product Management**: Admins can manage the product catalog.
- **Order Processing**: Customers can place orders; Admins can view all orders.
- **Customer Management**: Admins can view and manage customer accounts.

## Setup Instructions

1.  **Clone the repository**
    ```bash
    git clone https://github.com/xyferas/Order-Management-API.git
    cd Order-Management-API
    ```
2.  **Create and Activate Virtual Environment (If Needed)**
    ```bash
    python -m venv env
    # Windows
    .\env\Scripts\activate
    # Linux/Mac
    source env/bin/activate
    ```
3.  **Install Dependencies (If Needed)**
    
    *Key Dependencies: Django, Django REST Framework, SimpleJWT*
    ```bash
    pip install -r requirements.txt
    ```
4.  **Apply Migrations**
    ```bash
    cd order_management
    python manage.py makemigrations
    python manage.py migrate
    ```
5.  **Create Superuser (Admin)**
    ```bash
    python manage.py createsuperuser
    ```
6.  **Run Server**
    ```bash
    python manage.py runserver
    ```

## API Documentation

Base URL: `http://127.0.0.1:8000/`

### Authentication

| Feature | Method | Endpoint | Description |
| :--- | :--- | :--- | :--- |
| **Register** | `POST` | `/api/register/` | Register as a new Customer. |
| **Admin Login** | `POST` | `/api/login/` | Obtain Admin Access & Refresh Tokens. |
| **Login** | `POST` | `/api/login/` | Obtain Access & Refresh Tokens. |
| **Refresh Token** | `POST` | `/api/token/refresh/` | Refresh Access Token. |

**Register Payload:**
```json
{
    "username": "customer1",
    "password": "StrongPassword123!"
}
```
**Register Response:**
```json
{
    "message": "Customer Registered Successfully"
}
```

**Login Payload:**
```json
{
    "username": "customer1",
    "password": "StrongPassword123!"
}
```
**Login Response:**
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsIn...",
    "access": "eyJhbGciOiJIUzI1NiIsIn...",
    "role": "CUSTOMER"
}
```

**Admin Login Payload:**
```json
{
    "username": "admin",
    "password": "AdminPassword123!"
}
```
**Admin Login Response:**
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsIn...",
    "access": "eyJhbGciOiJIUzI1NiIsIn...",
    "role": "ADMIN"
}
```

---

### Admin APIs
_Requires `Bearer <admin_token>`_

#### Products
| Feature | Method | Endpoint | Description |
| :--- | :--- | :--- | :--- |
| **Create Product** | `POST` | `/api/products/` | Add a new product to the catalog. |
| **List Products** | `GET` | `/api/products/` | View all products. |
| **Update Product** | `PUT/PATCH` | `/api/products/<id>/` | Update product details. |
| **Delete Product** | `DELETE` | `/api/products/<id>/` | Remove a product (Returns 204). |

**Create Product Payload:**
```json
{
    "name": "Laptop",
    "price": "1200.00"
}
```
**Create Product Response:**
```json
{
    "id": 1,
    "name": "Laptop",
    "price": "1200.00"
}
```

**List Products Response:**
```json
[
    {
        "id": 1,
        "name": "Laptop",
        "price": "1200.00"
    },
    {
        "id": 2,
        "name": "Mouse",
        "price": "25.00"
    }
]
```
**Update Product Response:**
```json
{
    "id": 1,
    "name": "Laptop Pro",
    "price": "1300.00"
}
```
**Delete Product:** Returns `204 No Content`.

#### Customers
| Feature | Method | Endpoint | Description |
| :--- | :--- | :--- | :--- |
| **List Customers** | `GET` | `/api/customers/` | View all registered customers. |
| **Delete Customer** | `DELETE` | `/api/customers/<id>/` | Delete a customer account (Returns 204). |

**List Customers Response:**
```json
[
    {
        "id": 1,
        "username": "customer1",
        "email": "customer1@example.com",
        "role": "CUSTOMER"
    }
]
```
**Delete Customer:** Returns `204 No Content`.

#### Orders
| Feature | Method | Endpoint | Description |
| :--- | :--- | :--- | :--- |
| **List All Orders** | `GET` | `/api/orders/` | View every order in the system. |
| **Order Details** | `GET` | `/api/orders/<id>/` | View details of a specific order. |
| **Delete Order** | `DELETE` | `/api/orders/<id>/` | Remove an order (Returns 204). |

**List All Orders Response:**
```json
[
    {
        "id": 1,
        "customer": "customer1",
        "items": [
            {
                "product_id": 1,
                "quantity": 2
            }
        ],
        "total_amount": 2400.00,
        "created_at": "2024-10-27T10:00:00Z"
    }
]
```
**Order Details Response:**
```json
{
    "id": 1,
    "customer": "customer1",
    "items": [
        {
            "product_id": 1,
            "quantity": 2
        }
    ],
    "total_amount": 2400.00,
    "created_at": "2024-10-27T10:00:00Z"
}
```
**Delete Order:** Returns `204 No Content`.



---

### Customer APIs
_Requires `Bearer <customer_token>`_

#### Products
| Feature | Method | Endpoint | Description |
| :--- | :--- | :--- | :--- |
| **List Products** | `GET` | `/api/products/` | View available products. |
| **Product Details** | `GET` | `/api/products/<id>/` | View details of a single product. |

**List Products Response:**
```json
[
    {
        "id": 1,
        "name": "Laptop",
        "price": "1200.00"
    }
]
```
**Product Details Response:**
```json
{
    "id": 1,
    "name": "Laptop",
    "price": "1200.00"
}
```

#### Orders
| Feature | Method | Endpoint | Description |
| :--- | :--- | :--- | :--- |
| **Place Order** | `POST` | `/api/orders/` | Submit a new order. |
| **List My Orders** | `GET` | `/api/orders/` | View only your own orders. |
| **Order Details** | `GET` | `/api/orders/<id>/` | View details of your own order. |

**List My Orders Response:**
```json
[
    {
        "id": 1,
        "customer": "customer1",
        "items": [
            {
                "product_id": 1,
                "quantity": 2
            }
        ],
        "total_amount": 2400.00,
        "created_at": "2024-10-27T10:00:00Z"
    }
]
```
**Order Details Response:**
```json
{
    "id": 1,
    "customer": "customer1",
    "items": [
        {
            "product_id": 1,
            "quantity": 2
        }
    ],
    "total_amount": 2400.00,
    "created_at": "2024-10-27T10:00:00Z"
}
```

**Place Order Payload:**
```json
{
    "items": [
        {
            "product_id": 1,
            "quantity": 2
        },
        {
            "product_id": 2,
            "quantity": 1
        }
    ]
}
```
**Place Order Response:**
```json
{
    "id": 1,
    "customer": "customer1",
    "items": [
        {
            "product_id": 1,
            "quantity": 2
        },
        {
            "product_id": 2,
            "quantity": 1
        }
    ],
    "total_amount": 2500.00,
    "created_at": "2024-10-27T10:00:00Z"
}
```

## Rules & Permissions

- **Customers**:
    - Can **Register** and **Login**.
    - Can **View Products**.
    - Can **Place Orders**.
    - Can **View Own Orders**.
    - **Cannot** update or delete orders.
- **Admins**:
    - Have full access to **Manage Products** (Create/Update/Delete).
    - Can **View All Orders**.
    - Can **Delete Orders**.
    - Can **Manage Customers**.
- **Frontend**: This is a pure API backend. All interactions should be performed via API clients like Postman.
