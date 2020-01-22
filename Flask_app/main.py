from flask import Flask, render_template,jsonify

app = Flask(__name__)


# here basically tells what is returned on the home page
@app.route("/")
def home():
    return render_template("page.html")

# connect button to script

@app.route('/_get_data/',methods=['POST'])
def _get_data():
	myList = ["hello"]

	return jsonify({'data': render_template('response.html',myList = myList)})
    
if __name__ == "__main__":
    app.run(debug=True)