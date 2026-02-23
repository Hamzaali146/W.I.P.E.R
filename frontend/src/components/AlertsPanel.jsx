import { Card } from "./ui/card";
import { Badge } from "./ui/badge";
import { AlertTriangle, Info, CheckCircle, XCircle, Bell } from "lucide-react";
import { useState } from "react";

const mockAlerts = [
  {
    id: 1,
    type: "warning",
    title: "Battery Low",
    message: "Device battery at 25%. Consider charging soon.",
    timestamp: "2 min ago",
    read: false,
  },
  {
    id: 2,
    type: "success",
    title: "Session Complete",
    message: "North Field A completed with 98.2% efficiency.",
    timestamp: "15 min ago",
    read: false,
  },
  {
    id: 3,
    type: "info",
    title: "High Weed Density",
    message: "Zone C showing elevated weed density (92/100 sq ft).",
    timestamp: "1 hr ago",
    read: true,
  },
  {
    id: 4,
    type: "critical",
    title: "Laser Temperature High",
    message: "Laser temperature reached 65°C. System paused for cooling.",
    timestamp: "3 hrs ago",
    read: true,
  },
];

export function AlertsPanel() {
  const [alerts, setAlerts] = useState(mockAlerts);
  const unreadCount = alerts.filter(a => !a.read).length;

  const markAsRead = (id) => {
    setAlerts(prev =>
      prev.map(a =>
        a.id === id ? { ...a, read: true } : a
      )
    );
  };

  const markAllAsRead = () => {
    setAlerts(prev =>
      prev.map(a => ({ ...a, read: true }))
    );
  };

  const getIcon = (type) => {
    switch (type) {
      case "critical":
        return <XCircle className="w-5 h-5 text-red-500" />;
      case "warning":
        return <AlertTriangle className="w-5 h-5 text-orange-500" />;
      case "success":
        return <CheckCircle className="w-5 h-5 text-[#2a7d2f]" />;
      default:
        return <Info className="w-5 h-5 text-blue-500" />;
    }
  };

  const getBorderColor = (type) => {
    switch (type) {
      case "critical":
        return "border-red-500/40";
      case "warning":
        return "border-orange-500/40";
      case "success":
        return "border-[#2a7d2f]/40";
      default:
        return "border-blue-500/40";
    }
  };

  const getBgColor = (type) => {
    switch (type) {
      case "critical":
        return "from-white to-red-50/30";
      case "warning":
        return "from-white to-orange-50/30";
      case "success":
        return "from-white to-emerald-50/30";
      default:
        return "from-white to-blue-50/30";
    }
  };

  return (
    <Card className="p-6 bg-gradient-to-br from-white to-emerald-50/30 border-2 border-[#2a7d2f]/30 shadow-lg">
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-2">
          <Bell className="w-5 h-5 text-[#2a5c43]" />
          <h2 className="text-[#0a3d2c]">Alerts & Notifications</h2>
          {unreadCount > 0 && (
            <Badge className="bg-red-500 text-white">
              {unreadCount} new
            </Badge>
          )}
        </div>

        {unreadCount > 0 && (
          <button
            onClick={markAllAsRead}
            className="text-sm text-[#2a7d2f] hover:text-[#0a3d2c] transition-colors px-3 py-1 rounded-lg hover:bg-[#2a7d2f]/10"
          >
            Mark all as read
          </button>
        )}
      </div>

      <div className="space-y-3">
        {alerts.map((alert) => (
          <div
            key={alert.id}
            onClick={() => markAsRead(alert.id)}
            className={`p-4 border-2 rounded-xl transition-all cursor-pointer ${
              alert.read
                ? "bg-white border-[#2a7d2f]/20 hover:border-[#2a7d2f]/40"
                : `bg-gradient-to-r ${getBgColor(alert.type)} ${getBorderColor(alert.type)} shadow-sm hover:shadow-md`
            }`}
          >
            <div className="flex items-start gap-3">
              <div className="flex-shrink-0 mt-0.5">
                {getIcon(alert.type)}
              </div>

              <div className="flex-1 min-w-0">
                <div className="flex items-start justify-between mb-1">
                  <h4 className="text-[#0a3d2c]">{alert.title}</h4>
                  <span className="text-xs text-[#2a5c43] whitespace-nowrap ml-2">
                    {alert.timestamp}
                  </span>
                </div>
                <p className="text-sm text-[#2a5c43]">
                  {alert.message}
                </p>
              </div>

              {!alert.read && (
                <div className="w-2 h-2 bg-[#2a7d2f] rounded-full flex-shrink-0 mt-2"></div>
              )}
            </div>
          </div>
        ))}
      </div>

      {alerts.length === 0 && (
        <div className="text-center py-8">
          <CheckCircle className="w-12 h-12 text-[#2a7d2f] mx-auto mb-3 opacity-50" />
          <p className="text-[#2a5c43]">No alerts at this time</p>
          <p className="text-sm text-[#2a5c43] mt-1">
            All systems operating normally
          </p>
        </div>
      )}
    </Card>
  );
}