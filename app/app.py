from flask import Flask, request, jsonify
# temporary data source, it will be replaced with a database
from publications import publications

app = Flask(__name__)

@app.route('/')
def index():
    return "this site provide api access only."

@app.get('/publications')
def get_publications():
    return jsonify(publications)

@app.get('/publications/<int:id>')
def get_publication(id):
    if id > len(publications):
        return "404 page not found"
    else:
        return jsonify(publications[id])

@app.errorhandler(400)
def bad_request(e):
    return "400 bad request", 500

@app.errorhandler(403)
def forbidden(e):
    return "403 forbidden", 403

@app.errorhandler(404)
def page_not_found(e):
    return "404 page not found", 404

@app.errorhandler(405)
def method_not_allowed(e):
    return "405 method not allowed", 405

@app.errorhandler(500)
def internal_server_error(e):
    return "500 internal server error", 500

if __name__ == '__main__':
    app.run(debug = False)