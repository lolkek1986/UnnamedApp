from flask import Flask
from flask import request
from Parser import GrantParser
from flask import jsonify 
grant_parser = GrantParser()
app = Flask(__name__)
@app.route('/', methods=['POST'])
def return_grant():
    if request.method == 'POST':
        grant_info = grant_parser.search_grants(request.args.get('grant_type'))
        return jsonify(grant_info)

app.run(host='0.0.0.0', port=4200)
