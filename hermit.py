import scrape
import parse

def save_pages_from(text_file: str) -> None:
    with open(f'{text_file}', 'r', encoding="utf-8") as f:
        for coin in f: 
            print(coin.rstrip())
            scrape.save_page(coin.rstrip())
    return
def run_bot(): 
    # save_pages_from('coin_list.txt')
    with open('coin_list.txt', 'r', encoding="utf-8") as coin_list:
        for coin in coin_list:
            coin = coin.rstrip()
            output_filename = f'data/{coin}/data.csv'
            output_file = open(output_filename, "a+", encoding="utf-8")
            file_to_parse = f'data/{coin}/saved_pages/edits.html'
            page_soup = parse.load_html(file_to_parse)
            print(coin.upper())
            extracted_data = parse.parse_html(page_soup)
            output_file.write(extracted_data)

if __name__ == "__main__":
    run_bot()
