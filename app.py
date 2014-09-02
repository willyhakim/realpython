import os
from bottle import route, run, template

index_html = '''My first web app! by {{ author}}'''


@route('/anything')
def something (anything=''):
	return template(index_html, author=anything)


@route('/')
def index():
	return template(index_html, author='William Hakim')

if __name__=='__main__':
	port = int (os.environ.get('PORT', 8080))
	run(host='0.0.0.0', port=port, debug=True)
