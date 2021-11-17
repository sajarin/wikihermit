import scrape
import parse

def save_pages_from(text_file: str) -> None:
    with open(f'{text_file}', 'r', encoding="utf-8") as f:
        for coin in f: 
            scrape.save_page(coin)

def run_bot(): 
    save_pages_from('coin_list.txt')

    # filename = "data/2021/member.csv"
    # f = open(filename, "a+", encoding="utf-8")
    # for file in sorted(glob.glob('data/2021/saved_pages/*.html'), key=lambda x: int(x.split('\page')[1][:-5])):
    #     page_soup = parse.load_html(file)
    #     extracted_data = parse.parse_html(page_soup)
    #     f.write(extracted_data)

if __name__ == "__main__":
    run_bot()
