from flask import Flask, render_template, request
import random
import requests
import json
from faker import Faker
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
# @app.route('/lotto')
# def lotto():
#     #코드입력부분
#     url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
#     res = requests.get(url).text
#     lotto_dict = json.loads(res)
    
#     print(lotto_dict["drwNoDate"])
    
#     week_num = []
#     week_format_num = []
    
#     drwtNo = ["drwtNo1","drwtNo2","drwtNo3","drwtNo4","drwtNo5","drwtNo6"]
#     for num in drwtNo:
#         number = lotto_dict[num]
#         week_num.append(number)
#         print(week_num)
    
    
#     for i in range(1, 7):
#         num = lotto_dict["drwtNo{}".format(i)]
#         week_format_num.append(num)

    
#     # pick = 우리가 생성한 번호
#     # week_num = 이번주 당첨번호
#     #### 위의 두 값을 비교해서 로또 당첨 등수 출력!!
#     # sorted()
#     # 1등 : 6개의 숫자를 다 맞출 때
#     # 2등 : 5개 + 보너스
#     # 3등 : 5개
#     # 4등 : 4개
#     # 5등 : 3개
#     # 꽝
    
#     # 보너스번호
#     bonus = lotto_dict["bnusNo"]
    
    
#     # print(type(res))
#     # print(type(json.loads(res)))
    
#     num_list = range(1, 46)
#     pick = random.sample(num_list, 6)
#     pick = [2, 25, 28, 30, 33, 9]
#     pick.sort()
#     week_num.sort()
#     week_format_num.sort()
    
#     q = 0
#     for k in range(6):
#         for a in range(6):
#             if pick[k]==week_num[a]:
#                 q=q+1
    
#     #보너스번호 맞추기
#     two = 0
#     for k in range(6):
#         if pick[k]==bonus:
#             two = two+1
    
#     #등수 구하기
    
#     if q==6:
#         rank="1등"
#     elif q==5 and two==1:
#         rank="2등"
#     elif q==5: 
#         rank="3등"
#     elif q==4:
#         rank="4등"
#     elif q==3:
#         rank="5등"
#     else:
#         rank="꽝"
    
        
    
#     return render_template("lotto.html", lotto=pick, week_num=week_num, week_format_num=week_format_num, bonus=bonus, rank=rank)
    
    
@app.route('/lottery')
def lottery():
    # 로또 정보를 가져온다
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
    res = requests.get(url).text
    lotto_dict = json.loads(res)
    
    # 1등 당첨 번호를 week 리스트에 넣는다.
    week = []
    for i in range(1,7):
        num = lotto_dict["drwtNo{}".format(i)]
        week.append(num)
    
    # 보너스 번호를 bonus 변수에 넣는다.
    bonus = lotto_dict["bnusNo"]
    
    # 임의의 로또 번호를 생성한다.
    pick = random.sample(range(1,46),6)
    pick = [2, 25, 28, 30, 33, 6]
    # 비교해서 몇등인지 저장한다.
    match = len(set(pick) & set(week))
    
    if match==6:
        text = "1등"
    elif match==5:
        if bonus in pick:
            text = "2등"
        else:
            text = "3등"
    elif match==4:
        text = "4등"
    else:
        text = "꽝"
    
    # 사용자에게 데이터를 넘겨준다.
    
    return render_template("lottery.html",pick=pick, week=week,text=text)

@app.route('/ping')
def ping():
    return render_template("ping.html")
    
@app.route('/pong')
def pong():
    input_name = request.args.get('name')
    fake = Faker('ko_KR')
    fake_job = fake.job()
    return render_template("pong.html", html_name=input_name, fake_job=fake_job)



@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/out')
def out():
    input_name = request.args.get('name')
    fake = Faker('ko_KR')
    fake_job = fake.address()
    return render_template("out.html", html_name=input_name, fake_job=fake_job) 


    