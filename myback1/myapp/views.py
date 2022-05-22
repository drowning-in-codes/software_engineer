from django.shortcuts import render,redirect,HttpResponse
from . import models



#登录
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = models.userinfo.objects.filter(username=username, password=password).first()
        if user:
            request.session['name'] = user.name
            request.session['account'] = user.account
            return redirect("/index/")
        else:
            return render(request, "login.html")


#退出界面
def logout(request):
    request.session.clear()
    rep=redirect('/login/')
    rep.cookies.clear()
    return rep

#首页
def index(request):
    return render(request, 'index.html')
'''
题目信息操作
'''
#查询
def questionlist(request):
    questionlist = models.questioninfo.objects.all()
    return render(request, 'qusetion_list.html', {'questionlist':questionlist})
#添加
def questionadd(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        topic = request.POST.get('topic')
        A_Key = request.POST.get('A_Key')
        B_Key = request.POST.get('B_Key')
        C_Key = request.POST.get('C_Key')
        D_Key = request.POST.get('D_Key')
        R_Key = request.POST.get('R_Key')

        models.questioninfo.objects.create(number=number,topic=topic,A_Key=A_Key,B_Key=B_Key,C_Key=C_Key,D_Key=D_Key,R_Key=R_Key)

        return redirect('questionlist')
    return render(request, 'qusetioninfo_add.html')
#修改
def questionedit(request, id):
    if request.method == 'POST':
        obj_id = request.POST.get('id')
        question_obj = models.questioninfo.objects.get(id=obj_id)
        number = request.POST.get('number')
        topic = request.POST.get('topic')
        A_Key = request.POST.get('A_Key')
        B_Key = request.POST.get('B_Key')
        C_Key = request.POST.get('C_Key')
        D_Key = request.POST.get('D_Key')
        R_Key = request.POST.get('R_Key')
        question_obj.number = number
        question_obj.topic = topic
        question_obj.A_Key = A_Key
        question_obj.B_Key = B_Key
        question_obj.C_Key = C_Key
        question_obj.D_Key = D_Key
        question_obj.R_Key = R_Key
        question_obj.save()

        return redirect('questionlist')
    question_obj = models.questioninfo.objects.get(id=id)
    return render(request, 'questioninfo_edit.html', {'obj':question_obj})

#删除
def questiondel(request, id):
    book_obj = models.questioninfo.objects.get(id=id)
    book_obj.delete()
    return redirect('booklist')

'''
用户信息操作
'''
#查询
def userlist(request):
    userlist = models.userinfo.objects.all()
    return render(request, 'userinfo_list.html', {'userlist':userlist})

#增加
def useredit(request,id):
    if request.method == 'POST':
        obj_id = request.POST.get('id')
        user_obj = models.userinfo.objects.get(id=obj_id)
        account = request.POST.get('account')
        password = request.POST.get('password')
        name = request.POST.get('name')
        user_obj.name = name
        user_obj.account = account
        user_obj.password = password
        user_obj.save()

        return redirect('userlist')
    user_obj = models.userinfo.objects.get(id=id)

    return render(request, 'userinfo_edit.html', {'obj':user_obj})

#增加
#添加
def useradd(request):
    if request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('author')
        name = request.POST.get('name')

        models.userinfo.objects.create(account=account, password=password, name=name)
        return redirect('userlist')
    return render(request, 'userinfo_add.html')

#删除
def userdel(request, id):
    user_obj = models.userinfo.objects.get(id=id)
    user_obj.delete()
    return redirect('userlist')
'''
做题信息操作
'''
#查询
def recordlist(request):
    user_account = request.session.get('account')
    recordlist = models.record.objects.filter(account=user_account)

    return render(request, 'record_list.html', {'recordlist':recordlist})

#增加
def recordadd(request):
    user_account = request.session.get('account')
    '''
    联合查询此用户还没有做过的题得到question_list
    '''
    user_obj = models.userinfo.objects.get(account=user_account)
    question_list = models.questioninfo.exclude(id_in=[record.question_id for record in user_obj.record_set.all()])

    if request.method == 'POST':
        userid = request.POST.get('user_id')
        questionid = request.POST.get('question_id')
        evaluate = request.POST.get('evaluate')
        key = request.POST.get('key')
        models.record.objects.create(user_id=userid, question_id=questionid, evaluate=evaluate,key=key)
        return redirect('borrowlist')

    return render(request, 'record_add.html', {'questionlist':question_list,'account':user_account})



#删除
def recorddel(request,id):
    record_obj = models.record.objects.get(id=id)
    record_obj.delete()
    return redirect('recordlist')

#更改
def recordedit(request,id):
    if request.method == 'POST':
        obj_id = request.POST.get('id')
        record_obj = models.POST.get(id=obj_id)
        key = request.POST.get('key')
        evaluate = models.POST.get('evaluate')
        record_obj.key = key
        record_obj.evaluate = evaluate
        record_obj.save()

        return redirect('recordlist')
    record_obj = models.record.objects.get(id=id)
    return render(request, 'record_edit.html',{'obj':record_obj})













