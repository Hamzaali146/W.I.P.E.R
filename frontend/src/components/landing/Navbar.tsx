import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { Menu, X } from "lucide-react";
import wiperLogo from "@/assets/wiper-logo.png";

const navItems = ["About", "Features", "How It Works", "Tech Stack", "Contact"];

const Navbar = () => {
  const [scrolled, setScrolled] = useState(false);
  const [mobileOpen, setMobileOpen] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 50);
    window.addEventListener("scroll", onScroll);
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  const scrollTo = (id: string) => {
    document.getElementById(id.toLowerCase().replace(/ /g, "-"))?.scrollIntoView({ behavior: "smooth" });
    setMobileOpen(false);
  };

  return (
    <motion.nav
      initial={{ y: -100 }}
      animate={{ y: 0 }}
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
        scrolled ? "bg-background/80 backdrop-blur-xl border-b border-border" : "bg-transparent"
      }`}
    >
      <div className="container mx-auto px-6 py-4 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <img src={wiperLogo} alt="W.I.P.E.R Logo" className="h-8 w-8" />
          <span className="text-xl font-bold tracking-tight">
            W.I.P.E.<span className="text-accent">R</span>
          </span>
        </div>

        {/* Desktop */}
        <div className="hidden md:flex items-center gap-8">
          {navItems.map((item) => (
            <button
              key={item}
              onClick={() => scrollTo(item)}
              className="text-sm text-muted-foreground hover:text-foreground transition-colors"
            >
              {item}
            </button>
          ))}
        </div>

        {/* Mobile toggle */}
        <button className="md:hidden text-foreground" onClick={() => setMobileOpen(!mobileOpen)}>
          {mobileOpen ? <X size={24} /> : <Menu size={24} />}
        </button>
      </div>

      {/* Mobile menu */}
      {mobileOpen && (
        <motion.div
          initial={{ opacity: 0, height: 0 }}
          animate={{ opacity: 1, height: "auto" }}
          className="md:hidden bg-background/95 backdrop-blur-xl border-b border-border"
        >
          <div className="container mx-auto px-6 py-4 flex flex-col gap-4">
            {navItems.map((item) => (
              <button
                key={item}
                onClick={() => scrollTo(item)}
                className="text-left text-sm text-muted-foreground hover:text-foreground transition-colors"
              >
                {item}
              </button>
            ))}
          </div>
        </motion.div>
      )}
    </motion.nav>
  );
};

export default Navbar;
