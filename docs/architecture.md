# System Architecture

## High-Level Flow

Client → Flask API → Selenium WebDriver → Brave Browser → LinkedIn → Response

---

## Architecture Breakdown

1. Client sends LinkedIn profile URL
2. Flask API validates request
3. Selenium launches Brave with existing user session
4. LinkedIn profile page is loaded
5. Connect button is detected and clicked
6. Connection request is sent
7. Browser closes and response is returned

---

## Key Design Choices

* Uses real browser session (no bots)
* No LinkedIn API usage
* Human-like delays and scrolling
* Explicit waits for UI elements
