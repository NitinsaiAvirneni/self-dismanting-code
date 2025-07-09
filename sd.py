from flask import Flask, jsonify
import os
import sys

app = Flask(__name__)

@app.route('/run-once', methods=['GET'])
def run_once():
    # Your logic here
    response = {"message": "API executed. Script will self-delete now."}
    
    # Get current script path
    script_path = os.path.realpath(__file__)
    
    # Respond first, then delete script
    @app.after_request
    def shutdown_and_delete(response):
        try:
            os.remove(script_path)  # delete script
            print(f"{script_path} deleted.")
            os._exit(0)  # force stop the server
        except Exception as e:
            print(f"Error deleting script: {e}")
        return response

    return jsonify(response)

if __name__ == '__main__':
    app.run()
