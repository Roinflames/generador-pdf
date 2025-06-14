export async function loginUser(username, password) {
  const res = await fetch("http://localhost:5000/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    credentials: "include", // importa si usas sesión/cookie
    body: JSON.stringify({ username, password }),
  });

  if (!res.ok) {
    const error = await res.json();
    throw new Error(error.error || "Error al iniciar sesión");
  }

  return await res.json();
}
