# API Documentation

## POST /run

### Description

Triggers LinkedIn connection automation for a given profile URL.

---

### Request Headers

```
Content-Type: application/json
```

---

### Request Body

```json
{
  "url": "https://www.linkedin.com/in/example-profile/"
}
```

---

### Success Response (200)

```json
{
  "status": "success",
  "url": "https://www.linkedin.com/in/example-profile/"
}
```

---

### Error Responses

#### Missing URL (400)

```json
{
  "error": "Missing 'url' parameter"
}
```

#### Automation Failure (500)

```json
{
  "status": "failed",
  "url": "https://www.linkedin.com/in/example-profile/"
}
```
