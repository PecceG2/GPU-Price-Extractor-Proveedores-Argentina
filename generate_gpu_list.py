from selenium import webdriver
import json
import pandas as pd
import re
import time


# Config vars
websiteVENEX = 'https://www.venex.com.ar/componentes-de-pc/placas-de-video?vmm=12&limit=96'
websiteCG1 = 'https://compragamer.com/?seccion=3&cate=6'
websiteCG2 = 'https://compragamer.com/?seccion=3&cate=62'
driverPath = './chromedriver.exe'


# General Parse Functions
def getChipBrand(productName):
    nvidia = ["nvidia", "geforce", "rtx", "gt7", "gtx"]
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


# Getters
def getVENEX(webURL):
    driver = getWebDriver()
    driver.get(webURL)
    productos = driver.find_elements_by_class_name('product-box')

    productosFullList = []
    for producto in productos:
        # Selectors & parsers
        productSelector = producto.find_element_by_css_selector('.product-box-title a')
        productInfo = productSelector.get_attribute('onclick')
        productInfo = productInfo.replace('enhancedClick(', '')
        productInfo = productInfo[:-1]
        productInfoObj = json.loads(productInfo)
        productMediaClickSelector = producto.find_element_by_css_selector('.product-box-media a')
        
        productID = productInfoObj['id']
        productName = re.sub('Placa De Video ', '', productInfoObj['name'], flags=re.IGNORECASE)
        productBrand = productInfoObj['brand']
        productPrice = productInfoObj['price']
        productURL = productMediaClickSelector.get_attribute('href')
        productImageURL = producto.find_element_by_css_selector('.img-contained').get_attribute('src')


        # Product
        fullProductData = []
        fullProductData.append("VENEX")
        #fullProductData.append(productID)                    # No se le encontró un uso real para esto, pero si se desea, se puede descomentar.
        fullProductData.append(getChipBrand(productName))
        fullProductData.append(productBrand)
        fullProductData.append(productName)
        fullProductData.append(isLHR(productName))
        fullProductData.append(productPrice)
        fullProductData.append(productURL)
        fullProductData.append(productImageURL)
        
        productosFullList.append(fullProductData)
        
   
    closeWebDriver(driver)
    return productosFullList;
        

def getCG(webURL):

    driver = getWebDriver()
    driver.get(webURL)
    driver.execute_script("function pageScroll() { window.scrollBy(0,50); scrolldelay = setTimeout(pageScroll,10); } pageScroll()") # Scroll al fondo para evitar el lazy loading
    time.sleep(6)
    productos = driver.find_elements_by_class_name('card-product')

    productosFullList = []
    for producto in productos:
    
        # Selectors & parsers
        productName = re.sub('Placa De Video ', '', producto.find_element_by_css_selector('.theme_nombreProducto a span').text, flags=re.IGNORECASE)
        productURL = producto.find_element_by_css_selector('.theme_nombreProducto a').get_attribute('href')
        productPrice = producto.find_element_by_class_name('theme_precio').text
        productImageURL = producto.find_element_by_css_selector('.imagenPrincipal img').get_attribute('src')
            
        # Product
        fullProductData = []
        fullProductData.append("CompraGamer")
        fullProductData.append(getChipBrand(productName))
        fullProductData.append("Unknown")
        fullProductData.append(productName)
        fullProductData.append(isLHR(productName))
        fullProductData.append(productPrice)
        fullProductData.append(productURL)
        fullProductData.append(productImageURL)
        

        productosFullList.append(fullProductData)
        
  
    closeWebDriver(driver)
    return productosFullList;


# Run getters
productosObtenidos = []
productosObtenidos.extend(getVENEX(websiteVENEX))
productosObtenidos.extend(getCG(websiteCG1)) #NVIDIA
productosObtenidos.extend(getCG(websiteCG2)) #AMD


# Export to CSV
df = pd.DataFrame(productosObtenidos)
print(df)
df.to_csv('placas.csv', index=False)


