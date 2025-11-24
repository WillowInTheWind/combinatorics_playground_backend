from flask import Flask, request, Response
import DatabaseHandeler
import SequenceHandeler
import io
from flask import send_file
from base64 import encodebytes
from flask import jsonify
import flask_cors
from flask_cors import CORS, cross_origin

from SequenceGenerator import n_such_that_there_are_k_sequences
import json

app = Flask(__name__)
cors = CORS(app) # allow CORS for all domains on all routes.

DEFAULT_N = 10
DEFAULT_R = 10
MAX_N =  100
MAX_R = 100
OBJECT_TO_SEQUENCE_TABLE = {
    "starfolkspaths": 0,
    "pixelstrips": 0,
    "dyck_words": 1,
"dyckpaths": 1,
    "fullparentheses": 1,
    "domino_tiling": 2,
    "nonattackingrooks": 0,
    "binarytrees": 1,

}
@app.route("/api/<combinatorial_sequence>/<combinatorial_object>/<method>")
def return_subsets_by_n_r(combinatorial_sequence, combinatorial_object, method):
    n = request.args.get("n")
    r = request.args.get("r")
    if n == "" or r == "":
        return Response(response = "failed to specify n or r ", status = 400)
    try:
        n = int(n)
        r = int(r)
    except TypeError:
        return Response(response = "n or r was not an integer", status = 400)
    if n < r:
        return Response(response = "r may not be greater than n", status = 400)
    if n > MAX_N:
        return Response(response = "n was to large", status = 400)
    try:
        bar = getattr(SequenceHandeler, combinatorial_object + "_by_" + method)
    except:
        return Response(response = "object reference incorrectly specified", status = 400)
    result = bar(n,r)

    print(f"REQUEST MADE - {n}, {r}, {len(result) }")
    return jsonify({'result': result})

@app.route("/sequences")
def all_sequences():
    return DatabaseHandeler.sequences()

if __name__ == "__main__":
    app.run()



@app.route("/api/fixed_total/<combinatorial_object>")
def return_cards_up_to_total_k( combinatorial_object):
    combinatorial_sequence = OBJECT_TO_SEQUENCE_TABLE[combinatorial_object]
    total = request.args.get("total")
    if total == "" :
        return Response(response = "failed to specify n or r ", status = 400)
    if total == "0" :
        return Response(response = "failed to specify n  ", status = 400)
    try:
        total = int(total)
    except TypeError:
        return Response(response = "n was not an integer", status = 400)
    if total > MAX_N:
        return Response(response = "n was to large", status = 400)
    try:
        bar = getattr(SequenceHandeler, combinatorial_object + "_up_to" )
    except:
        return Response(response = "object reference incorrectly specified", status = 400)
    result = bar(n_such_that_there_are_k_sequences(total, combinatorial_sequence))[0:total]

    print(f"REQUEST MADE - {total}, {len(result) }")
    return Response(json.dumps(result), status = 200)

