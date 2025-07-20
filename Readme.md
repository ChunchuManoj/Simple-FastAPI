# HROne Backend Intern Task

This is a sample e-commerce backend application built using **FastAPI** and **MongoDB**, as part of the HROne Backend Intern hiring challenge.

## 🔧 Tech Stack

- **Python 3.10+**
- **FastAPI**
- **MongoDB Atlas**
- **Pymongo**
- **Uvicorn**
- **Dotenv**

---

## 📦 API Endpoints

### 1. Create Product

- **POST** `/products`
- **Request Body:**

```json
{
  "name": "Premium Hoodie",
  "price": 1299.99,
  "sizes": [
    { "size": "small", "quantity": 15 },
    { "size": "large", "quantity": 8 }
  ]
}
```

- **Response:**

```json
{
  "id": "product_object_id"
}
```

---

### 2. List Products

- **GET** `/products`
- **Query Parameters (optional):** `name`, `size`, `limit`, `offset`
- **Response:**

```json
{
  "data": [
    {
      "id": "product_id",
      "name": "Premium Hoodie",
      "price": 1299.99
    }
  ],
  "page": {
    "next": "10",
    "limit": 0,
    "previous": -10
  }
}
```

---

### 3. Create Order

- **POST** `/orders`
- **Request Body:**

```json
{
  "userId": "user_1",
  "items": [{ "productId": "product_id", "qty": 2 }]
}
```

- **Response:**

```json
{
  "id": "order_object_id"
}
```

---

### 4. Get Orders by User

- **GET** `/orders/{userId}`
- **Query Parameters (optional):** `limit`, `offset`
- **Response:**

```json
{
  "data": [
    {
      "id": "order_id",
      "items": [
        {
          "productDetails": {
            "name": "Premium Hoodie",
            "id": "product_id"
          },
          "qty": 2
        }
      ],
      "total": 0.0
    }
  ],
  "page": {
    "next": "10",
    "limit": 0,
    "previous": -10
  }
}
```

---

## 🚀 Running Locally

1. Clone the repo:

```bash
git clone https://github.com/your-username/hrone-task.git
cd hrone-task
```

2. Create a `.env` file:

```
MONGO_URI=your_mongodb_connection_string
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the server:

```bash
uvicorn main:app --reload
```

Access Swagger docs at:
👉 `http://localhost:8000/docs`

---

## ✅ Deployment

Deployed on: **Render/Railway**
Base URL:

```
https://yourapp.onrender.com
```

---

## 👤 Author

- Name: _Manoj_ _Chunchu_
- GitHub: [github.com/ChunchuManoj](https://github.com/ChunchuManoj)
