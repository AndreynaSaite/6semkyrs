async function login(event) {
    event.preventDefault();

    const data = {
        email: document.querySelector("#email").value,
        password: document.querySelector("#password").value,
    };

    const res = await post("login/", data);

    if (res.access) {
        localStorage.setItem("access", res.access);
        localStorage.setItem("refresh", res.refresh);

        window.location.href = "/";
    } else {
        alert("Login failed");
    }
    
}

async function register(event) {
    event.preventDefault();

    const data = {
        first_name: document.querySelector("#first_name").value,
        last_name: document.querySelector("#last_name").value,
        email: document.querySelector("#email").value,
        password: document.querySelector("#password").value,
        confirm_password: document.querySelector("#confirm_password").value,
    };

    // client-side check (быстрее UX)
    if (data.password !== data.confirm_password) {
        alert("Пароли не совпадают");
        return;
    }

    const res = await post("register/", data);

    if (res.access) {
        localStorage.setItem("access", res.access);
        localStorage.setItem("refresh", res.refresh);

        localStorage.setItem("user", JSON.stringify({
            email: data.email,
            first_name: data.first_name,
            last_name: data.last_name
        }));

        window.location.href = "/";
    } else {
        alert("Ошибка регистрации");
        console.log(res);
    }
}