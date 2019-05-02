from myapp.apps.root import module as A
@A.route('/root-template')
def B():from flask import render_template as A;return A('index.html')