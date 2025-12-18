import { useEffect } from "react";
import WebApp from "@twa-dev/sdk";
import PresetCard from "./PresetCard";
import SwipeActions from "./SwipeActions";
import "./styles.css";

function App() {
  useEffect(() => {
    WebApp.ready();
  }, []);

  return (
    <div className="app">
      <header>
        <h1>Kino Bot</h1>
        <p>Свайпай фильмы, собирай совпадения с друзьями.</p>
      </header>
      <PresetCard />
      <SwipeActions />
    </div>
  );
}

export default App;
