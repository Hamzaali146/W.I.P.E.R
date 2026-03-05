import { useMemo } from "react";
import { AlertTriangle, Info, CheckCircle, XCircle, Bell } from "lucide-react";

import { Card } from "./ui/card";
import { Badge } from "./ui/badge";

export function AlertsPanel({ alerts = [], onMarkRead, onMarkAllRead }) {
  const unreadCount = useMemo(() => alerts.filter((a) => !a.read).length, [alerts]);

  const getIcon = (type) => {
    switch (type) {
      case "critical":
        return <XCircle className="w-5 h-5 text-red-500" />;
      case "warning":
        return <AlertTriangle className="w-5 h-5 text-orange-500" />;
      case "success":
        return <CheckCircle className="w-5 h-5 text-emerald-600" />;
      default:
        return <Info className="w-5 h-5 text-cyan-600" />;
    }
  };

  const getBorderColor = (type) => {
    switch (type) {
      case "critical":
        return "border-red-500/35";
      case "warning":
        return "border-orange-400/35";
      case "success":
        return "border-emerald-500/30";
      default:
        return "border-cyan-500/30";
    }
  };

  const getBgColor = (type) => {
    switch (type) {
      case "critical":
        return "from-red-50/80 to-red-100/30";
      case "warning":
        return "from-amber-50/80 to-orange-100/30";
      case "success":
        return "from-emerald-50/80 to-lime-100/35";
      default:
        return "from-cyan-50/80 to-sky-100/30";
    }
  };

  return (
    <Card className="p-6 surface-card">
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-2">
          <Bell className="w-5 h-5 text-primary" />
          <h2 className="section-title">Alerts & Notifications</h2>
          {unreadCount > 0 && (
            <Badge className="status-pill status-pill--warm">{unreadCount} new</Badge>
          )}
        </div>

        {unreadCount > 0 && (
          <button
            onClick={onMarkAllRead}
            className="text-sm transition-colors px-3 py-1 rounded-lg chip-cyan"
            style={{ color: "#0f766e" }}
          >
            Mark all as read
          </button>
        )}
      </div>

      <div className="space-y-3 stagger-list">
        {alerts.map((alert) => (
          <div
            key={alert.id}
            onClick={() => onMarkRead?.(alert.id)}
            className={`p-4 rounded-xl transition-all cursor-pointer ${
              alert.read
                ? "list-row border"
                : `bg-gradient-to-r border list-row ${getBgColor(alert.type)} ${getBorderColor(alert.type)} shadow-sm hover:shadow-md`
            }`}
          >
            <div className="flex items-start gap-3">
              <div className="flex-shrink-0 mt-0.5">{getIcon(alert.type)}</div>

              <div className="flex-1 min-w-0">
                <div className="flex items-start justify-between mb-1">
                  <h4 className="text-foreground">{alert.title}</h4>
                  <span className="text-xs text-muted-foreground whitespace-nowrap ml-2">
                    {alert.timestamp ? new Date(alert.timestamp).toLocaleTimeString() : ""}
                  </span>
                </div>
                <p className="text-sm text-muted-foreground">{alert.message}</p>
              </div>

              {!alert.read && (
                <div className="w-2 h-2 bg-primary rounded-full flex-shrink-0 mt-2 animate-pulse" />
              )}
            </div>
          </div>
        ))}
      </div>

      {alerts.length === 0 && (
        <div className="text-center py-8">
          <CheckCircle className="w-12 h-12 text-primary mx-auto mb-3 opacity-50" />
          <p className="text-muted-foreground">No alerts at this time</p>
          <p className="text-sm text-muted-foreground mt-1">All systems operating normally</p>
        </div>
      )}
    </Card>
  );
}