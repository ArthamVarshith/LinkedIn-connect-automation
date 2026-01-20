# Selenium Automation Logic

## Browser Configuration

* Uses Brave browser
* Loads existing user data directory
* Disables automation flags for detection avoidance

---

## Automation Steps

1. Open LinkedIn profile URL
2. Scroll page to simulate human behavior
3. Locate "Connect" button via:

   * Button text
   * aria-label attributes
4. Click Connect
5. Handle connection popup
6. Optionally add a personalized note
7. Submit request
8. Close browser

---

## Anti-Detection Measures

* Randomized delays
* Real user profile
* No headless mode
* Disabled automation extensions
