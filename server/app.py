from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/validate', methods=['POST'])
def validate():
    request_info = request.get_json()
    pod_name = request_info['request']['object']['metadata']['name']

    if 'badpod' in pod_name:
        return jsonify({
            "response": {
                "uid": request_info['request']['uid'],
                "allowed": False,
                "status": {
                    "message": f"Pod name '{pod_name}' is not allowed."
                }
            }
        })
    else:
        return jsonify({
            "response": {
                "uid": request_info['request']['uid'],
                "allowed": True
            }
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, ssl_context=('certs/cert.pem', 'certs/key.pem'))