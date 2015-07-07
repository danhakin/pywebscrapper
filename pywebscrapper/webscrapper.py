from lxml import html
import requests

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.text)

buyers = tree.xpath('//div[@title="buyer-name"]/text()')
prices = tree.xpath('//span[@class="item-price"]/text()')
pages  = tree.xpath('//a/@href')

print 'Buyers: ', buyers
print 'Prices: ', prices
print 'Pages: ', pages
