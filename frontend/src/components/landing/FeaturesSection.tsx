import { motion } from "framer-motion";
import { Eye, Zap, Shield, Cpu } from "lucide-react";

const features = [
  {
    icon: Eye,
    title: "AI Weed Detection",
    description: "YOLO-powered vision system identifies weeds with high confidence, publishing detections on /weedbot/detections in real-time.",
    accent: true,
  },
  {
    icon: Zap,
    title: "Laser Eradication",
    description: "Galvo-steered laser converts pixel coordinates to precise DAC voltages, delivering controlled pulses to destroy weeds at the root.",
    accent: false,
  },
  {
    icon: Shield,
    title: "Safety Interlocks",
    description: "Multi-layer safety: software arm/disarm, hardware E-stop, key switch, enclosure lid switch, and dry-run mode for testing.",
    accent: false,
  },
  {
    icon: Cpu,
    title: "ROS2 Architecture",
    description: "Modular weedbot_control node with configurable parameters for camera FOV, galvo limits, shot cooldown, and serial communication.",
    accent: true,
  },
];

const FeaturesSection = () => {
  return (
    <section id="features" className="py-24 relative">
      <div className="absolute inset-0 bg-grid opacity-10" />
      <div className="container mx-auto px-6 relative z-10">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="text-center mb-16"
        >
          <span className="text-xs font-mono text-accent tracking-widest uppercase mb-4 block">
            Core Capabilities
          </span>
          <h2 className="text-3xl sm:text-5xl font-bold tracking-tight">
            Built for the <span className="text-gradient">Field</span>
          </h2>
        </motion.div>

        <div className="grid sm:grid-cols-2 gap-6">
          {features.map((feature, i) => (
            <motion.div
              key={feature.title}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.1 }}
              className={`group relative p-8 rounded-2xl border transition-all duration-300 hover:-translate-y-1 ${
                feature.accent
                  ? "border-primary/30 bg-primary/5 hover:glow-violet"
                  : "border-border bg-card hover:border-accent/30 hover:glow-lime"
              }`}
            >
              <div
                className={`w-12 h-12 rounded-xl flex items-center justify-center mb-5 ${
                  feature.accent
                    ? "bg-primary/20 text-primary"
                    : "bg-accent/10 text-accent"
                }`}
              >
                <feature.icon size={24} />
              </div>
              <h3 className="text-xl font-semibold mb-3">{feature.title}</h3>
              <p className="text-muted-foreground text-sm leading-relaxed">
                {feature.description}
              </p>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default FeaturesSection;
