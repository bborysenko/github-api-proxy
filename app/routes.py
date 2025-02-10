from flask import request, jsonify
import requests

def configure_routes(app):
    @app.route('/search')
    def search():
        query = request.args.get('q')
        if not query:
            return jsonify({"error": "Missing required query parameter 'q'."}), 400

        params = {'q': query}

        try:
            response = requests.get(app.config['GITHUB_SEARCH_URL'], params=params)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return jsonify({"error": "Error fetching data from GitHub API.", "details": str(e)}), 500

        return jsonify(response.json())
