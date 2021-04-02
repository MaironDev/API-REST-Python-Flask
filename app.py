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
@app.route ('/add_products', methods=['POST'])
def addProduct ():
    newproduct = {
        "name": request.json ['name'],
        "price": request.json ['price'],
        "quantity": request.json ['quantity']
    }
    
    #guardar en la db
    products.append(newproduct)

    
    return jsonify ({"Lista nueva": products})

# Actualizar productos 
@app.route ('/update_products/<string:name>', methods=['PUT'])
def updateProduct(name):
    
    productFound = [product for product in products if product['name']==name]
    if (len(productFound)>0):
        productFound[0]['name'] = request.json ['name']
        productFound[0]['price'] = request.json ['price']
        productFound[0]['quantity'] = request.json ['quantity']
        
        return jsonify ({
            "message": "Product Update Succesfully",
            "product": productFound[0]
        })
    return jsonify({"message": "Product not found"})   
 
 #Eliminar productos
 
@app.route('/delete/<string:name>' , methods=['DELETE'])
def deleteProduct(name):
    productFound = [product for product in products if product ['name']==name]
    if (len(productFound)>0):
        products.remove(productFound[0])
        
        return jsonify({
            "message": "Product removed",
            "productos": products
            })
    return jsonify({"message": "Product not found"})


if __name__  == '__main__':
    app.run (debug=True,port=4000)