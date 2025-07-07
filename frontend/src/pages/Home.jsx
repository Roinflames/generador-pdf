import React, { useState } from "react";

export default function Home() {
  const handleLogout = async () => {
    await fetch("http://127.0.0.1:5000/api/logout", {
      method: "POST",
      credentials: "include",
    });
    window.location.href = "/login";
  };

  // Estructura de menú con enlaces finales
  const menu = {
    Civil: {
      Herencia: [
        { label: "En proceso" },
      ],
      Conservador: [
        { label: "Escritura de Compraventa", url: "http://127.0.0.1:5000/escritura_compraventa" }
      ],
      Poder: [
        { label: "Delegación de Poder", url: "http://127.0.0.1:5000/delega_poder" },
        { label: "Patrocinio de Poder", url: "http://127.0.0.1:5000/patrocinio_de_poder" },
        { label: "Reconocimiento de Firma", url: "http://127.0.0.1:5000/reconocimiento" },
      ],
    },
    Familia: {
      "Juicio de Alimentos": [
        { label: "En proceso" },
      ],
      "Cuidado Personal": [
        { label: "En proceso" },
      ],
      "Divorcio Unilateral": [
        { label: "En proceso" },
      ],
    },
    Tributario: {
      "Liquidación de Persona Natural": [
        { label: "Liquidación de Persona Natural", url: "http://127.0.0.1:5000/liquidacion_de_persona_natural" }
      ],
      "Informe Tributario": [
        { label: "Generar Informe", url: "http://127.0.0.1:5000/generar_informe" }
      ]
    },
  };

  const [openMain, setOpenMain] = useState(null);
  const [openSub, setOpenSub] = useState(null);

  return (
    <div style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h2>Generador de Documentos</h2>
      <p>
        Bienvenido, <strong>Usuario</strong> |{" "}
        <button onClick={handleLogout}>Cerrar sesión</button>
      </p>

      <h3>Selecciona una categoría para generar documento</h3>

      {/* Menú anidado */}
      <div>
        {Object.entries(menu).map(([main, subs]) => (
          <div key={main} style={{ marginBottom: "1rem" }}>
            <button
              style={{ fontWeight: "bold", width: "100%", textAlign: "left" }}
              onClick={() =>
                setOpenMain(openMain === main ? null : main)
              }
            >
              {main}
            </button>

            {openMain === main &&
              Object.entries(subs).map(([sub, links]) => (
                <div key={sub} style={{ paddingLeft: "1rem" }}>
                  <button
                    style={{
                      fontStyle: "italic",
                      background: "none",
                      border: "none",
                      cursor: "pointer",
                      color: "#333",
                    }}
                    onClick={() =>
                      setOpenSub(openSub === sub ? null : sub)
                    }
                  >
                    {sub}
                  </button>

                  {openSub === sub && links.length > 0 && (
                    <ul style={{ paddingLeft: "1.5rem", listStyle: "disc" }}>
                      {links.map((link, i) => (
                        <li key={i}>
                          <a href={link.url} target="_blank" rel="noopener noreferrer">
                            {link.label}
                          </a>
                        </li>
                      ))}
                    </ul>
                  )}
                </div>
              ))}
          </div>
        ))}
      </div>
    </div>
  );
}
