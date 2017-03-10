"""Scrape."""
# coding: utf-8
from app.browser import Browser
from selenium.common.exceptions import NoSuchElementException


class Scrapernt():
    def __init__():
        pass


    def consultants_list(self, zipcode):
        check_exists_by_name("por-avancada")

        inputZipCode = driver.find_element_by_xpath("""//*[@id="txtBuscaEnderecoCN"]""")
        inputZipCode.send_keys("18075570")

        print("Type CEP Code...")
        btnSearch = driver.find_element_by_xpath("""//*[@id="btnBuscar"]""")
        btnSearch.click()

        print("find representantes list...")
        driver.implicitly_wait(3)
        consultants = driver.find_elements_by_class_name('element-consultant')
        consultants_list = []
        for consultant in consultants:
            print(consultant.text)
            consultants_data = str(consultant.text).splitlines()
            consultants_list.append(consultants_data)

            print(consultants_list)
            with open('output.txt', 'w') as target:
                for info in consultants_list:
                    print(info)
                    target.write(str(info))
# def check_exists(type, search):
    def check_exists_by_name(byname):
        """Test if the element exist in HTML Page."""
        try:
            inputtxtAvancedSearch = driver.find_element_by_name("por-avancada")
            inputtxtAvancedSearch.click()

        except NoSuchElementException:
            print "element by name not found!"
            return False
        return True


    def pagination():
        paginads = driver.find_elements_by_class_name("wrapper-pagination")
        for b in paginads:
            print(b.tag_name)
