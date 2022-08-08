from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class newbot:

    def __init__(self, nome_bot):
        self.driver = webdriver.Chrome("chromedriver")

    def climaTempo(self, cidades = []):

        try:
            #Cria um laço de repetição que vai acessar cada cidade recebida por parametro
            for cidade in cidades:
                site = 'https://www.climatempo.com.br'
                self.driver.get(site)
                sleep(5)
                self.driver.find_element_by_xpath('//*[@id="bt_modalSearch_mobile"]/i').click()
                elemento = self.driver.find_element_by_id("searchGeneralMobile")
                print('****  ' + cidade + '  ****')

                for letra in cidade:
                    elemento.send_keys(letra)
                    sleep(0.5)

                self.driver.implicitly_wait(3)
                li = self.driver.find_element_by_xpath('//*[@id="searchGeneralMobile_autocomplete"]/li[2]/a')
                print(li.get_attribute('href'))
                self.driver.get(li.get_attribute('href'))
                sleep(6)
                temperatura_minima = self.driver.find_element_by_xpath('//*[@id="min-temp-1"]').text
                temperatura_maxima = self.driver.find_element_by_xpath('//*[@id="max-temp-1"]').text
                chuva = self.driver.find_element_by_xpath(
                    '//*[@id="mainContent"]/div[4]/div[5]/div[1]/div[2]/div[2]/div[2]/div[1]/ul/li[2]/div/span').text\
                    .split('- ')
                quantidade_chuva = chuva[0]
                probabilidade_chuva = chuva[1]
                vento = self.driver.find_element_by_xpath(
                    '//*[@id="mainContent"]/div[4]/div[5]/div[1]/div[2]/div[2]/div[2]/div[1]/ul/li[3]/div').text\
                    .split("-")
                umidade_minima = self.driver.find_element_by_xpath(
                    '//*[@id="mainContent"]/div[4]/div[5]/div[1]/div[2]/div[2]/div[2]/div[1]/ul/li[4]/div/p/span[1]')\
                    .text
                umidade_maxima = self.driver.find_element_by_xpath(
                    '//*[@id="mainContent"]/div[4]/div[5]/div[1]/div[2]/div[2]/div[2]/div[1]/ul/li[4]/div/p/span[2]')\
                    .text
                dados = 'Temperatura Mínima: ' + temperatura_minima + '\n' \
                        'Temperatura Máxima: ' + temperatura_maxima + '\n' \
                        'Chuva (Probabilade): ' + quantidade_chuva + '(' + probabilidade_chuva + ')\n' \
                        'Vento: ' + vento[1] + '\n' \
                        'Umidade Mínima: ' + umidade_minima + '\n' \
                        'Umidade Máxima: ' + umidade_maxima
                print(dados)
                print('-----------------------------------------------------------------------------------------------')

        except:
            self.driver.close()
            self.erro()


    def erro(self):
         self.climaTempo()