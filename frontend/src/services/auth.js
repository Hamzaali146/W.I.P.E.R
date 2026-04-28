const API_BASE = import.meta.env.VITE_API_AUTH_URL|| "http://127.0.0.1:8002";

export async function signupUser(payload) {
  const res = await fetch(`${API_BASE}/auth/signup`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  const data = await res.json();

  if (!res.ok) {
    throw new Error(data?.detail || "Signup failed");
  }

  return data;
}

export async function loginUser(payload) {
  const res = await fetch(`${API_BASE}/auth/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  const data = await res.json();

  if (!res.ok) {
    throw new Error(data?.detail || "Login failed");
  }

  return data;
}

export function saveAuth(authData) {
  localStorage.setItem("wiper_token", authData.access_token);
  localStorage.setItem("wiper_user", JSON.stringify(authData.user));
}

export function getToken() {
  return localStorage.getItem("wiper_token");
}

export function getUser() {
  const raw = localStorage.getItem("wiper_user");
  return raw ? JSON.parse(raw) : null;
}

export function logoutUser() {
  localStorage.removeItem("wiper_token");
  localStorage.removeItem("wiper_user");
}

export function isLoggedIn() {
  const token = getToken();
  if (!token) return false;

  try {
    const payload = JSON.parse(atob(token.split(".")[1]));
    if (payload.exp && Date.now() >= payload.exp * 1000) {
      logoutUser();
      return false;
    }
    return true;
  } catch {
    logoutUser();
    return false;
  }
}
