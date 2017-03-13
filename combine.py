import lxml # parsing xml and html
import requests # to access http
import csv # to read from and write into csv file format 
import os # used to gather info about process and locaton
import re 
from lxml import html

URL = 'http://www.infoplease.com/t/hist/state-of-the-union/'
pagesource = requests.get(URL)
tree = html.fromstring(pagesource.content)
sub_links = tree.xpath('//span/a/@href')

i = 1

for link in range(len(sub_links)-1):
	address = URL+sub_links[link]
	source = requests.get(address)
	tree = html.fromstring(source.content)
	var1 = tree.xpath('//div[@class = "titlepage"]/div/div/h2/text()')
	var1=''.join(j for j in var1)
	Name = re.sub(r'\s*\(.*\)\s*',r'',var1) # regex used to replace special characters
	Year = re.search('\\((.*?)\\)',var1)    # regex used to extract data inside special characters 
	if Year: 
		fetch=Year.group(1)
		Year=fetch.replace(",","") # replace , by NULL
		Year=Year.replace(" ","-")
	content = tree.xpath('//div[@class = "article"]/p/text()') # xpath to extract values from html data
	content = [k.replace('\n','') for k in content] # to replace the \n values with NULL
	var2 = ''.join(a for a in content) # converting the content into string
	temp = ""
	temp=sub_links[link].split('.')[0]
	location = 'C:\\Users\\Sri Vishnu theja\\Parse\\'+temp+'.txt'
	path=os.path.join(location) # used to append the location 
	txt=open(path, 'w') # writing to a text file
	txt.write(var2)
	txt.close # closing the text file
	
	headers = ['Name of the president', 'Date of the union address', 'Link to Address', 'Filename_AddressText'] # headers used to represent header fields for CSV
	var3 = csv.DictWriter(open('Data.csv', 'a'), lineterminator='\n', fieldnames=headers) # append to CSV
	
	if i==1:
		var3.writeheader() # To write header fields only once
		i = i-1
	var3.writerow({'Name of the president': Name, 'Date of the union address': Year, 'Link to Address': address, 'Filename_AddressText': path})
	# writing the contents to CSV file


filepath = 'C:\\Users\\Sri Vishnu theja\\Parse\\file.txt'
filepath=os.path.join(filepath)
txt=open(filepath, 'w') # to write to the file all the President Names, Year and their Speech
nl = "\n"

for links in range(len(sub_links)-1):
	address = URL+sub_links[links]
	source = requests.get(address)
	tree = html.fromstring(source.content)
	var1 = tree.xpath('//div[@class = "titlepage"]/div/div/h2/text()')
	var1=''.join(j for j in var1)
	Name = re.sub(r'\s*\(.*\)\s*',r'',var1)
	Year = re.search('\\((.*?)\\)',var1)
	if Year: 
		fetch=Year.group(1)
		Year=fetch.replace(",","")
	content = tree.xpath('//div[@class = "article"]/p/text()')
	content = [k.replace('\n','') for k in content]
	var2 = ''.join(a for a in content)
	txt.write(Name)
	txt.writelines(nl)
	txt.write(Year)
	txt.writelines(nl)
	txt.write(var2)
	txt.writelines(nl)
txt.close


