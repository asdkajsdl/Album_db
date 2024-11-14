import { useState } from "react";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <header>
        <h1 className="Texto1">Alan Sutton Y Las Criaturitas De La Anciedad</h1>
      </header>
      <div className="links">
        <div>
          <a
            className="Texto-links"
            href="https://open.spotify.com/intl-es/artist/3OFrGQrdXwm0UgTERW6LAV"
          >
            Spotify
          </a>
          <a
            className="Texto-links"
            href="https://www.youtube.com/@alansuttonylascriaturitas"
          >
            Youtube
          </a>
          <a
            className="Texto-links"
            href="https://www.tiktok.com/@alansuttonylascriaturita?lang=en"
          >
            Tiktok
          </a>
          <a
            className="Texto-links"
            href="https://www.instagram.com/alansuttonylascriaturitas/"
          >
            Instagram
          </a>
        </div>
      </div>
      <h1 className="Textocolor">Albumnes:</h1>
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

        <integrantes />

        <div className="margin">
          <h2 className="Textocolor">Musicas Populares</h2>
        </div>
        <div className="backgroundcolor">
          <div className="gapo">
            <a
              className="centrar"
              href="https://open.spotify.com/intl-es/track/6KDSrToeuM3UGiqEB1qNRN#login"
            >
              <li className="Textocolor">1</li>
              <img src="/public/2.png" alt="" width={40} height={40} />
              <ul className="populares">TutanK'mon</ul>
            </a>
          </div>

          <div className="gapo">
            <a
              className="centrar"
              href="https://open.spotify.com/intl-es/track/3QaLlAMZDXa2s8eyVoowjw"
            >
              <li className="Textocolor">2</li>
              <img src="/public/2.png" alt="" width={40} height={40} />
              <ul className="populares">No Tengo Hambre, Tengo Anciedad</ul>
            </a>
          </div>

          <div className="gapo">
            <a
              className="centrar"
              href="https://open.spotify.com/intl-es/track/072yPZOZLx9HmR3pdEhNwn"
            >
              <li className="Textocolor">3</li>
              <img src="/public/2.png" alt="" width={40} height={40} />
              <ul className="populares">Bonsai</ul>
            </a>
          </div>

          <div className="gapo">
            <a
              className="centrar"
              href="https://open.spotify.com/intl-es/track/51hLPZbwyJTgz0Ku8ksXfO"
            >
              <li className="Textocolor">4</li>
              <img src="/public/4.png" alt="" width={40} height={40} />
              <ul className="populares">Omatopopih</ul>
            </a>
          </div>

          <div className="gapo">
            <a
              className="centrar"
              href="https://open.spotify.com/intl-es/track/2mMlizGENm5czbZG7YsG5g"
            >
              <li className="Textocolor">5</li>
              <img src="/public/Dopamina.jpg" alt="" width={40} height={40} />
              <ul className="populares">Dopamina</ul>
            </a>
          </div>

          <div className="gapo">
            <a
              className="centrar"
              href="https://open.spotify.com/intl-es/track/0YlJPYsw6tQbQyy5eNJw5s"
            >
              <li className="Textocolor">6</li>
              <img src="/public/2.png" alt="" width={40} height={40} />
              <ul className="populares">
                El Mundo Siempre Estuvo Dividido En Dos
              </ul>
            </a>
          </div>

          <div className="gapo">
            <a
              className="centrar"
              href="https://open.spotify.com/intl-es/track/3EqINdYgqCMeKzRwzQlHiJ"
            >
              <li className="Textocolor">7</li>
              <img src="/public/4.png" alt="" width={40} height={40} />
              <ul className="populares">Paris Es Un Buen Lugar para Morir</ul>
            </a>
          </div>

          <div className="gapo">
            <a
              className="centrar"
              href="https://open.spotify.com/intl-es/track/3LUmfbAsFNUcuLyd6uSbun"
            >
              <li className="Textocolor">8</li>
              <img src="/public/2.png" alt="" width={40} height={40} />
              <ul className="populares">Cuktura Porno Disney</ul>
            </a>
          </div>

          <div className="gapo">
            <a
              className="centrar"
              href="https://open.spotify.com/intl-es/track/6dzsBX9dJzIOaURSAgfYxH"
            >
              <li className="Textocolor">9</li>
              <img src="/public/1.png" alt="" width={40} height={40} />
              <ul className="populares">El Heroe de Constitucion</ul>
            </a>
          </div>

          <div className="gapo">
            <a
              className="centrar"
              href="https://open.spotify.com/intl-es/track/5KRXGRFDEBA7ukH5MUTQH1"
            >
              <li className="Textocolor">10</li>
              <img
                src="/public/NicolasCage.jpg"
                alt=""
                width={40}
                height={40}
              />
              <ul className="populares">Nicolas Cage</ul>
            </a>
          </div>
        </div>
        <h2 className="info">Informacion:</h2>

        <div>
          <div className="informacion">
            <h3 className="text-informacion">
              Alan Sutton y las criaturitas de la ansiedad es una banda de
              Buenos Aires, Argentina que surge del encuentro entre Jerónimo
              Romero y Alan Sutton. Ya sea desde una dura crítica social, un
              existencialismo desgarrador, o un optimismo exultante, escuchar a
              "Las Criaturitas" es siempre un viaje distinto. Cada canción tiene
              su propia búsqueda, su propia identidad, y su propio universo
              sonoro. Resultado de la unión entre cantautor y productor, la
              banda no busca definirse en un género, sino más bien ampliar sus
              propios horizontes; el cambio y la transformación como motor en un
              mundo repleto de estímulos y ansiedad. Alan era un músico
              callejero que había comenzado a escribir sus primeras canciones y
              buscaba grabarlas de alguna manera. Su intención no era hacer un
              disco, ni formar una banda, sino más bien tener un registro de sus
              escritos. Por una de esas vueltas de la vida, Alan conoce a Jero,
              un joven apasionado de la producción musical, quien le dice las
              palabras que cambiarían su vida: "tus canciones son increíbles,
              grabemos un disco y hagamos una banda". Fue ese entusiasmo, esa
              mutua intensidad y esa química lo que, aunque no lo supieran,
              empezaba a darle forma a un universo de juego y creación, al que
              nunca podrían haber accedido sin el otro. En 2023 lanzaron su 3er
              álbum ALGO TIENE QUE CAMBIAR Fotos por Diego Homez
            </h3>
          </div>
        </div>
        <div className="links">
          <div>
            <a
              className="Texto-links"
              href="https://open.spotify.com/intl-es/artist/3OFrGQrdXwm0UgTERW6LAV"
            >
              Spotify
            </a>
            <a
              className="Texto-links"
              href="https://www.youtube.com/@alansuttonylascriaturitas"
            >
              Youtube
            </a>
            <a
              className="Texto-links"
              href="https://www.tiktok.com/@alansuttonylascriaturita?lang=en"
            >
              Tiktok
            </a>
            <a
              className="Texto-links"
              href="https://www.instagram.com/alansuttonylascriaturitas/"
            >
              Instagram
            </a>
          </div>
        </div>
      </div>
    </>
  );
}

export default App;
