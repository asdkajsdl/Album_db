import { useState } from "react";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <header>
        <h1 className="Texto1">Alan Sutton y Las Criaturitas de la Anciedad</h1>
        </header>
      <div>
        <div className="centrar">
            <a href="https://open.spotify.com/intl-es/album/2dJfWjL7AHKli4i7MjCp3E">
            <img className="imagen" src="/public/1.png" alt="" />
            </a>

            <a href="https://open.spotify.com/intl-es/album/2iKR4ZBb3NLJM0Zg8yhQvi">
            <img className="imagen" src="/public/2.png" alt="" />
            </a>

            <a href="https://open.spotify.com/intl-es/album/7hgxTp99yKwlzXDZgV6O8I">
            <img className="imagen" src="/public/3.png" alt="" />
            </a>

            <a href="https://open.spotify.com/intl-es/album/3i0EZnMVNrETaQcHKs3bib">
            <img className="imagen" src="/public/4.png" alt="" />
            </a>

            <a href="https://open.spotify.com/intl-es/album/4Wlrq1ImA0Se5pJ0BiB4iL">
            <img className="imagen" src="/public/5.png" alt="" />
            </a>
        </div>
        
        <div>
          <div>
              <li className="Textocolor" >1</li>
              
          </div>
        </div>
      </div>
    </>
  );
}

export default App;
