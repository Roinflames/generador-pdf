import { useState } from "react";
import { useNavigate } from "react-router-dom";
import React from "react";

export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [errorMsg, setErrorMsg] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setErrorMsg("");

    try {
      const res = await fetch("http://127.0.0.1:5000/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include", // 🔐 para que se guarde la cookie de sesión
        body: JSON.stringify({ username, password }),
      });

      const data = await res.json();

      if (!res.ok) {
        throw new Error(data.error || "Error desconocido");
      }

      alert("Login exitoso");
      navigate("/"); // o a dashboard
    } catch (err) {
      setErrorMsg(err.message);
    }
  };

  return (
    <div style={{ maxWidth: 400, margin: "auto" }}>
      <h2>Iniciar sesión</h2>
      <form onSubmit={handleLogin}>
        <input
          type="text"
          placeholder="Usuario"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        /><br /><br />
        <input
          type="password"
          placeholder="Contraseña"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        /><br /><br />
        {errorMsg && <p style={{ color: "red" }}>{errorMsg}</p>}
        <button type="submit">Entrar</button>
      </form>
    </div>
  );
}
