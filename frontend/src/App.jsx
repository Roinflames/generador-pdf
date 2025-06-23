import React, { useState, useEffect } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Home from "./pages/Home"; // 👈 importa el nuevo componente
import PrivateRoute from "./components/PrivateRoute";

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
  fetch("http://127.0.0.1:5000/api/me", { credentials: "include" })
    .then(res => {
      if (res.ok) {
        setIsAuthenticated(true);
      } else if (res.status === 401) {
        setIsAuthenticated(false);
      } else {
        throw new Error("Error inesperado");
      }
    })
    .catch(() => setIsAuthenticated(false));
}, []);

  
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login setIsAuthenticated={setIsAuthenticated} />} />
        <Route
          path="/"
          element={
            <PrivateRoute isAuthenticated={isAuthenticated}>
              <Home />
            </PrivateRoute>
          }
        />
        {/* otras rutas */}
      </Routes>
    </BrowserRouter>
  );
}

export default App;