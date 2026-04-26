const API = "/api/article/";

let currentArticleId = null;
let page = 1;
let loading = false;
let searchQuery = "";

/* ---------------- AUTH ---------------- */

function getToken() {
    return localStorage.getItem("access");
}

function getHeaders(auth = false) {
    let headers = {};

    if (auth) {
        headers["Authorization"] = "Bearer " + getToken();
    }

    return headers;
}

function logout() {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    localStorage.removeItem("user");
    location.href = "/";
}

/* ---------------- LOAD ARTICLES ---------------- */

async function loadArticles(reset = false) {
    if (loading) return;

    loading = true;

    const container = document.getElementById("articlesContainer");

    if (reset) {
        container.innerHTML = "";
        page = 1;
    }

    let url = API + "articles/?page=" + page;

    if (searchQuery) {
        url += "&search=" + encodeURIComponent(searchQuery);
    }

    const res = await fetch(url);
    const data = await res.json();

    const articles = data.results || data;

    articles.forEach(renderArticleCard);

    page++;
    loading = false;
}

function renderArticleCard(article) {
    const container = document.getElementById("articlesContainer");

    const card = document.createElement("div");
    card.className = "article-card";

    card.innerHTML = `
        <h2>${article.title}</h2>
        <p>${article.content.substring(0, 180)}...</p>

        <div class="meta">
            <span>${article.category}</span>
            <span>${article.author_first_name} ${article.author_last_name}</span>
        </div>

        <div class="meta">
            <span>${article.reviews_count} reviews</span>
        </div>

        <button onclick="openArticle(${article.id})">
            Open
        </button>
    `;

    container.appendChild(card);
}

/* ---------------- SEARCH ---------------- */



/* ---------------- INFINITE SCROLL ---------------- */

window.addEventListener("scroll", () => {
    if (
        window.innerHeight + window.scrollY >=
        document.body.offsetHeight - 300
    ) {
        loadArticles();
    }
});

/* ---------------- ARTICLE DETAIL ---------------- */

async function openArticle(id) {
    currentArticleId = id;

    const res = await fetch(API + "articles/");
    const data = await res.json();

    const list = data.results || data;

    const article = list.find(a => a.id === id);

    document.getElementById("articleView").innerHTML = `
        <h2>${article.title}</h2>
        <p><b>Author:</b> ${article.author_first_name} ${article.author_last_name}</p>
        <p><b>Category:</b> ${article.category}</p>
        <p><b>Keywords:</b> ${article.keywords}</p>
        <p>${article.content}</p>

        <a href="${article.pdf_file}" target="_blank">Open PDF</a>
    `;

    loadReviews(id);

    document.getElementById("articleModal").classList.remove("hidden");
}

function closeArticle() {
    document.getElementById("articleModal").classList.add("hidden");
}

/* ---------------- REVIEWS ---------------- */

async function loadReviews(articleId) {
    const res = await fetch(API + "review-list/" + articleId + "/");
    const reviews = await res.json();

    const container = document.getElementById("reviews");

    container.innerHTML = "";

    reviews.forEach(r => {
        container.innerHTML += `
            <div class="review">
                <b>${r.user.first_name} ${r.user.last_name}</b>
                ⭐ ${r.rating}
                <p>${r.text}</p>
            </div>
        `;
    });
}

async function sendReview() {
    const text = document.getElementById("reviewText").value;
    const rating = document.getElementById("rating").value;

    const form = {
        article: currentArticleId,
        text: text,
        rating: rating
    };

    await fetch(API + "review-create/", {
        method: "POST",
        headers: {
            ...getHeaders(true),
            "Content-Type": "application/json"
        },
        body: JSON.stringify(form)
    });

    document.getElementById("reviewText").value = "";

    loadReviews(currentArticleId);
}

/* ---------------- PROFILE ---------------- */

async function openProfile() {
    const user = JSON.parse(localStorage.getItem("user"));

    document.getElementById("profileInfo").innerHTML = `
        <p>${user.email}</p>
        <p>${user.first_name} ${user.last_name}</p>
    `;

    const res = await fetch(API + "my-articles/", {
        headers: getHeaders(true)
    });

    const articles = await res.json();

    const container = document.getElementById("myArticles");

    container.innerHTML = "";

    articles.forEach(a => {
        container.innerHTML += `
            <div class="mini-card">
                ${a.title}
            </div>
        `;
    });

    document.getElementById("profileModal").classList.remove("hidden");
}

function closeProfile() {
    document.getElementById("profileModal").classList.add("hidden");
}

/* ---------------- CREATE ARTICLE ---------------- */

function openCreateModal() {
    document.getElementById("createModal").classList.remove("hidden");
}

function closeCreateModal() {
    document.getElementById("createModal").classList.add("hidden");
}

async function createArticle() {
    const formData = new FormData();

    formData.append("title", document.getElementById("title").value);
    formData.append("content", document.getElementById("content").value);
    formData.append("category", document.getElementById("category").value);
    formData.append("keywords", document.getElementById("keywords").value);

    const file = document.getElementById("pdf").files[0];
    formData.append("pdf_file", file);

    await fetch(API + "create/", {
        method: "POST",
        headers: getHeaders(true),
        body: formData
    });

    closeCreateModal();
    loadArticles(true);
}

/* ---------------- START ---------------- */

document.addEventListener("DOMContentLoaded", () => {

    const search = document.getElementById("searchInput");

    if (search) {
        search.addEventListener("input", function () {
            searchQuery = this.value;
            loadArticles(true);
        });
    }

    loadArticles();

});