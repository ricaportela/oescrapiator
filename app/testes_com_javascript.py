# coding: utf-8
from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://www.revistanatura.com.br/html/widget/index_desktop.html?header=true&https=true")
element1 = driver.find_element_by_name('por-avancada')
element1.click()
txtCEP = driver.find_element_by_id("txtBuscaEnderecoCN")
driver.execute_script("document.getElementById('txtBuscaEnderecoCN').setAttribute('value', '08275030')")
driver.execute_script("document.getElementById('btnBuscar').click()")
driver.implicitly_wait(3)

# btnBuscar = driver.find_element_by_xpath("""//*[@id="btnBuscar"]""")
# btnBuscar.click()
listConsultores = driver.find_elements_by_class_name("element-consultant")
for x in listConsultores:
    print(x.text)
