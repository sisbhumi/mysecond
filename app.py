from flask import Flask, request, jsonify
from collections import OrderedDict
import json

app = Flask(__name__)


@app.get("/")
def get_countries():
    return {"message" : "Hello World"}


@app.post("/bhfl")
def post_request():
    if request.is_json:
        data = request.get_json()
        _list = data['data']
        _num_list = []
        _alpha_list = []
        success = True
        for i in _list:
            if str(i).isalnum():
                if str(i).isdigit():
                    _num_list.append(int(i))
                elif str(i).isalpha():
                    _alpha_list.append(i)
        od  = OrderedDict({
            "is_success": "true",
            "user_id": "vaishnavi_munjewar_31032001",
            "email": "vaishnavimunjewar03@gmail.com",
            "roll_number": "0827CI191062",
            "numbers": json.dumps(_num_list),
            "alphabets": json.dumps(_alpha_list)
        })
        return  od
        """
            {
            "is_success": "true",
            "user_id": "vaishnavi_munjewar_31032001",
            "email": "vaishnavimunjewar03@gmail.com",
            "roll_number": "0827CI191062",
            "numbers": json.dumps(_num_list),
            "alphabets": json.dumps(_alpha_list)
        }, 201
        """
    return {"is_success": False}


if __name__ == '__main__':
    app.run(debug=True)
