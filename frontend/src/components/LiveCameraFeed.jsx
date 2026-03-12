import { useMemo } from "react";
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

  const defaultStats = {
    detectionRate: "N/A",
    accuracy: "N/A",
    falsePositives: "N/A",
    fps: 0,
  };

  const defaultModelInfo = "ROS camera stream is ready when backend is connected.";

  const activeStats = stats || defaultStats;
  const activeModelInfo = modelInfo || defaultModelInfo;

  const activeDetections = useMemo(() => {
    if (!Array.isArray(detections)) {
      return [];
    }

    return detections
      .map((det, index) => {
        if (typeof det?.top === "string" && typeof det?.left === "string") {
          return {
            id: det.id || index,
            top: det.top,
            left: det.left,
            width: det.width || "16%",
            height: det.height || "16%",
            label: det.label || "Weed",
          };
        }

        const bboxX = typeof det?.bbox_x === "number" ? det.bbox_x : 0;
        const bboxY = typeof det?.bbox_y === "number" ? det.bbox_y : 0;
        const bboxW = typeof det?.bbox_w === "number" ? det.bbox_w : 0.12;
        const bboxH = typeof det?.bbox_h === "number" ? det.bbox_h : 0.12;
        const confidence = typeof det?.confidence === "number" ? Math.round(det.confidence * 100) : null;

        const left = Math.max(0, Math.min(96, bboxX * 100));
        const top = Math.max(0, Math.min(96, bboxY * 100));
        const width = Math.max(4, Math.min(100 - left, bboxW * 100));
        const height = Math.max(4, Math.min(100 - top, bboxH * 100));

        return {
          id: det?.id || index,
          top: `${top}%`,
          left: `${left}%`,
          width: `${width}%`,
          height: `${height}%`,
          label: confidence === null ? "Weed" : `Weed ${confidence}%`,
        };
      })
      .filter(Boolean);
  }, [detections]);

  return (
    <Card className="p-6 surface-card">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2">
          <h2 className="section-title">Live Camera Feed</h2>

          <Badge className="status-pill status-pill--warm">
            <span className="w-2 h-2 bg-white rounded-full mr-1 animate-pulse"></span>
            Recording
          </Badge>
        </div>

        <Camera className="w-5 h-5 text-primary" />
      </div>

      <div className="relative aspect-video bg-black camera-frame">
        <ImageWithFallback
          src={streamUrl || defaultStream}
          alt="Live camera feed"
          className="w-full h-full object-cover opacity-80"
        />

        <div className="absolute inset-0">
          <div className="absolute inset-0 bg-gradient-to-br from-primary/10 via-transparent to-accent/10" />
          <svg className="absolute inset-0 w-full h-full opacity-50">
            <line x1="50%" y1="0" x2="50%" y2="100%" stroke="hsl(174, 78%, 26%)" strokeWidth="1.5" />
            <line x1="0" y1="50%" x2="100%" y2="50%" stroke="hsl(174, 78%, 26%)" strokeWidth="1.5" />
          </svg>

          {activeDetections.map((det) => (
            <div
              key={det.id}
              className="absolute border-2 border-accent animate-pulse shadow-lg"
              style={{
                top: det.top,
                left: det.left,
                width: det.width,
                height: det.height,
              }}
            >
              <div className="absolute -top-6 left-0 bg-accent text-white px-2 py-0.5 text-xs rounded-md shadow-md">
                {det.label}
              </div>
            </div>
          ))}

          {activeDetections.length === 0 && (
            <div className="absolute top-4 left-4 bg-black/70 text-white text-xs px-3 py-1 rounded-lg border border-white/20">
              No detections yet
            </div>
          )}

          <div className="absolute bottom-4 left-4 right-4 flex items-center justify-between">
            <div className="flex items-center gap-2 camera-hud text-white px-4 py-2">
              <Crosshair className="w-4 h-4 text-primary-foreground" />
              <span className="text-sm">AI Detection Active</span>
            </div>

            <div className="camera-hud text-white px-4 py-2">
              <span className="text-sm">FPS: {activeStats.fps || 0}</span>
            </div>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-3 gap-3 mt-4 stagger-list">
        <div className="text-center p-3 metric-tile-light chip-cyan">
          <p className="text-sm text-muted-foreground mb-1">Detection Rate</p>
          <p className="text-primary">{activeStats.detectionRate}</p>
        </div>

        <div className="text-center p-3 metric-tile-light chip-lime">
          <p className="text-sm text-muted-foreground mb-1">Accuracy</p>
          <p className="text-primary">{activeStats.accuracy}</p>
        </div>

        <div className="text-center p-3 metric-tile-light chip-orange">
          <p className="text-sm text-muted-foreground mb-1">False Positives</p>
          <p className="text-primary">{activeStats.falsePositives}</p>
        </div>
      </div>

      <div className="mt-4 p-4 notice-panel flex items-start gap-3">
        <AlertTriangle className="w-5 h-5 text-primary mt-0.5 flex-shrink-0" />
        <div className="text-sm text-foreground">
          <p>{activeModelInfo}</p>
        </div>
      </div>
    </Card>
  );
}
