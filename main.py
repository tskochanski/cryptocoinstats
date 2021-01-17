# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import bs4
from bs4 import BeautifulSoup
import requests



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
r = requests.get('https://www.usclimatedata.com/climate/united-states/us')
soup = BeautifulSoup(requests.text)
print(soup.title)
print(soup.title.string)





html = "";
parsed_html = bs4.BeautifulSoup(html, "html.parser")
print(len(r.text))
text_found = parsed_html.findAll("div", attrs={"class": "classname"}).text
print(text_found)

