import React from "react";

export default function Home() {
  const handleLogout = async () => {
    await fetch('http://127.0.0.1:5000/api/logout', {
      method: 'POST',
      credentials: 'include'
    })
    .then(res => {
      if (res.ok) {
        window.location.href = '/login';  // redirige el navegador
      } else {
        console.log("Error al cerrar sesión");
      }
    });
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h2>Generador de Documentos</h2>
      <p>
        Bienvenido, <strong>{/* aquí podrías poner el nombre del usuario */}</strong> |{" "}
        <button onClick={handleLogout}>Cerrar sesión</button>
      </p>

      <p>Selecciona el tipo de documento que deseas generar:</p>
      <ul>
        <li><a href="http://127.0.0.1:5000/delega_poder"><button>Delegación de Poder</button></a></li>
        <li><a href="http://127.0.0.1:5000/diagrama"><button>Diagrama</button></a></li>
        <li><a href="http://127.0.0.1:5000/escritura_compraventa"><button>Escritura de Compraventa</button></a></li>
        <li><a href="http://127.0.0.1:5000/generar_informe"><button>Generar Informe</button></a></li>
        <li><a href="http://127.0.0.1:5000/liquidacion_de_persona_natural"><button>Liquidación de Persona Natural</button></a></li>
        <li><a href="http://127.0.0.1:5000/reconocimiento"><button>Reconocimiento de Firma</button></a></li>
        <li><a href="http://127.0.0.1:5000/opone_excepciones"><button>Escrito Opone Excepciones</button></a></li>
        <li><a href="http://127.0.0.1:5000/patrocinio_de_poder"><button>Patrocinio de poder</button></a></li>
      </ul>
    </div>
  );
}
