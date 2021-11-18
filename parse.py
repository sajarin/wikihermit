from bs4 import BeautifulSoup

def load_html(file_path: str) -> BeautifulSoup:
    try: 
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_html = f.read()
            soup = BeautifulSoup(raw_html, 'lxml')
            return soup
    except OSError as err:
        print("OSError: {0}".format(err))

def parse_html(page_soup: BeautifulSoup) -> str:
    data_tables = page_soup.find_all('table', {"class": "table"})
    data_tables = [data_tables[0], data_tables[1], data_tables[2], data_tables[3]]

    general_stats = data_tables[0].find_all('td')
    page_size = general_stats[5].text.strip()
    total_edits = general_stats[7].text.strip()
    num_of_editors = general_stats[9].text.strip()

    edit_stats = data_tables[2].find_all('td')
    avg_time_between_edits = edit_stats[2].text.strip()
    avg_edits_per_user = edit_stats[4].text.strip()
    avg_edits_per_day = edit_stats[6].text.strip()
    avg_edits_per_month = edit_stats[8].text.strip()
    avg_edits_per_year = edit_stats[10].text.strip()
    edits_in_last_24_hours = edit_stats[12].text.strip()
    edits_in_last_30_days = edit_stats[14].text.strip()
    edits_in_last_30_days = edit_stats[16].text.strip()
    edits_in_last_year = edit_stats[18].text.strip()

    link_stats = data_tables[3].find_all('td')
    links_to_this_page = link_stats[2].a.text.strip()

    extracted_data = "" + (
        page_size.replace(",", "") + ',' + total_edits.replace(",", "") + ',' + 
        num_of_editors.replace(",", "") + ',' + avg_time_between_edits.replace(",", "") + ',' +
        avg_edits_per_user.replace(",", "") + ',' + avg_edits_per_day.replace(",", "") + ',' +
        avg_edits_per_month.replace(",", "") + ',' + avg_edits_per_year.replace(",", "") + ',' +
        edits_in_last_24_hours.replace(",", "") + ',' + edits_in_last_30_days.replace(",", "") + ',' +
        edits_in_last_year.replace(",", "") + ',' + links_to_this_page.replace(",", "") + ',' + '\n'
    )

    return extracted_data