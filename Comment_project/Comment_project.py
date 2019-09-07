from flask import Flask, render_template, request, redirect, url_for, session
import config
from exts import db
from models import User, Comment, Answer
from decorators import login_required

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/user')
def user():
    return render_template('user.html')


@app.route('/photos')
def photos():
    return render_template('photos.html')


@app.route('/')
def index():
    context = {
        'comments': Comment.query.order_by('-create_time').all()
    }
    return render_template('index.html',**context)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone == telephone, User.password == password).first()  # 过滤
        if user:
            session['user_id'] = user.id
            # 如果在31天内都不需要登录
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return '您的手机号或密码错误，请确认后在登录-^-!'


@app.route('/regist', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # 手机号码验证，如果被注册了，就不能再注册了
        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return '该手机号已被注册，请更换手机号注册-^-'
        else:
            # password1 和password2 要相等才行
            if password1 != password2:
                return '两次密码不相等，请核对后再填写！'
            else:
                user = User(telephone=telephone, username=username, password=password1)
                db.session.add(user)
                db.session.commit()
                # 如果注册成功，则跳转到登录的页面
                return redirect(url_for('login'))


@app.route('/logout')
def logout():
    # session.pop('user_id')
    # del session['user_id']
    session.clear()
    return redirect(url_for('login'))


@app.route('/comment', methods=['GET', 'POST'])
@login_required
def comment():
    if request.method == 'GET':
        return render_template('comment.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        comment = Comment(title=title, content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        comment.author = user
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/detail/<comment_id>/')
def detail(comment_id):
    comment_model = Comment.query.filter(Comment.id == comment_id).first()
    return render_template('detail.html', comment=comment_model)


@app.route('/add_answer/', methods=['POST'])
@login_required
def add_answer():
    content = request.form.get('answer_content')
    comment_id = request.form.get('comment_id')
    answer = Answer(content=content)
    user_id = session['user_id']
    user = User.query.filter(User.id == user_id).first()
    answer.author = user
    comment = Comment.query.filter(Comment.id == comment_id).first()
    answer.comment = comment
    db.session.add(answer)
    db.session.commit()
    return redirect(url_for('detail', comment_id=comment_id))


@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    return {}


if __name__ == '__main__':
    app.run()
