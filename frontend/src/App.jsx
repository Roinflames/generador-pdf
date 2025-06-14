import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import React from "react";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        {/* otras rutas */}
        <Route path="/" element={<h1>Home (privado)</h1>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
