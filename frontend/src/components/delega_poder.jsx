import React, { useEffect, useState } from "react";

export default function DelegacionPDF() {
  const [formData, setFormData] = useState(null);
  const [originalData, setOriginalData] = useState(null); // para restaurar
  const [pdfUrl, setPdfUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // Cargar los datos actuales desde el backend
  useEffect(() => {
    fetch("http://127.0.0.1:5000/delega_poder/data")
      .then((res) => res.json())
      .then((data) => {
        setFormData(data);
        setOriginalData(data); // guarda copia para "restaurar"
      })
      .catch((err) =>
        setError("❌ Error al cargar datos desde el backend: " + err.message)
      );
  }, []);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleGeneratePDF = async () => {
    setLoading(true);
    setError("");

    try {
      const response = await fetch("http://127.0.0.1:5000/delega_poder/generar_pdf", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (response.ok && data.pdf_url) {
        setPdfUrl(`http://127.0.0.1:5000${data.pdf_url}?t=${Date.now()}`);
      } else {
        setError(data.error || "No se pudo generar el PDF.");
      }
    } catch (err) {
      setError("❌ Error de red: " + err.message);
    }

    setLoading(false);
  };

  const handleRestoreData = () => {
    setFormData(originalData);
    setPdfUrl(""); // limpia vista previa si quieres
  };

  if (error) return <p style={{ color: "red" }}>{error}</p>;
  if (!formData) return <p>Cargando datos...</p>;

  return (
    <div style={{ padding: "2rem" }}>
      <h2>📄 Delegación de Poder</h2>

      {/* Formulario de edición */}
      <div style={{ maxWidth: "600px", marginBottom: "2rem" }}>
        {[
          "nombre",
          "rut",
          "tribunal",
          "abogado_patrocinante",
          "caratula",
          "rol",
          "demandado",
          "rut_demandado",
        ].map((field) => (
          <div key={field} style={{ marginBottom: "1rem" }}>
            <label style={{ textTransform: "capitalize" }}>
              {field.replace(/_/g, " ")}:
            </label>
            <input
              type="text"
              name={field}
              value={formData[field] || ""}
              onChange={handleChange}
              style={{ width: "100%" }}
            />
          </div>
        ))}

        <div style={{ display: "flex", gap: "1rem" }}>
          <button
            onClick={handleGeneratePDF}
            disabled={loading}
            style={{ marginTop: "1rem" }}
          >
            {loading ? "Generando PDF..." : "Generar PDF"}
          </button>

          <button
            onClick={handleRestoreData}
            disabled={loading}
            style={{ marginTop: "1rem", backgroundColor: "#ccc" }}
          >
            Restaurar datos originales
          </button>
        </div>
      </div>

      {/* Previsualización HTML en vivo */}
      <div style={{ border: "1px solid #ccc", padding: "1rem", marginBottom: "2rem" }}>
        <h4>Previsualización HTML (antes del PDF)</h4>
        <p>
          Yo, <strong>{formData.nombre || "________"}</strong> (RUT:{" "}
          <strong>{formData.rut || "________"}</strong>), delego poder legal para realizar
          trámites ante el <strong>{formData.tribunal || "________"}</strong>, en la causa{" "}
          <strong>{formData.caratula || "________"}</strong> (rol{" "}
          <strong>{formData.rol || "________"}</strong>), patrocinada por{" "}
          <strong>{formData.abogado_patrocinante || "________"}</strong>, en contra de{" "}
          <strong>{formData.demandado || "________"}</strong> (RUT:{" "}
          <strong>{formData.rut_demandado || "________"}</strong>).
        </p>
      </div>

      {/* Vista del PDF si ya fue generado */}
      {pdfUrl ? (
        <div>
          <h4>📄 Vista previa PDF generado:</h4>
          <iframe
            src={pdfUrl}
            title="Vista previa PDF"
            width="100%"
            height="800px"
            style={{ border: "1px solid #ccc" }}
          />
        </div>
      ) : (
        <p style={{ fontStyle: "italic", color: "#555" }}>
          Aún no se ha generado el PDF. Completa los datos y haz clic en "Generar PDF".
        </p>
      )}
    </div>
  );
}
