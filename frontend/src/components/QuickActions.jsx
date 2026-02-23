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
        iconBg: "from-[#2a7d2f] to-[#0a3d2c]",
        badgeText: "Active",
      },
      {
        key: "gps",
        title: "GPS Tracking",
        subtitle: "Signal strength: Strong",
        icon: <MapPin className="w-5 h-5 text-white" />,
        iconBg: "from-blue-500 to-blue-600",
        badgeText: "Active",
      },
      {
        key: "battery",
        title: "Battery Level",
        subtitle: "87% remaining",
        icon: <Battery className="w-5 h-5 text-white" />,
        iconBg: "from-amber-500 to-amber-600",
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
      {/* Today's Summary */}
      <Card className="p-6 bg-gradient-to-br from-[#0a3d2c] to-[#2a5c43] border-2 border-[#2a7d2f] shadow-xl text-white">
        <h2 className="mb-4 text-white">Today's Summary</h2>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div className="text-center p-4 bg-white/10 backdrop-blur-sm rounded-xl border border-white/20">
            <Zap className="w-6 h-6 mx-auto mb-2 text-[#86efac]" />
            <p className="text-sm text-emerald-100 mb-1">Weeds Eliminated</p>
            <p className="text-white">{s.weedsEliminated}</p>
          </div>

          <div className="text-center p-4 bg-white/10 backdrop-blur-sm rounded-xl border border-white/20">
            <MapPin className="w-6 h-6 mx-auto mb-2 text-[#86efac]" />
            <p className="text-sm text-emerald-100 mb-1">Area Covered</p>
            <p className="text-white">{s.areaCovered}</p>
          </div>

          <div className="text-center p-4 bg-white/10 backdrop-blur-sm rounded-xl border border-white/20">
            <Clock className="w-6 h-6 mx-auto mb-2 text-[#86efac]" />
            <p className="text-sm text-emerald-100 mb-1">Active Time</p>
            <p className="text-white">{s.activeTime}</p>
          </div>

          <div className="text-center p-4 bg-white/10 backdrop-blur-sm rounded-xl border border-white/20">
            <TrendingUp className="w-6 h-6 mx-auto mb-2 text-[#86efac]" />
            <p className="text-sm text-emerald-100 mb-1">Efficiency</p>
            <p className="text-white">{s.efficiency}</p>
          </div>
        </div>
      </Card>

      {/* Quick Actions */}
      <Card className="p-6 bg-gradient-to-br from-white to-emerald-50/30 border-2 border-[#2a7d2f]/30 shadow-lg">
        <h3 className="mb-4 text-[#0a3d2c]">Quick Actions</h3>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
          <Button
            onClick={handleStartSession}
            className="h-auto py-4 bg-gradient-to-r from-[#2a7d2f] to-[#0a3d2c] hover:from-[#0a3d2c] hover:to-[#2a5c43] shadow-md hover:shadow-lg"
          >
            <div className="flex items-center gap-3">
              <Play className="w-5 h-5" />
              <div className="text-left">
                <div>Start New Session</div>
                <div className="text-xs text-emerald-100 mt-0.5">
                  Begin weed detection
                </div>
              </div>
            </div>
          </Button>

          <Button
            onClick={handleStop}
            variant="outline"
            className="h-auto py-4 border-2 border-red-500/40 text-red-600 hover:bg-red-50 hover:border-red-500"
          >
            <div className="flex items-center gap-3">
              <Pause className="w-5 h-5" />
              <div className="text-left">
                <div>Stop Session</div>
                <div className="text-xs text-red-500 mt-0.5">Immediate halt</div>
              </div>
            </div>
          </Button>
        </div>
      </Card>

      {/* System Status */}
      <Card className="p-6 bg-gradient-to-br from-white to-emerald-50/30 border-2 border-[#2a7d2f]/30 shadow-lg">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-[#0a3d2c]">System Status</h3>
          <Badge className="bg-[#2a7d2f] text-white">
            <span className="w-2 h-2 bg-white rounded-full mr-1.5 animate-pulse"></span>
            {status.overallLabel}
          </Badge>
        </div>

        <div className="space-y-3">
          {status.items.map((item) => (
            <div
              key={item.key}
              className="flex items-center justify-between p-3 bg-white rounded-xl border border-[#2a7d2f]/20"
            >
              <div className="flex items-center gap-3">
                <div
                  className={`w-10 h-10 rounded-lg bg-gradient-to-br ${item.iconBg} flex items-center justify-center`}
                >
                  {item.icon}
                </div>

                <div>
                  <p className="text-sm text-[#0a3d2c]">{item.title}</p>
                  <p className="text-xs text-[#2a5c43]">{item.subtitle}</p>
                </div>
              </div>

              <Badge className="bg-emerald-100 text-[#2a7d2f] border border-[#2a7d2f]/20">
                {item.badgeText}
              </Badge>
            </div>
          ))}
        </div>
      </Card>
    </div>
  );
}