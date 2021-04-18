import pickle
import time
import os
global names,authors,nums,order_nums,d1,d3
d1=1 #用于main判断
d3=1 #用于UI判断
names=[]
authors=[]
nums=[]
order_nums=[]
global user_data
user_data={}
title='序号\t\t书名\t\t作者\t\t数量\n'
global start_dir #文件夹路径
global way #用户书库（多个）
global data_way #资料库路径（多个）
global user_way #存用户账号密码（1个）
start_dir='D:/Library' 
user_way=start_dir + '/Users.lyf'


#以二进制写入资料库
def save_data():
    global names,authors,nums,order_nums
    #转二进制保存
    f=open(data_way,'wb') #以二进制写入
    pickle.dump(order_nums,f) #将序号存入
    pickle.dump(names,f) #将书名写入
    pickle.dump(authors,f) #将作者写入
    pickle.dump(nums,f) #将数量写入
    f.close()

#将二进制文件导入列表
def out_data():
    global names,authors,nums,order_nums
    f=open(data_way,'rb')
    order_nums=pickle.load(f)
    names=pickle.load(f)
    authors=pickle.load(f)
    nums=pickle.load(f)
    f.close()

#加书
def add_book():
    global names,authors,nums,order_nums
    #如果文件存在则将二进制导入列表
    if os.path.isfile(data_way):
        out_data()
    temp_name=input('请输入需要放进去的书名：')

    #如果已经存在这本书则加数量
    if temp_name in names:
        key=names.index(temp_name) #这本书的索引值
        print('这本书在库中已经有{}本了'.format(nums[key]))
        temp_num=input('你想要放多少本进去：')

        #判断是否输入数字
        while not temp_num.isdigit():
            temp_num=input('输入有误，请重新输入：')
        nums[key]=int(temp_num) + int(nums[key]) #赋值回去

    #否则加书
    else:
        names.append(temp_name)
        authors.append(input('作者是：'))
        temp_num=input('你想要放多少本进去：')
        while not temp_num.isdigit():
            temp_num=input('输入有误，请重新输入：')
        nums.append(temp_num) #赋值数量
        order_nums.append(len(order_nums)+1)
    save_data() #将列表导入资料库
    print('成功添加书籍！')
    
#输出用户书库
def out_book():
    global names,authors,nums,order_nums
    out_data() #导出数据
    f=open(way,'w')
    f.write(title)
    
    for a in order_nums:
        i=a-1 #索引值
        f.write('%d\t\t%s\t\t%s\t\t%s\n' %(order_nums[i],names[i],authors[i],nums[i]))
    f.close()

#初始化
def first():
    if os.path.isfile(way):
        os.remove(way)
    if os.path.isfile(data_way):
        os.remove(data_way)
    add_book() #加书
    out_book() #添加到用户书库
    print('初始化成功！')
    time.sleep(0.5)

#查书
def watching():
    global names,authors,nums,order_nums
    d2=1 #用于本函数的判断
    #输出
    def see(key):
        print(title)
        print('%d\t\t%s\t\t%s\t\t%s' % (order_nums[key],names[key],authors[key],nums[key]))
    def one():
        print(title)
        for key1 in order_nums:
            key=key1-1 
            print('%d\t\t%s\t\t%s\t\t%s' % (order_nums[key],names[key],authors[key],nums[key]))
    def two():
        temp=input('请输入需要查找的序号：')
        key=int(temp)-1 #索引值
        see(key)
    def three():
        temp=input('请输入需要查找的书名：')
        key=names.index(temp) #索引值
        see(key)
    def four():
        temp=input('请输入需要查找的作者：')
        key=authors.index(temp) #索引值
        see(key)
    def five():
        num_book=[] #存索引值
        count=-1 #索引值
        temp=input('请输入需要查找书本的数量：')
        for i in nums:
            count+=1
            if int(temp) == int(i):
                num_book.append(count) #如果数量符合则返回索引值
        if len(num_book) > 0:
            print(title)
            for key in num_book:
                print('%d\t\t%s\t\t%s\t\t%s' % (order_nums[key],names[key],authors[key],nums[key]))
    while d2:
        print('''
    *************
      1.全部查看
      2.序 号 找
      3.书 名 找
      4.作 者 找
      5.数 量 找
      6.返回菜单
    *************
        ''')
        out_data() #读取数据
        choise=input('请输入需要的功能：')
        if choise=='1':
            one()
            time.sleep(0.8)
        elif choise=='2':
            two()
            time.sleep(0.8)
        elif choise=='3':
            three()
            time.sleep(0.8)
        elif choise=='4':
            four()
            time.sleep(0.8)
        elif choise=='5':
            five()
            time.sleep(0.8)
        elif choise=='6':
            d2=0
        else:
            print('输入有误！')
            time.sleep(0.8)

#图书入库
def entering():
    global names,authors,nums,order_nums,d
    add_book() #将资料导入列表加书
    out_book() #输出用户书库
    print('入库成功！')
    choise=input('请选择是否查看全部书籍(Y/N):')
    if choise =='Y' or choise =='y':
        print(title)
        for a in order_nums:
            i=a-1 #索引值
            print('%d\t\t%s\t\t%s\t\t%s' % (order_nums[i],names[i],authors[i],nums[i]))
    elif choise =='N' or choise =='n':
        d1=1
    else:
        print('输入有误！')

#图书借出
def lending():
    global names,authors,nums,order_nums
    out_data() #将资料导入列表
    book=input('请输入需要借走的书名：')
    if book in names:
        key=names.index(book)
        print('该书还剩下{}本'.format(nums[key]))
        num=input('请问你需要多少本？')
        while not num.isdigit() or int(num) <=0:
            print('输入有误！')
            num=input('请重新输入：')
        if int(num) <= int(nums[key]):
            temp=int(nums[key])-int(num)
            nums[key]=temp
            save_data() #存入资料库
            out_book() #导出用户书库
            print('借出成功！')
        elif int(num) > int(nums[key]):
            print('抱歉，没有这么多本书！')
    else:
        print('抱歉，库中没有这本书！')

def main():
    global d1,d3
    while d1:
        print('''
**********************************
     欢迎使用图书管理信息系统
**********************************
            1.查看图书
            2.图书入库
            3.图书借出
            4.退出账号
            5.退出系统
        ''')
        choise=input("请选择你的操作：")
        if choise=='1':
            watching()
        elif choise=='2':
            entering()
        elif choise=='3':
            lending()
        elif choise=='4':
            d1=0
        elif choise=='5':
            d1=0
            d3=0

#主界面
def UI():
    global d3
    while d3:
        print('''
    *************
      1.注   册
      2.登   陆
      3.退出系统
    *************
    ''')
        choise=input('请选择：')
        if choise=='1':
            newuser()
        elif choise=='2':
            olduser()
        elif choise=='3':
            d3=0
        else:
            print('输入有误！')

#注册
def newuser():
    global user_data
    print('！！！温馨提示，文件在D:/Library中！！！')
    #判断是否存在文件夹，没有则创建
    if not os.path.isdir(start_dir):
        os.mkdir(start_dir)
    #二进制导入列表
    if os.path.isfile(user_way):
        f=open(user_way,'rb')
        user_data=pickle.load(f)
        f.close()

    user_name=input('创建用户名：')
    while user_name in user_data:
        user_name=input('该用户名已经被使用，请重新输入：')

    password=input('设置密码：')
    user_data[user_name]=password
    
    #二进制加用户
    f=open(user_way,'wb')
    pickle.dump(user_data,f)
    f.close()
    print('注册成功，请登录！')
    time.sleep(0.5)

    #为每位用户创建新的书库文件
    global way
    global data_way
    way=start_dir + '/' + user_name + '_Books.txt'
    data_way=start_dir + '/' +user_name + '_bookdata.lyf'
    first() #初始化

#登陆
def olduser():
    global user_data
    #导出列表
    try:
        f=open(user_way,'rb')
        user_data=pickle.load(f)
        user_name=input('请输入用户名：')
        if user_name not in user_data:
            print('该用户不存在，请注册!')
        else:
            password=input('请输入密码：')
            while password != user_data[user_name]:
                password=input('密码错误，请重新输入密码：')
            global way
            global data_way
            #修改到每一个账号指定的路径文件
            way = start_dir + '/' + user_name + '_Books.txt'
            data_way = start_dir + '/' + user_name + '_bookdata.lyf'
            print('登陆成功！')
        f.close()
        main() #登陆成功后跳转图书界面
    except OSError:
        print('请先注册！')
        time.sleep(0.8)
    

#程序开头
UI()
print('退出成功！')