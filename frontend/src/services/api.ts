// src/services/api.ts
import axios from "axios";

// URL base do seu backend FastAPI
const api = axios.create({
  baseURL: "http://127.0.0.1:8000", // ajuste se usar outra porta/host
});

export default api;
