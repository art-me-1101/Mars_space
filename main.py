from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                  </head>
                  <body>
                    <h1>Миссия Колонизация Марса</h1>
                  </body>
                </html>"""


@app.route('/index')
def index():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                      </head>
                      <body>
                        <h1>И на Марсе будут яблони цвести!</h1>
                      </body>
                    </html>"""


@app.route('/promotion')
def promotion():
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                          </head>
                          <body>
                            <h1>Человечество вырастает из детства.
                            <br>Человечеству мала одна планета.
                            <br>Мы сделаем обитаемыми безжизненные пока планеты.
                            <br>И начнем с Марса!<br>
                            Присоединяйся!</h1>
                          </body>
                        </html>"""


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <title>Привет, Марс!</title>
                          </head>
                          <body>
                            <h1>Жди нас, Марс!</h1>
                            <img src="{url_for('static', filename='img/mars.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                            <p>Вот она какая, красная планета.</p>
                          </body>
                        </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.2.1/dist/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
                            <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
                            <title>Привет, Марс!</title>
                          </head>
                          <body>
                            <h1>Жди нас, Марс!</h1>
                            <img src="{url_for('static', filename='img/mars.png')}" alt="здесь должна была быть картинка, но не нашлась">
                            <div class="alert alert-primary" role="alert">
                              <h3>Человечество вырастает из детства.</h3>
                            </div>
                            <div class="alert alert-secondary" role="alert">
                              <h3>Человечеству мала одна планета.</h3>
                            </div>
                            <div class="alert alert-success" role="alert">
                              <h3>Мы сделаем обитаемыми безжизненные пока планеты.</h3>
                            </div>
                            <div class="alert alert-danger" role="alert">
                              <h3>И начнем с Марса!</h3>
                            </div>
                            <div class="alert alert-warning" role="alert">
                              <h3>Присоединяйся!</h3>
                            </div>
                            
                          </body>
                        </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    return f"""<!doctype html>
                    <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                              href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                              integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                              crossorigin="anonymous">
                        <link rel="stylesheet" href="{url_for('static', filename='css/style2.css')}"/>
                        <title>Пример формы</title>
                    </head>
                    <body>
                    <h1 class="text">Анкета претендента</h1>
                    <h4 class="text">на участие в миссии</h4>
                    <div>
                        <form class="login_form" method="post">
                            <div style="margin-bottom: 10px">
                            <input type="text" class="form-control" id="familia" placeholder="Введите фамилию" name="familia">
                            <input type="text" class="form-control" id="name" placeholder="Введите Имя" name="name">
                                </div>
                            <input type="email" class="form-control" id="email" aria-describedby="emailHelp"
                                   placeholder="Введите адрес почты" name="email" style="margin-bottom: 10px">
                            <div class="form-group" style="margin-bottom: 10px">
                                <label for="educSelect">Какое у Вас образование?</label>
                                <select class="form-control" id="educSelect" name="class">
                                    <option>Начальное</option>
                                    <option>Основное</option>
                                    <option>Среднее общее</option>
                                    <option>среднее профессиональное</option>
                                    <option>высшее образование</option>
                                </select>
                            </div>
                            <div class="form-group form-prof" style="margin-bottom: 10px">
                                <label style="margin-bottom: 10px">Какие у вас есть профессии?</label>
                                <div>
                                <input type="checkbox" class="form-check-input" id="injiner-advenute" name="accept">
                                <label class="form-check-label">Инженер-исследователь</label>
                                </div>
                                <div>
                                <input type="checkbox" class="form-check-input" id="pilot" name="accept">
                                <label class="form-check-label">Пилот</label>
                                    </div>
                                <div>
                                <input type="checkbox" class="form-check-input" id="bilder" name="accept">
                                <label class="form-check-label" >Строитель</label>
                                    </div>
                                <div>
                                <input type="checkbox" class="form-check-input" id="ecobiolog" name="accept">
                                <label class="form-check-label">Экзобиолог</label>
                                    </div>
                                <div>
                                <input type="checkbox" class="form-check-input" id="doctor" name="accept">
                                <label class="form-check-label">Врач</label>
                                    </div>
                                <div>
                                <input type="checkbox" class="form-check-input" id="injiner-makelife" name="accept">
                                <label class="form-check-label">Инженер жизнеобеспечения</label>
                                    </div>
                                <div>
                                <input type="checkbox" class="form-check-input" id="meteorolog" name="accept">
                                <label class="form-check-label">Метеоролог</label>
                                    </div>
                                <div>
                                <input type="checkbox" class="form-check-input" id="rover_operator" name="accept">
                                <label class="form-check-label">Оператор марсохода</label>
                                    </div>
                            </div>
                            <div class="form-group" style="margin-bottom: 10px">
                                <label style="margin-bottom: 10px">Укажите пол</label>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                    <label class="form-check-label" for="male">
                                        Мужской
                                    </label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                    <label class="form-check-label" for="female">
                                        Женский
                                    </label>
                                </div>
                            </div>
                            <div class="form-group" style="margin-bottom: 10px">
                                <label for="about" style="margin-bottom: 10px">Почему вы хотите учавствовать в миссиии?</label>
                                <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                            </div>
                            <div class="form-group" style="margin-bottom: 10px">
                                <label for="photo" style="margin-bottom: 10px">Приложите фотографию</label>
                                <input type="file" class="form-control-file" id="photo" name="file">
                            </div>
                            <button type="submit" class="btn btn-primary">Записаться</button>
                        </form>
                    </div>
                    </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
