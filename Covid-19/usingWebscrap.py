#THIS FILE SCRAPES DATA DIRECTLY FROM WEB PAGE AND SHOWS THE NUMBERS ACC TO BELOW FORMAT

#test with these URLs-
# http://127.0.0.1:5000/discharged
#http://127.0.0.1:5000/active
#http://127.0.0.1:5000/deaths
#http://127.0.0.1:5000/vaccinated


#-------------------------------------------------------------------------


from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


url="https://www.mohfw.gov.in/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html5lib')

@app.route('/discharged', methods=['GET'])
def discharge():
    main_div=soup.find("div", {"id": "main-content"})
    upper_data=main_div.find('div',{"class":"site-stats-count"})
    inside_list=upper_data.find('li', attrs={'class': 'bg-green'})
    l=inside_list.find_all('span',{'class':"mob-show"})
    return jsonify({'discharged':l[-1].text})


@app.route('/active', methods=['GET'])
def active():
    main_div=soup.find("div", {"id": "main-content"})
    upper_data=main_div.find('div',{"class":"site-stats-count"})
    inside_list=upper_data.find('li', attrs={'class': 'bg-blue'})
    l=inside_list.find_all('span',{'class':"mob-show"})
    return jsonify({'active':l[-1].text})


@app.route('/deaths', methods=['GET'])
def deaths():
    main_div=soup.find("div", {"id": "main-content"})
    upper_data=main_div.find('div',{"class":"site-stats-count"})
    inside_list=upper_data.find('li', attrs={'class': 'bg-red'})
    l=inside_list.find_all('span',{'class':"mob-show"})
    return jsonify({'deaths':l[-1].text})


@app.route('/vaccinated', methods=['GET'])
def vaccinated():
    main_div=soup.find("div", {"id": "main-content"})
    upper_data=main_div.find('div',{"class":"sitetotal"})
    l=upper_data.find('div',{'class':"fullbol"})
    final=l.find('span',{'class':"coviddata"})
    return jsonify({'vaccinated':final.text})












if __name__ == '__main__':
   app.run(debug=True)