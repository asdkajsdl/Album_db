import React from "react"; // Importamos React (aunque en versiones más recientes de React esto es opcional, es una buena práctica)
import "./Integrantes.css"; // Asegúrate de que la ruta al archivo CSS sea correcta

function Integrantes() {
  return (
    <>
      <header>
        <h1>Informacion de la banda</h1>
      </header>
      <h3>hola</h3>
      <img src="/1.png" alt="Imagen de integrantes" />{" "}
      {/* No se usa '/public/' en la ruta */}
    </>
  );
}

export default Integrantes;
