import { useEffect, useState } from "react";
import { Battery, Wifi, Thermometer, Zap, Camera } from "lucide-react";

import { Card } from "./ui/card";
import { Badge } from "./ui/badge";

export function LiveDeviceStatus({ data }) {
  const defaultData = {
    weedCount: 119,
    areaCovered: "450 sq feet",
    battery: "87%",
    connection: "Strong",
    laserTemp: "42 C",
    cameraStatus: "Active",
    isLive: true,
  };

  const hasBackendData = Boolean(data);
  const device = data || defaultData;
  const [weedCount, setWeedCount] = useState(device.weedCount || 0);

  useEffect(() => {
    setWeedCount(device.weedCount || 0);
  }, [device.weedCount]);

  useEffect(() => {
    if (hasBackendData) {
      return undefined;
    }

    const interval = setInterval(() => {
      setWeedCount((prev) => prev + Math.floor(Math.random() * 2));
    }, 1500);

    return () => clearInterval(interval);
  }, [hasBackendData]);

  return (
    <Card className="p-6 surface-card">
      <div className="flex items-start justify-between mb-6">
        <div>
          <div className="flex items-center gap-2 mb-1">
            <h2 className="section-title">Device Status</h2>

            {device.isLive && (
              <Badge className="status-pill">
                <span className="w-2 h-2 bg-emerald-500 rounded-full mr-1 animate-pulse"></span>
                Live
              </Badge>
            )}
          </div>
          <p className="text-sm text-muted-foreground">Tractor-mounted laser weeding system</p>
        </div>
      </div>

      <div className="mb-6 p-6 elevated-card">
        <div className="text-center">
          <p className="text-sm text-emerald-100 mb-2">Total Weeds Eliminated Today</p>

          <div className="flex items-center justify-center gap-3">
            <Zap className="w-10 h-10 text-emerald-200 float-subtle" />
            <h1 className="text-white text-5xl tracking-tight">{weedCount.toLocaleString()}</h1>
          </div>

          <div className="mt-4 text-sm text-emerald-100">{device.areaCovered}</div>
        </div>
      </div>

      <div className="grid grid-cols-2 gap-3 stagger-list">
        <div className="p-4 metric-tile-light chip-cyan">
          <div className="flex items-center gap-2 mb-1">
            <Battery className="w-4 h-4 text-primary" />
            <span className="text-sm text-foreground">Battery</span>
          </div>
          <p className="text-primary">{device.battery}</p>
        </div>

        <div className="p-4 metric-tile-light chip-lime">
          <div className="flex items-center gap-2 mb-1">
            <Wifi className="w-4 h-4 text-primary" />
            <span className="text-sm text-foreground">Connection</span>
          </div>
          <p className="text-primary">{device.connection}</p>
        </div>

        <div className="p-4 metric-tile-light chip-orange">
          <div className="flex items-center gap-2 mb-1">
            <Thermometer className="w-4 h-4 text-orange-500" />
            <span className="text-sm text-foreground">Laser Temp</span>
          </div>
          <p className="text-foreground">{device.laserTemp}</p>
        </div>

        <div className="p-4 metric-tile-light chip-cyan">
          <div className="flex items-center gap-2 mb-1">
            <Camera className="w-4 h-4 text-blue-600" />
            <span className="text-sm text-foreground">Camera</span>
          </div>
          <p className="text-primary">{device.cameraStatus}</p>
        </div>
      </div>
    </Card>
  );
}
