import { motion } from "framer-motion";
import laserImage from "@/assets/laser-targeting.jpg";

const AboutSection = () => {
  return (
    <section id="about" className="py-24 relative">
      <div className="container mx-auto px-6">
        <div className="grid lg:grid-cols-2 gap-16 items-center">
          <motion.div
            initial={{ opacity: 0, x: -40 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
          >
            <span className="text-xs font-mono text-accent tracking-widest uppercase mb-4 block">
              About the Project
            </span>
            <h2 className="text-3xl sm:text-5xl font-bold tracking-tight mb-6">
              Farming Without{" "}
              <span className="text-gradient">Chemicals</span>
            </h2>
            <p className="text-muted-foreground leading-relaxed mb-6">
              W.I.P.E.R is a tractor-mounted robotic system that uses computer vision to identify weeds 
              in real-time and eliminates them with a precision galvo-steered laser — no herbicides needed.
            </p>
            <p className="text-muted-foreground leading-relaxed mb-8">
              Powered by ROS2, a YOLO-based detection pipeline, and an STM32-controlled laser assembly with 
              DAC8563 galvanometer control, the system achieves sub-centimeter targeting accuracy at field speeds.
            </p>
            <div className="grid grid-cols-3 gap-6">
              {[
                { value: "< 50ms", label: "Detection Latency" },
                { value: "ROS2", label: "Control Framework" },
                { value: "0%", label: "Chemical Usage" },
              ].map((stat) => (
                <div key={stat.label} className="text-center p-4 rounded-lg bg-secondary/50 border border-border">
                  <div className="text-2xl font-bold text-accent mb-1">{stat.value}</div>
                  <div className="text-xs text-muted-foreground font-mono">{stat.label}</div>
                </div>
              ))}
            </div>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, x: 40 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="relative"
          >
            <div className="rounded-2xl overflow-hidden glow-violet">
              <img src={laserImage} alt="Laser targeting weeds" className="w-full h-auto" />
            </div>
            {/* Floating badge */}
            <div className="absolute -bottom-4 -right-4 bg-accent text-accent-foreground px-5 py-3 rounded-xl font-mono text-sm font-semibold shadow-lg">
              Zero Herbicides
            </div>
          </motion.div>
        </div>
      </div>
    </section>
  );
};

export default AboutSection;
