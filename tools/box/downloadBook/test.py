import sys
sys.path.append('/home/ubuntu/Python_Workspace/SJTB/')
from tools.box.downloadBook.spyder import aszwParser
from tools.box.downloadBook.db import dbController

def testInsertBook():
    chapters=[{'chapter_name':'第一章','chapter_url':'https://www.23zw.me/olread/68/68913/c10f9c35044ae520694a837c12ecf81e.html'},
              {'chapter_name':'第二章','chapter_url':'https://www.23zw.me/olread/68/68913/6e872de41acaf237553a93d84b7d4edb.html'}]
    book={}
    book['name']="第一本书"
    book['category']='默认'
    book['auth']='张杰'
    book['create_date']=''
    book['wordage']=660000
    book['book_url']='http://www.23zw.me/olread/68/68913/'
    book['chapters']=chapters

    dbC= dbController.dbc('bookwarehouse')
    dbC.insetBook(book)

def testfind_section_urls():
    url='https://www.23zw.me/olread/79/79709/index.html'
    parser= aszwParser.aszwParser()
    parser.find_section_urls(url)

def testInitDatabase():
    dbC= dbController.dbc('bookwarehouse')
    dbC.initDatebase()

def testAddAccount():
    dbC=dbController.dbc('bookwarehouse')
    dbC.addAccount({'name':'sujie1997','password':'sujie1997','source':1})

def testInitCookies():
    dbC = dbController.dbc('bookwarehouse')
    dbC.initCookies()

def testGetCookies():
    dbC = dbController.dbc('bookwarehouse')
    for cookie in dbC.getCookies():
        print(cookie)


if __name__ == '__main__':
    # testInsertBook()
    # testfind_section_urls()
    testInitDatabase()
    # testAddAccount()
    # testInitCookies()
    # testGetCookies()
