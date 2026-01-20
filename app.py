"""
LinkedIn Connect Automation API

This Flask application exposes an endpoint that triggers
a Selenium-based automation to send LinkedIn connection
requests using a logged-in Brave browser profile.

Intended for controlled, internal, or educational use only.
"""

import os
import time
import random
from flask import Flask, request, jsonify

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# =======================
# CONFIG (Environment Variables)
# =======================

BRAVE_PATH = os.getenv("BRAVE_PATH")
CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH")
USER_DATA_DIR = os.getenv("USER_DATA_DIR")
PROFILE_DIR = os.getenv("PROFILE_DIR", "Default")

ADD_NOTE = False
NOTE_MESSAGE = "Hey! I came across your profile and would love to connect!"


# =======================
# VALIDATION
# =======================

if not all([BRAVE_PATH, CHROMEDRIVER_PATH, USER_DATA_DIR]):
    raise RuntimeError(
        "Missing required environment variables: "
        "BRAVE_PATH, CHROMEDRIVER_PATH, USER_DATA_DIR"
    )


# =======================
# SELENIUM BOT FUNCTION
# =======================

def run_linkedin_bot(profile_url: str) -> bool:
    print(f"🌐 Opening LinkedIn profile: {profile_url}")

    chrome_options = Options()
    chrome_options.binary_location = BRAVE_PATH
    chrome_options.add_argument(f"--user-data-dir={USER_DATA_DIR}")
    chrome_options.add_argument(f"--profile-directory={PROFILE_DIR}")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    wait = WebDriverWait(driver, 15)

    try:
        driver.get(profile_url)
        time.sleep(6)

        # Scroll to simulate human behavior
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 3);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

        # Locate Connect button
        buttons = driver.find_elements(By.TAG_NAME, "button")
        print(f"🔍 Found {len(buttons)} buttons... scanning for 'Connect'...")

        connect_btn = None
        for btn in buttons:
            try:
                text = btn.text.strip()
                aria = btn.get_attribute("aria-label")
                if "Connect" in text or (aria and "invite" in aria.lower()):
                    connect_btn = btn
                    print(f"👍 Connect button found: {text}")
                    break
            except Exception:
                continue

        if not connect_btn:
            print("⚠️ No connect button found. Possibly already connected.")
            return False

        # Click Connect
        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            connect_btn
        )
        time.sleep(1)
        driver.execute_script("arguments[0].click();", connect_btn)
        print("🫱 Clicked 'Connect'")

        # Handle popup
        try:
            popup = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'artdeco-modal__content')]")
                )
            )
            print("💬 Connect popup detected.")
            time.sleep(1)

            if ADD_NOTE:
                try:
                    add_note_btn = popup.find_element(
                        By.XPATH, "//button[contains(@aria-label, 'Add a note')]"
                    )
                    driver.execute_script("arguments[0].click();", add_note_btn)

                    textarea = wait.until(
                        EC.presence_of_element_located(
                            (By.XPATH, "//textarea[contains(@id, 'custom-message')]")
                        )
                    )
                    textarea.send_keys(NOTE_MESSAGE)

                    send_btn = popup.find_element(
                        By.XPATH, "//button[contains(@aria-label, 'Send')]"
                    )
                    driver.execute_script("arguments[0].click();", send_btn)
                    print("🎯 Sent connection request with note.")
                except Exception:
                    print("⚠️ Failed to send with note.")
            else:
                try:
                    send_btn = wait.until(
                        EC.element_to_be_clickable(
                            (By.XPATH, "//button[contains(@aria-label, 'Send without a note')]")
                        )
                    )
                    driver.execute_script("arguments[0].click();", send_btn)
                    print("🎯 Sent connection request without note.")
                except Exception:
                    print("⚠️ Send button not found.")

        except TimeoutException:
            print("⚠️ Connection popup did not appear.")

        time.sleep(random.randint(6, 10))
        return True

    finally:
        driver.quit()
        print("✅ Browser closed")


# =======================
# FLASK API
# =======================

app = Flask(__name__)


@app.route("/run", methods=["POST"])
def run_bot_api():
    data = request.get_json(silent=True)
    url = data.get("url") if data else None

    if not url:
        return jsonify({"error": "Missing 'url' parameter"}), 400

    print(f"🚀 API received URL: {url}")

    success = run_linkedin_bot(url)

    if success:
        return jsonify({"status": "success", "url": url})
    return jsonify({"status": "failed", "url": url}), 500


# =======================
# SERVER START
# =======================

if __name__ == "__main__":
    app.run(port=5000)
