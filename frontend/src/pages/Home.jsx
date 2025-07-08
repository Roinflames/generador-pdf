import React, { useState } from "react";
import { Link as RouterLink, useNavigate } from 'react-router-dom';

export default function Home() {
  const [openMain, setOpenMain] = useState([]);
  const [openSubs, setOpenSubs] = useState([]);
  const navigate = useNavigate();

  const toggleMain = (main) => {
    setOpenMain((prev) =>
      prev.includes(main) ? prev.filter((m) => m !== main) : [...prev, main]
    );
  };

  const toggleSub = (sub) => {
    setOpenSubs((prev) =>
      prev.includes(sub) ? prev.filter((s) => s !== sub) : [...prev, sub]
    );
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    navigate('/login');
  };

  const menu = {
    Civil: {
      Herencia: [{ label: "En proceso" }],
      Conservador: [
        { label: "Escritura de Compraventa", url: "http://127.0.0.1:5000/escritura_compraventa" },
      ],
      Poder: [
        { label: "Delegación de Poder", url: "/delegacion_poder", internal: true },
        { label: "Patrocinio de Poder", url: "http://127.0.0.1:5000/patrocinio_de_poder" },
        { label: "Reconocimiento de Firma", url: "http://127.0.0.1:5000/reconocimiento" },
      ],
    },
    Familia: {
      "Juicio de Alimentos": [{ label: "En proceso" }],
      "Cuidado Personal": [{ label: "En proceso" }],
      "Divorcio Unilateral": [{ label: "En proceso" }],
    },
    Tributario: {
      "Liquidación de Persona Natural": [
        { label: "Liquidación de Persona Natural", url: "http://127.0.0.1:5000/liquidacion_de_persona_natural" },
      ],
      "Informe Tributario": [
        { label: "Generar Informe", url: "http://127.0.0.1:5000/generar_informe" },
      ],
    },
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "'Segoe UI', sans-serif" }}>
      <header style={{ display: "flex", justifyContent: "space-between", marginBottom: "2rem" }}>
        <h2>📄 Generador de Documentos</h2>
        <button onClick={handleLogout} style={{ background: "#e74c3c", color: "#fff", padding: "0.5rem 1rem", border: "none", borderRadius: "4px" }}>
          Cerrar sesión
        </button>
      </header>

      <h3 style={{ marginBottom: "1rem" }}>Selecciona una categoría:</h3>

      {Object.entries(menu).map(([main, subs]) => (
        <div key={main} style={{ marginBottom: "1rem" }}>
          <button
            onClick={() => toggleMain(main)}
            style={{
              width: "100%",
              textAlign: "left",
              backgroundColor: "#2c3e50",
              color: "white",
              padding: "0.75rem 1rem",
              border: "none",
              borderRadius: "4px",
              fontSize: "1rem",
              cursor: "pointer",
            }}
          >
            {openMain.includes(main) ? "▼" : "►"} {main}
          </button>

          {openMain.includes(main) &&
            Object.entries(subs).map(([sub, links]) => (
              <div key={sub} style={{ marginLeft: "1rem", marginTop: "0.5rem" }}>
                <button
                  onClick={() => toggleSub(sub)}
                  style={{
                    background: "#ecf0f1",
                    border: "none",
                    padding: "0.5rem",
                    fontStyle: "italic",
                    width: "100%",
                    textAlign: "left",
                    borderRadius: "4px",
                    cursor: "pointer",
                  }}
                >
                  {openSubs.includes(sub) ? "▼" : "►"} {sub}
                </button>

                {openSubs.includes(sub) && (
                  <ul style={{ marginLeft: "1.5rem", marginTop: "0.5rem" }}>
                    {links.map((link, i) => (
                      <li key={i}>
                        {link.url ? (
                          link.internal ? (
                            <RouterLink
                              to={link.url}
                              style={{ textDecoration: "none", color: "#2980b9" }}
                            >
                              {link.label}
                            </RouterLink>
                          ) : (
                            <a
                              href={link.url}
                              target="_blank"
                              rel="noopener noreferrer"
                              style={{ textDecoration: "none", color: "#2980b9" }}
                            >
                              {link.label}
                            </a>
                          )
                        ) : (
                          <span style={{ color: "#999", fontStyle: "italic" }}>
                            {link.label}
                          </span>
                        )}
                      </li>
                    ))}
                  </ul>
                )}
              </div>
            ))}
        </div>
      ))}
    </div>
  );
}
