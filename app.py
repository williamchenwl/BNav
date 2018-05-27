from flask import Flask, render_template, redirect
from flask_script import Manager 
from flask_bootstrap import Bootstrap
from view import QueryForm
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
        return redirect('/route')
    return render_template('index.html', form=form)


@app.route('/route', methods = ['GET', 'POST'])
def outside():
    
   return render_template('outside.html')

@app.route('/result')
def result():
    return render_template('index.html')

if __name__ == '__main__':

    app.run()
