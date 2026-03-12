import { motion } from "framer-motion";
import { Camera, Brain, Crosshair } from "lucide-react";

const steps = [
  {
    icon: Camera,
    step: "01",
    title: "See",
    description: "The onboard camera captures the crop field in real-time as the tractor moves through rows.",
  },
  {
    icon: Brain,
    step: "02",
    title: "Detect",
    description: "YOLO AI model processes each frame, identifying weeds with confidence scores and bounding boxes.",
  },
  {
    icon: Crosshair,
    step: "03",
    title: "Eliminate",
    description: "Galvo mirrors steer a precision laser to the weed center. STM32 fires a controlled pulse — weed eliminated.",
  },
];

const HowItWorksSection = () => {
  return (
    <section id="how-it-works" className="py-24 relative overflow-hidden">
      <div className="container mx-auto px-6">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="text-center mb-16"
        >
          <span className="text-xs font-mono text-accent tracking-widest uppercase mb-4 block">
            The Pipeline
          </span>
          <h2 className="text-3xl sm:text-5xl font-bold tracking-tight">
            How It <span className="text-gradient">Works</span>
          </h2>
        </motion.div>

        <div className="grid md:grid-cols-3 gap-8 relative">
          {/* Connecting line */}
          <div className="hidden md:block absolute top-24 left-[20%] right-[20%] h-px bg-gradient-to-r from-primary via-accent to-primary opacity-30" />

          {steps.map((step, i) => (
            <motion.div
              key={step.step}
              initial={{ opacity: 0, y: 40 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.2 }}
              className="relative text-center"
            >
              <div className="relative inline-flex items-center justify-center w-20 h-20 rounded-full border-2 border-primary/30 bg-secondary mb-6 mx-auto">
                <step.icon size={32} className="text-accent" />
                <div className="absolute -top-2 -right-2 w-7 h-7 rounded-full bg-accent text-accent-foreground text-xs font-bold flex items-center justify-center">
                  {step.step}
                </div>
              </div>
              <h3 className="text-2xl font-bold mb-3">{step.title}</h3>
              <p className="text-muted-foreground text-sm leading-relaxed max-w-xs mx-auto">
                {step.description}
              </p>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default HowItWorksSection;
