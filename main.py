from scrapper import GameScrapper
from models import Games
from database import save_game

SEARCH_TEXT = "fireboy"

def main():
    print("Iniciando Scrapper!")
    scraper = GameScrapper()
    scraper.start()
    scraper.accept_cookies()
    gamesURL = scraper.search_game(SEARCH_TEXT)

    GamesList = []

    for url in gamesURL:
        game = scraper.scrape_game(url)
        GamesList.append(game)
        print(game)

    for game in GamesList:
        save_game(game)
    print("Finalizando Scrapper!")
        
if __name__ == "__main__":
    main()