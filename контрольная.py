import sqlite3
import requests
from bs4 import BeautifulSoup
from collections import Counter
class Database:
    def __init__(self, db_name="search_engine.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS websites (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    url TEXT UNIQUE
                )
            """)

    def add_website(self, url):
        with self.conn:
            self.conn.execute("INSERT OR IGNORE INTO websites (url) VALUES (?)", (url,))

    def get_websites(self):
        with self.conn:
            return [row[0] for row in self.conn.execute("SELECT url FROM websites")]

    def clear_websites(self):
        with self.conn:
            self.conn.execute("DELETE FROM websites")
class WebParser:
    def fetch_content(self, url):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.text
        except requests.RequestException:
            return ""

    def count_keyword(self, html_content, keyword):
        soup = BeautifulSoup(html_content, 'html.parser')
        text = soup.get_text()
        words = text.split()
        return Counter(words)[keyword]
class UserInterface:
    def __init__(self):
        self.db = Database()
        self.parser = WebParser()

    def add_website(self):
        url = input("Введите URL сайта для добавления: ")
        self.db.add_website(url)
        print("Сайт добавлен!")

    def clear_database(self):
        self.db.clear_websites()
        print("База данных очищена!")

    def search(self):
        keyword = input("Введите слово для поиска: ")
        websites = self.db.get_websites()

        if not websites:
            print("База данных пуста. Добавьте сайты перед поиском.")
            return

        results = []
        for url in websites:
            print(f"Обработка {url}...")
            html_content = self.parser.fetch_content(url)
            count = self.parser.count_keyword(html_content, keyword)
            if count > 0:
                results.append((url, count))

        results.sort(key=lambda x: x[1], reverse=True)
        for url, count in results:
            print(f"{url} — {count} совпадений")

    def run(self):
        while True:
            print("\nМеню:")
            print("1. Добавить сайт")
            print("2. Очистить базу данных")
            print("3. Поиск")
            print("4. Выйти")
            choice = input("Выберите действие: ")

            if choice == "1":
                self.add_website()
            elif choice == "2":
                self.clear_database()
            elif choice == "3":
                self.search()
            elif choice == "4":
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()
