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
          DEFAULT: "#14E2A4", // cor principal da logo
          light: "#5CF5C4",   // variação clara
          dark: "#0FA37A",    // variação escura
          bg: "#002B29",      // fundo da logo
        },
      },
    },
  },
  plugins: [],
} satisfies Config
