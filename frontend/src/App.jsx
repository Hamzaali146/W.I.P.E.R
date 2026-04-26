import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { useState } from "react";

import LandingPage from "./components/LandingPage";
import Dashboard from "./components/Dashboard";
import { Auth } from "./components/Auth";

import { getUser, isLoggedIn, logoutUser } from "./services/auth";

// ProtectedRoute: re-checks token validity on every navigation
function ProtectedRoute({ authenticated, children }) {
  if (!authenticated || !isLoggedIn()) {
    return <Navigate to="/auth" replace />;
  }
  return children;
}

export default function App() {

  const [authenticated, setAuthenticated] = useState(isLoggedIn());
  const [user, setUser] = useState(getUser());

  const adminEmail = import.meta.env.VITE_ADMIN_EMAIL;
  const isAdmin = user?.email === adminEmail;

  const handleAuthSuccess = (loggedInUser) => {
    setAuthenticated(true);
    setUser(loggedInUser);
  };

  const handleLogout = () => {
    logoutUser();
    setAuthenticated(false);
    setUser(null);
  };


  return (
    <BrowserRouter>

      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route
          path="/auth"
          element={<Auth onAuthSuccess={handleAuthSuccess} />}
        />
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute authenticated={authenticated}>
              <Dashboard user={user} onLogout={handleLogout} isAdmin={isAdmin}/>
            </ProtectedRoute>
          }
        />

      </Routes>
    </BrowserRouter>
  );
}