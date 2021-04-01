from flask import Flask, jsonify, request
from products import products 
from flask_cors import CORS, cross_origin

app = Flask (__name__)
cors=CORS(app)


@app.route("/")
@cross_origin()
def helloWorld():
  return "Hello, cross-origin-world!"


#Entregamos los datos de la db metodo GET 
@app.route('/products', methods=['GET'])
def getProducts ():
    return jsonify(products)

#buscamos un dato especifico 
@app.route ('/products/<string:name>', methods=['GET'])
def getProduct (name):
    productfound = [product for product in products if product['name']==name]
    if (len(productfound)>0):
        return jsonify({"Producto": productfound[0]})
    
    return jsonify({"message": "Product not found"})

#Añadir datos 
@app.route ('/adding', methods=['POST'])
def addProduct ():
    newproduct = {
        "name": request.json ['name'],
        "price": request.json ['price'],
        "quantity": request.json ['quantity']
    }
    
    #guardar en la db
    products.append(newproduct)
    
    print (newproduct)
    return jsonify ({"Lista nueva": products})

if __name__  == '__main__':
    app.run ( port=4000)