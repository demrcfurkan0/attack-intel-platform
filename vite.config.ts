/// <reference types="vitest" />
import path from "path";
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc"; 

export default defineConfig({
  plugins: [react()],
  
  test: {
    globals: true,
    environment: 'jsdom', 
    setupFiles: './src/setupTests.ts', 
  },

  resolve: {
    alias: {

      "@": path.resolve(__dirname, "./src"),
    },
  },

  server: {
    host: "::",
    port: 8080,
  },
});