# Setup Guide

## Prerequisites

* Python 3.8+
* Brave Browser (installed)
* ChromeDriver (compatible with Brave)
* Active LinkedIn login in Brave browser

---

## Step 1: Clone Repository

```bash
git clone https://github.com/your-username/linkedin-connect-automation.git
cd linkedin-connect-automation
```

---

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 3: Configure Browser Paths

Update the following constants in `app.py`:

* `BRAVE_PATH`
* `CHROMEDRIVER_PATH`
* `USER_DATA_DIR`
* `PROFILE_DIR`

Ensure the LinkedIn account is already logged in via this browser profile.

---

## Step 4: Run Server

```bash
python app.py
```

Server starts at:

```
http://127.0.0.1:5000
```
