// attack-simulation/tailwind.config.ts

import type { Config } from "tailwindcss"

const config = {
  darkMode: ["class"],
  content: [
    './pages/**/*.{ts,tsx}',
    './components/**/*.{ts,tsx}',
    './app/**/*.{ts,tsx}',
    './src/**/*.{ts,tsx}',
	],
  prefix: "",
  theme: {
    container: {
      center: true,
      padding: "2rem",
      screens: {
        "2xl": "1400px",
      },
    },
    extend: {
      colors: {
        // --- BU RENKLERİ EKLE ---
        'cyber-dark': 'hsl(var(--background))',       // Ana arka plan rengimiz
        'cyber-darker': 'hsl(var(--card))',           // Kartlar ve diğer elementler için daha koyu
        'cyber-primary': 'hsl(var(--primary))',       // Ana vurgu rengi (yeşil)
        'cyber-secondary': 'hsl(var(--secondary))',   // İkincil renk
        'cyber-accent': 'hsl(var(--destructive))',    // Vurgu rengi (kırmızı/yıkıcı)
        'cyber-warning': '#ffaa00',                   // Uyarı rengi (sarı/turuncu)
        'cyber-light': 'hsl(var(--border))',          // Kenarlık rengi
        // --- RENKLERİN SONU ---
        
        // Mevcut shadcn/ui renk tanımları
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        },
        accent: {
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))",
        },
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))",
        },
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))",
        },
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
      keyframes: {
        "accordion-down": {
          from: { height: "0" },
          to: { height: "var(--radix-accordion-content-height)" },
        },
        "accordion-up": {
          from: { height: "var(--radix-accordion-content-height)" },
          to: { height: "0" },
        },
      },
      animation: {
        "accordion-down": "accordion-down 0.2s ease-out",
        "accordion-up": "accordion-up 0.2s ease-out",
      },
      boxShadow: {
        'cyber-glow': '0 0 15px rgba(0, 255, 136, 0.4)',
        'warning-glow': '0 0 15px rgba(255, 170, 0, 0.4)',
      }
    },
  },
  plugins: [require("tailwindcss-animate")],
} satisfies Config

export default config