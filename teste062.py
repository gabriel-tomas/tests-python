from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
def click_proximo():
    serv = Service('/usr/local/bin/geckodriver')
    nav = webdriver.Firefox(service=serv)
    nav.get('https://www.magazineluiza.com.br/selecao/ofertasdodia/')
    bot_prox = nav.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div[3]/ul[2]/li[10]/a').click()
click_proximo()
def varredura():
    req = requests.get('https://www.amazon.com/s?k=gaming+keyboard&pd_rd_r=0dc4e477-5aef-4e99-aa39-c6411f2ddeec&pd_rd_w=N2eF5&pd_rd_wg=AsFd2&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=1R5AA4A3QVTVWZEMSS1A&ref=pd_gw_unk')
    bs = BeautifulSoup(req.content, 'html.parser')
    produtos = bs.find('div', {'class': 's-main-slot s-result-list s-search-results sg-row'})
    print(req)


