"""Scrape."""
# coding: utf-8
import sys
from selenium import webdriver
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))
display.start()

driver = webdriver.Firefox()
url = "https://www.revistanatura.com.br/html/widget"
driver.get(url)

txtBuscaAvancada = driver.find_element_by_name("por-avancada")
txtBuscaAvancada.click()
txtCEP = driver.find_element_by_xpath("""//*[@id="txtBuscaEnderecoCN"]""")
txtCEP.send_keys("18075570")
print("Type CEP Code...")
btnBuscar = driver.find_element_by_xpath("""//*[@id="btnBuscar"]""")
btnBuscar.click()
print("find representantes list...")

driver.implicitly_wait(3)
consultants = driver.find_elements_by_class_name('element-consultant')
string2 = []
for x in consultants:
    print(x.text)
    string1 = str(x.text).splitlines()
    string2.append(string1)

print(string2)
with open('output.txt', 'w') as target:
    for ab in string2:
        print(ab)
        target.write(str(ab))

paginads = driver.find_elements_by_class_name("wrapper-pagination")
for b in paginads:
    print(b.tag_name)

display.stop()
