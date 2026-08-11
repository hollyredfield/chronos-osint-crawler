document.getElementById('searchForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const url = document.getElementById('url').value;
    const date = document.getElementById('date').value;
    
    // Recolectar módulos seleccionados
    const checkboxes = document.querySelectorAll('input[name="module"]:checked');
    const modules = Array.from(checkboxes).map(cb => cb.value);
    
    if (modules.length === 0) {
        alert('Por favor selecciona al menos un módulo de búsqueda.');
        return;
    }
    
    // UI Updates: Loading state
    const submitBtn = document.getElementById('submitBtn');
    const btnText = submitBtn.querySelector('.btn-text');
    const spinner = submitBtn.querySelector('.spinner');
    const resultsPanel = document.getElementById('resultsPanel');
    const timelineContainer = document.getElementById('timelineContainer');
    const resultsCount = document.getElementById('resultsCount');
    const previewContainer = document.getElementById('previewContainer');
    
    btnText.textContent = 'RASTREANDO...';
    spinner.classList.remove('hidden');
    submitBtn.disabled = true;
    
    // Limpiar resultados anteriores
    timelineContainer.innerHTML = '';
    previewContainer.innerHTML = `
        <div class="placeholder">
            <span class="icon">⌛</span>
            <p>Generando renderizado de la captura...</p>
        </div>
    `;
    
    try {
        const response = await fetch('/api/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                url: url,
                target_date: date,
                modules: modules
            })
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            resultsPanel.classList.remove('hidden');
            resultsCount.textContent = `${data.total_results} Encontrados`;
            
            if (data.data.length === 0) {
                timelineContainer.innerHTML = '<p style="color:var(--text-muted)">No se encontraron resultados en los módulos seleccionados para esta fecha.</p>';
            } else {
                data.data.forEach(item => {
                    const card = document.createElement('div');
                    card.className = 'result-card';
                    card.innerHTML = `
                        <div class="result-meta">
                            <span class="source">[${item.source}]</span>
                            <span class="timestamp">${item.timestamp}</span>
                        </div>
                        <div class="result-desc">${item.description}</div>
                        <a href="${item.url}" target="_blank" class="result-link">
                            🔗 Ver Origen
                        </a>
                    `;
                    timelineContainer.appendChild(card);
                });
            }
            
            // Cargar imagen de preview si existe
            if (data.preview_image) {
                previewContainer.innerHTML = `<img src="${data.preview_image}" alt="Web Reconstruida">`;
            } else {
                previewContainer.innerHTML = `
                    <div class="placeholder">
                        <span class="icon">⚠️</span>
                        <p>No se pudo generar una captura completa. Revisa los enlaces del timeline.</p>
                    </div>
                `;
            }
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Ocurrió un error al contactar al servidor OSINT.');
    } finally {
        btnText.textContent = 'INICIAR RASTREO';
        spinner.classList.add('hidden');
        submitBtn.disabled = false;
    }
});
