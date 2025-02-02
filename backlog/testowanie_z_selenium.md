# Testowanie w Django za pomocą Selenium

## 1. Wprowadzenie
Selenium to narzędzie do automatyzacji testów interfejsu użytkownika. W Django Selenium może być używane do testowania interakcji użytkownika z aplikacją, takich jak wypełnianie formularzy, klikanie przycisków i sprawdzanie treści renderowanych stron.

## 2. Instalacja Selenium
Aby rozpocząć testowanie w Selenium, należy zainstalować odpowiednie pakiety:

```sh
pip install selenium
```

Należy również pobrać odpowiedni WebDriver dla używanej przeglądarki, np. [Chromedriver](https://chromedriver.chromium.org/downloads) dla Google Chrome.

## 3. Konfiguracja testów Selenium w Django
Django oferuje `LiveServerTestCase`, który uruchamia testowy serwer HTTP, umożliwiając interakcję z aplikacją w Selenium.

```python
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class MySeleniumTests(StaticLiveServerTestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        service = Service('/path/to/chromedriver')  # Podaj ścieżkę do WebDrivera
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_homepage_loads(self):
        self.driver.get(self.live_server_url)
        self.assertIn("Django", self.driver.title)
```

## 4. Przykłady testów Selenium
### 4.1. Testowanie formularza logowania
```python
class LoginTest(StaticLiveServerTestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        service = Service('/path/to/chromedriver')
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_user_can_login(self):
        self.driver.get(f'{self.live_server_url}/login/')
        username_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")
        submit_button = self.driver.find_element(By.TAG_NAME, "button")
        
        username_input.send_keys("testuser")
        password_input.send_keys("password")
        submit_button.click()
        
        time.sleep(2)  # Czekanie na przekierowanie
        self.assertIn("Dashboard", self.driver.page_source)
```

### 4.2. Testowanie dodawania elementu na stronie
```python
class AddItemTest(StaticLiveServerTestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        service = Service('/path/to/chromedriver')
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_user_can_add_item(self):
        self.driver.get(f'{self.live_server_url}/items/')
        input_box = self.driver.find_element(By.NAME, "item_name")
        submit_button = self.driver.find_element(By.NAME, "submit")
        
        input_box.send_keys("Nowy przedmiot")
        submit_button.click()
        
        time.sleep(2)  # Czekanie na aktualizację strony
        self.assertIn("Nowy przedmiot", self.driver.page_source)
```

## 5. Debugowanie i najlepsze praktyki
- **Unikaj `time.sleep()`** – zamiast tego używaj `WebDriverWait` dla dynamicznych elementów.
- **Używaj selektorów CSS i XPath ostrożnie**, by uniknąć zależności od zmian w kodzie HTML.
- **Izoluj testy**, używając unikalnych danych testowych.
- **Włącz tryb bezgłowy**, jeśli nie potrzebujesz interakcji wizualnej:
  ```python
  from selenium.webdriver.chrome.options import Options
  
  options = Options()
  options.add_argument("--headless")
  driver = webdriver.Chrome(service=service, options=options)
  ```

## 6. Uruchamianie testów Selenium
Testy można uruchomić przy użyciu:
```sh
python manage.py test
```

Dla `pytest`:
```sh
pytest
```

## 7. Podsumowanie
- Selenium umożliwia testowanie interakcji użytkownika z aplikacją Django.
- `LiveServerTestCase` pozwala na testowanie aplikacji w warunkach przypominających rzeczywiste środowisko.
- Można testować logowanie, formularze, klikanie przycisków i inne akcje użytkownika.
- Używaj `WebDriverWait`, aby obsługiwać dynamiczne elementy strony.

Testowanie z Selenium jest nieocenione dla aplikacji opartej na interfejsie webowym, zapewniając niezawodność i stabilność systemu!

