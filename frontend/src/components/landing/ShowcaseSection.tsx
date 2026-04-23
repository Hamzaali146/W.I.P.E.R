import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { X, ChevronLeft, ChevronRight, ZoomIn } from "lucide-react";
import img1 from "@/assets/1.jpg";
import img2 from "@/assets/2.jpeg";
import img3 from "@/assets/3.jpeg";
import demoVideo from "@/assets/demo.mp4";

const images = [
  { src: img1, caption: "Project photo 1" },
  { src: img2, caption: "Project photo 2" },
  { src: img3, caption: "Project photo 3" },
];

const ShowcaseSection = () => {
  const [lightboxIndex, setLightboxIndex] = useState<number | null>(null);

  const prev = () =>
    setLightboxIndex((i) => (i === null ? null : (i - 1 + images.length) % images.length));
  const next = () =>
    setLightboxIndex((i) => (i === null ? null : (i + 1) % images.length));

  return (
    <section id="showcase" className="py-24 relative">
      <div className="absolute inset-0 bg-grid opacity-10" />
      <div className="container mx-auto px-6 relative z-10">

        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="text-center mb-16"
        >
          <span className="text-xs font-mono text-accent tracking-widest uppercase mb-4 block">
            In Action
          </span>
          <h2 className="text-3xl sm:text-5xl font-bold tracking-tight">
            See the <span className="text-gradient">System</span>
          </h2>
        </motion.div>

        {/* Portrait video — centered, phone-style frame */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="flex flex-col items-center mb-14"
        >
          <p className="text-xs font-mono text-muted-foreground text-center mb-3 tracking-widest uppercase">
            Live Demo
          </p>
          <div className="relative w-[220px] sm:w-[260px] rounded-[2.5rem] border-[6px] border-primary/40 bg-black shadow-2xl shadow-primary/20 overflow-hidden">
            <div className="absolute top-0 left-1/2 -translate-x-1/2 w-20 h-5 bg-black rounded-b-xl z-10" />
            <video
              src={demoVideo}
              autoPlay
              loop
              muted
              playsInline
              className="w-full aspect-[9/16] object-cover"
            />
          </div>
        </motion.div>

        {/* Image grid — below the video */}
        <div className="grid sm:grid-cols-3 gap-4">
          {images.map((img, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.1 }}
              onClick={() => setLightboxIndex(i)}
              className="group relative rounded-xl overflow-hidden border border-border hover:border-accent/40 cursor-pointer transition-all duration-300 hover:-translate-y-1 hover:glow-lime aspect-[4/3]"
            >
              <img
                src={img.src}
                alt={img.caption}
                className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
              />
              <div className="absolute inset-0 bg-black/0 group-hover:bg-black/40 transition-all duration-300 flex items-center justify-center">
                <ZoomIn size={28} className="text-white opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
              </div>
              <div className="absolute bottom-0 left-0 right-0 px-3 py-2 bg-gradient-to-t from-black/70 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                <p className="text-white text-xs font-mono">{img.caption}</p>
              </div>
            </motion.div>
          ))}
        </div>
      </div>

      {/* Lightbox */}
      <AnimatePresence>
        {lightboxIndex !== null && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 z-50 bg-black/90 flex items-center justify-center p-4"
            onClick={() => setLightboxIndex(null)}
          >
            <button
              className="absolute top-4 right-4 text-white/70 hover:text-white transition-colors"
              onClick={() => setLightboxIndex(null)}
            >
              <X size={28} />
            </button>
            <button
              className="absolute left-4 top-1/2 -translate-y-1/2 text-white/70 hover:text-white transition-colors"
              onClick={(e) => { e.stopPropagation(); prev(); }}
            >
              <ChevronLeft size={36} />
            </button>
            <motion.div
              key={lightboxIndex}
              initial={{ opacity: 0, scale: 0.95 }}
              animate={{ opacity: 1, scale: 1 }}
              exit={{ opacity: 0, scale: 0.95 }}
              className="max-w-4xl w-full"
              onClick={(e) => e.stopPropagation()}
            >
              <img
                src={images[lightboxIndex].src}
                alt={images[lightboxIndex].caption}
                className="w-full max-h-[80vh] object-contain rounded-xl"
              />
              <p className="text-center text-white/60 text-sm font-mono mt-3">
                {images[lightboxIndex].caption}
              </p>
            </motion.div>
            <button
              className="absolute right-4 top-1/2 -translate-y-1/2 text-white/70 hover:text-white transition-colors"
              onClick={(e) => { e.stopPropagation(); next(); }}
            >
              <ChevronRight size={36} />
            </button>
          </motion.div>
        )}
      </AnimatePresence>
    </section>
  );
};

export default ShowcaseSection;
