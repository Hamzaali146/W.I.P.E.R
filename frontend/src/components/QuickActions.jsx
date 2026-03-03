import { Card } from "./ui/card";
import { Button } from "./ui/button";
import { Badge } from "./ui/badge";
import {
  Play,
  Pause,
  MapPin,
  Zap,
  TrendingUp,
  Clock,
  Battery,
} from "lucide-react";

export function QuickActions({
  summary,
  systemStatus,
  onStart,
  onStop,
}) {
  const defaultSummary = {
    weedsEliminated: "800",
    areaCovered: "3000 sq ft",
    activeTime: "2h 15m",
    efficiency: "94.2%",
  };

  const defaultSystemStatus = {
    overallLabel: "All Systems Operational",
    items: [
      {
        key: "laser",
        title: "Laser System",
        subtitle: "Operating normally",
        icon: <Zap className="w-5 h-5 text-white" />,
        iconBg: "linear-gradient(135deg, #0f766e, #10b981)",
        badgeText: "Active",
      },
      {
        key: "gps",
        title: "GPS Tracking",
        subtitle: "Signal strength: Strong",
        icon: <MapPin className="w-5 h-5 text-white" />,
        iconBg: "linear-gradient(135deg, #385d75, #2b7c9e)",
        badgeText: "Active",
      },
      {
        key: "battery",
        title: "Battery Level",
        subtitle: "87% remaining",
        icon: <Battery className="w-5 h-5 text-white" />,
        iconBg: "linear-gradient(135deg, #f97316, #fb923c)",
        badgeText: "Good",
      },
    ],
  };

  const s = summary || defaultSummary;
  const status = systemStatus || defaultSystemStatus;

  const handleStartSession = () => {
    if (onStart) return onStart();
    alert("Starting new session...");
  };

  const handleStop = () => {
    if (onStop) return onStop();
    if (confirm("Are you sure you want to emergency stop the device?")) {
      alert("Emergency stop activated!");
    }
  };

  return (
    <div className="space-y-6">
      <Card className="p-6 elevated-card text-white">
        <h2 className="mb-4 text-white">Today&apos;s Summary</h2>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 stagger-list">
          <div className="text-center p-4 metric-tile">
            <Zap className="w-6 h-6 mx-auto mb-2 text-emerald-200 float-subtle" />
            <p className="text-sm text-emerald-100 mb-1">Weeds Eliminated</p>
            <p className="text-white">{s.weedsEliminated}</p>
          </div>

          <div className="text-center p-4 metric-tile">
            <MapPin className="w-6 h-6 mx-auto mb-2 text-cyan-200 float-subtle" />
            <p className="text-sm text-emerald-100 mb-1">Area Covered</p>
            <p className="text-white">{s.areaCovered}</p>
          </div>

          <div className="text-center p-4 metric-tile">
            <Clock className="w-6 h-6 mx-auto mb-2 text-orange-200 float-subtle" />
            <p className="text-sm text-emerald-100 mb-1">Active Time</p>
            <p className="text-white">{s.activeTime}</p>
          </div>

          <div className="text-center p-4 metric-tile">
            <TrendingUp className="w-6 h-6 mx-auto mb-2 text-emerald-200" />
            <p className="text-sm text-emerald-100 mb-1">Efficiency</p>
            <p className="text-white">{s.efficiency}</p>
          </div>
        </div>
      </Card>

      <Card className="p-6 surface-card">
        <h3 className="mb-4 section-title">Quick Actions</h3>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
          <Button
            onClick={handleStartSession}
            className="h-auto py-4 rounded-xl action-primary group"
          >
            <div className="flex items-center gap-3">
              <Play className="w-5 h-5 transition-transform group-hover:translate-x-0.5" />
              <div className="text-left">
                <div>Start New Session</div>
                <div className="text-xs text-orange-50 mt-0.5">Begin weed detection</div>
              </div>
            </div>
          </Button>

          <Button
            onClick={handleStop}
            variant="outline"
            className="h-auto py-4 rounded-xl action-outline group"
          >
            <div className="flex items-center gap-3">
              <Pause className="w-5 h-5 transition-transform group-hover:-translate-y-0.5" />
              <div className="text-left">
                <div>Stop Session</div>
                <div className="text-xs text-red-500 mt-0.5">Immediate halt</div>
              </div>
            </div>
          </Button>
        </div>
      </Card>

      <Card className="p-6 surface-card">
        <div className="flex items-center justify-between mb-4">
          <h3 className="section-title">System Status</h3>
          <Badge className="status-pill">
            <span className="w-2 h-2 bg-emerald-500 rounded-full animate-pulse"></span>
            {status.overallLabel}
          </Badge>
        </div>

        <div className="space-y-3 stagger-list">
          {status.items.map((item) => (
            <div key={item.key} className="flex items-center justify-between p-3 metric-tile-light list-row">
              <div className="flex items-center gap-3">
                <div
                  className="w-10 h-10 rounded-lg flex items-center justify-center"
                  style={{ background: item.iconBg }}
                >
                  {item.icon}
                </div>

                <div>
                  <p className="text-sm text-foreground">{item.title}</p>
                  <p className="text-xs text-muted-foreground">{item.subtitle}</p>
                </div>
              </div>

              <Badge className={`status-pill ${item.badgeText === "Good" ? "status-pill--warm" : "status-pill--cool"}`}>
                {item.badgeText}
              </Badge>
            </div>
          ))}
        </div>
      </Card>
    </div>
  );
}
