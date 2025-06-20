import { Toaster } from "@/components/ui/toaster";
import { Toaster as Sonner } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import LoginPage from "./pages/LoginPage";
import DashboardContainer from "./pages/DashboardContainer";
import NotFound from "./pages/NotFound";
import PrivateRoute from "./components/PrivateRoute"; 



const queryClient = new QueryClient();

const App = () => (
  <QueryClientProvider client={queryClient}>
    <TooltipProvider>
      <Toaster />
      <Sonner />
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          
          <Route element={<PrivateRoute />}>
            <Route path="/" element={<DashboardContainer />} />
            <Route path="/dashboard" element={<DashboardContainer />} />
            <Route path="/simulation" element={<DashboardContainer />} />
            <Route path="/alerts" element={<DashboardContainer />} />
            <Route path="/logs" element={<DashboardContainer />} />
            <Route path="/response/:predictionId" element={<DashboardContainer />} />          
            <Route path="/response" element={<DashboardContainer />} />
            <Route path="/users" element={<DashboardContainer />} />
          </Route>
          
          <Route path="*" element={<NotFound />} />
        </Routes>
      </BrowserRouter>
    </TooltipProvider>
  </QueryClientProvider>
);

export default App;