import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./Integrantes.css";
import Integrantes from "./Integrantes.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <Integrantes />
  </StrictMode>
);
