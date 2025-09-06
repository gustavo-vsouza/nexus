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
          DEFAULT: "#005B41", // cor principal da logo
          light: "#008170",   // variação clara
          dark: "#232D3F",    // variação escura
          bg: "#0F0F0F",      // fundo da logo
        },
      },
    },
  },
  plugins: [],
} satisfies Config
