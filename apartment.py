import requests
import xmltodict
import json

def apt_danji(sido):
    url = 'http://apis.data.go.kr/1613000/AptListService2/getSidoAptList'

    param ={'serviceKey' : service_dkey, 'sidoCode' : sido, 'pageNo' : 1, 'numOfRows' : '1' }
    r = requests.get(url, params=param)

    xmlData = r.content.decode('utf-8')
    parseData = xmltodict.parse(xmlData)
    jData = json.loads(json.dumps(parseData))
    # print(jData)
    rows = jData['response']['body']['totalCount']
    print(f'단지 코드수 : {int(rows):,} 개')

    pages = int(int(rows)/100) + 1
    print(f'pages: {pages}')

    row_cnt = 1
    for i in range(1, pages + 1):
        params ={'serviceKey' : service_dkey, 'sidoCode' : sido, 'pageNo' : i, 'numOfRows' : '100' }

        response = requests.get(url, params=params)
        # print(response.content)  # ascii

        xml_data = response.content.decode('utf-8')
        # print(xml_data)

        parse_data = xmltodict.parse(xml_data)
        # print(parse_data)

        ord_data = parse_data['response']['body']['items']['item']
        print(ord_data)
        print(f'page: {i} End\n{"=" * 50}')

        try:
            ## json() 활용하여 데이터 변환 
            jdata = json.loads(json.dumps(ord_data))
            
            for code_data in jdata:
                print(f'row_cnt: {row_cnt}\n{code_data}\n')
                row_cnt += 1

        except Exception as e:
            print(f'Error: {e}\n')
            break

sido_code = 50
apt_danji(sido_code)