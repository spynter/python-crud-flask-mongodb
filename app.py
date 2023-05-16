from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase
from producto import Producto

db = dbase.dbConnection()

app = Flask(__name__,template_folder='templates')

#Rutas de la app
@app.route('/')
def home():
    productos = db['productos']
    productosRecibidos = productos.find()
    return render_template('index.html', productos = productosRecibidos)

#Metodo Post
@app.route('/productos', methods=['POST'])
def addProduct():
    productos = db['productos']
    nombre = request.form['nombre']
    precio = request.form['precio']
    cantidad = request.form['cantidad']

    if nombre and precio and cantidad:
        producto = Producto(nombre,precio,cantidad)
        productos.insert_one(producto.toDBCollection())
        response = jsonify({
            'nombre' : nombre,
            'precio' : precio,
            'cantidad' : cantidad
        })
        return redirect(url_for('home'))
    else:
        return notFound()

#Metodo Delete
@app.route('/delete/<string:producto_nombre>')
def delete(producto_nombre):
    productos = db['productos']
    productos.delete_one({'nombre' : producto_nombre})
    return redirect(url_for('home'))

#Metodo Put
@app.route('/edit/<string:producto_nombre>', methods=['POST'])
def edit(producto_nombre):
    productos = db['productos']
    nombre = request.form['nombre']
    precio = request.form['precio']
    cantidad = request.form['cantidad']

    if nombre and precio and cantidad:
        productos.update_one({'nombre' : producto_nombre}, {'$set' : {'nombre' : nombre, 'precio' : precio, 'cantidad' : cantidad}})
        response = jsonify({'mensaje' : 'producto' + producto_nombre + 'actualizado correctamente'})
        return redirect(url_for('home'))
    else:
        return notFound()

@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'no encontrado' + request.url,
        'status': '404 not found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True, port=4000)