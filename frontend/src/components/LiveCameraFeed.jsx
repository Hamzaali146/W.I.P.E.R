import { useEffect, useState } from "react";
import { Card } from "./ui/card";
import { Badge } from "./ui/badge";
import { Camera, Crosshair, AlertTriangle } from "lucide-react";
import { ImageWithFallback } from "./figma/ImageWithFallback";

export function LiveCameraFeed({
  streamUrl,
  detections,
  stats,
  modelInfo,
}) {
  const defaultStream =
    "https://images.unsplash.com/photo-1715194717972-bc42451ec72c?auto=format&fit=crop&w=1080&q=80";

  const defaultDetections = [
    { id: 1, top: "20%", left: "30%", label: "Weed" },
    { id: 2, top: "60%", left: "65%", label: "Weed" },
  ];

  const defaultStats = {
    detectionRate: "98.5%",
    accuracy: "99.2%",
    falsePositives: "0.8%",
    fps: 30,
  };

  const defaultModelInfo =
    "AI Model: WeedNet v2.1 | Confidence threshold: 95%";

  const [showDetections, setShowDetections] = useState(true);

  // Optional simulation toggle
  useEffect(() => {
    const interval = setInterval(() => {
      setShowDetections((prev) => !prev);
    }, 2000);

    return () => clearInterval(interval);
  }, []);

  const activeDetections =
    Array.isArray(detections) && detections.length
      ? detections
      : defaultDetections;

  const activeStats = stats || defaultStats;
  const activeModelInfo = modelInfo || defaultModelInfo;

  return (
    <Card className="p-6 bg-gradient-to-br from-white to-emerald-50/30 border-2 border-[#2a7d2f]/30 shadow-lg">
      {/* Header */}
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2">
          <h2 className="text-[#0a3d2c]">Live Camera Feed</h2>

          <Badge className="bg-red-500 text-white shadow-md">
            <span className="w-2 h-2 bg-white rounded-full mr-1 animate-pulse"></span>
            Recording
          </Badge>
        </div>

        <Camera className="w-5 h-5 text-[#2a5c43]" />
      </div>

      {/* Camera View */}
      <div className="relative aspect-video bg-black rounded-xl overflow-hidden border-2 border-[#2a7d2f]/30 shadow-inner">
        <ImageWithFallback
          src={streamUrl || defaultStream}
          alt="Live camera feed"
          className="w-full h-full object-cover opacity-80"
        />

        {/* Overlay */}
        <div className="absolute inset-0">
          {/* Crosshair grid */}
          <svg className="absolute inset-0 w-full h-full opacity-50">
            <line
              x1="50%"
              y1="0"
              x2="50%"
              y2="100%"
              stroke="#2a7d2f"
              strokeWidth="2"
            />
            <line
              x1="0"
              y1="50%"
              x2="100%"
              y2="50%"
              stroke="#2a7d2f"
              strokeWidth="2"
            />
          </svg>

          {/* Detection Boxes */}
          {showDetections &&
            activeDetections.map((det) => (
              <div
                key={det.id}
                className="absolute w-16 h-16 border-2 border-red-500 animate-pulse shadow-lg"
                style={{ top: det.top, left: det.left }}
              >
                <div className="absolute -top-6 left-0 bg-red-500 text-white px-2 py-0.5 text-xs rounded-md shadow-md">
                  {det.label}
                </div>
              </div>
            ))}

          {/* Bottom Status */}
          <div className="absolute bottom-4 left-4 right-4 flex items-center justify-between">
            <div className="flex items-center gap-2 bg-black/80 text-white px-4 py-2 rounded-xl backdrop-blur-md border border-white/20">
              <Crosshair className="w-4 h-4 text-[#86efac]" />
              <span className="text-sm">AI Detection Active</span>
            </div>

            <div className="bg-black/80 text-white px-4 py-2 rounded-xl backdrop-blur-md border border-white/20">
              <span className="text-sm">FPS: {activeStats.fps}</span>
            </div>
          </div>
        </div>
      </div>

      {/* Camera Stats */}
      <div className="grid grid-cols-3 gap-3 mt-4">
        <div className="text-center p-3 bg-white rounded-xl border border-[#2a7d2f]/20 shadow-sm">
          <p className="text-sm text-[#2a5c43] mb-1">Detection Rate</p>
          <p className="text-[#2a7d2f]">{activeStats.detectionRate}</p>
        </div>

        <div className="text-center p-3 bg-white rounded-xl border border-[#2a7d2f]/20 shadow-sm">
          <p className="text-sm text-[#2a5c43] mb-1">Accuracy</p>
          <p className="text-[#2a7d2f]">{activeStats.accuracy}</p>
        </div>

        <div className="text-center p-3 bg-white rounded-xl border border-[#2a7d2f]/20 shadow-sm">
          <p className="text-sm text-[#2a5c43] mb-1">False Positives</p>
          <p className="text-[#2a7d2f]">{activeStats.falsePositives}</p>
        </div>
      </div>

      {/* AI Model Info */}
      <div className="mt-4 p-4 bg-gradient-to-r from-[#2a7d2f]/10 to-[#0a3d2c]/10 rounded-xl border border-[#2a7d2f]/30 flex items-start gap-3">
        <AlertTriangle className="w-5 h-5 text-[#2a7d2f] mt-0.5 flex-shrink-0" />
        <div className="text-sm text-[#0a3d2c]">
          <p>{activeModelInfo}</p>
        </div>
      </div>
    </Card>
  );
}