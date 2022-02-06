from selenium import webdriver
import json
import pandas as pd
import re

website = 'https://www.venex.com.ar/componentes-de-pc/placas-de-video?vmm=12&limit=96'
driverPath = './chromedriver.exe'

driver = webdriver.Chrome(driverPath)
driver.get(website)

productos = driver.find_elements_by_class_name('product-box')

productosFullList = []

for producto in productos:
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
    if "LHR" in productName:
        productLHR = "LHR"
    else:
        productLHR = "NO LHR"


    fullProductData = []
    fullProductData.append("VENEX")
    fullProductData.append(productID)
    fullProductData.append(productBrand)
    fullProductData.append(productName)
    fullProductData.append(productLHR)
    fullProductData.append(productPrice)
    fullProductData.append(productURL)
    fullProductData.append(productImageURL)
    

    productosFullList.append(fullProductData)
    
    
driver.quit()


# Export
df = pd.DataFrame(productosFullList)
print(df)
df.to_csv('placas.csv', index=False)