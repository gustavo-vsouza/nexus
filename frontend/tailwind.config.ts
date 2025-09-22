import type { Config } from "tailwindcss"

export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: "#00FFB2", // verde neon (principal)
          light: "#00C2FF",   // azul neon (variação)
          dark: "#A020F0",    // roxo neon (variação)
          accent: "#FF2E92",  // rosa neon (destaque)
          bg: "#06022D",      // fundo principal
          second: "#0D0D2B",   // fundo secundário
        },
        neutral: {
          white: "#f0f0f0",
          gray: "#D1D5DB",
        },
      },
    },
  },
  plugins: [],
} satisfies Config
