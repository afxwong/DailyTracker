from flask import Flask, render_template, request, redirect, url_for
from GenericLinePlot import GenericLinePlot
import csv
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('menu.html')


@app.route('/favicon.ico')
def favicon():
    return "Doesn't exist"


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        with open('data.csv', 'a') as f:
            writer = csv.writer(f)
            temp = [datetime.datetime.now()]
            for item in list(request.form.values()):
                temp.append(item)
            writer.writerow(temp)
        return redirect(url_for('index'))
    return render_template('form.html')


@app.route('/<string:plot_name>')
def test(plot_name):
    glp = GenericLinePlot(plot_name)
    glp.plot()
    return render_template('{}.html'.format(plot_name))


if __name__ == "__main__":
    app.run(debug=True)
