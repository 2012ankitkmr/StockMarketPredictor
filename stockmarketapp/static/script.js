document.addEventListener('DOMContentLoaded', function() {
    const preloader = document.getElementById('preloader');
    const stocksContainer = document.getElementById('stocks-container');

    fetch('/api/stocks')
        .then(response => response.json())
        .then(data => {
            // Hide preloader and show stocks container
            preloader.style.display = 'none';
            stocksContainer.style.display = 'block';

            data.forEach(stock => {
                const price = typeof stock.price === 'number' ? '$' + stock.price.toFixed(2) : stock.price;
                const card = `
                    <div class="col s12 m6 l4">
                        <div class="card-panel">
                            <h5>${stock.symbol}</h5>
                            <p>${price}</p>
                        </div>
                    </div>
                `;
                stocksContainer.innerHTML += card;
            });
        })
        .catch(error => {
            preloader.style.display = 'none';
            stocksContainer.innerHTML = '<p class="center-align">Error fetching stock data. Please try again later.</p>';
            stocksContainer.style.display = 'block';
            console.error('Error fetching stock data:', error);
        });
});
