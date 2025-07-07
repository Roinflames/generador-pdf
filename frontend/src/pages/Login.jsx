import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

export default function Login({ setIsAuthenticated }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [remember, setRemember] = useState(false);
  const [errorMsg, setErrorMsg] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const lastUser = localStorage.getItem("lastUsername");
    if (lastUser) {
      setUsername(lastUser);
      setRemember(true);
    }
  }, []);

  const handleLogin = async (e) => {
    e.preventDefault();
    setErrorMsg("");

    try {
      const res = await fetch("http://127.0.0.1:5000/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify({ username, password }),
      });

      const data = await res.json();

      if (!res.ok) throw new Error(data.error || "Error desconocido");

      if (remember) {
        localStorage.setItem("lastUsername", username);
      } else {
        localStorage.removeItem("lastUsername");
      }

      setIsAuthenticated(true);
      navigate("/");
    } catch (err) {
      setErrorMsg(err.message);
    }
  };

  return (
    <div style={outerContainer}>
      <div style={loginBox}>
        <h2 style={{ textAlign: "center" }}>Iniciar sesión</h2>
        <form onSubmit={handleLogin}>
          <input
            type="text"
            placeholder="Usuario"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
            style={inputStyle}
          />
          <input
            type="password"
            placeholder="Contraseña"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            style={inputStyle}
          />
          <div style={{ marginBottom: "1rem" }}>
            <label>
              <input
                type="checkbox"
                checked={remember}
                onChange={() => setRemember(!remember)}
              />{" "}
              Recordar usuario
            </label>
          </div>
          {errorMsg && <p style={{ color: "salmon" }}>{errorMsg}</p>}
          <button type="submit" style={buttonStyle}>Entrar</button>
        </form>
      </div>
    </div>
  );
}

// Estilos
const outerContainer = {
  position: "fixed",
  top: 0,
  left: 0,
  width: "100vw",
  height: "100vh",
  display: "flex",
  justifyContent: "center",
  alignItems: "center",
  backgroundColor: "#1e1e1e",
  zIndex: 10,
};

const loginBox = {
  backgroundColor: "#2a2a2a",
  padding: "2rem",
  borderRadius: "8px",
  boxShadow: "0 0 15px rgba(0,0,0,0.5)",
  width: "100%",
  maxWidth: "400px",
  color: "#f0f0f0"
};

const inputStyle = {
  width: "100%",
  padding: "0.75rem",
  marginBottom: "1rem",
  border: "1px solid #444",
  borderRadius: "4px",
  backgroundColor: "#1c1c1c",
  color: "#f0f0f0"
};

const buttonStyle = {
  width: "100%",
  padding: "0.75rem",
  backgroundColor: "#007bff",
  color: "#fff",
  border: "none",
  borderRadius: "4px",
  cursor: "pointer"
};
