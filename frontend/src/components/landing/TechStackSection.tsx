import { motion } from "framer-motion";

const techItems = [
  { category: "Vision", items: ["YOLO Detection", "Camera FOV Mapping", "Confidence Filtering"] },
  { category: "Control", items: ["ROS2 Humble", "weedbot_control Node", "Galvo Angle Mapping"] },
  { category: "Hardware", items: ["STM32 MCU", "DAC8563 Galvo", "USB-TTL Serial"] },
  { category: "Safety", items: ["Arm/Disarm System", "Dry Run Mode", "Hardware Interlocks"] },
];

const packetExample = `$ARM,1*4E
$SHOT,42,32768,32768,500,1000,750*3A
>ACK,42`;

const TechStackSection = () => {
  return (
    <section id="tech-stack" className="py-24 relative">
      <div className="absolute inset-0 bg-grid opacity-10" />
      <div className="container mx-auto px-6 relative z-10">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="text-center mb-16"
        >
          <span className="text-xs font-mono text-accent tracking-widest uppercase mb-4 block">
            Under the Hood
          </span>
          <h2 className="text-3xl sm:text-5xl font-bold tracking-tight">
            Tech <span className="text-gradient">Stack</span>
          </h2>
        </motion.div>

        <div className="grid lg:grid-cols-2 gap-8">
          {/* Tech grid */}
          <div className="grid grid-cols-2 gap-4">
            {techItems.map((group, i) => (
              <motion.div
                key={group.category}
                initial={{ opacity: 0, scale: 0.95 }}
                whileInView={{ opacity: 1, scale: 1 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.1 }}
                className="p-6 rounded-2xl border border-border bg-card"
              >
                <h3 className="text-accent font-mono text-xs tracking-widest uppercase mb-4">
                  {group.category}
                </h3>
                <ul className="space-y-2">
                  {group.items.map((item) => (
                    <li key={item} className="text-sm text-muted-foreground flex items-center gap-2">
                      <span className="w-1.5 h-1.5 rounded-full bg-primary" />
                      {item}
                    </li>
                  ))}
                </ul>
              </motion.div>
            ))}
          </div>

          {/* Terminal */}
          <motion.div
            initial={{ opacity: 0, x: 30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            className="rounded-2xl border border-border bg-card overflow-hidden"
          >
            <div className="flex items-center gap-2 px-4 py-3 border-b border-border bg-secondary/50">
              <div className="w-3 h-3 rounded-full bg-destructive/60" />
              <div className="w-3 h-3 rounded-full bg-accent/40" />
              <div className="w-3 h-3 rounded-full bg-accent/60" />
              <span className="text-xs font-mono text-muted-foreground ml-2">protocol.md — Packet Format</span>
            </div>
            <div className="p-6">
              <pre className="font-mono text-sm text-muted-foreground leading-relaxed">
                <code>
                  <span className="text-accent">{"// Frame format"}</span>{"\n"}
                  <span className="text-foreground">{"$<payload>*<CS>\\n"}</span>{"\n\n"}
                  <span className="text-accent">{"// Example commands"}</span>{"\n"}
                  {packetExample.split("\n").map((line, i) => (
                    <span key={i}>
                      <span className={line.startsWith(">") ? "text-accent" : "text-primary"}>
                        {line}
                      </span>
                      {"\n"}
                    </span>
                  ))}
                </code>
              </pre>
            </div>
          </motion.div>
        </div>
      </div>
    </section>
  );
};

export default TechStackSection;
