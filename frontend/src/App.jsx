import { useEffect, useMemo, useState } from "react";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "./components/ui/tabs";

import { LiveCameraFeed } from "./components/LiveCameraFeed";
import { LiveDeviceStatus } from "./components/LiveDeviceStatus";
import { SessionHistoryEnhanced } from "./components/SessionHistoryEnhanced";
import { EfficiencyMetrics } from "./components/EfficiencyMetrics";
import { FieldsOverview } from "./components/FieldsOverview";
import { FieldCoverageMap } from "./components/FieldCoverageMap";
import { AlertsPanel } from "./components/AlertsPanel";
import { PerformanceComparison } from "./components/PerformanceComparison";
import { QuickActions } from "./components/QuickActions";

import { Menu, Bell, Target, Sparkles } from "lucide-react";
import { Button } from "./components/ui/button";
import { Badge } from "./components/ui/badge";

function buildWebSocketUrl(apiBaseUrl) {
  return `${apiBaseUrl.replace(/^http/i, "ws")}/ws/detections`;
}

export default function App() {
  const [systemStatus, setSystemStatus] = useState(null);
  const [summaryStats, setSummaryStats] = useState(null);
  const [latestDetections, setLatestDetections] = useState([]);
  const [alerts, setAlerts] = useState([]);
  const unreadCount = useMemo(
    () => alerts.filter((a) => !a.read).length,
    [alerts],
  );
  const [latestInferenceMs, setLatestInferenceMs] = useState(null);
  const [wsStatus, setWsStatus] = useState("connecting");

  const apiBaseUrl = useMemo(() => {
    const configuredUrl =
      import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";
    return configuredUrl.replace(/\/+$/, "");
  }, []);

  useEffect(() => {
    let isMounted = true;

    const fetchSystemStatus = async () => {
      try {
        const response = await fetch(`${apiBaseUrl}/api/system/status`);
        if (!response.ok) {
          return;
        }

        const data = await response.json();
        if (isMounted) {
          setSystemStatus(data);
        }
      } catch (error) {
        // Keep previous state on transient network failures
      }
    };

    fetchSystemStatus();
    const intervalId = setInterval(fetchSystemStatus, 2000);

    return () => {
      isMounted = false;
      clearInterval(intervalId);
    };
  }, [apiBaseUrl]);

  // For Alerts
  useEffect(() => {
    let mounted = true;

    const fetchAlerts = async () => {
      try {
        const res = await fetch(`${apiBaseUrl}/api/alerts?limit=7`);
        if (!res.ok) return;
        const data = await res.json();
        if (mounted) setAlerts(Array.isArray(data.alerts) ? data.alerts : []);
      } catch {
        // ignore
      }
    };

    fetchAlerts();
    const t = setInterval(fetchAlerts, 3000);
    return () => {
      mounted = false;
      clearInterval(t);
    };
  }, [apiBaseUrl]);

  useEffect(() => {
    let isMounted = true;

    const fetchSummaryStats = async () => {
      try {
        const response = await fetch(`${apiBaseUrl}/api/stats/summary`);
        if (!response.ok) {
          return;
        }

        const data = await response.json();
        if (isMounted) {
          setSummaryStats(data);
        }
      } catch (error) {
        // Keep previous state on transient network failures
      }
    };

    fetchSummaryStats();
    const intervalId = setInterval(fetchSummaryStats, 3000);

    return () => {
      isMounted = false;
      clearInterval(intervalId);
    };
  }, [apiBaseUrl]);

  useEffect(() => {
    let ws = null;
    let reconnectTimer = null;
    let isCleaningUp = false;

    const connect = () => {
      setWsStatus("connecting");
      ws = new WebSocket(buildWebSocketUrl(apiBaseUrl));

      ws.onopen = () => {
        if (!isCleaningUp) {
          setWsStatus("connected");
        }
      };

      ws.onmessage = (event) => {
        try {
          const payload = JSON.parse(event.data);
          if (payload.type === "ping") {
            return;
          }

          if (payload.type === "detection") {
            setLatestDetections(
              Array.isArray(payload.detections) ? payload.detections : [],
            );
            if (typeof payload.inference_time_ms === "number") {
              setLatestInferenceMs(payload.inference_time_ms);
            }
          }
        } catch (error) {
          // Ignore malformed payloads and keep stream alive
        }
      };

      ws.onerror = () => {
        if (!isCleaningUp) {
          setWsStatus("error");
        }
      };

      ws.onclose = () => {
        if (isCleaningUp) {
          return;
        }

        setWsStatus("disconnected");
        reconnectTimer = setTimeout(connect, 2000);
      };
    };

    connect();

    return () => {
      isCleaningUp = true;

      if (reconnectTimer) {
        clearTimeout(reconnectTimer);
      }

      if (ws && ws.readyState === WebSocket.OPEN) {
        ws.close();
      }
    };
  }, [apiBaseUrl]);

  const streamUrl = `${apiBaseUrl}/api/video/stream`;

  const cameraStats = useMemo(() => {
    const weedsPerFrame =
      typeof summaryStats?.average_weeds_per_frame === "number"
        ? summaryStats.average_weeds_per_frame.toFixed(2)
        : "N/A";

    return {
      detectionRate: `${weedsPerFrame} weeds/frame`,
      accuracy: "N/A",
      falsePositives: "N/A",
      fps: latestInferenceMs
        ? Math.max(1, Math.round(1000 / latestInferenceMs))
        : 0,
    };
  }, [summaryStats, latestInferenceMs]);

  const modelInfo = useMemo(() => {
    const cameraActive = systemStatus?.vision_active ? "active" : "inactive";
    const lastDetection = systemStatus?.last_detection_time
      ? new Date(systemStatus.last_detection_time).toLocaleTimeString()
      : "none";

    return `ROS WS: ${wsStatus} | Camera: ${cameraActive} | Last detection: ${lastDetection}`;
  }, [systemStatus, wsStatus]);

  const liveDeviceData = useMemo(
    () => ({
      weedCount: summaryStats?.total_weeds_detected || 0,
      areaCovered: "N/A",
      battery: "N/A",
      connection: wsStatus,
      laserTemp: "N/A",
      GPS:"N/A",
      cameraStatus:
        systemStatus?.camera_active || systemStatus?.vision_active
          ? "Active"
          : "Inactive",
      isLive: wsStatus === "connected",
    }),
    [summaryStats, systemStatus, wsStatus],
  );

  const markAlertRead = async (id) => {
    setAlerts((prev) =>
      prev.map((a) => (a.id === id ? { ...a, read: true } : a)),
    );
    try {
      await fetch(`${apiBaseUrl}/api/alerts/${id}/read`, { method: "POST" });
    } catch {
    }
  };

  const markAllAlertsRead = async () => {
    setAlerts((prev) => prev.map((a) => ({ ...a, read: true })));
    try {
      await fetch(`${apiBaseUrl}/api/alerts/read-all`, { method: "POST" });
    } catch {}
  };

  return (
    <div className="min-h-screen app-shell">
      <header className="sticky top-0 z-10 app-header app-enter">
        <div className="header-orb header-orb--one" />
        <div className="header-orb header-orb--two" />
        <div className="container mx-auto px-4 py-5 space-y-3">
          <div className="flex flex-wrap items-center justify-between gap-3">
            <div className="flex items-center gap-3">
              <Button
                variant="ghost"
                size="icon"
                className="lg:hidden text-white hover:bg-white/20 rounded-xl"
              >
                <Menu className="w-5 h-5" />
              </Button>

              <div className="brand-mark">
                <Target className="w-6 h-6 text-emerald-200" />
              </div>

              <div>
                <h1 className="app-title">W.I.P.E.R Control Hub</h1>
                <p className="app-subtitle">
                  Weed Identification, Prediction and Eradication Robot
                </p>
              </div>
            </div>

            <div className="flex items-center gap-2">
              <Badge
                className={`header-chip hidden sm:flex ${
                  wsStatus === "connected"
                    ? "header-chip--cool"
                    : "header-chip--warm"
                }`}
              >
                <span
                  className={`w-2 h-2 rounded-full animate-pulse ${
                    wsStatus === "connected"
                      ? "bg-emerald-300"
                      : "bg-orange-300"
                  }`}
                />
                {wsStatus === "connected" ? "Live Link" : "Reconnecting"}
              </Badge>

              <div className="relative w-10 h-10 flex items-center justify-center rounded-xl text-white hover:bg-white/20">
                <Bell className="w-5 h-5" />
                {unreadCount > 0 && (
                  <span className="absolute -top-1 -right-1 bg-red-500 text-white rounded-full w-5 h-5 text-xs flex items-center justify-center">
                    {unreadCount}
                  </span>
                )}
              </div>
            </div>
          </div>

          <div className="flex flex-wrap items-center gap-2">
            <span className="header-chip header-chip--cool">
              <Sparkles className="w-3 h-3" />
              Autonomous vision online
            </span>
            <span className="header-chip header-chip--warm hidden sm:inline-flex">
              Visual tracking engaged
            </span>
            <span className="header-meta">{modelInfo}</span>
          </div>
        </div>
      </header>

      <main className="container mx-auto px-2 sm:px-4 py-4 sm:py-8">
        <Tabs
          defaultValue="dashboard"
          className="space-y-4 sm:space-y-6 app-enter"
        >
          <TabsList className="modern-tabs-list grid w-full max-w-3xl grid-cols-5 h-10 sm:h-12 text-xs sm:text-sm">
            <TabsTrigger value="dashboard" className="modern-tab-trigger">
              Dashboard
            </TabsTrigger>
            <TabsTrigger value="live" className="modern-tab-trigger">
              Live
            </TabsTrigger>
            <TabsTrigger value="analytics" className="modern-tab-trigger">
              Analytics
            </TabsTrigger>
            <TabsTrigger value="fields" className="modern-tab-trigger">
              Fields
            </TabsTrigger>
            <TabsTrigger value="history" className="modern-tab-trigger">
              History
            </TabsTrigger>
          </TabsList>

          <TabsContent value="dashboard" className="space-y-4 sm:space-y-6">
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-4 sm:gap-6 stagger-children">
              <div className="lg:col-span-2 space-y-4 sm:space-y-6">
                <QuickActions />
                <EfficiencyMetrics />
              </div>
              <div className="space-y-4 sm:space-y-6">
                <AlertsPanel
                  alerts={alerts}
                  onMarkRead={markAlertRead}
                  onMarkAllRead={markAllAlertsRead}
                />
                <FieldCoverageMap />
              </div>
            </div>
          </TabsContent>

          <TabsContent value="live" className="space-y-4 sm:space-y-6">
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-4 sm:gap-6 stagger-children">
              <div className="lg:col-span-2 space-y-4 sm:space-y-6">
                <LiveCameraFeed
                  streamUrl={streamUrl}
                  detections={latestDetections}
                  stats={cameraStats}
                  modelInfo={modelInfo}
                />
                <LiveDeviceStatus data={liveDeviceData} />
              </div>
              <div className="space-y-4 sm:space-y-6">
                <AlertsPanel
                  alerts={alerts}
                  onMarkRead={markAlertRead}
                  onMarkAllRead={markAllAlertsRead}
                />
                <FieldCoverageMap />
              </div>
            </div>
          </TabsContent>

          <TabsContent
            value="analytics"
            className="space-y-4 sm:space-y-6 stagger-children"
          >
            <EfficiencyMetrics />
            <PerformanceComparison />
          </TabsContent>

          <TabsContent value="fields" className="space-y-4 sm:space-y-6">
            <FieldsOverview />
          </TabsContent>

          <TabsContent value="history" className="space-y-4 sm:space-y-6">
            <SessionHistoryEnhanced />
          </TabsContent>
        </Tabs>
      </main>
    </div>
  );
}
