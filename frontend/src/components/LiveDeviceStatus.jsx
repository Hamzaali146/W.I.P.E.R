import { useEffect, useState } from "react";
import { Card } from "./ui/card";
import { Badge } from "./ui/badge";
import {
  Battery,
  Wifi,
  Thermometer,
  Zap,
  Camera,
} from "lucide-react";

export function LiveDeviceStatus({
  data, // pass backend device data 
}) {
  
  const defaultData = {
    weedCount: 119,
    areaCovered: "450 sq feet",
    battery: "87%",
    connection: "Strong",
    laserTemp: "42°C",
    cameraStatus: "Active",
    isLive: true,
  };

  const device = data || defaultData;

  // Optional simulation (remove when backend connected)
  const [weedCount, setWeedCount] = useState(device.weedCount);

  useEffect(() => {
    const interval = setInterval(() => {
      setWeedCount((prev) => prev + Math.floor(Math.random() * 2));
    }, 1500);

    return () => clearInterval(interval);
  }, []);

  return (
    <Card className="p-6 bg-gradient-to-br from-white to-emerald-50/30 border-2 border-[#2a7d2f]/30 shadow-lg">
      {/* Header */}
      <div className="flex items-start justify-between mb-6">
        <div>
          <div className="flex items-center gap-2 mb-1">
            <h2 className="text-[#0a3d2c]">Device Status</h2>

            {device.isLive && (
              <Badge className="bg-[#2a7d2f] text-white shadow-md">
                <span className="w-2 h-2 bg-white rounded-full mr-1 animate-pulse"></span>
                Live
              </Badge>
            )}
          </div>

          <p className="text-sm text-[#2a5c43]">
            Tractor-mounted laser weeding system
          </p>
        </div>
      </div>

      {/* Main Counter */}
      <div className="mb-6 p-6 bg-gradient-to-br from-[#0a3d2c] to-[#2a5c43] rounded-xl border-2 border-[#2a7d2f] shadow-xl">
        <div className="text-center">
          <p className="text-sm text-emerald-100 mb-2">
            Total Weeds Eliminated Today
          </p>

          <div className="flex items-center justify-center gap-3">
            <Zap className="w-10 h-10 text-[#86efac]" />
            <h1 className="text-white text-5xl">
              {weedCount.toLocaleString()}
            </h1>
          </div>

          <div className="mt-4 text-sm text-emerald-100">
            {device.areaCovered}
          </div>
        </div>
      </div>

      {/* Status Grid */}
      <div className="grid grid-cols-2 gap-3">
        <div className="p-4 bg-white rounded-xl border border-[#2a7d2f]/20 shadow-sm">
          <div className="flex items-center gap-2 mb-1">
            <Battery className="w-4 h-4 text-[#2a7d2f]" />
            <span className="text-sm text-[#0a3d2c]">Battery</span>
          </div>
          <p className="text-[#2a7d2f]">{device.battery}</p>
        </div>

        <div className="p-4 bg-white rounded-xl border border-[#2a7d2f]/20 shadow-sm">
          <div className="flex items-center gap-2 mb-1">
            <Wifi className="w-4 h-4 text-[#2a7d2f]" />
            <span className="text-sm text-[#0a3d2c]">Connection</span>
          </div>
          <p className="text-[#2a7d2f]">{device.connection}</p>
        </div>

        <div className="p-4 bg-white rounded-xl border border-[#2a7d2f]/20 shadow-sm">
          <div className="flex items-center gap-2 mb-1">
            <Thermometer className="w-4 h-4 text-orange-500" />
            <span className="text-sm text-[#0a3d2c]">Laser Temp</span>
          </div>
          <p className="text-[#0a3d2c]">{device.laserTemp}</p>
        </div>

        <div className="p-4 bg-white rounded-xl border border-[#2a7d2f]/20 shadow-sm">
          <div className="flex items-center gap-2 mb-1">
            <Camera className="w-4 h-4 text-blue-600" />
            <span className="text-sm text-[#0a3d2c]">Camera</span>
          </div>
          <p className="text-[#2a7d2f]">{device.cameraStatus}</p>
        </div>
      </div>
    </Card>
  );
}