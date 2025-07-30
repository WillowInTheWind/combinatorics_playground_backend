from flask import Flask, request, Response
import DatabaseHandeler
import SequenceHandeler
import io
from flask import send_file
from base64 import encodebytes
from flask import jsonify


app = Flask(__name__)
DEFAULT_N = 10
DEFAULT_R = 10
MAX_N =  100
MAX_R = 100
@app.route("/api/<combinatorial_sequence>/<combinatorial_object>/<method>")
def return_subsets_by_n_r(combinatorial_sequence, combinatorial_object, method):
    n = request.args.get("n")
    r = request.args.get("r")
    # handle incorrect inputs
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
    encoded_imges = []

    #result[0].save("me.png")
    for image in result:
        byte_arr = io.BytesIO()
        image.save(byte_arr, format='PNG')  # convert the PIL image to byte array
        encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii')  # encode as base64
        encoded_imges.append(encoded_img)


    return jsonify({'result': encoded_imges})




# @app.route("/api/<combinatorial_sequence>/<combinatorial_object>/less-than")
# def return_subsets_by_n_r(combinatorial_sequence, combinatorial_object, method):
#     n = request.args.get("n")
#     r = request.args.get("r")
#     # handle incorrect inputs
#     if n == "" or r == "":
#         return Response(response = "failed to specify n or r ", status = 400)
#     try:
#         n = int(n)
#         r = int(r)
#     except TypeError:
#         return Response(response = "n or r was not an integer", status = 400)
#
#     if n < r:
#         return Response(response = "r may not be greater than n", status = 400)
#     if n > MAX_N:
#         return Response(response = "n was to large", status = 400)
#
#     try:
#         bar = getattr(SequenceHandeler, combinatorial_object + "_less_than_n")
#     except:
#         return Response(response = "object reference incorrect specified", status = 400)
#
#     result = bar(n,r)
#     return result
@app.route("/sequences")
def all_sequences():
    return DatabaseHandeler.sequences()
