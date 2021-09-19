from appium import webdriver
import XpathLibrary

desired_cap ={
  "deviceName": "Android Emulator",
  "platformName": "Android"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

def case1():
    if checkHomePageExist() == 1:
        print("Ok.")
    else:
        print("Fail.")
    if changesCategoryToWater() == 1:
        print("Ok.")
    else:
        print("Fail.")
    productName, productPrice = openFirstProductDetail()
    if addProductToBasket() == 1:
        print("Ok.")
    else:
        print("Fail.")
    if goToBasket() == 1:
        print("Ok.")
    else:
        print("Fail.")
    if controlAddedProductAndPrice(productName, productPrice) == 1:
        print("Ok.")
    else:
        print("Fail.")
    if deleteProductFromBasket() == 1:
        print("Ok.")
    else:
        print("Fail.")
    print("Case1 Finished!")

def case2():
    if checkHomePageExist() == 1:
        print("Ok.")
    else:
        print("Fail.")
    if openTheHamburgerMenu() == 1:
        print("Ok.")
    else:
        print("Fail.")
    if goToCategoryBabyCare() == 1:
        print("Ok.")
    else:
        print("Fail.")
    if openThirdProductDetail() == 1:
        print("Ok.")
    else:
        print("Fail.")
    if controlsPageExistence() == 1:
        print("Ok")
    else:
        print("Fail.")
    print("Case2 Finished!")

def checkHomePageExist():
    try:
        if driver.find_element_by_xpath(XpathLibrary.HamburgerMenu).is_enabled():
            if driver.find_element_by_xpath(XpathLibrary.Header).is_enabled():
                if driver.find_element_by_xpath(XpathLibrary.SearchIcon).is_enabled():
                    if driver.find_element_by_xpath(XpathLibrary.Notifications).is_enabled():
                        if driver.find_element_by_xpath(XpathLibrary.Basket).is_enabled():
                            return 1
    except :
        return 0

def changesCategoryToWater():
    try:
        driver.find_element_by_xpath(XpathLibrary.Water).click()
        return 1
    except:
        return 0

def openFirstProductDetail():
    try:
        driver.find_element_by_xpath(XpathLibrary.FirstItem).click()
        productName = driver.find_element_by_xpath(XpathLibrary.ProcuctNameInDetailPage).text
        productPrice = driver.find_element_by_xpath(XpathLibrary.ProductPriceInDetailPage).text
        return productName, productPrice
    except:
        return 0

def addProductToBasket():
    try:
        driver.find_element_by_xpath(XpathLibrary.AddToCardButton).click()
        driver.back()
        return 1
    except:
        return 0

def goToBasket():
    try:
        driver.find_element_by_xpath(XpathLibrary.Basket).click()
        return 1
    except:
        return 0

def controlAddedProductAndPrice(productName, productPrice):
    try:
        if productName == driver.find_element_by_xpath(XpathLibrary.ProcuctNameInBasketsFirstItem).text:
            print("Product Name is True")
        if productPrice == driver.find_element_by_xpath(XpathLibrary.ProductPriceInBasketsFirstItem).text:
            print("Product Price is True")
        return 1
    except:
        return 0

def deleteProductFromBasket():
    try:
        driver.find_element_by_xpath(XpathLibrary.DeleteProductButtonFirstItem).click()
        driver.back()
        return 1
    except:
        return 0

def openTheHamburgerMenu():
    try:
        driver.find_element_by_xpath(XpathLibrary.HamburgerMenu).click()
        return 1
    except:
        return 0

def goToCategoryBabyCare():
    try:
        driver.find_element_by_xpath(XpathLibrary.BabyCare).click()
        return 1
    except:
        return 0

def openThirdProductDetail():
    try:
        driver.find_element_by_xpath(XpathLibrary.ThirdItem).click()
        driver.back()
        return 1
    except:
        return 0

def controlsPageExistence():
    try:
        if driver.find_element_by_xpath(XpathLibrary.BabyCaree).is_selected():
            return 1
        else:
            return 0
    except:
        return 0

if __name__ == '__main__':
    case1()
    case2()