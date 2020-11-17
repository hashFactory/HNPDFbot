from shutil import which
import subprocess
import os
import pdfkit

# could be CHROMIUM or WK
engine = "WK"
chromium_location = ""

wk_options = {
    'page-size': 'Letter',
    'margin-top': '0.0in',
    'margin-right': '0.0in',
    'margin-bottom': '0.0in',
    'margin-left': '0.0in',
    'encoding': "UTF-8",
    'no-outline': None,
	'javascript-delay': '1000'
}

def choose_engine():
    global engine, chromium_location
    chromium = which("chromium")
    chromium_browser = which("chromium-browser")
    if chromium is not None:
        engine = "CHROMIUM"
        chromium_location = chromium
    elif chromium_browser is not None:
        engine = "CHROMIUM"
        chromium_location = chromium_browser
    print("Using " + engine)
    

def render(url, path):
    if engine == "WK":
        pdfkit.from_url(url, path, options=wk_options)
    elif engine == "CHROMIUM":
        subprocess.run([chromium_location, "--headless", "--run-all-compositor-stages-before-draw", "--no-margins", \
         "--print-to-pdf-no-header", "--print-to-pdf=" + path, url])
