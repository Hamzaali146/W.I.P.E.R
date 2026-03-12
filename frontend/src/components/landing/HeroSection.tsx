import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import { ChevronDown } from "lucide-react";
import heroImage from "@/assets/hero-wiper.jpg";

const HeroSection = () => {
  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
      {/* Background image */}
      <div className="absolute inset-0">
        <img src={heroImage} alt="W.I.P.E.R robot in field" className="w-full h-full object-cover opacity-40" />
        <div className="absolute inset-0 bg-gradient-to-b from-background/60 via-background/40 to-background" />
      </div>

      {/* Grid overlay */}
      <div className="absolute inset-0 bg-grid opacity-20" />

      {/* Scan line effect */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="w-full h-px bg-accent/30 animate-scan-line" />
      </div>

      {/* Content */}
      <div className="relative z-10 container mx-auto px-6 text-center">
        <motion.div
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
        >
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full border border-border bg-secondary/50 backdrop-blur-sm mb-8">
            <span className="w-2 h-2 rounded-full bg-accent animate-pulse" />
            <span className="text-xs font-mono text-muted-foreground tracking-wider uppercase">
              Final Year Project — Precision Agriculture
            </span>
          </div>

          <h1 className="text-5xl sm:text-7xl lg:text-8xl font-bold tracking-tighter leading-none mb-4">
            W.I.P.E.<span className="text-gradient">R</span>
          </h1>

          <p className="text-lg sm:text-xl font-mono text-muted-foreground tracking-wider mb-2">
            Weed Identification Prediction
          </p>
          <p className="text-lg sm:text-xl font-mono text-accent tracking-wider mb-10">
            & Eradication Robot
          </p>

          <p className="max-w-2xl mx-auto text-muted-foreground text-base sm:text-lg mb-12 leading-relaxed">
            An AI-powered, laser-wielding robot that mounts on your tractor to detect and eliminate weeds 
            in real-time — no herbicides, no chemicals, just precision.
          </p>

          <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
            <Button variant="hero" size="lg" className="text-base px-8" onClick={() => document.getElementById("features")?.scrollIntoView({ behavior: "smooth" })}>
              Explore Features
            </Button>
            <Button variant="heroOutline" size="lg" className="text-base px-8" onClick={() => document.getElementById("how-it-works")?.scrollIntoView({ behavior: "smooth" })}>
              How It Works
            </Button>
          </div>
        </motion.div>
      </div>

      {/* Scroll indicator */}
      <motion.div
        className="absolute bottom-8 left-1/2 -translate-x-1/2"
        animate={{ y: [0, 10, 0] }}
        transition={{ repeat: Infinity, duration: 2 }}
      >
        <ChevronDown className="text-muted-foreground" size={28} />
      </motion.div>
    </section>
  );
};

export default HeroSection;
