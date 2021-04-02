from flask import Flask, jsonify, request
from products import products 
from flask_cors import CORS, cross_origin

app = Flask (__name__)
cors=CORS(app)


@app.route("/")
@cross_origin()
def helloWorld():
  return "Hello,this is the main page!"


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
        "id": request.json['id'],
        "name": request.json ['name'],
        "price": request.json ['price'],
        "quantity": request.json ['quantity'],
        "url": request.json ['url_image']
    }
    
    #guardar en la db
    products.append(newproduct)

    
    return jsonify ({"Lista nueva": products})

# Actualizar productos 
@app.route ('/update_products/<string:id>', methods=['PUT'])
def updateProduct(id):
    
    productFound = [product for product in products if product['id']==id]
    if (len(productFound)>0):
        productFound[0]['id'] = request.json ['id']
        productFound[0]['name'] = request.json ['name']
        productFound[0]['price'] = request.json ['price']
        productFound[0]['quantity'] = request.json ['quantity']
        productFound[0]['url_image']= request.json ['url_image']
        
        return jsonify ({
            "message": "Product Update Succesfully",
            "product": productFound[0]
        })
    return jsonify({"message": "Product not found"})   
 
 #Eliminar productos
 
@app.route('/delete/<string:id>' , methods=['DELETE'])
def deleteProduct(id):
    productFound = [product for product in products if product ['id']==id]
    if (len(productFound)>0):
        products.remove(productFound[0])
        
        return jsonify({
            "message": "Product removed",
            "productos": products
            })
    return jsonify({"message": "Product not found"})


if __name__  == '__main__':
    app.run (debug=True,port=4000)