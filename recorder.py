from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from obswebsocket import obsws, requests
import time

# --- 1. Open lecture page ---
browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
browser.get("https://live.rbg.tum.de/login")
print("Firefox opened. Waiting...")
# Optional: login automatically (you’ll need to handle TUM login page)
# browser.find_element(By.ID, "username").send_keys("your_tum_id")
# browser.find_element(By.ID, "password").send_keys("your_password")
#
browser.find_element("link text", "TUM Login").click()

browser.find_element(By.ID, "btnLogin").click()
# Navigate to the lecture link
# browser.get("https://tumlecturelink...")


# --- 2. Connect to OBS via WebSocket ---
host = "localhost"
port = 4455  # default OBS websocket port
password = "your_obs_password"

#ws = obsws(host, port, password)
#ws.connect()

# --- 3. Start recording ---
#ws.call(requests.StartRecord())

#print("Recording started...")

# --- 4. Wait for 1h30 (5400 seconds) ---
#time.sleep(5400)
time.sleep(50)
# --- 5. Stop recording ---
#ws.call(requests.StopRecord())
#print("Recording stopped.")

# --- 6. Clean up ---
#ws.disconnect()
browser.quit()
