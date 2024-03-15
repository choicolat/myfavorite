import requests
response = requests.get('http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=pWs1QJmxlF1%2BTShg5OYKZuAm05y1%2BRWyGo%2BUvJ%2FujyYbGQQdTIsg%2BuqWR69DiPxweRwIIqCRS6nfuTkDuighNQ%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0')
response = response.json()
#구글링으로 관련 사이트 찾고 회원가입 후 활용신청
#리턴타입 json으로바꾸고 미리보기에서 url 복붙 후 s빼기. json은 "" 씀
import pprint #데이터가 더 이쁘게
pprint.pprint(response.json())

#a 시도별 실시간 측정정보 조회에서  확인 가능한 시도 이름을 전부 작성하시오.
#전국, 서울, 부산, 대구, 인천, 광주, 대전, 울산, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주, 세종
# print(data['response']['body']['items']['sidoName'])


#b 서울의 데이터에 대해, 초 미세먼지 농도가 낮은 stationName순으로 정렬
#print(data['pm25Value', ascending== False])
data= response.get('response').get('body').get('items')
#pprint(data[0]['pm25Value'])
sorted_data= sorted(data, key=lambda x : x.get('pm25Value'))
lst = [[datum.get('stationName'), datum.get('pm25Value')] for datum in sorted_data]
pprint(lst)
#c 서울의 데이터를 stationName으로 접근하기 쉬운 자료구조로 재구성하시오. 단 값이 None인 key는 제외하시오.
#'stationName' 

#d 종로구의 pm10Value, pm25Value의 1달치 데이터를 정리
#인사이트 요청
#print(data['response']['body']['items']['sidoName': '종로구'])
