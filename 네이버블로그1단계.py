import requests
from bs4 import BeautifulSoup

search_keyword = "아이폰15"
url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}"

# Sending a GET request to the URL
response = requests.get(url)

# Parsing the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Finding all the blog elements
blog_elements = soup.find_all('li', class_='bx')

# Extracting information from each blog element
for blog in blog_elements:
    blog_address = blog.find('a', class_='api_txt_lines total_tit').get('href')
    blog_name = blog.find('a', class_='sub_txt sub_name').text
    post_title = blog.find('a', class_='api_txt_lines total_tit').text
    posting_date = blog.find('span', class_='sub_time').text

    print("Blog Address:", blog_address)
    print("Blog Name:", blog_name)
    print("Post Title:", post_title)
    print("Posting Date:", posting_date)
    print("\n")
