from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import string
import pandas as pd

def config():
	"start the necessary moduls"
	global b
	global c
	"start Firefox browsers"
	b = webdriver.Firefox()
	c = webdriver.Firefox()
	global df
	"load excel list in dataframe"
	df = load_excel('/Users/markmurtagh/todayiinvest/iinvest/homepage/Add.xlsx')



def get_link_investingcom():
	"script to get links from investing.com. ISIN numbers are read from a excel list and add into the search box. The best result is then selected"
	for i in range(0,len(df.index)):
		try:
			b.get('https://www.investing.com/')
			element = b.find_element_by_css_selector('.searchText')
			key = df['ISIN'][i]
			element.send_keys(key)
			element.send_keys(Keys.RETURN)
			time.sleep(1)
			element = b.find_element_by_css_selector('a.js-inner-all-results-quote-item:nth-child(1)')
			df.loc[df.index==i,'Investingcom_link'] = element.get_attribute('href')
			df.to_excel('/Users/markmurtagh/todayiinvest/iinvest/homepage/Add.xlsx')
			time.sleep(1)
		except Exception as e:
			print(e)


def aktie(link):
    for i, row in df.iterrows():
        ISIN= row[27]
        link = row[0]
        currency = row[1]
        price = row[2]
        markCap = row[3]
        divCap = row[4]
        divCapZero = row[5]
        divCapOne = row[6]
        divCapTwo = row[7]
        divCapThird = row[8]
        divCapFour = row[9]
        divCapFive = row[10]
        divCapSix = row[11]
        resCap = row[12]
        ownZero = row[13]
        ownOne = row[14]
        ownTwo = row[15]
        ownThree = row[16]
        ownFour = row[17]
        ownFive = row[18]
        ownSix = row[19]
        forCap = row[20]
        forZero = row[21]
        forOne = row[22]
        forThree = row[23]
        forFour = row[24]
        forFive = row[25]
        forSix = row[26]
        views.make_typetwo_entry(ISIN,link,currency,price,markCap,divCap,divCapZero,divCapOne,divCapTwo,divCapThird,divCapFour,divCapFive,divCapSix,resCap,ownZero,ownOne,ownTwo,ownThree,ownFour,ownFive,ownSix,forCap,forZero,forOne,forThree,forFour,forFive,forSix,revOne,revTwo,revThree,revFour,revFive,revSix)

	for i in range(0,len(df.index)):
		b.get(df[link][i])
		c.get(df[link][i])
		try:
			c.find_element_by_css_selector('.om-trigger-close').click()
		    #clickt app fenster weg
		except Exception as e:
			pass
		try:
			c.find_element_by_css_selector('#infoBoxTable > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(4) > a:nth-child(1)').click()
		except Exception as e:
			pass

		################################finanzen.net#################################################
		scraped('.instrument-id', i, data = 'ISIN')
		scraped('div.quotebox:nth-child(1) > div:nth-child(1)', i, data = 'curprice')
		scraped('#ShareQuotes_1 > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(5) > td:nth-child(2)', i, data = 'market')
		scraped(' ', i, data = 'REV')
		scraped(' ', i, data = 'EPS')
		scraped(' ', i, data = 'DIV')
		scraped(' ', i, data = 'RES')
		scraped(' ', i, data = 'OWN')
		scraped(' ', i, data = 'FOREIGN')

		################################Investing.com#################################################

		#scraped(' ', i, data = 'CURASSET')
		#scraped(' ', i, data = 'CURLIAB')
		#scraped(' ', i, data = 'CURTOTASSET')
		#scraped(' ', i, data = 'CURTOTLIAB')
		#scraped(' ', i, data = 'INVDATE')
		#scraped(' ', i, data = 'CURREDEARN')
		#scraped(' ', i, data = 'GOODWILL')
		#scraped(' ', i, data = 'INTANGE')

		# df.to_excel('/Users/markmurtagh/todayiinvest/iinvest/homepage/output.xlsx')
		#time.sleep(5)
        return



def load_excel(data):
	"Method to load excel data and store it to Dataframe"
	df = pd.read_excel(data)
	return df


def scraped(css, pos, **kwargs):
	try:

		##########################################################finanzen.net###################################################################################
		if kwargs['data'] == 'ISIN':
			syear = c.find_element_by_css_selector('div.table-quotes:nth-child(1) > div:nth-child(3) > table:nth-child(1) > thead:nth-child(2) > tr:nth-child(1) > th:nth-child(3)').text
			text = b.find_element_by_css_selector(css).text.split()
			print(text)
			for i in range(len(text)):
				if 'ISIN' in text[i]:
					isin = text[i+1]
					df.loc[df.index==pos,'ISIN'] = isin


		elif kwargs['data'] == 'curprice':
			text = b.find_element_by_css_selector(css).text
			price = text[0:len(text)-3]
			cur = text[len(text)-3:len(text)]
			df.loc[df.index==pos,'Currency'] = cur
			df.loc[df.index==pos,'Price'] = price

		elif kwargs['data'] == 'market':
			text = b.find_element_by_css_selector(css).text
			df.loc[df.index==pos,'Market cap'] = text

		elif kwargs['data'] == 'REV':
			for i in range(7):
				css = 'div.box:nth-child(5) > div:nth-child(3) > table:nth-child(1) > tbody:nth-child(3) > tr:nth-child(1) > td:nth-child(' + str(i+3) + ')'
				text = c.find_element_by_css_selector(css).text
				df.loc[df.index==pos,'REV' + str(i)] = text
			caption = c.find_element_by_css_selector('div.box:nth-child(3) > h2:nth-child(1)').text
			caption = caption.split('(')
			caption = caption[1].replace(')','')
			df.loc[df.index==pos,'REV Cap'] = caption


		elif kwargs['data'] == 'EPS':
			for i in range(7):
				css = 'div.table-quotes:nth-child(1) > div:nth-child(3) > table:nth-child(1) > tbody:nth-child(3) > tr:nth-child(2) > td:nth-child(' + str(i+3) + ')'
				text = c.find_element_by_css_selector(css).text
				caption = c.find_element_by_css_selector('div.box:nth-child(9) > h2:nth-child(1)').text
				#Vorsicht manchmal geht caption nicht
				caption = caption.split('(')
				caption = caption[1].replace(')','')
				df.loc[df.index==pos,'EPS Cap'] = caption
				df.loc[df.index==pos,'EPS' + str(i)] = text

		elif kwargs['data'] == 'DIV':
			for i in range(7):
				css = 'div.box:nth-child(9) > div:nth-child(3) > table:nth-child(1) > tbody:nth-child(3) > tr:nth-child(5) > td:nth-child(' + str(i+3) + ')'
				text = c.find_element_by_css_selector(css).text
				caption = c.find_element_by_css_selector('div.box:nth-child(9) > h2:nth-child(1)').text
				caption = caption.split('(')
				caption = caption[1].replace(')','')
				df.loc[df.index==pos,'DIV Cap'] = caption
				df.loc[df.index==pos,'DIV' + str(i)] = text

		elif kwargs['data'] == 'RES':
			for i in range(7):
				css = 'div.box:nth-child(5) > div:nth-child(3) > table:nth-child(1) > tbody:nth-child(3) > tr:nth-child(9) > td:nth-child(' + str(i+3) + ')'
				text = c.find_element_by_css_selector(css).text
				caption = c.find_element_by_css_selector('div.box:nth-child(5) > h2:nth-child(1)').text
				caption = caption.split('(')
				caption = caption[1].replace(')','')
				df.loc[df.index==pos,'RES Cap'] = caption
				df.loc[df.index==pos,'RES' + str(i)] = text

		elif kwargs['data'] == 'OWN':
			for i in range(7):
				css = 'div.box:nth-child(7) > div:nth-child(3) > table:nth-child(1) > tbody:nth-child(3) > tr:nth-child(3) > td:nth-child(' + str(i+3) + ')'
				text = c.find_element_by_css_selector(css).text
				caption = c.find_element_by_css_selector('div.box:nth-child(7) > h2:nth-child(1)').text
				caption = caption.split('(')
				caption = caption[1].replace(')','')
				df.loc[df.index==pos,'OWN Cap'] = caption
				df.loc[df.index==pos,'OWN' + str(i)] = text

		elif kwargs['data'] == 'FOREIGN':
			for i in range(7):
				css = 'div.box:nth-child(7) > div:nth-child(3) > table:nth-child(1) > tbody:nth-child(3) > tr:nth-child(1) > td:nth-child(' + str(i+3) + ')'
				text = c.find_element_by_css_selector(css).text
				caption = c.find_element_by_css_selector('div.box:nth-child(7) > h2:nth-child(1)').text
				caption = caption.split('(')
				caption = caption[1].replace(')','')
				df.loc[df.index==pos,'FOREIGN Cap'] = caption
				df.loc[df.index==pos,'FOREIGN' + str(i)] = text

				#########################################Investing.com##############################
		if kwargs['data'] == 'INVDATE':
			text = b.find_element_by_css_selector('#header_row > th:nth-child(2) > span:nth-child(1)').text + b.find_element_by_css_selector('#header_row > th:nth-child(2) > div:nth-child(2)').text
			df.loc[df.index==pos,'INVDATE'] = text

		if kwargs['data'] == 'CURASSET':
			text = b.find_element_by_css_selector('tr.openTr:nth-child(1) > td:nth-child(2)').text
			df.loc[df.index==pos,'CURASSET'] = text

		if kwargs['data'] == 'CURLIAB':
			text = b.find_element_by_css_selector('tr.openTr:nth-child(5) > td:nth-child(2)').text
			df.loc[df.index==pos,'CURLIAB'] = text

		if kwargs['data'] == 'CURTOTASSET':
			text = b.find_element_by_css_selector('tr.openTr:nth-child(3) > td:nth-child(2)').text
			df.loc[df.index==pos,'CURTOTASSET'] = text

		if kwargs['data'] == 'CURTOTLIAB':
			text = b.find_element_by_css_selector('tr.openTr:nth-child(7) > td:nth-child(2)').text
			df.loc[df.index==pos,'CURTOTLIAB'] = text

		if kwargs['data'] == 'CURREDEARN':
			text = b.find_element_by_css_selector('tr.noHover:nth-child(10) > td:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(2)').text
			df.loc[df.index==pos,'CURTOTLIAB'] = text

		if kwargs['data'] == 'GOODWILL':
			text = b.find_element_by_css_selector('tr.noHover:nth-child(4) > td:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2)').text
			df.loc[df.index==pos,'GOODWILL'] = text

		if kwargs['data'] == 'INTANGE':
			text = b.find_element_by_css_selector('tr.noHover:nth-child(4) > td:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(2)').text
			df.loc[df.index==pos,'INTANGE'] = text

	except Exception as e:
		print(e)

config()
#get_link_investingcom()
aktie('link')
