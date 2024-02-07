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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
