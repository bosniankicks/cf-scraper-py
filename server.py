from flask import Flask, request, jsonify
import subprocess
import json
import sys

app = Flask(__name__)

@app.route('/get_cf_clearance', methods=['POST'])
def get_cf_clearance():
    data = request.json
    url = data.get('url')

    if not url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        print(f"Received request for URL: {url}")
        print(f"Flask server is using Python executable: {sys.executable}")
        result = subprocess.run(
            [sys.executable, 'get_cf_clearance.py', url],
            capture_output=True, text=True
        )
        
        print(f"Subprocess stdout: {result.stdout}")
        print(f"Subprocess stderr: {result.stderr}")
        try:
            output = json.loads(result.stdout)
        except json.JSONDecodeError as e:
            print("JSON decode error:", e, file=sys.stderr)
            print(f"Subprocess stdout: {result.stdout}", file=sys.stderr)
            return jsonify({'error': 'Failed to parse Playwright script output'}), 500

        cf_clearance = output.get('cf_clearance')
        user_agent = output.get('user_agent')

        if cf_clearance and user_agent:
            response_data = {
                'cf_clearance': cf_clearance,
                'user_agent': user_agent
            }
            formatted_response = json.dumps(response_data, indent=4)
            return app.response_class(formatted_response, content_type='application/json')
        else:
            return jsonify({'error': 'Could not retrieve cf_clearance token'}), 500
    except subprocess.CalledProcessError as e:
        print(f"Subprocess error: {e}", file=sys.stderr)
        print(f"Standard Output: {e.stdout}")
        print(f"Standard Error: {e.stderr}")
        return jsonify({'error': 'Failed to execute Playwright script', 'stdout': e.stdout, 'stderr': e.stderr}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # Make sure to use a free port
