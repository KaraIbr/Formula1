// Variables de paginación
const elementosPorPagina = 5;
let paginaActualPilotos = 1;
let paginaActualSesiones = 1;

function actualizarPaginacion(items, paginaActual, contenedor, infoContainer) {
    const totalPaginas = Math.ceil(items.length / elementosPorPagina);
    const inicio = (paginaActual - 1) * elementosPorPagina;
    const fin = inicio + elementosPorPagina;

    items.forEach((item, index) => {
        item.classList.toggle('hidden', index < inicio || index >= fin);
    });

    const anteriorBtn = contenedor.querySelector('button:first-child');
    const siguienteBtn = contenedor.querySelector('button:last-child');
    anteriorBtn.disabled = paginaActual === 1;
    siguienteBtn.disabled = paginaActual === totalPaginas;

    infoContainer.textContent = `Página ${paginaActual} de ${totalPaginas}`;
}

function filtrarPilotos() {
    const busqueda = document.getElementById('buscarPiloto').value.toLowerCase();
    const equipo = document.getElementById('filtroEquipo').value;
    const pais = document.getElementById('filtroPais').value;
    const pilotos = document.querySelectorAll('#lista-pilotos .piloto-card');
    let contadorVisible = 0;
    let pilotosVisibles = [];

    pilotos.forEach(piloto => {
        const nombre = piloto.getAttribute('data-nombre');
        const equipoPiloto = piloto.getAttribute('data-equipo');
        const paisPiloto = piloto.getAttribute('data-pais');
        
        const coincideBusqueda = nombre.includes(busqueda);
        const coincideEquipo = !equipo || equipoPiloto === equipo;
        const coincidePais = !pais || paisPiloto === pais;
        
        const visible = coincideBusqueda && coincideEquipo && coincidePais;
        piloto.classList.toggle('hidden', !visible);
        if (visible) {
            contadorVisible++;
            pilotosVisibles.push(piloto);
        }
    });

    document.getElementById('pilotosCount').textContent = 
        `Mostrando ${contadorVisible} piloto${contadorVisible !== 1 ? 's' : ''}`;
    
    paginaActualPilotos = 1;
    actualizarPaginacion(
        pilotosVisibles,
        paginaActualPilotos,
        document.getElementById('paginacionPilotos'),
        document.getElementById('infoPaginacionPilotos')
    );
}

function filtrarSesiones() {
    const busqueda = document.getElementById('buscarSesion').value.toLowerCase();
    const ubicacion = document.getElementById('filtroUbicacion').value;
    const tipo = document.getElementById('filtroTipoSesion').value;
    const sesiones = document.querySelectorAll('#lista-sesiones .sesion-card');
    let contadorVisible = 0;
    let sesionesVisibles = [];

    sesiones.forEach(sesion => {
        const nombre = sesion.getAttribute('data-nombre');
        const ubicacionSesion = sesion.getAttribute('data-ubicacion');
        const tipoSesion = sesion.getAttribute('data-tipo');
        
        const coincideBusqueda = nombre.includes(busqueda);
        const coincideUbicacion = !ubicacion || ubicacionSesion === ubicacion;
        const coincideTipo = !tipo || tipoSesion === tipo;
        
        const visible = coincideBusqueda && coincideUbicacion && coincideTipo;
        sesion.classList.toggle('hidden', !visible);
        if (visible) {
            contadorVisible++;
            sesionesVisibles.push(sesion);
        }
    });

    document.getElementById('sesionesCount').textContent = 
        `Mostrando ${contadorVisible} sesión${contadorVisible !== 1 ? 'es' : ''}`;
    
    paginaActualSesiones = 1;
    actualizarPaginacion(
        sesionesVisibles,
        paginaActualSesiones,
        document.getElementById('paginacionSesiones'),
        document.getElementById('infoPaginacionSesiones')
    );
}

function cambiarPaginaPilotos(delta) {
    const pilotosVisibles = Array.from(document.querySelectorAll('#lista-pilotos .piloto-card'))
        .filter(p => !p.classList.contains('hidden'));
    const totalPaginas = Math.ceil(pilotosVisibles.length / elementosPorPagina);
    
    paginaActualPilotos = Math.max(1, Math.min(paginaActualPilotos + delta, totalPaginas));
    
    actualizarPaginacion(
        pilotosVisibles,
        paginaActualPilotos,
        document.getElementById('paginacionPilotos'),
        document.getElementById('infoPaginacionPilotos')
    );
}

function cambiarPaginaSesiones(delta) {
    const sesionesVisibles = Array.from(document.querySelectorAll('#lista-sesiones .sesion-card'))
        .filter(s => !s.classList.contains('hidden'));
    const totalPaginas = Math.ceil(sesionesVisibles.length / elementosPorPagina);
    
    paginaActualSesiones = Math.max(1, Math.min(paginaActualSesiones + delta, totalPaginas));
    
    actualizarPaginacion(
        sesionesVisibles,
        paginaActualSesiones,
        document.getElementById('paginacionSesiones'),
        document.getElementById('infoPaginacionSesiones')
    );
}

// Eliminar duplicados en los selectores
window.onload = function() {
    ['filtroEquipo', 'filtroPais', 'filtroUbicacion', 'filtroTipoSesion'].forEach(id => {
        const select = document.getElementById(id);
        const opciones = new Set();
        Array.from(select.options).forEach(option => {
            if (option.value && opciones.has(option.value)) {
                option.remove();
            } else {
                opciones.add(option.value);
            }
        });
    });

    // Inicializar paginación
    filtrarPilotos();
    filtrarSesiones();
};
