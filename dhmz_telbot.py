from selenium import webdriver 
import webbrowser #only to show a picture

# options
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--hide-scrollbar')
options.add_argument('--force-device-scale-factor=1')
driver = webdriver.Chrome(options=options) 

# set size of the window -> size of the screenshot
driver.set_window_size(1000, 850)

#choose your city
driver.get('https://prognoza.hr/3dslika2_print_tp.php?Code=Zapresic') 

driver.save_screenshot('screenshot.png')

# to print screenshot on screen
webbrowser.open('screenshot.png')

# close browser after our manipulations 
driver.close() 
