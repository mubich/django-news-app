from django.shortcuts import render, HttpResponse

key = "e3ff963e63e240c1a272186b528d7e49"; # newsapi.org API key
import bs4
import requests
import json

try:
	dt_req = requests.get('https://dailytimes.com.pk', verify = False)
except:
	print("request dailytimes failed")

soup = bs4.BeautifulSoup(dt_req.content, 'html.parser')
hero_entry = soup.find('article', class_="entry hero-entry")
req_h_url = hero_entry.a['href']
req_hero = requests.get(req_h_url)
soup_h = bs4.BeautifulSoup(req_hero.content, 'html.parser')


main_news_title = soup_h.find('h1', class_ = 'entry-title').text
main_news_des = soup_h.find('div', class_ = 'site-inner')
main_pic_src = main_news_des.img['data-lazy-src'] 


pak_dt_main = main_news_des.findAll('p')
pak_p = []
for p in pak_dt_main:
	pak_p.append(p.text)
pak_p = pak_p[:-8]

base_url = "http://newsapi.org/v2/top-headlines?country=us&category=sports&apikey=";

url_req = base_url + key;
req = requests.get(url_req)

json_content = json.loads(req.content)

articles = json_content['articles']


# source_name, author, title, description, url, urlToImage, publishedAt, content = [], [], [], [], [], [], [], []
# for article in articles:
# 	source_name += article['source']['name']
# 	author += article['author']
# 	title += article['title']
# 	description += article['description']
# 	url += article['url']
# 	urlToImage += article['urlToImage']
# 	publishedAt += article['publishedAt']
# 	content += article['content']




# Create your views here.
def index(request):

	# data = {'source_name': source_name,'author': author,'title': title,'description': description,'url': url,'urlToImage': urlToImage,'publishedAt': publishedAt,'content': content}
	return render(request, 'NewsAgg/index.html',
		{
			'main_news_title' : main_news_title,
			'pak_p': pak_p,
			'main_pic_src' : main_pic_src

		})
def sports(request):
	return render(request, 'NewsAgg/sports.html',
	{
		'articles': articles
	})

"""TheNews part"""
try:
	tn_req = requests.get("https://www.thenews.com.pk/", verify = False)
except:
	print("request to thenews failed.")

tn_soup = bs4.BeautifulSoup(tn_req.content, 'html.parser')

main_story_left = tn_soup.find('div', class_ = "main_story_left")

url_main = main_story_left.a['href']

try:
	main_req = requests.get(url_main, verify = False)
except:
	print("request to thenews main-page failed.")

main_req = bs4.BeautifulSoup(main_req.content, 'html.parser')

dc = main_req.find('div', class_ = 'detail-center')

tn_h1 = dc.h1.text

tn_story_detail = dc.find('div', class_ = 'story-detail')

tn_sd_img_src = tn_story_detail.img['src'];

tn_p = tn_story_detail.find_all('p');
tn_pt = []
for p in tn_p:
	tn_pt.append(p.text)
#tn_pt = tn_pt[4:-1]
def the_news(request):
	return render(request, 'NewsAgg/the_news.html', {
		'tn_h1' : tn_h1,
		'tn_sd_img_src' : tn_sd_img_src,
		'tn_p' : tn_pt 
		})
