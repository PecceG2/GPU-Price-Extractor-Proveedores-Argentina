from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import json
import pandas as pd
import re
import time


# Config vars
websiteVENEX = 'https://www.venex.com.ar/componentes-de-pc/placas-de-video?vmm=12&limit=96'
websiteCG1 = 'https://compragamer.com/?seccion=3&cate=6'
websiteCG2 = 'https://compragamer.com/?seccion=3&cate=62'
websiteFullH4rd = 'https://www.fullh4rd.com.ar/cat/supra/3/placas-de-video/'
websiteLOGG = 'https://www.logg.com.ar/PRODUCTOS/PLACA-DE-VIDEO'
driverPath = './chromedriver.exe'

# Placas list
listadoGPUs = []


# General Parse Functions
def getChipBrand(productName):
    nvidia = ["nvidia", "geforce", "rtx", "gt7", "gtx", "quadro"]
    amd = ["amd", "radeon", "RX5", "RX6"]
    intel = ["intel", "arc", "alchemist"]

    if any(element.upper() in productName.upper() for element in nvidia):
        return "NVIDIA"
    elif any(element.upper() in productName.upper() for element in amd):
        return "AMD"
    elif any(element.upper() in productName.upper() for element in intel):
        return "Intel"
    else:
        return "Other"
        
    
def getBrand(productName):
    brands = ["palit", "msi", "gigabyte", "powercolor", "sapphire", "afox", "asrock", "pny", "gainward", "evga", "zotac", "xfx", "arktek", "asus", "coolermaster", "inno3d"]
    if any(ext in productName.lower() for ext in brands):
        return [ext for ext in brands if(ext in productName.lower())][0]
    
    
def isLHR(productName):
    if "LHR" in productName:
        return "LHR"
    else:
        return "NO LHR"
    

# Driver
def getWebDriver():
    return webdriver.Chrome(driverPath)
def closeWebDriver(driver):
    driver.quit()

def addGPU(proveedor, chipBrand, productBrand, productName, LHR, productPrice, productURL, productImageURL):
    individualGPU = []
    individualGPU.append(proveedor)
    individualGPU.append(chipBrand)
    individualGPU.append(productBrand)
    individualGPU.append(productName)
    individualGPU.append(LHR)
    individualGPU.append(productPrice)
    individualGPU.append(productURL)
    individualGPU.append(productImageURL)
    listadoGPUs.append(individualGPU)
    print("[" + proveedor + "] " + productName)

def elementExistsByCSSSelector(driver, selector):
    try:
        driver.find_element(By.CSS_SELECTOR, selector)
    except NoSuchElementException:
        return False
    return True

# Getters
def getVENEX(webURL):
    driver = getWebDriver()
    driver.get(webURL)
    productos = driver.find_elements(By.CLASS_NAME, 'product-box')

    productosFullList = []
    for producto in productos:
        # Selectors & parsers
        productSelector = producto.find_element(By.CSS_SELECTOR, '.product-box-title a')
        productInfo = productSelector.get_attribute('onclick')
        productInfo = productInfo.replace('enhancedClick(', '')
        productInfo = productInfo[:-1]
        productInfoObj = json.loads(productInfo)
        productMediaClickSelector = producto.find_element(By.CSS_SELECTOR, '.product-box-media a')
        
        productID = productInfoObj['id']
        productName = re.sub('Placa De Video ', '', productInfoObj['name'], flags=re.IGNORECASE)
        productBrand = productInfoObj['brand']
        productPrice = productInfoObj['price']
        productURL = productMediaClickSelector.get_attribute('href')
        productImageURL = producto.find_element(By.CSS_SELECTOR, '.img-contained').get_attribute('src')

        # Add
        addGPU("VENEX", getChipBrand(productName), productBrand, productName, isLHR(productName), productPrice, productURL, productImageURL)
   
    closeWebDriver(driver)
    return productosFullList;
        
def getCG(webURL):

    driver = getWebDriver()
    driver.get(webURL)
    driver.execute_script("function pageScroll() { window.scrollBy(0,50); scrolldelay = setTimeout(pageScroll,10); } pageScroll()") # Scroll al fondo para evitar el lazy loading
    time.sleep(6)
    productos = driver.find_elements(By.CLASS_NAME, 'card-product')

    productosFullList = []
    for producto in productos:
    
        # Selectors & parsers
        productName = re.sub('Placa De Video ', '', producto.find_element(By.CSS_SELECTOR, '.theme_nombreProducto a span').text, flags=re.IGNORECASE)
        productURL = producto.find_element(By.CSS_SELECTOR, '.theme_nombreProducto a').get_attribute('href')
        productPrice = producto.find_element(By.CLASS_NAME, 'theme_precio').text
        productImageURL = producto.find_element(By.CSS_SELECTOR, '.imagenPrincipal img').get_attribute('src')
            
        # Add
        addGPU("CompraGamer", getChipBrand(productName), getBrand(productName), productName, isLHR(productName), productPrice, productURL, productImageURL)
        
  
    closeWebDriver(driver)
    return productosFullList;

def getFullH4rd(webURL):
    
    pasoPaginacionActual = 1
    while (pasoPaginacionActual <= 200): #Si tiene mas de 200 pasos está loco.
        driver = getWebDriver()
        driver.get(webURL+str(pasoPaginacionActual))
        productos = driver.find_elements(By.CSS_SELECTOR, '.list .item')
        
        # Check if existe siguiente paso de paginación
        
        
        if elementExistsByCSSSelector(driver, '.paginator .item:last-child a'):
            pasoPaginacionActual = pasoPaginacionActual+1
        else:
            pasoPaginacionActual = pasoPaginacionActual+200
        
        productosFullList = []
        for producto in productos:
        
            # Selectors & parsers
            productName = re.sub('VIDEO ', '', producto.find_element(By.CSS_SELECTOR, '.info h3').text, flags=re.IGNORECASE)
            productURL = producto.find_element(By.CSS_SELECTOR, 'a:first-child').get_attribute('href')
            productPrice = producto.find_element(By.CLASS_NAME, 'price').text.split()[0]
            productImageURL = producto.find_element(By.CSS_SELECTOR, '.image img').get_attribute('src')
                
            # Add
            addGPU("FULLH4RD", getChipBrand(productName), getBrand(productName), productName, isLHR(productName), productPrice, productURL, productImageURL)
            
        closeWebDriver(driver)

def getLOGG(webURL):

    driver = getWebDriver()
    driver.get(webURL)
    time.sleep(6)
    productos = driver.find_elements(By.CLASS_NAME, 'producto-box')

    productosFullList = []
    for producto in productos:
    
        # Selectors & parsers
        productName = producto.find_element(By.CSS_SELECTOR, '.card-title a').get_attribute('innerHTML')
        productURL = producto.find_element(By.CSS_SELECTOR, '.card-title a').get_attribute('href')
        productPrice = producto.find_element(By.CLASS_NAME, 'card-price').text
        productImageURL = producto.find_element(By.CSS_SELECTOR, '.card-header img').get_attribute('src')
            
        # Add
        addGPU("LOGG Hardstore", getChipBrand(productName), getBrand(productName), productName, isLHR(productName), productPrice, productURL, productImageURL)
        
  
    closeWebDriver(driver)
    return productosFullList;



# Run getters
getVENEX(websiteVENEX)
getCG(websiteCG1) #NVIDIA
getCG(websiteCG2) #AMD
getFullH4rd(websiteFullH4rd)
getLOGG(websiteLOGG)

# Export to CSV
df = pd.DataFrame(listadoGPUs)
print(df)
df.to_csv('placas.csv', index=False)


