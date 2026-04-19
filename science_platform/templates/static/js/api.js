const API_URL = "/api/";

async function post(url, data) {
    const response = await fetch(API_URL + url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    });

    return response.json();
}