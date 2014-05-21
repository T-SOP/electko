#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import urllib
from lxml import etree as ET
import collections
import re


def newsInfo():
    infos = []
    electionCode = [{3: "시도지사선거"}, {4: "구시군의장선거"},{5:"시도의회의원선거"},{6: "구시군의회의원선거"},{10: "교육의원선거"},{11 : "교육감선거"}];
    cityCode = [{1100: "서울특별시"},{2600: "부산광역시"},{2700: "대구광역시"},{2800: "인천광역시"},{2900: "광주광역시"}
                ,{3000: "대전광역시"},{3100: "울산광역시"},{5100: "세종특별자치시"},{4100: "경기도"},{4200: "강원도"}
                ,{4300: "충청북도"},{4400: "충청남도"},{4500: "전라북도"},{4600: "전라남도"},{4700: "경상북도"}
                ,{4800: "경상남도"},{4900: "제주특별자치도"}];
    url = 'http://info.nec.go.kr/electioninfo/electionInfo_report.xhtml?'
    url += 'electionId=0020140604&requestURI=%2Felectioninfo%2F0020140604%2Fpc%2Fpcri03_ex.jsp&statementId=PCRI03_%2311&electionCode=3&cityCode=1100'
    
    data = {}
    data = urllib.urlencode(data)
    req = urllib2.Request(url,data)
    print req
    response = urllib2.urlopen(req)
    xml =  response.read()#.decode('cp949', 'ignore').encode('utf-8')
    parser = ET.HTMLParser()
    html =  ET.fromstring(xml,parser = parser)
#   print html
    head = html.findall(".//table[@id='table01']/thead/tr/th")
    print len(head)
    heads = [];
    for h in head:              # setting head
        heads.append(h.text)
        
    result = []   
    items = html.findall(".//table[@id='table01']/tbody/tr")
    print len(items)
    for item in items:
        td = item.findall("td")
        v = {}
        for i in td:
            v[heads[td.index(i)]] =  ET.tostring(i,method="text",encoding="utf-8").strip()
            #i.text.strip()
#            print ET.tostring(i,method="text",encoding="utf-8").strip()
            img = i.find("img")
            if img is not None:
                imglink = "http://info.nec.go.kr" + img.attrib['src']
                v[heads[td.index(i)]] = imglink
        result.append(v)
    for r in result:
        for keys,values in r.items():
            print "%s = %s" % (keys,values.decode('utf-8'))
        print ""

if __name__ == "__main__":
    newsInfo()
