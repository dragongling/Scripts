from bs4 import BeautifulSoup
import requests
import urllib.request
import os


def download_images(source_tag, out_path):
    for image_tag in source_tag.find_all("img"):
        image_name = image_tag["src"].split("/")[-1]
        if not os.path.exists(os.getcwd() + out_path + image_name):
            print("Downloading \"" + image_name + "\"...", end='')
            urllib.request.urlretrieve(hostname + image_tag['src'], os.getcwd() + out_path + image_name)
            print("Completed!")
        else:
            print("File \"" + image_name + "\" is already downloaded")
        image_tag['src'] = '.' + out_path + image_name


def download_scripts(source_tag):
    for script_tag in source_tag.find_all("script"):
        if 'src' in script_tag.attrs:
            filename = script_tag.attrs["src"].split("/")[-1]
            if not os.path.exists(os.getcwd() + filename):
                print("Downloading \"" + filename + "\"...", end='')
                urllib.request.urlretrieve(hostname + script_tag.attrs['src'], os.getcwd() + '\\' + filename)
                print("Completed!")
            else:
                print("File \"" + filename + "\" is already downloaded")
            script_tag.attrs['src'] = filename

hostname = 'http://startandroid.ru'
lesson_url = "/ru/uroki/vse-uroki-spiskom/168-urok-103-multitouch-obrabotka-mnozhestvennyh-kasanij.html"
page = requests.get(hostname + lesson_url)
soup = BeautifulSoup(page.content, 'html.parser')
article = BeautifulSoup(str(soup.find('article')), 'html.parser')
redundant = []
redundant += article.select('article section div')
redundant += article.select('article hr')
redundant += article.select('article ul')
redundant += article.find(class_="article-info-term")
# scripts = soup.find_all('script')
# for script in scripts:
    # if 'src' in script.attrs:
    #     script_names = script.attrs['src'].split("/")[-1]
    #     for script_name in script_names.split('+'):
    #         if script_name[0:7] != 'shBrush':
    #             script.extract()
    # else:
    # script.extract()
redundant += soup.find_all('script')
for element in redundant:
    element.extract()
download_images(article, '/images/')
lesson_html = open("lesson.html", "bw+")
head = soup.find('head')
head_scripts = """
"""
html_head = """<!DOCTYPE html>
<html lang="ru-ru" dir="ltr" class='com_content view-article itemid-110 j36 mm-hover '>""" + str(head) + str(head_scripts) + \
            """<body>
            <div id="t3-content" class="t3-content col-xs-12 col-sm-8 col-sm-push-4 col-md-9 col-md-push-3">
            """
html_tail = """
</div>
</body>
</html>"""
lesson_html.write(str(html_head + str(article) + html_tail).encode('utf-8'))
lesson_html.close()