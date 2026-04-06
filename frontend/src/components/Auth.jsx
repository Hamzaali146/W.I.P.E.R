import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import Navbar from "./landing/Navbar";
import { Card } from "./ui/card";
import { Button } from "./ui/button";
import { Input } from "./ui/input";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "./ui/tabs";
import { Badge } from "./ui/badge";
import { Mail, Lock, User, Eye, EyeOff } from "lucide-react";
import { loginUser, signupUser, saveAuth } from "../services/auth";

const animStyles = `
  @keyframes logoSpin {
    0%, 80%, 100% { transform: rotate(0deg) scale(1); }
    35%            { transform: rotate(360deg) scale(1.08); }
  }
  @keyframes ringPulse {
    0%, 100% { box-shadow: 0 0 0 0px rgba(134,239,172,0.0); }
    50%       { box-shadow: 0 0 0 10px rgba(134,239,172,0.15); }
  }
  @keyframes badgeDot {
    0%, 100% { opacity: 1; transform: scale(1); }
    50%       { opacity: 0.35; transform: scale(0.7); }
  }
  @keyframes featFade {
    from { opacity: 0; transform: translateX(-12px); }
    to   { opacity: 1; transform: translateX(0); }
  }
  .logo-animated {
    animation: logoSpin 5s ease-in-out infinite, ringPulse 3s ease-in-out infinite;
  }
  .badge-dot { animation: badgeDot 2s ease-in-out infinite; }
  .feat-1 { animation: featFade 0.5s ease 0.3s both; }
  .feat-2 { animation: featFade 0.5s ease 0.55s both; }
  .feat-3 { animation: featFade 0.5s ease 0.8s both; }
`;

export function Auth({ onAuthSuccess }) {
  const navigate = useNavigate();
  const [activeTab, setActiveTab] = useState("login");

  const [loginForm, setLoginForm] = useState({
    email: "",
    password: "",
  });

  const [signupForm, setSignupForm] = useState({
    user_name: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const [showLoginPassword, setShowLoginPassword] = useState(false);
  const [showSignupPassword, setShowSignupPassword] = useState(false);
  const [showSignupConfirmPassword, setShowSignupConfirmPassword] =
    useState(false);

  const handleLoginChange = (e) => {
    const { name, value } = e.target;
    setLoginForm((prev) => ({ ...prev, [name]: value }));
  };

  const handleSignupChange = (e) => {
    const { name, value } = e.target;
    setSignupForm((prev) => ({ ...prev, [name]: value }));
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setSuccess("");
    try {
      const result = await loginUser({
        email: loginForm.email,
        password: loginForm.password,
      });
      saveAuth(result);
      if (onAuthSuccess) onAuthSuccess(result.user);
      navigate("/dashboard");
    } catch (err) {
      setError(err.message || "Login failed");
    } finally {
      setLoading(false);
    }
  };

  const handleSignup = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setSuccess("");
    if (signupForm.password !== signupForm.confirmPassword) {
      setError("Passwords do not match");
      setLoading(false);
      return;
    }
    try {
      await signupUser({
        user_name: signupForm.user_name,
        email: signupForm.email,
        password: signupForm.password,
      });
      setSuccess("Account created successfully. Please login.");
      setActiveTab("login");
      setLoginForm({ email: signupForm.email, password: "" });
      setSignupForm({
        user_name: "",
        email: "",
        password: "",
        confirmPassword: "",
      });
    } catch (err) {
      setError(err.message || "Signup failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <style>{animStyles}</style>

      <Navbar />
     <div className="min-h-screen bg-background flex items-center justify-center px-4 py-20">
        <div className="w-full max-w-6xl mx-auto">
          <div className="min-h-[700px]! flex flex-row justify-center items-stretch ">
            <Card className="w-full lg:flex-1 lg:basis-1/2 flex flex-col justify-between p-8 min-h-[650px] bg-card border border-border shadow-xl text-foreground overflow-hidden relative">
              <div className="absolute -top-20 -left-20 w-72 h-72 rounded-full bg-emerald-400/10 blur-3xl pointer-events-none" />
              <div className="absolute -bottom-16 -right-16 w-56 h-56 rounded-full bg-green-300/10 blur-3xl pointer-events-none" />

              <div className="relative z-10">
                <div className="flex items-center gap-3 mb-6">
                  <div>
                    <h1 className="text-3xl text-white">W.I.P.E.R</h1>
                    <p className="text-emerald-100 text-sm">
                      Weed Identification, Prediction and Eradication Robot
                    </p>
                  </div>
                </div>

                <Badge className="bg-white/15 text-white border border-white/20 mb-6 flex items-center gap-2 w-fit">
                  <span className="badge-dot w-2 h-2 rounded-full bg-emerald-400 inline-block" />
                  Smart Agriculture Dashboard
                </Badge>

                <div className="flex flex-col gap-3">
                  <div className="feat-1 flex items-center gap-3">
                    <span className="flex items-center justify-center w-6 h-8 rounded-lg bg-white/10 text-sm shrink-0">
                      🌿
                    </span>
                    <span className="text-sm text-emerald-100/85">
                      AI-powered weed detection in real-time
                    </span>
                  </div>
                  <div className="feat-2 flex items-center gap-3">
                    <span className="flex items-center justify-center w-6 h-8 rounded-lg bg-white/10 text-sm shrink-0">
                      🤖
                    </span>
                    <span className="text-sm text-emerald-100/85">
                      Autonomous robotic eradication system
                    </span>
                  </div>
                  <div className="feat-3 flex items-center gap-3">
                    <span className="flex items-center justify-center w-6 h-8 rounded-lg bg-white/10 text-sm shrink-0">
                      📊
                    </span>
                    <span className="text-sm text-emerald-100/85">
                      Weed eradication analytics
                    </span>
                  </div>
                </div>
              </div>

              <p className="relative z-10 text-sm text-emerald-100/60 border-t border-white/10 pt-5 mt-8">
                Login or create an account to continue.
              </p>
            </Card>

            <Card className="w-full lg:flex-1 lg:basis-1/2 p-8 min-h-[650px] bg-card border border-border shadow-xl">
             <Tabs
                value={activeTab}
                onValueChange={(v) => {
                  setActiveTab(v);
                  setError("");
                  setSuccess("");
                }}
                className="space-y-6 h-full"
              >
                <TabsList className="grid grid-cols-2 w-full bg-muted border border-border">
                  <TabsTrigger
                    value="login"
                    className="data-[state=active]:bg-primary
data-[state=active]:text-primary-foreground"
                  >
                    Login
                  </TabsTrigger>
                  <TabsTrigger
                    value="signup"
                    className="data-[state=active]:bg-primary
data-[state=active]:text-primary-foreground"
                  >
                    Sign Up
                  </TabsTrigger>
                </TabsList>

                {(error || success) && (
                  <div
                    className={`rounded-xl px-4 py-3 text-sm border ${
                      error
                        ? "bg-[#7f1d1d] text-[#fecaca] border-[#ef4444]"
                        : "bg-emerald-50 text-[#2a7d2f] border-[#2a7d2f]/20"
                    }`}
                  >
                    {error || success}
                  </div>
                )}

                <div className="min-h-[420px]">
                  <TabsContent value="login" className="mt-0">
                    <form onSubmit={handleLogin} className="space-y-4">
                      <div>
                        <label className="text-sm text-[#2a5c43] mb-2 block">
                          Email
                        </label>
                        <div className="relative flex items-center">
                          <Mail className="w-4 h-4 absolute left-3 text-[#2a5c43] pointer-events-none z-10" />
                          <Input
                            name="email"
                            type="email"
                            placeholder="Enter your email"
                            value={loginForm.email}
                            onChange={handleLoginChange}
                            className="pl-10 border-border bg-input"
                            required
                          />
                        </div>
                      </div>

                      <div>
                        <label className="text-sm text-[#2a5c43] mb-2 block">
                          Password
                        </label>

                        <div className="relative">
                          <Lock className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-[#2a5c43] pointer-events-none z-10" />

                          <Input
                            name="password"
                            type={showLoginPassword ? "text" : "password"}
                            placeholder="Enter your password"
                            value={loginForm.password}
                            onChange={handleLoginChange}
                            className="w-full pl-10 pr-12 border-border bg-input"
                            required
                          />

                          <button
                            type="button"
                            onClick={() =>
                              setShowLoginPassword((prev) => !prev)
                            }
                            className="absolute right-3 top-1/2 -translate-y-1/2 text-[#2a5c43] hover:text-[#0a3d2c] transition-colors"
                            tabIndex={-1}
                          >
                            {showLoginPassword ? (
                              <EyeOff className="w-4 h-4" />
                            ) : (
                              <Eye className="w-4 h-4" />
                            )}
                          </button>
                        </div>
                      </div>
                      <Button
                        type="submit"
                        disabled={loading}
                        className="w-full bg-primary text-primary-foreground hover:opacity-90"
                      >
                        {loading ? "Logging in..." : "Login"}
                      </Button>
                    </form>
                  </TabsContent>

                  <TabsContent value="signup" className="mt-0">
                    <form onSubmit={handleSignup} className="space-y-4">
                      <div>
                        <label className="text-sm text-[#2a5c43] mb-2 block">
                          User Name
                        </label>
                        <div className="relative flex items-center">
                          <User className="w-4 h-4 absolute left-3 text-[#2a5c43] pointer-events-none z-10" />
                          <Input
                            name="user_name"
                            type="text"
                            placeholder="Enter your name"
                            value={signupForm.user_name}
                            onChange={handleSignupChange}
                            className="pl-10 border-border bg-input"
                            required
                          />
                        </div>
                      </div>

                      <div>
                        <label className="text-sm text-[#2a5c43] mb-2 block">
                          Email
                        </label>
                        <div className="relative flex items-center">
                          <Mail className="w-4 h-4 absolute left-3 text-[#2a5c43] pointer-events-none z-10" />
                          <Input
                            name="email"
                            type="email"
                            placeholder="Enter your email"
                            value={signupForm.email}
                            onChange={handleSignupChange}
                            className="pl-10 border-border bg-input"
                            required
                          />
                        </div>
                      </div>

                      <div>
                        <label className="text-sm text-[#2a5c43] mb-2 block">
                          Password
                        </label>
                        <div className="relative flex items-center">
                          <Lock className="w-4 h-4 absolute left-3 text-[#2a5c43] pointer-events-none z-10" />
                          <Input
                            name="password"
                            type={showSignupPassword ? "text" : "password"}
                            placeholder="Create password"
                            value={signupForm.password}
                            onChange={handleSignupChange}
                            className="pl-10 pr-10 border-border bg-input"
                            required
                          />
                          <button
                            type="button"
                            onClick={() =>
                              setShowSignupPassword((prev) => !prev)
                            }
                            className="absolute right-3 text-[#2a5c43] hover:text-[#0a3d2c] transition-colors"
                            tabIndex={-1}
                          >
                            {showSignupPassword ? (
                              <EyeOff className="w-4 h-4" />
                            ) : (
                              <Eye className="w-4 h-4" />
                            )}
                          </button>
                        </div>
                      </div>

                      <div>
                        <label className="text-sm text-[#2a5c43] mb-2 block">
                          Confirm Password
                        </label>
                        <div className="relative flex items-center">
                          <Lock className="w-4 h-4 absolute left-3 text-[#2a5c43] pointer-events-none z-10" />
                          <Input
                            name="confirmPassword"
                            type={
                              showSignupConfirmPassword ? "text" : "password"
                            }
                            placeholder="Confirm password"
                            value={signupForm.confirmPassword}
                            onChange={handleSignupChange}
                            className="pl-10 pr-10 border-border bg-input"
                            required
                          />
                          <button
                            type="button"
                            onClick={() =>
                              setShowSignupConfirmPassword((prev) => !prev)
                            }
                            className="absolute right-3 text-[#2a5c43] hover:text-[#0a3d2c] transition-colors"
                            tabIndex={-1}
                          >
                            {showSignupConfirmPassword ? (
                              <EyeOff className="w-4 h-4" />
                            ) : (
                              <Eye className="w-4 h-4" />
                            )}
                          </button>
                        </div>
                      </div>

                      <Button
                        type="submit"
                        disabled={loading}
                        className="w-full bg-primary text-primary-foreground hover:opacity-90"
                      >
                        {loading ? "Creating account..." : "Create Account"}
                      </Button>
                    </form>
                  </TabsContent>
                </div>
              </Tabs>
            </Card>
          </div>
        </div>
      </div>
    </>
  );
}
