import json

from flask import Flask, url_for, request, render_template, redirect

from flask02les.loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '1qm3Ui09_oiu875___kijvsd5ilh_i_kgye'


@app.route('/<title>')
@app.route('/index/<title>')
def title(title):
    param = {}
    param['title'] = title
    return render_template('base.html', **param)


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['username'] = "Ученик Яндекс.Лицея"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    param = {}
    param["title"] = "Анкета"
    param["surname"] = "Wanty"
    param["name"] = "Mark"
    param["education"] = "Выше среднего"
    param["profession"] = "Штурман марсохода"
    param["sex"] = "male"
    param["motivation"] = "Всегда мечтал застрять на Марсе!"
    param["ready"] = "True"
    return render_template('auto_answer.html', **param)


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=2)


@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', news=news_list)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
