import time
import base64
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


script = 'return document.documentElement.innerText'
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)

def to_image_data(html):
    
    driver.get('https://html2canvas.qaiik.repl.co/auto-data.html?code='+html)
    time.sleep(0.5)

    data = driver.execute_script(script)

    outbytes = base64.b64decode(data.encode())

    return outbytes

def to_PIL_image(html):
    
    driver.get('https://html2canvas.qaiik.repl.co/auto-data.html?code='+html)
    time.sleep(0.5)

    data = driver.execute_script(script)

    outbytes = base64.b64decode(data.encode())

    return Image.open(BytesIO(outbytes))

def stop_rendering():
    driver.quit()

def tk(img):
    from PIL import Image, ImageTk
    try:
        import Tkinter as tkinter
    except:
        import tkinter

    root = tkinter.Tk()

    # Create a photoimage object of the image in the path
    image1 = img
    test = ImageTk.PhotoImage(image1)

    label1 = tkinter.Label(image=test)
    label1.image = test

    # Position image
    label1.place(x=0, y=0)
    root.mainloop()

to_tk_image = to_PIL_image
    
    
