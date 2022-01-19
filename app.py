from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask import jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
_port = os.environ.get('PORT',5000)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config['MYSQL_HOST'] = 'cursophp.com.ar'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fullstack'
app.config['MYSQL_DB'] = 'cv'
mysql = MySQL(app)


@app.route('/')
def inicial():
			cur = mysql.connection.cursor()
			cur.execute('SELECT * FROM referencias')
			mysql.connection.commit()
			datos = cur.fetchall()
			listado=[]
			contenido={}
			for resultado in datos:
				contenido = {'id': resultado[0], 'nombre': resultado[1], 'cargo': resultado[2]
				, 'empresa': resultado[3], 'email': resultado[4]}
				listado.append(contenido)
				contenido = {}
			return jsonify(listado)
			
@app.route('/datos')
def datos():
			cur = mysql.connection.cursor()
			cur.execute('SELECT texto FROM datos')
			mysql.connection.commit()
			datos = cur.fetchall()
			listado=[]
			contenido={}
			for resultado in datos:
				contenido = {'texto': resultado[0]}
				listado.append(contenido)
				contenido = {}
			return jsonify(listado)			

@app.route('/nuevo', methods=['POST'])	
@cross_origin()	
def nuevo():
		if request.method == 'POST':
			request_data = request.get_json()
			nombre = request_data['nombre']
			email =request_data['email']
			mensaje=request_data['mensaje']
			cur = mysql.connection.cursor()
			cur.execute('INSERT INTO mensajes (nombre,email,mensaje) VALUES (%s, %s, %s)', (nombre,email,mensaje) )			
			mysql.connection.commit()
			return "Guardado OK"
					
			
if __name__	== '__main__':
			app.run(host='0.0.0.0',port=_port)
			
