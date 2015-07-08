from lxml import html
import requests

start_url = 'http://econpy.pythonanywhere.com/ex/001.html'


def get_page_content(url):
	page = requests.get(url)
	return html.fromstring(page.text)

def extract_data(content):
	return (
		content.xpath('//div[@title="buyer-name"]/text()'),
		content.xpath('//span[@class="item-price"]/text()')
	)

def get_pages():
	return tree.xpath('//a/@href')

tree = get_page_content(start_url)
buyers , prices = extract_data(tree)
pages = get_pages()

for url in pages:
	print "Extracting data from ", url
	tree = get_page_content(url)
	data = extract_data(tree)
	buyers += data[0]
	prices += data[1]


print 'Buyers: ', buyers
print 'Prices: ', prices
print 'Pages: ', pages

print 'Total Buyers: ', len(buyers)
print 'Total Prices: ', len(prices)
print 'Total Pages:  ', len(pages)
