import bs4 #Beautiful soup for web scraping
import urllib.request #package to direct mails
import smtplib #library to send mail via smtp
import time #frequency of checking the product price  


prices_list=[] #list of updated prices for the given time

def check_price():
    url = 'https://www.amazon.in/theproduct' #Paste the Product URL here
    sauce= urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(sauce,"html.parser")
    prices = soup.find(id="priceblock_ourprice").get_text()
    prices = float(prices.replace(",","").replace("₹",""))
    prices_list.append(prices)
    return prices

def send_email(message):
    s= smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("frommailaddress","frompassword") #TYPE THEM!
    s.sendmail("frommailaddress","tomailaddress",message) #TYPE THEM!
    s.quit()
send_email("HELLO")    #SENDER MESSAGE


def price_decrease_check(price_list):
    if prices_list[-1] < prices_list[-2]: #checks whether the recent price in the list is lesser 
        return True
    else:
        return False    

count = 1 
while True:
    current_price = check_price()
    if count > 1: #index constraint? Checks only if the list has two updated prices
        flag = price_decrease_check(prices_list)
        if flag:
            decrease= prices_list[-1] - prices_list[-2]
            message= "PRICE DECREASED CHECK! . The price decreased by {decrease} rupees.Check https://www.amazon.in/Samsung-Galaxy-Ocean-128GB-Storage/dp/B07HGGYWL6/ref=sr_1_1?dchild=1&keywords=poco+x2&qid=1598001158&sr=8-1"
            send_email(message)
    time.sleep(43000)
    count += 1        