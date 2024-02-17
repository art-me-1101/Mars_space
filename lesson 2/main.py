from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'


@app.route("/training/<string:prof>")
def training(prof):
    if 'инженер' in prof.lower() or 'строитель' in prof.lower():
        img = url_for('static', filename='img/engin.png')
        name = 'Инженерные тренажеры'
    else:
        img = url_for('static', filename='img/since.png')
        name = 'Научные симуляторы'
    return render_template('base2.html', profession=name, url=img)


@app.route("/list_prof/<string:type>")
def list_prof(type):
    prof_list = ['инженер-исследователь', ' пилот', ' строитель', ' экзобиолог', ' врач',
                 ' инженер по терраформированию', ' климатолог', ' специалист по радиационной защите', ' астрогеолог',
                 ' гляциолог', ' инженер жизнеобеспечения', ' метеоролог', ' оператор марсохода', ' киберинженер',
                 ' штурман', ' пилот дронов']
    return render_template('base3.html', type=type, prof_list=prof_list)


if __name__ == '__main__':
    app.run(port=8080, host="127.0.0.1")
