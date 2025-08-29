# Formula 1 Data Viewer

Aplicación web para visualizar datos de la Fórmula 1, incluyendo información de pilotos y sesiones de carrera.

## Características

- Visualización de datos de pilotos:
  - Información personal (nombre, equipo, país, edad)
  - Estadísticas (puntos, victorias, podios, poles)
  - Filtrado por nombre, equipo y país
  - Paginación de resultados

- Visualización de sesiones:
  - Detalles de la sesión (tipo, ubicación, fecha)
  - Información del circuito (longitud, vueltas)
  - Condiciones climáticas (temperatura, viento, clima)
  - Filtrado por nombre, ubicación y tipo
  - Paginación de resultados

## Tecnologías Utilizadas

- Backend:
  - Django 5.2.5
  - SQLite3 para base de datos
  - Sistema de comandos personalizados para carga de datos

- Frontend:
  - HTML5 con etiquetas semánticas
  - CSS3 con diseño responsive
  - JavaScript vanilla para interactividad
  - Fetch API para consumo de datos

## Estructura del Proyecto

```
formular1/
├── formular1/           # Configuración principal de Django
├── races/               # Aplicación principal
│   ├── data/           # Datos JSON
│   ├── management/     # Comandos personalizados
│   ├── static/         # Archivos estáticos
│   │   └── races/
│   │       ├── css/    # Estilos CSS
│   │       └── js/     # JavaScript
│   └── templates/      # Templates HTML
└── requirements.txt    # Dependencias del proyecto
```

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone <url-repositorio>
   cd Formula1
   ```

2. Crear y activar entorno virtual:
   ```bash
   python -m venv .venv
   # En Windows:
   .venv\Scripts\activate
   # En Unix:
   source .venv/bin/activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Aplicar migraciones:
   ```bash
   cd formular1
   python manage.py migrate
   ```

5. Cargar datos iniciales:
   ```bash
   python manage.py cargar_datos_json
   ```

6. Iniciar servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

7. Visitar http://127.0.0.1:8000/ en el navegador

## Estructura de Archivos Estáticos

- `races/static/races/css/main.css`: Estilos principales
  - Diseño responsive
  - Variables CSS para colores
  - Animaciones y transiciones
  - Grid layout para cards

- `races/static/races/js/main.js`: JavaScript
  - Filtrado en tiempo real
  - Paginación dinámica
  - Manejo de eventos
  - Fetch de datos

## Modelos de Datos

### Piloto
- Información personal (nombre, equipo, país)
- Estadísticas de carrera (puntos, podios, victorias)
- Ordenamiento por puntos

### Sesión
- Detalles de la sesión
- Información del circuito
- Datos meteorológicos
- Ordenamiento por fecha

## Características de Implementación

1. **Semántica HTML5**
   - Uso de `header`, `section`, `footer`
   - Estructura clara y accesible
   - Atributos data para JavaScript

2. **Estilos CSS**
   - Archivo CSS separado
   - Variables CSS
   - Media queries para responsive
   - Animaciones y transiciones

3. **JavaScript**
   - Archivo JS separado
   - Eventos del DOM
   - Fetch API
   - Manipulación dinámica

4. **Django**
   - Modelos bien definidos
   - Sistema de rutas
   - Templates con herencia
   - Comandos personalizados

## Autor

[Tu Nombre]

## Licencia

MIT