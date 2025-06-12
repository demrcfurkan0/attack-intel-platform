import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';

const useAuth = () => {
  // Basit bir kontrol: Tarayıcı hafızasında token var mı?
  const token = localStorage.getItem('authToken');
  return !!token; // true veya false döndürür
};

const PrivateRoute = () => {
  const isAuthenticated = useAuth();

  // Eğer kullanıcı giriş yapmışsa, alt rotaları (Outlet) göster.
  // Değilse, /login sayfasına yönlendir.
  return isAuthenticated ? <Outlet /> : <Navigate to="/login" replace />;
};

export default PrivateRoute;