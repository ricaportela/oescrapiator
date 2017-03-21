# coding: utf-8
""""Scrape htmlpage to return consultants list."""
from selenium import webdriver


class Browse_Webdriver():
    """Drive into HTML to Scrape."""

    # URL = "https://www.revistanatura.com.br/html/widget/index_desktop.html?header=true&https=true"

    def open_browser_webdriver():
        """Open firefox browser."""
        driver = webdriver.Firefox()
        return driver

    def open_link(driver, URL):
        """Open html page to scrape."""
        driver.get(URL)
        element1 = driver.find_element_by_name('por-avancada')
        element1.click()
        # txtCEP = driver.find_element_by_id("txtBuscaEnderecoCN")
        driver.execute_script("document.getElementById('txtBuscaEnderecoCN').setAttribute('value', '18075570')")
        driver.execute_script("document.getElementById('btnBuscar').click()")

        """ Paginacao
        numero total de paginas = totalpages
        numero pagina atual = currentpage
        CAPTCHA
          os dados estao em imagens
          para acessar é necessario quebrar o captcha pelo menos uma vez
          antes de gerar a lista dos consultores executar o quebra captcha
        """

        currentpage = 1
        totalpages = driver.find_elements_by_class_name('element-pagination')
        totalpages = int(totalpages[6].text)
        print(totalpages)
        listnames = []
        while currentpage <= totalpages:
            driver.implicitly_wait(3)
            print("Pagina atual", currentpage)
            listConsultores = driver.find_elements_by_class_name("element-consultant")
            for x in listConsultores:
                listnames = listnames.insert(str(x.text).splitlines())

            currentpage += 19

        print(listnames)
        # driver.execute_script("document.getElementByName('element-next active').click()")
        # element2 = driver.find_elements_by_class_name('element-next active')
        # element2.click()

# <p class="element-next active" onclick="BuscaAvancada('2')">Próximo</p>
