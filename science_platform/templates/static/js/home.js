function parseJwt(token) {
    try {
        return JSON.parse(atob(token.split('.')[1]));
    } catch (e) {
        return null;
    }
}

function loadProfile() {
    const token = localStorage.getItem("access");

    const guestView = document.getElementById("guest-view");
    const profileView = document.getElementById("profile-view");

    if (!token) {
        guestView.style.display = "block";
        profileView.style.display = "none";
        return;
    }

    const payload = parseJwt(token);

    if (!payload) {
        logout();
        return;
    }

    guestView.style.display = "none";
    profileView.style.display = "block";

    // JWT payload (SimpleJWT обычно содержит email, user_id)
    const user = JSON.parse(localStorage.getItem("user"));

    document.getElementById("user-email").innerText = user?.email;
    document.getElementById("user-first").innerText = user?.first_name;
    document.getElementById("user-last").innerText = user?.last_name;
}

function logout() {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    window.location.href = "/";
}

loadProfile();