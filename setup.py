from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException 

option = webdriver.ChromeOptions()
# navegação anonima
option.add_argument("-incognito")

# instanciando o objeto chromedriver
browser = webdriver.Chrome('C:\chromedriver\chromedriver', options=option)

# entrando em um site por esse objeto
browser.get("https://github.com/TheDancerCodes")

# esperar 20 segundo para a página carregar
timeout = 20

# pegando a foto do github
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='avatar avatar-user width-full border color-bg-default']")))
except TimeoutException:
    print("Acabou o tempo estimado para carregar a página")
    browser.quit()

# selenium object - vamos iterar para pegar os titulos que há nesse perfil
titles_element = browser.find_elements(By.XPATH, "//span[@class='repo']")

titles = [x.text for x in titles_element]

print("Titles: ")
print(titles, '\n')

# pegaremos agora a linguagem que está no perfil do github
language_element = browser.find_elements(By.XPATH, "//span[@class='d-inline-block mr-3']/span[2]")

# list comprehension para cada linguagem
languages = [x.text for x in language_element] 

print("Languages:")
print(languages, '\n')

# Vamos combinar os resultados para ver
for title, language in zip(titles, languages):
    print("Reponame : Language")
    print(f"{title} : {language}, \n")
