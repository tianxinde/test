import random
# choose=['石头','剪刀','布']
# rule={
#     '0':'开始游戏',
#     '1':'石头',
#     '2':'剪刀',
#     '3':'布',
#     '4':'退出',
#     'win' :['1剪刀','2布','3石头'],
#     'lose':['1布','2石头','3剪刀'],
#     'ping':['1石头','2剪刀','3布']
# }
# print('')
# hum=input("请选择")
# comptuer=random.choice(choose)
# print(comptuer)
# hum_comptuer=hum+comptuer
# if hum_comptuer in rule.get('win'):
#     print('win')
# elif hum_comptuer in rule.get('lose'):
#     print('lose')
# elif hum_comptuer in rule.get('ping'):
#     print('ping')

# def view():
#     print()
#
#      hum=input("")
#      if hum == '0':
#
#      elif hum == '4':
#          break
#      else:

#
# def zhuche():
#     name=input("name")
#     age=input("age")
#     high=input("high")
#     info={
#         'name':None,
#         'age':None,
#         'high':None,
#     }
#     info['name']= name
#     info['age']= age
#     info['high']= high
#     return info
# i=0
# list=[]
# while i<5:
#     info_zhuche=zhuche()
#     list.append(info_zhuche)
#     print(list)
#     print(info_zhuche)
#     i +=1

def game():
     win=0
     lose=0
     ping=0
     while True:
        print("win:{} lose:{} ping:{}".format(win,lose,ping))
        # print("")
        print("请选择：1石头 2剪刀 3布 4退出")
     # print('''
     # 请选择：
     #        1 石头
     #        2 剪刀
     #        3 布
     #        4 退出
     # ''')
     # # win=0
     # lose=0
     # ping=0
        hum=input("你选择")
        if hum == '1' or hum =='2'  or hum =='3':
            comptuer=random.choice(choose)
            print("电脑选择：%s" %comptuer)
            hum_comptuer=hum+comptuer
        #i=0
        # win=0
        # lose=0
        # ping=0
            if hum_comptuer in rule.get('win'):
            #i +=1
            #win=i
                win +=1
                print('你赢了')
                print("win %d " %win)
            # print('''
            # win %d
            # lose %d
            # ping %d
            # '''%win%lose%ping)
            # return win
            elif hum_comptuer in rule.get('lose'):
            # i +=1
            # lose=i
                lose +=1
                print('你输了')
                print("lose %d" %lose)
            # print('''
            # win %d
            # lose %d
            # ping %d
            # '''%win%lose%ping)
            # return lose
            elif hum_comptuer in rule.get('ping'):
            # i +=1
            # ping=i
                ping +=1
                print('打和')
                print("ping %d" %ping)
            # print('''
            # win %d
            # lose %d
            # ping %d
            # '''%win%lose%ping)
            # return ping
      # print("    win {win}  ,lose {lose} ,ping {ping}".format(win,lose,ping))
     # print("win %d" %count())
     # print("lose %d" %lose)
     # print("ping %d" %ping)

        elif hum == '4':
          # print("win %d" %win)
          # print("lose %d" %lose)
          # print("ping %d" %ping)
          view()
        else:
         print('选择有误，请正确输入')
         game()

def view():
    print('''
    1开始
    2规则
    3退出
    4扩展
    5设置
    ''')
    hum=input("请选择")
    if hum == '1':
        win=0
        lose=0
        ping=0
        while True:
            # print("win:{} lose:{} ping:{}".format(win,lose,ping))
            game()
            # print("win:{} lose:{} ping:{}".format(win,lose,ping))
        # print('win %s'%win)
        # prin('lose %d'%lose)
        # print("ping %d"%ping)

    elif hum == '2':
        print(rule)
        view()
    elif hum == '3':
        exit()
    elif hum == '4':
        print('在努力升级中')
        view()
    elif hum == '5':
        print("在努力设计中")
        view()
    else:
        print('输入不合法，请重新选择')
        view()




def register():
    username=input('username')
    password=input('password')
    info={
        'username':None,
        'password':None
    }
    info['username']=username
    info['password']=password
    return info
# def load():
#     username=input('username')
#     password=input('password')

# def game():
#     print('')
#

def load():
    i=1
    while i<=5:
        info_load=register()
        if info_load in list and info_load not in lockuser_list:
            print("登录成功")
            view()
        else:
            print("登录失败 %d次，请重新登录" %i)
            i +=1
            lockuser_list.append(info_load)



def hello_view():
    print('请选择模式1登录2注册')
    choose=input("1 登录 ，2 注册：")
    if choose == '1':
        # pass
        load()
    elif choose =='2':
        list.append(register())

        print('注册成功')
        print(list)
        hello_view()
    else:
        print('输入错误，请重新输入')
        hello_view()


list=[{'username':'li','password':'123'}]
lockuser_list=[]

choose = ['石头', '剪刀', '布']
rule={
    '1':'石头',
    '2':'剪刀',
    '3':'布',
    '4':'退出',
    'win' :['1剪刀','2布','3石头'],
    'lose':['1布','2石头','3剪刀'],
    'ping':['1石头','2剪刀','3布']
}
hello_view()
# load()
# view()
# while True:
#     game()