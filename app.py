from flask import Flask, render_template, redirect, Response, make_response
from flask_script import Manager 
from flask_bootstrap import Bootstrap
from view import QueryForm, BQueryForm
import static
from model import query
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


@app.route('/bindex', methods=['GET', 'POST'])
def bindex():
    #return "Hello World"
    form = BQueryForm()
    if form.validate_on_submit():
        print(form.location.data, form.destination.data)
        #query(form.location.data, form.destination.data)
        return redirect('/broute/{}/{}'.format(form.location.data[0], form.destination.data[0]))
    return render_template('bindex.html', form=form)


@app.route('/route/<src>/<dst>', methods = ['GET', 'POST'])
def outside(src, dst):  
    print(src)
    print(dst)
    ax, ay = static.getLat(src)
    bx, by = static.getLat(dst)
    return render_template('outside.html', ax = ax, ay = ay, bx = bx, by = by)

@app.route('/broute/<src>/<dst>', methods = ['GET', 'POST'])
def broute(src, dst):
    query(src, dst)    
    return render_template('binside.html', img_id= src + dst)

@app.route('/showphoto/<filename>', methods=['GET'])

def showphoto(filename):

    image_data = open('tmp/{}.png'.format(filename), 'rb').read()

    response = make_response(image_data)

    response.headers['Content-Type'] = 'image/png'

    return response

@app.route('/result')
def result():
    return render_template('index.html')

@app.route('/map.png')
def show_map():
    image = open("sources/map.png")
    resp = Response(image, mimetype="image/png")

if __name__ == '__main__':

    app.run()
