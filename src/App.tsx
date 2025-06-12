import { Toaster } from "@/components/ui/toaster";
import { Toaster as Sonner } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import DashboardContainer from "./pages/DashboardContainer"; // Ana layout'u içeren konteyner
import NotFound from "./pages/NotFound";

const queryClient = new QueryClient();

const App = () => (
  <QueryClientProvider client={queryClient}>
    <TooltipProvider>
      <Toaster />
      <Sonner />
      <BrowserRouter>
        <Routes>
          {/* Her sekme için ayrı bir rota tanımlıyoruz, hepsi aynı bileşeni render ediyor */}
          <Route path="/" element={<DashboardContainer />} />
          <Route path="/dashboard" element={<DashboardContainer />} />
          <Route path="/simulation" element={<DashboardContainer />} />
          <Route path="/alerts" element={<DashboardContainer />} />
          <Route path="/logs" element={<DashboardContainer />} />
          <Route path="/response" element={<DashboardContainer />} />
          <Route path="/users" element={<DashboardContainer />} />
          
          {/* Yakalayıcı rota en sonda kalmalı */}
          <Route path="*" element={<NotFound />} />
        </Routes>
      </BrowserRouter>
    </TooltipProvider>
  </QueryClientProvider>
);

export default App;