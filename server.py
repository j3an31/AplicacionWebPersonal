from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import mysql.connector

# Configuracion de la base de datos
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''  # En XAMPP la contraseña por defecto esta vacia
DB_NAME = 'left4dead_db'

# Contraseña para ver los registros (pagina de admin)
PASSWORD_ADMIN = 'admin123'

# Funcion para conectar con MySQL
def conectar_db():
    try:
        conexion = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conexion
    except mysql.connector.Error as error:
        print("Error al conectar:", error)
        return None


# Funcion para crear la base de datos y tabla si no existen
def crear_base_datos():
    try:
        # Primero se conecta sin especificar la base de datos
        conexion = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conexion.cursor()
        
        # Crea la base de datos
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        print("Base de datos creada o ya existia")
        
        # Ahora usamos la base de datos
        cursor.execute(f"USE {DB_NAME}")
        
        # Crea la tabla de registros
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS registros (
                id INT AUTO_INCREMENT PRIMARY KEY,
                correo VARCHAR(100) NOT NULL,
                nombre_usuario VARCHAR(50) NOT NULL,
                password VARCHAR(100) NOT NULL,
                fecha_registro DATETIME NOT NULL
            )
        """)
        print("Tabla creada o ya existia")
        
        conexion.commit()
        cursor.close()
        conexion.close()
    except mysql.connector.Error as error:
        print("Error creando base de datos:", error)


# Funcion para guardar un nuevo registro en la base de datos
def guardar_en_db(correo, usuario, password):
    conexion = conectar_db()
    if conexion is None:
        return False
    
    try:
        cursor = conexion.cursor()
        
        # Obtenemos la fecha actual
        from datetime import datetime
        fecha = datetime.now()
        
        # Insertamos el registro
        query = "INSERT INTO registros (correo, nombre_usuario, password, fecha_registro) VALUES (%s, %s, %s, %s)"
        valores = (correo, usuario, password, fecha)
        cursor.execute(query, valores)
        
        conexion.commit()
        cursor.close()
        conexion.close()
        print(f"Registro guardado: {usuario}")
        return True
    except mysql.connector.Error as error:
        print("Error al guardar:", error)
        return False


# Funcion para obtener todos los registros
def obtener_registros():
    conexion = conectar_db()
    if conexion is None:
        return []
    
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT id, correo, nombre_usuario, fecha_registro FROM registros ORDER BY id DESC")
        registros = cursor.fetchall()
        cursor.close()
        conexion.close()
        return registros
    except mysql.connector.Error as error:
        print("Error al obtener registros:", error)
        return []


# Clase principal del servidor
class ServidorHTTP(BaseHTTPRequestHandler):
    
    # Maneja las peticiones GET (cuando pides una pagina)
    def do_GET(self):
        # Pagina principal del servidor
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html = """
            <html>
            <head>
                <title>Servidor Left 4 Dead</title>
                <style>
                    body {
                        font-family: Arial;
                        background: #2c3e50;
                        color: white;
                        text-align: center;
                        padding: 50px;
                    }
                    h1 { color: #3498db; }
                    a {
                        display: inline-block;
                        margin: 20px;
                        padding: 15px 30px;
                        background: #3498db;
                        color: white;
                        text-decoration: none;
                        border-radius: 5px;
                    }
                </style>
            </head>
            <body>
                <h1>Servidor Backend - Left 4 Dead</h1>
                <p>El servidor esta funcionando correctamente</p>
                <a href="/admin">Ver Registros (Admin)</a>
            </body>
            </html>
            """
            self.wfile.write(html.encode())
        
        # Pagina de administracion
        elif self.path == '/admin':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.pagina_admin().encode())
        
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>404 - Pagina no encontrada</h1>')
    
    
    # Maneja las peticiones POST (cuando se envía datos de un formulario)
    def do_POST(self):
        # Obtenemos el tamaño de los datos
        content_length = int(self.headers['Content-Length'])
        # Leemos los datos
        post_data = self.rfile.read(content_length)
        
        # Si es el formulario de registro
        if self.path == '/registro':
            # Decodificamos los datos del formulario
            datos = urllib.parse.parse_qs(post_data.decode('utf-8'))
            
            correo = datos['correo'][0]
            nombre = datos['nombre'][0]
            password = datos['password'][0]
            
            # Guardamos en la base de datos
            if guardar_en_db(correo, nombre, password):
                respuesta = "OK"
            else:
                respuesta = "ERROR"
            
            # Enviamos la respuesta
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(respuesta.encode())
        
        # Si es la verificacion de contraseña del admin
        elif self.path == '/verificar-admin':
            datos = urllib.parse.parse_qs(post_data.decode('utf-8'))
            password = datos['password'][0]
            
            if password == PASSWORD_ADMIN:
                # Obtenemos los registros
                registros = obtener_registros()
                
                # Creamos el HTML de la tabla
                html_tabla = "<h2>Registros de Usuarios</h2>"
                html_tabla += f"<p>Total de registros: {len(registros)}</p>"
                html_tabla += "<table border='1' style='width:100%; border-collapse: collapse;'>"
                html_tabla += "<tr style='background: #3498db;'><th>ID</th><th>Correo</th><th>Usuario</th><th>Fecha</th></tr>"
                
                for reg in registros:
                    html_tabla += f"<tr><td>{reg[0]}</td><td>{reg[1]}</td><td>{reg[2]}</td><td>{reg[3]}</td></tr>"
                
                html_tabla += "</table>"
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(html_tabla.encode())
            else:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<p style='color: red;'>Contrasena incorrecta</p>")
    
    
    # Pagina HTML para el panel de administracion
    def pagina_admin(self):
        return """
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Panel de Administracion</title>
            <style>
                body {
                    font-family: Arial;
                    background: #34495e;
                    color: white;
                    padding: 20px;
                }
                .contenedor {
                    max-width: 1000px;
                    margin: 0 auto;
                    background: white;
                    color: black;
                    padding: 30px;
                    border-radius: 10px;
                }
                input {
                    padding: 10px;
                    width: 200px;
                    margin: 10px;
                }
                button {
                    padding: 10px 20px;
                    background: #3498db;
                    color: white;
                    border: none;
                    cursor: pointer;
                }
                button:hover {
                    background: #2980b9;
                }
                table {
                    margin-top: 20px;
                    width: 100%;
                }
                th, td {
                    padding: 10px;
                    text-align: left;
                    color: black;
                }
                th {
                    background: #3498db;
                    color: white;
                }
            </style>
        </head>
        <body>
            <div class="contenedor">
                <h1>Panel de Administración</h1>
                <p>Ingresa la contraseña para ver los registros:</p>
                <input type="password" id="password" placeholder="Contraseña">
                <button onclick="verificar()">Ver Registros</button>
                
                <div id="resultado"></div>
            </div>
            
            <script>
                function verificar() {
                    var password = document.getElementById('password').value;
                    
                    if (password == '') {
                        alert('Ingresa una contraseña');
                        return;
                    }
                    
                    fetch('/verificar-admin', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded',
                        },
                        body: 'password=' + password
                    })
                    .then(response => response.text())
                    .then(data => {
                        document.getElementById('resultado').innerHTML = data;
                    })
                    .catch(error => {
                        alert('Error de conexion');
                    });
                }
            </script>
        </body>
        </html>
        """
    
    # Para no mostrar tanto log en la consola
    def log_message(self, format, *args):
        print(f"{self.address_string()} - {format % args}")


# Funcion principal para iniciar el servidor
def iniciar_servidor():
    print("Iniciando servidor...")
    print("-" * 50)
    
    # Creamos la base de datos y tabla
    crear_base_datos()
    
    print("-" * 50)
    print("Servidor corriendo en: http://localhost:8000")
    print("Panel de Admin: http://localhost:8000/admin")
    print("Contraseña de Admin:", PASSWORD_ADMIN)
    print("-" * 50)
    print("Presiona Ctrl+C para detener")
    print()
    
    # Iniciamos el servidor en el puerto 8000
    servidor = HTTPServer(('localhost', 8000), ServidorHTTP)
    
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido")
        servidor.server_close()


# Ejecutamos el servidor
if __name__ == '__main__':
    iniciar_servidor()