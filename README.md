# 🚀 FastAPI HTTP Request Practice

This project is a **practice API** built with **FastAPI**, demonstrating how to handle:

* ✅ **Query parameters**
* ✅ **HTTP headers**
* ✅ **Request body (JSON)**

It simulates how to build a small REST API and test it using Postman or a web browser.

---

## 📦 **Requirements**

* Python 3.9+
* FastAPI
* Uvicorn (for running the server)

Install dependencies:

```bash
pip install fastapi uvicorn
```

---

## ▶️ **How to Run the API**

Run the server using Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://localhost:8000
```

---

## 🔍 **Available Routes**

### 1. **GET /hello**

#### ➤ Description:

* Reads two query parameters: `name` (**str**) and `is_teacher` (**bool**).
* Returns a message depending on the parameters.

#### ➤ Examples:

| URL Example                           | Response                   |
| ------------------------------------- | -------------------------- |
| `/hello?name=Ryan&is_teacher=true`    | Hello Teacher Ryan !       |
| `/hello?name=Rakoto&is_teacher=false` | Hello Rakoto !             |
| `/hello`                              | Hello world                |
| `/hello?name=Ryan`                    | Hello Ryan !               |
| `/hello?is_teacher=true`              | Hello Teacher Non fourni ! |

---

### 2. **GET /top-secret**

#### ➤ Description:

* Checks the **Authorization header**.
* If the header is not equal to `my-secret-key`, responds with **403 Forbidden**.

#### ➤ Header Example:

| Header Name   | Value         |
| ------------- | ------------- |
| Authorization | my-secret-key |

| Scenario                | Response                               |
| ----------------------- | -------------------------------------- |
| Correct header          | Welcome to the secret area!            |
| Wrong or missing header | 403 Forbidden, shows what was provided |

---

### 3. **POST /welcome**

#### ➤ Description:

* Expects a JSON body with a `secret_code` (**int**).
* Accepts only **4-digit numbers** (from 1000 to 9999).

#### ➤ Body Example (valid):

```json
{
  "secret_code": 1234
}
```

| Secret Code | Response                              |
| ----------- | ------------------------------------- |
| 1234        | Access Granted! Secret code accepted. |
| 123         | 400 Bad Request - Invalid code        |
| 12345       | 400 Bad Request - Invalid code        |

---

## 🔧 **Future Improvements**

* Add automatic API documentation at `/docs`.
* Add authentication and error logging.
* Add unit tests.

---

## 🛠️ **License**

MIT — educational use only.

---