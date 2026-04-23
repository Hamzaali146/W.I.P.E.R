import { motion } from "framer-motion";
import { Mail, Github } from "lucide-react";
import wiperLogo from "@/assets/wiper-logo.png";

const FooterSection = () => {
  return (
    <footer id="contact" className="py-16 border-t border-border">
      <div className="container mx-auto px-6">
        <div className="grid md:grid-cols-3 gap-12 mb-12">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <div className="flex items-center gap-3 mb-4">
              <img src={wiperLogo} alt="W.I.P.E.R" className="h-8 w-8" />
              <span className="text-xl font-bold">
                W.I.P.E.<span className="text-accent">R</span>
              </span>
            </div>
            <p className="text-sm text-muted-foreground leading-relaxed">
              Weed Identification Prediction & Eradication Robot — a final year project pushing the boundaries of precision agriculture.
            </p>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.1 }}
          >
            <h4 className="font-semibold mb-4 text-accent font-mono text-xs tracking-widest uppercase">
              Quick Links
            </h4>
            <ul className="space-y-2">
              {["About", "Features", "How It Works", "Tech Stack"].map((link) => (
                <li key={link}>
                  <button
                    onClick={() =>
                      document
                        .getElementById(link.toLowerCase().replace(/ /g, "-"))
                        ?.scrollIntoView({ behavior: "smooth" })
                    }
                    className="text-sm text-muted-foreground hover:text-foreground transition-colors"
                  >
                    {link}
                  </button>
                </li>
              ))}
            </ul>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.2 }}
          >
            <h4 className="font-semibold mb-4 text-accent font-mono text-xs tracking-widest uppercase">
              Get in Touch
            </h4>
            <div className="space-y-3">
              <a
                href="mailto:wiper-project@university.edu"
                className="flex items-center gap-3 text-sm text-muted-foreground hover:text-foreground transition-colors"
              >
                <Mail size={16} />
                hamzaaly105@gmail.com
              </a>
              <a
                href="https://github.com/Hamzaali146/W.I.P.E.R/"
                className="flex items-center gap-3 text-sm text-muted-foreground hover:text-foreground transition-colors"
              >
                <Github size={16} />
                GitHub Repository
              </a>
            </div>
          </motion.div>
        </div>

        <div className="border-t border-border pt-8 text-center">
          <p className="text-xs text-muted-foreground font-mono">
            © 2026 W.I.P.E.R — Final Year Project. Built with precision.
          </p>
        </div>
      </div>
    </footer>
  );
};

export default FooterSection;
