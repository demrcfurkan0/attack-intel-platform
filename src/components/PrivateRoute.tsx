import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';

const useAuth = () => {
  const token = localStorage.getItem('authToken');
  return !!token; 
};

const PrivateRoute = () => {
  const isAuthenticated = useAuth();

  return isAuthenticated ? <Outlet /> : <Navigate to="/login" replace />;
};

export default PrivateRoute;