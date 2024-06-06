import os
from . import sdm 
from . import sdn
from flask import *

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_mapping(SECRET_KEY = 'dev', )    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/', methods = ('GET', 'POST'))
    @app.route('/home', methods = ('GET', 'POST'))
    def home():
        if request.method == 'POST':
                imgp = request.form['imgprompt']
                audp = request.form['audprompt']  
                ist = request.form['istyle'] 
                ast = request.form['astyle'] 

                if imgp!=None and audp!=None:
                    try:
                        sdn.getimg(imgp+' '+ist)      
                        sdm.getaudio(audp+' '+ast)
                                   
                    except Exception as ex:
                        print(ex)                        
                    else:
                        return redirect(url_for("disp"))
        return render_template('basecopy.html')
    
    @app.route('/disp', methods = ('GET', 'POST'))
    def disp():        
        return render_template('disp.html')
    
    return app