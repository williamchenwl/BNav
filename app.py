from flask import Flask, render_template, redirect, Response
from flask_script import Manager 
from flask_bootstrap import Bootstrap
from view import QueryForm
import static
#from model import query
app = Flask(__name__)

app.config['SECRET_KEY'] = 'william'

bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    #return "Hello World"
    form = QueryForm()
    if form.validate_on_submit():
        print(form.location.data, form.destination.data)
        #query(form.location.data, form.destination.data)
        return redirect('/route/{}/{}'.format(form.location.data[0], form.destination.data[0]))
    return render_template('index.html', form=form)


@app.route('/route/<src>/<dst>', methods = ['GET', 'POST'])
def outside(src, dst):  
    print(src)
    print(dst)
    ax, ay = static.getLat(src)
    bx, by = static.getLat(dst)
    return render_template('outside.html', ax = ax, ay = ay, bx = bx, by = by)

@app.route('/result')
def result():
    return render_template('index.html')

@app.route('/map.png')
def show_map():
    image = open("sources/map.png")
    resp = Response(image, mimetype="image/png")

if __name__ == '__main__':

    app.run()
