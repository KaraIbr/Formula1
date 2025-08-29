// Función para cargar los datos
async function cargarDatos() {
    try {
        // Cargar datos de pilotos
        const respPilotos = await fetch('http://127.0.0.1:8000/pilotos/');
        const dataPilotos = await respPilotos.json();
        mostrarPilotos(dataPilotos.pilotos);

        // Cargar todos los datos
        const respTodo = await fetch('http://127.0.0.1:8000/');
        const dataTodo = await respTodo.json();
        mostrarSesiones(dataTodo.sesiones);
    } catch (error) {
        console.error('Error al cargar datos:', error);
    }
}

// Función para mostrar pilotos
function mostrarPilotos(pilotos) {
    const container = document.getElementById('lista-pilotos');
    container.innerHTML = pilotos.map(piloto => `
        <div class="piloto-card">
            <h3>${piloto.nombre_completo}</h3>
            <p>Equipo: ${piloto.equipo}</p>
            <p>Número: ${piloto.numero_carro}</p>
        </div>
    `).join('');
}

// Función para mostrar sesiones
function mostrarSesiones(sesiones) {
    const container = document.getElementById('lista-sesiones');
    container.innerHTML = sesiones.map(sesion => `
        <div class="sesion-card">
            <h3>${sesion.nombre_sesion}</h3>
            <p>Ubicación: ${sesion.ubicacion}</p>
            <p>Inicio: ${new Date(sesion.fecha_inicio).toLocaleString()}</p>
        </div>
    `).join('');
}

// Cargar datos cuando la página esté lista
document.addEventListener('DOMContentLoaded', cargarDatos);
