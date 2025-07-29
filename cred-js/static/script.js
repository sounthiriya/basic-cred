async function createUser() {
    const id = document.getElementById("id").value;
    const username = document.getElementById("username").value;

    const response = await fetch("/create-user", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id, username }),
    });

    const data = await response.json();
    alert(data.message);
}

async function getUser() {
    const userId = document.getElementById("getId").value;

    const response = await fetch(`/get-user/${userId}`);
    const result = document.getElementById("userResult");

    if (response.ok) {
        const data = await response.json();
        result.textContent = `ID: ${data.id}, Username: ${data.username}`;
    } else {
        result.textContent = "User not found";
    }
}