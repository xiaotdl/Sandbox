from flask import Flask

from routes import init_api_routes
from routes import init_website_routes


# create the Flask application
app = Flask(__name__)

init_api_routes(app)
init_website_routes(app)


#
# Template filters
#
@app.template_filter('senior_candidate')
def senior_candidate(candidates):
    result = []
    for candidate in candidates:
        for experience in candidate['experience']:
            if experience['years'] >= 5:
                result.append({
                    'first_name':candidate['first_name'],
                    'last_name':candidate['last_name'],
                    'years':experience['years'],
                    'domain':experience['domain']
                })
                break

    return result



if __name__ == "__main__":
    app.run(debug=True)
