#encoding=utf-8
from flask import Flask,redirect,render_template,url_for,flash,session,make_response,send_file, send_from_directory
from flask.ext.bootstrap import Bootstrap
from flask_wtf import FlaskForm
from connect_Mysql import *
from wtforms import *
from wtforms.validators import DataRequired,length
from flask_admin import Admin, AdminIndexView
from excel import exportSum,exportTime
from excel2sql import importExcelToMysql


app = Flask(__name__)
#设置密匙
app.config['SECRET_KEY'] = 'hard to guess'
bootstrap = Bootstrap(app)
#
admin = Admin(app=app,
              #base_template='my_base.html',
              index_view=AdminIndexView(template='index.html')
              )


#登陆表单
class loginForm(FlaskForm):
    user_id = StringField('学号',validators=[DataRequired()])
    password = StringField('密码',validators=[DataRequired()])
    submit = SubmitField('提交')

#记录工时的表单
class timeForm(FlaskForm):
    #time = StringField('工作时长',validators=[DataRequired()])
    time = SelectField('工作时长',choices=[('0.5', '0.5h'),('1', '1h'),('2', '2h'),('3', '3h'),('4', '4h')],validators=[DataRequired()])
    date = DateTimeField('日期',format='%Y-%m-%d',validators=[DataRequired()])
    content = TextAreaField('工作内容',validators=[DataRequired()])
    submit = SubmitField('提交')



#主页
@app.route('/')
def hello_world():
    if 'user_id' in session:
        return redirect('/index')
    else:
        return redirect('/login')

#真正的主页
@app.route('/index',methods=['GET','POST'])
def index():
    #如果id在session就直接登录了
    if 'user_id' in session and 'password' in session:
        if session['user_id'] == 'admin':
            return redirect('/adm')
        if select_password_sql(session['user_id'])==session['password']:
            name = session['username']
            #id = session['user_id']
            results = select_time_sql(session['user_id'])
            return render_template('index.html',name =name,results = results)
        else:
            return render_template('index.html', name=None)
    else:
        name = None
        return render_template('index.html',name=name)



#登陆界面
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()

    if form.validate_on_submit():
        if form.user_id.data == 'admin' and form.password.data=='admin':
            session['password'] = 'admin'
            session['username'] = 'admin'
            session['user_id'] =  'admin'
            return redirect('/adm')
        if form.password.data == select_password_sql(form.user_id.data):
            session['user_id'] = form.user_id.data
            session['username'] = select_name_sql(form.user_id.data)
            session['password'] = select_password_sql(form.user_id.data)
            return redirect(url_for('index'))
        else:
            flash('用户名或密码错误')
    return render_template('login.html',form = form)

#退出页面
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('user_id', None)
    return redirect(url_for('index'))

#个人的工时记录页面
@app.route('/time', methods=['GET', 'POST'])
def time():
    name = session['username']
    id2 = session['user_id']
    form = timeForm()
    if form.validate_on_submit():
        id= session['user_id']
        time = form.time.data
        date = form.date.data
        content = form.content.data
        if insert_time_sql(id,time,date,content)==1:
            flash('提交成功')
            return redirect(url_for('index'))
        else:
            flash('也不知道咋回事提交失败了')

    return render_template('time.html',form=form,name=name,id2 = id2)

#管理员界面
@app.route('/adm')
def admin():
    if session['username']=='admin' and session['password']=='admin':
        name = 'admin'
        results = select_all_sql()
        return render_template('adm.html', results=results,name=name)
    else:
        return redirect('/login')

#下载文件用的
@app.route("/download/<filename>", methods=['GET'])
def download_file(filename):


    #response = make_response(send_file("/home/www/SM3/file/"+filename))

    if filename =='time.xls':
        if 1:

            response = make_response(send_file("./file/" + filename))
            response.headers["Content-Disposition"] = "attachment; filename=times.xls;"
        else:
            flash('也不知道咋回事导出数据失败了')
            return redirect('/adm')
    else:
        if 1:
            response = make_response(send_file("./file/" + filename))
            response.headers["Content-Disposition"] = "attachment; filename=timeSums.xls;"
        else:
            flash('也不知道咋回事导出数据失败了')
            return redirect('/adm')
    return response


if __name__ == '__main__':
    # ##tb_play_type表
    # path = r"user.xls"
    #
    # ##调用函数
    # importExcelToMysql(path)
    app.run('0.0.0.0')