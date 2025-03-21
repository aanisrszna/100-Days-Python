const fetchBreweries = async () => {
    const city = document.getElementById('search').value;
    if (!city) {
        alert("Please enter a city name.");
        return;
    }

    const url = `https://api.openbrewerydb.org/v1/breweries?by_city=${city}`;

    try {
        const response = await fetch(url);
        const data = await response.json();
        displayBreweries(data);
    } catch (error) {
        console.error("Error fetching breweries:", error);
    }
};

const displayBreweries = (breweries) => {
    const tableBody = document.getElementById('brewery-list');
    tableBody.innerHTML = ''; // Clear previous results

    if (breweries.length === 0) {
        tableBody.innerHTML = "<tr><td colspan='5'>No breweries found</td></tr>";
        return;
    }

    breweries.forEach(brewery => {
        const row = `<tr>
            <td>${brewery.name}</td>
            <td>${brewery.brewery_type}</td>
            <td>${brewery.city}</td>
            <td>${brewery.state}</td>
            <td>${brewery.website_url ? `<a href="${brewery.website_url}" target="_blank">Visit</a>` : 'N/A'}</td>
        </tr>`;
        tableBody.innerHTML += row;
    });
};
