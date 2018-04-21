# external modules
from flask import Flask, render_template, url_for, request

# local libraries
from db import Database
from students import Students

# globals
def new_db_conn():
	return Database('D:\sqlite\hackathon.db')

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def search():
	if request.method == 'POST':
		skillsandexp = request.form.get('skillsandexp', '')
		location = request.form.get('location', '')
		db = new_db_conn()
		results = Students().search(db, location=location)

		template_vars = {
			'search_results': results
		}
		return render_template('search.html', **template_vars)
	return "500 Error"

if __name__ == "__main__":
	app.run(debug=True)