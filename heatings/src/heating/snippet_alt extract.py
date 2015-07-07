
down vote
accepted
	

Here is an example from the Scrapy Shell:

$ scrapy shell index.html
In [1]: for cell in response.xpath("//div[@class='sth1']/table/tr/td"):
   ...:     href = cell.xpath("a/@href").extract()   
   ...:     alt = cell.xpath("a/img/@alt").extract()
   ...:     print href, alt

[u'link1'] [u'alt1']
[u'link1'] []
[u'link2'] [u'alt2']
[u'link2'] []

