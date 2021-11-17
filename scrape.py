import pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

def configure_page(base_url: str, search_query: str) -> WebDriver:
    driver = webdriver.Chrome()
    driver.get(base_url)
    assert "Page History" in driver.title
    search_box = driver.find_element(By.ID, 'article_input')
    search_box.clear()
    search_box.send_keys(search_query)
    submit_btn = driver.find_element(By.CLASS_NAME, 'form-submit')
    submit_btn.click()
    return driver.page_source

def save_page(coin_name: str) -> None:
    edits_url = 'https://xtools.wmflabs.org/articleinfo/en.wikipedia.org'
    edits_page_source = configure_page(edits_url, coin_name)
    pathlib.Path(f'data/{coin_name}/saved_pages/').mkdir(parents=True, exist_ok=True)
    with open(f'data/{coin_name}/saved_pages/edits.html', 'w', encoding="utf-8") as f:
        f.write(edits_page_source)