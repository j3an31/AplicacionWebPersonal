# 🧟‍♂️ Left 4 Dead 2 - Guía Definitiva

> Aplicación web informativa tipo wiki sobre el videojuego Left 4 Dead 2, con sistema de registro de usuarios y panel de administración.

---

## 👨‍💻 Autor

**Gian Franco Apaza Quispe**

- 📧 Email: gapazaqui@unsa.edu.pe
- 🎓 Universidad: Universidad Nacional de San Agustín de Arequipa
- 📚 Curso: Introducción al Desarrollo Web
- 🗓️ Año: 2025

---

## 🔗 Links

- **Aplicación Web hospedada en GitHub:** [Visita el sitio](https://j3an31.github.io/AplicacionWebPersonal/)
- **Repositorio en GitHub:** [Ver código fuente](https://github.com/j3an31/AplicacionWebPersonal.git)

---

## 📖 Descripción

Esta aplicación web es una plataforma informativa tipo wiki del videojuego Left 4 Dead 2, que ofrece contenido detallado sobre supervivientes, infectados, campañas, armas y objetos del juego. Cuenta con una interfaz visual atractiva que incluye videos de fondo, galerías animadas y un carrusel interactivo. 

La aplicación integra funcionalidades frontend con HTML, CSS y JavaScript para validación de formularios, y un backend en Python que gestiona el almacenamiento de registros de usuarios en una base de datos MySQL, además de un panel de administración protegido para consultar los datos registrados.

**Desarrollado como proyecto final para el curso:** Introducción al Desarrollo Web

---

## ✨ Características

- 🎨 **6 páginas HTML** interconectadas con diseño responsive
- 🎬 **Video de fondo** en loop en todas las páginas
- 🎠 **Carrusel interactivo** para navegación de campañas
- 🖼️ **Galería infinita animada** de armas y objetos
- ✅ **Validación en tiempo real** de formularios con JavaScript
- 🐍 **Servidor backend** desarrollado en Python puro
- 🗄️ **Base de datos MySQL** para almacenamiento de registros
- 🔐 **Panel de administración** protegido con contraseña
- 📱 **Diseño responsive** con Flexbox y CSS Grid

---

## 🛠️ Tecnologías Utilizadas

### Frontend
- **HTML5** - Estructura de las páginas
- **CSS3** - Estilos y animaciones
  - Flexbox y CSS Grid para layouts
  - Animaciones CSS personalizadas
  - Video de fondo
- **JavaScript (ES6)** - Interactividad
  - Validación de formularios con RegEx
  - Carrusel de imágenes
  - Fetch API para comunicación con backend

### Backend
- **Python 3.x** - Lenguaje de programación
- **http.server** - Servidor HTTP integrado de Python
- **mysql-connector-python** - Conector para MySQL

### Base de Datos
- **MySQL** - Sistema de gestión de bases de datos
- **phpMyAdmin** - Interfaz web para administrar MySQL

### Herramientas
- **XAMPP** - Paquete de servidor (MySQL + Apache)
- **Git & GitHub** - Control de versiones

---

## 📦 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

### 1. Python 3.7 o superior
- **Descargar:** [python.org/downloads](https://www.python.org/downloads/)
- **Verificar instalación:**
  ```bash
  python --version
  ```
  o
  ```bash
  python3 --version
  ```

### 2. XAMPP
- **Descargar:** [apachefriends.org](https://www.apachefriends.org/)
- Incluye MySQL y phpMyAdmin
- No requiere configuración adicional

### 3. Git (opcional, para clonar el repositorio)
- **Descargar:** [git-scm.com](https://git-scm.com/)

---

## 🚀 Instalación

### Paso 1: Clonar o descargar el repositorio

**Opción A - Con Git:**
```bash
git clone https://github.com/j3an31/AplicacionWebPersonal.git
cd AplicacionWebPersonal
```

**Opción B - Descarga directa:**
1. Ve a [github.com/j3an31/AplicacionWebPersonal](https://github.com/j3an31/AplicacionWebPersonal)
2. Haz clic en **"Code"** → **"Download ZIP"**
3. Extrae el archivo ZIP en tu carpeta de proyectos

### Paso 2: Instalar dependencias de Python

Abre la terminal en la carpeta del proyecto y ejecuta:

```bash
pip install mysql-connector-python
```

Si tienes problemas con `pip`, intenta:
```bash
python -m pip install mysql-connector-python
```

o

```bash
python3 -m pip install mysql-connector-python
```

---

## ⚙️ Configuración

### 1. Configurar XAMPP

1. **Abre XAMPP Control Panel**
2. Haz clic en **"Start"** en:
   - ✅ **MySQL** (obligatorio - base de datos)
   - ✅ **Apache** (necesario para phpMyAdmin)
3. Espera a que ambos servicios se pongan en **verde** ("Running")

### 2. Crear la base de datos

Tienes **dos opciones**:

#### Opción A - Automática (recomendada)
El servidor Python creará automáticamente la base de datos al iniciarse por primera vez. **No necesitas hacer nada más.**

#### Opción B - Manual (con phpMyAdmin)
1. Abre tu navegador
2. Ve a: `http://localhost/phpmyadmin`
3. Haz clic en la pestaña **"SQL"**
4. Copia y pega el contenido del archivo `database.sql`
5. Haz clic en **"Continuar"**

**Contenido de database.sql:**
```sql
CREATE DATABASE IF NOT EXISTS left4dead_db;

USE left4dead_db;

CREATE TABLE IF NOT EXISTS registros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    correo VARCHAR(100) NOT NULL,
    nombre_usuario VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL,
    fecha_registro DATETIME NOT NULL
);
```

### 3. Configurar credenciales de MySQL (si es necesario)

Si tu instalación de MySQL tiene contraseña, edita el archivo `server.py`:

```python
# Líneas 6-9
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''  # ← Cambia aquí si tienes contraseña
DB_NAME = 'left4dead_db'
```

**Nota:** XAMPP por defecto **NO tiene contraseña**, así que puedes dejarlo vacío (`''`).

---

## ▶️ Ejecución

### Paso 1: Asegúrate de que XAMPP esté corriendo

- ✅ MySQL debe estar en **verde** (Running)
- ✅ Apache debe estar en **verde** (Running)

### Paso 2: Inicia el servidor Python

1. Abre la terminal en la carpeta del proyecto
2. Ejecuta:

```bash
python server.py
```

o si tienes Python 3:

```bash
python3 server.py
```

3. Deberías ver algo como:

```
Iniciando servidor...
--------------------------------------------------
Base de datos creada o ya existia
Tabla creada o ya existia
--------------------------------------------------
Servidor corriendo en: http://localhost:8000
Panel de Admin: http://localhost:8000/admin
Contraseña de Admin: admin123
--------------------------------------------------
Presiona Ctrl+C para detener
```

**⚠️ IMPORTANTE:** No cierres esta terminal mientras uses la aplicación.

### Paso 3: Accede a la aplicación

Abre tu navegador y ve a:

**🌐 Página Principal:**
```
file:///ruta/a/tu/proyecto/paginaPersonal.html
```

o simplemente abre el archivo `paginaPersonal.html` desde tu explorador de archivos.

**🔧 Servidor Backend:**
```
http://localhost:8000
```

**🔐 Panel de Administración:**
```
http://localhost:8000/admin
```
- **Contraseña:** `admin123`

---

## 📁 Estructura del Proyecto

```
AplicacionWebPersonal/
│
├── 📄 server.py                    # Servidor backend en Python
├── 📄 database.sql                 # Script SQL para crear la BD
├── 📄 README.md                    # Este archivo
│
├── 📄 paginaPersonal.html          # Página principal (home)
├── 📄 supervivientes.html          # Información de supervivientes
├── 📄 infectados.html              # Información de infectados
├── 📄 campañas.html                # Campañas con carrusel
├── 📄 armasYobjetos.html           # Armas con galería animada
├── 📄 registrar.html               # Formulario de registro
│
├── 📁 css/
│   ├── styles.css                  # Estilos principales
│   ├── campañas.css                # Estilos del carrusel
│   ├── armasYobjetos.css           # Estilos de la galería
│   └── registrar.css               # Estilos del formulario
│
├── 📁 JavaScript/
│   ├── campañas.js                 # Lógica del carrusel
│   └── registrar.js                # Validación y envío al backend
│
└── 📁 Extras/
    ├── zombies-moviendose.mp4      # Video de fondo
    ├── l4d2-logo.webp              # Logo del juego
    ├── 📁 supervivientes-img/      # Imágenes de personajes
    ├── 📁 armas-img/                # Imágenes de armas
    ├── 📁 objetos-img/              # Imágenes de objetos
    └── 📁 mapas-img/                # Imágenes de campañas
```

---

## 🎯 Funcionalidades

### 1. **Navegación y Diseño**
- Navegación sticky con 6 secciones interconectadas
- Video de fondo en loop en todas las páginas
- Diseño responsive con Flexbox y CSS Grid
- Efectos hover y transiciones suaves

### 2. **Carrusel Interactivo**
Ubicado en la página de **Campañas**:
- Navegación con botones anterior/siguiente
- Indicadores clicables
- Navegación con teclas de flecha (← →)
- Animaciones de transición suaves

### 3. **Galería Infinita Animada**
Ubicada en la página de **Armas y Objetos**:
- Desplazamiento automático continuo
- Efecto de bucle infinito
- Se pausa al pasar el cursor

### 4. **Validación de Formulario**
Ubicado en la página de **Registro**:
- **Correo:** Formato válido (ejemplo@dominio.com)
- **Usuario:** 3-10 caracteres, debe iniciar con letra
- **Contraseña:** 6-10 caracteres, con mayúscula, minúscula y número
- **Confirmar:** Debe coincidir con la contraseña
- Mensajes de error en tiempo real
- Efectos visuales en campos inválidos

### 5. **Sistema de Registro**
- Envío de datos al servidor Python mediante Fetch API
- Almacenamiento en base de datos MySQL
- Validación de duplicados (correo y usuario únicos)
- Confirmación visual con alert

### 6. **Panel de Administración**
Acceso en: `http://localhost:8000/admin`
- Autenticación con contraseña
- Visualización de todos los registros
- Tabla dinámica con:
  - ID
  - Correo electrónico
  - Nombre de usuario
  - Fecha de registro
- Ordenados del más reciente al más antiguo

---

## 🐛 Solución de Problemas

### Problema 1: "No module named 'mysql.connector'"

**Solución:**
```bash
pip install mysql-connector-python
```

### Problema 2: "Can't connect to MySQL server"

**Causas posibles:**
- MySQL no está corriendo en XAMPP
- Puerto 3306 ocupado por otro programa

**Solución:**
1. Abre XAMPP Control Panel
2. Verifica que MySQL esté en **verde** (Running)
3. Si no inicia, haz clic en "Config" → "my.ini" y verifica el puerto

### Problema 3: "Access denied for user 'root'"

**Solución:**
1. Abre `server.py`
2. Verifica la línea 8:
   ```python
   DB_PASSWORD = ''  # Debe estar vacío para XAMPP
   ```

### Problema 4: El formulario no envía datos / Error de CORS

**Solución:**
1. Verifica que el servidor Python esté corriendo (`python server.py`)
2. Abre la consola del navegador (F12) y busca errores
3. Si hay error de CORS, abre Chrome con:
   ```bash
   chrome.exe --disable-web-security --user-data-dir="C:/temp/chrome"
   ```

### Problema 5: No se ve phpMyAdmin

**Solución:**
1. Verifica que **Apache** esté corriendo en XAMPP (debe estar en verde)
2. Ve a: `http://localhost/phpmyadmin`

### Problema 6: "Port 8000 already in use"

**Solución:**
Cambia el puerto en `server.py` (línea final):
```python
servidor = HTTPServer(('localhost', 8080), ServidorHTTP)  # Cambia 8000 por 8080
```

---

## 🎓 Uso del Sistema

### Para Usuarios Finales

1. **Navegar por el sitio:**
   - Usa el menú superior para cambiar entre secciones
   - Explora información de personajes, enemigos y mapas

2. **Registrarse:**
   - Ve a "Registrarse" en el menú
   - Llena el formulario con tus datos
   - Haz clic en "Unirse"
   - Verás un mensaje de confirmación si el registro fue exitoso

3. **Consejos:**
   - Usa flechas del teclado (← →) en la página de Campañas
   - Pasa el cursor sobre las armas para pausar la galería

### Para Administradores

1. **Acceder al panel:**
   - Ve a: `http://localhost:8000/admin`
   - Ingresa la contraseña: `admin123`

2. **Consultar registros:**
   - Haz clic en "Ver Registros"
   - Verás una tabla con todos los usuarios registrados

3. **Ver datos en phpMyAdmin:**
   - Ve a: `http://localhost/phpmyadmin`
   - Selecciona la base de datos `left4dead_db`
   - Haz clic en la tabla `registros`

---

## ✨ Palabras Finales

Gracias por explorar este proyecto. Estaré trabajando continuamente para mejorar la experiencia y añadir nuevas funcionalidades, al mismo tiempo que adquiero nuevos conocimientos, con el objetivo de ser mejor cada día.
Si tienes alguna sugerencia o encuentras algún error, no dudes en abrir un *issue* o contactarme. Tus comentarios y sugerencias son siempre bienvenidos.
