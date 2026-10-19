from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from models import Games

class GameScrapper():
    def __init__(self,):
        self.driver = webdriver.Chrome() 

    def start(self):
        self.driver.get("https://gamedistribution.com/games/")

    def close(self):
        if self.driver:
            self.driver.quit()

    def accept_cookies(self):
        try:
            accept_cookies = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/button[1]"))
            ).click()
            print("Click boton aceptar cookies")
        except Exception as e:
            print("No hay boton de cookies")

    def search_game(self, SEARCH_TEXT):
        wait = WebDriverWait(self.driver, 10)
        product_item_div = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='grid gap-2 grid-cols-2 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-5 mb-10']")))
        first_product_item = product_item_div.find_element(By.XPATH, ".//div[1]")    

        search_input = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div[1]/div/div[1]/input")

        search_input.clear()
        search_input.send_keys(SEARCH_TEXT)
        search_input.send_keys(Keys.ENTER)

        wait.until(EC.staleness_of(first_product_item))
        product_item_div = None
        try:
            GamesUrl = []
            wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'ProductItem_productList')]")))
            product_item_div = self.driver.find_element(By.XPATH, "//div[@class='grid gap-2 grid-cols-2 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-5 mb-10']")
            product_items = product_item_div.find_elements(By.XPATH, "./div")
            for ProductItem in product_items:
                GamesUrl.append(ProductItem.find_element(By.XPATH, ".//a[contains(@class, 'product-name')]").get_attribute("href").strip())
            return GamesUrl
        except Exception as e:
            print("no hay resultados")
            return []

    def scrape_game(self, url):
        external_id = None
        game_title = None
        published_by = None
        languages = None
        android = None
        ios = None
        description = None
        age_groups = None
        genres = None
        tags = None
        instruction = None

        try:
            self.driver.get(url)
            external_id = self.driver.find_element(By.XPATH, '//div[@class="row"]//span[@class="copy-input"]').text.strip()
            external_id = external_id.split("/")[3]

            game_title = self.driver.find_element(By.XPATH, '//strong[@class="font-semibold pl-1"]').text.strip()
            published_by = self.driver.find_element(By.XPATH, '//a[@class="text-interdimensional underline pl-1"]').text.strip()

            spans = self.driver.find_element(By.XPATH, '//span[@class="flex flex-1"][text()="Language"]/following-sibling::div')
            spans = spans.find_elements(By.XPATH, "./span")
            languages = [asd.text.strip() for asd in spans]

            spans = self.driver.find_element(By.XPATH, '//span[contains(text(), "Mobile Web Compatible")]').text.strip()
            android = False
            ios = False
            if "Android" in spans:
                android = True
            if "IOS" in spans:
                ios = True

            description = self.driver.find_element(By.XPATH, '//p[@class="mb-10"]').text.strip()

            spans = self.driver.find_element(By.XPATH, '//span[@class="flex"][text()="Age Group"]/following-sibling::div')
            spans = spans.find_elements(By.XPATH, "./span")
            age_groups = [asd.text.strip() for asd in spans]

            spans = self.driver.find_element(By.XPATH, '//h4[text()="Genres"]/following-sibling::div')
            spans = spans.find_elements(By.XPATH, "./span")
            genres = [asd.text.strip() for asd in spans]

            spans = self.driver.find_element(By.XPATH, '//h4[text()="Tags"]/following-sibling::div')
            spans = spans.find_elements(By.XPATH, "./span")
            tags = [asd.text.strip() for asd in spans]

            instruction = self.driver.find_element(By.XPATH, '//p[@class="mb-10"]/following-sibling::p').text.strip()
        except Exception as e:
            return ""

        return Games(
            external_id, game_title, published_by,
            languages, android, ios, description,
            age_groups, genres, tags, instruction
        )

