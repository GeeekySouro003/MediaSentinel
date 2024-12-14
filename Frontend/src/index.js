import React from "react";
import { createRoot } from "react-dom/client";
import App from "./App";
import Modal from "react-modal";

// Additional imports
import 'remixicon/fonts/remixicon.css';
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

// Set Modal app element
const container = document.getElementById("root");
const root = createRoot(container);

Modal.setAppElement("#root");

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
