document.addEventListener("DOMContentLoaded", () => {
    let selectedYear = 2012;
    let selectedCategory = "all";
    const searchForm = document.getElementById("search-form");
    const searchInput = document.getElementById("search-input");
    const yearButtons = document.querySelectorAll(".year-btn");
    const filterButtons = document.querySelectorAll(".filter-btn");
    const loader = document.getElementById("loader");
    const resultsSection = document.getElementById("results-section");
    const resultsGrid = document.getElementById("results-grid");
    const targetYearDisplay = document.getElementById("target-year-display");
    const resultsCount = document.getElementById("results-count");

    // Handle year selection
    yearButtons.forEach(button => {
        button.addEventListener("click", () => {
            yearButtons.forEach(btn => btn.classList.remove("active"));
            button.classList.add("active");
            selectedYear = parseInt(button.dataset.year, 10);

            if (searchInput.value.trim() !== "") {
                performSearch(searchInput.value.trim(), selectedYear, selectedCategory);
            }
        });
    });

    // Handle category filter selection
    filterButtons.forEach(button => {
        button.addEventListener("click", () => {
            filterButtons.forEach(btn => btn.classList.remove("active"));
            button.classList.add("active");
            selectedCategory = button.dataset.category;

            if (searchInput.value.trim() !== "") {
                performSearch(searchInput.value.trim(), selectedYear, selectedCategory);
            }
        });
    });

    // Handle form submit
    searchForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const query = searchInput.value.trim();
        if (query) {
            performSearch(query, selectedYear, selectedCategory);
        }
    });

    // Extract clean domain name from URL
    function getDomain(url) {
        try {
            const parsed = new URL(url);
            return parsed.hostname.replace("www.", "");
        } catch (e) {
            return "Sitio Web";
        }
    }

    // Perform Search
    async function performSearch(query, year, category) {
        loader.classList.remove("hidden");
        resultsSection.classList.add("hidden");
        resultsGrid.innerHTML = "";

        try {
            let url = `/api/search?q=${encodeURIComponent(query)}&year=${year}&category=${category}`;
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error("Error en la respuesta del servidor");
            }
            const data = await response.json();
            displayResults(data, year);
        } catch (error) {
            console.error("Search failed:", error);
            showErrorState();
        } finally {
            loader.classList.add("hidden");
        }
    }

    // Display search results
    function displayResults(results, year) {
        targetYearDisplay.textContent = year;
        resultsCount.textContent = `${results.length} ${results.length === 1 ? 'resultado' : 'resultados'}`;
        resultsGrid.innerHTML = "";

        if (results.length === 0) {
            resultsGrid.innerHTML = `
                <div class="no-results-card">
                    <p>No se encontraron resultados archivados para esta búsqueda en el año ${year}.</p>
                </div>
            `;
        } else {
            results.forEach((item, index) => {
                const domain = getDomain(item.original_url);
                const card = document.createElement("a");
                card.href = item.wayback_url;
                card.target = "_blank";
                card.className = "result-card";
                card.style.animationDelay = `${index * 50}ms`; // Staggered entrance animation

                card.innerHTML = `
                    <div class="card-image-bg" style="background-image: url('${item.image_url}')"></div>
                    <div class="card-overlay"></div>
                    <div class="card-content">
                        <div class="card-meta">
                            <span class="card-domain">${domain}</span>
                            <span class="card-time-badge">${item.archive_source} (${year})</span>
                        </div>
                        <h3>${escapeHtml(item.title)}</h3>
                        <p class="card-snippet">${escapeHtml(item.snippet)}</p>
                        <div class="card-action">
                            <span>Ver sitio en el pasado (${year})</span>
                            <span class="icon">→</span>
                        </div>
                    </div>
                `;
                resultsGrid.appendChild(card);
            });
        }

        resultsSection.classList.remove("hidden");
    }

    // Error UI State
    function showErrorState() {
        resultsCount.textContent = "Error";
        resultsGrid.innerHTML = `
            <div class="no-results-card error-card">
                <p>Hubo un problema al buscar las capturas históricas. Por favor, inténtalo de nuevo.</p>
            </div>
        `;
        resultsSection.classList.remove("hidden");
    }

    // Helper to prevent HTML Injection
    function escapeHtml(text) {
        const div = document.createElement("div");
        div.innerText = text;
        return div.innerHTML;
    }
});
