# LinkedIn Connect Automation API

A Flask-based automation service that uses **Selenium with a logged-in Brave browser profile** to send LinkedIn connection requests programmatically.

The API exposes an endpoint that accepts a LinkedIn profile URL and triggers a browser automation flow to send a connection request, with optional personalized notes.

---

## 📌 Project Purpose

This project automates the **manual LinkedIn connection process** while maintaining human-like behavior by:

* Using a real browser (Brave)
* Reusing an authenticated user profile
* Avoiding direct LinkedIn scraping or APIs

---

## 🎯 Use Cases

* Recruiter outreach automation
* Sales and lead generation
* Networking automation
* Internal hiring tools
* Controlled LinkedIn engagement workflows

---

## 🛠 Tech Stack

| Component     | Technology   |
| ------------- | ------------ |
| Language      | Python       |
| API Framework | Flask        |
| Automation    | Selenium     |
| Browser       | Brave        |
| Driver        | ChromeDriver |

---

## 📂 Project Structure

```
.
├── app.py
├── requirements.txt
├── README.md
├── docs/
└── examples/
```

---

## 🌐 API Overview

### Endpoint

```
POST /run
```

### Description

Triggers Selenium automation to send a LinkedIn connection request to the given profile URL.

---

## 📖 Documentation Index

* [Setup Guide](docs/setup.md)
* [System Architecture](docs/architecture.md)
* [API Reference](docs/api.md)
* [Selenium Automation Logic](docs/selenium.md)
* [Configuration Guide](docs/configuration.md)
* [Limitations](docs/limitations.md)
* [Compliance & Safety](docs/compliance.md)

---

## 👨‍💻 Author

**Artham Varshith**
Software Engineer
