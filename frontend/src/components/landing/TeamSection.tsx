import { motion } from "framer-motion";
import { Linkedin, Github } from "lucide-react";
import teamImg1 from "@/assets/team-placeholder-1.jpg";
import teamImg2 from "@/assets/team-placeholder-2.jpg";
import teamImg3 from "@/assets/team-placeholder-3.jpg";
import teamImg4 from "@/assets/team-placeholder-4.jpg";
import advisorImg from "@/assets/team-advisor.jpg";

const members = [
  { name: "Sanya Sajid", role: "Integrations/DB", image: teamImg1, linkedin: "", github: "https://github.com/SanyaSajid" },
  { name: "Hamza Ali", role: "Computer Vision/AI & ROS2 Integration", image: teamImg2, linkedin: "https://www.linkedin.com/in/hamza-ali-4502189146102032428/", github: "https://github.com/Hamzaali146" },
  { name: "Fatima Kashif", role: "Full Stack Developer", image: teamImg3, linkedin: "", github: "https://github.com/Fatima-Kashif" },
  { name: "Farzam Nasir", role: "Embedded Systems Hardware & Firmware", image: teamImg4, linkedin: "https://www.linkedin.com/in/farzam-nasir/", github: "https://github.com/FarzamNasir" },
];

const TeamSection = () => {
  return (
    <section id="team" className="py-24 relative">
      <div className="container mx-auto px-6">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="text-center mb-16"
        >
          <span className="text-xs font-mono text-accent tracking-widest uppercase mb-4 block">
            The Minds Behind It
          </span>
          <h2 className="text-3xl sm:text-5xl font-bold tracking-tight">
            Meet the <span className="text-gradient">Team</span>
          </h2>
        </motion.div>

        {/* Advisor */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="flex flex-col items-center mb-16"
        >
          <div className="relative group mb-5">
            <div className="w-32 h-32 rounded-full overflow-hidden border-2 border-accent glow-lime transition-all duration-300 group-hover:scale-105">
              <img src={advisorImg} alt="Dr. Muhammad Khurram" className="w-full h-full object-cover" />
            </div>
            <div className="absolute -bottom-2 left-1/2 -translate-x-1/2 bg-accent text-accent-foreground text-[10px] font-mono font-bold px-3 py-1 rounded-full tracking-wider uppercase whitespace-nowrap">
              Advisor
            </div>
          </div>
          <h3 className="text-xl font-bold">Dr. Muhammad Khurram</h3>
          <p className="text-sm text-muted-foreground font-mono">Project Supervisor</p>
        </motion.div>

        {/* Divider */}
        <div className="flex items-center gap-4 mb-12">
          <div className="flex-1 h-px bg-gradient-to-r from-transparent via-primary/30 to-transparent" />
          <span className="text-xs font-mono text-muted-foreground tracking-widest uppercase">Team Members</span>
          <div className="flex-1 h-px bg-gradient-to-r from-transparent via-primary/30 to-transparent" />
        </div>

        {/* Members grid */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-8">
          {members.map((member, i) => (
            <motion.div
              key={member.name}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.1 }}
              className="group text-center"
            >
              <div className="relative mx-auto w-28 h-28 sm:w-32 sm:h-32 rounded-full overflow-hidden border-2 border-border mb-4 transition-all duration-300 group-hover:border-primary group-hover:glow-violet group-hover:scale-105">
                <img src={member.image} alt={member.name} className="w-full h-full object-cover" />
              </div>
              <h3 className="font-semibold text-base mb-1">{member.name}</h3>
              <p className="text-xs text-muted-foreground font-mono">{member.role}</p>
              <div className="flex items-center justify-center gap-3 mt-3 opacity-0 group-hover:opacity-100 transition-opacity">
                {member.linkedin && (
                  <a href={member.linkedin} target="_blank" rel="noopener noreferrer" className="text-muted-foreground hover:text-primary transition-colors">
                    <Linkedin size={14} />
                  </a>
                )}
                {member.github && (
                  <a href={member.github} target="_blank" rel="noopener noreferrer" className="text-muted-foreground hover:text-primary transition-colors">
                    <Github size={14} />
                  </a>
                )}
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default TeamSection;
