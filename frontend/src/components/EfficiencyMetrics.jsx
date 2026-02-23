import { useEffect, useState } from "react";
import { Card } from "./ui/card";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const dummyHourlyData = [
  { time: "6:00", weedsPerHour: 40, efficiency: 96 },
  { time: "7:00", weedsPerHour: 85, efficiency: 97 },
  { time: "8:00", weedsPerHour: 90, efficiency: 98 },
  { time: "9:00", weedsPerHour: 35, efficiency: 98 },
  { time: "10:00", weedsPerHour: 15, efficiency: 97 },
];

export function EfficiencyMetrics({ data }) {
  const [hourlyData, setHourlyData] = useState(data && data.length ? data : dummyHourlyData);

  useEffect(() => {
    if (Array.isArray(data) && data.length) {
      setHourlyData(data);
    }
  }, [data]);


  const loadHourlyData = async () => {
    // const res = await fetch("/your-api");
    // const json = await res.json();
    // setHourlyData(json.data);

    setHourlyData(dummyHourlyData);
  };

  return (
    <div className="space-y-6">
      <Card className="p-6 bg-gradient-to-br from-white to-emerald-50/30 border-2 border-[#2a7d2f]/30 shadow-lg">
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-[#0a3d2c]">Hourly Performance</h2>

          <button
            onClick={loadHourlyData}
            className="text-sm text-[#2a7d2f] hover:text-[#0a3d2c] transition-colors px-3 py-1 rounded-lg hover:bg-[#2a7d2f]/10"
          >
            Reload
          </button>
        </div>

        <ResponsiveContainer width="100%" height={250}>
          <LineChart data={hourlyData}>
            <CartesianGrid strokeDasharray="3 3" stroke="#2a7d2f" opacity={0.2} />
            <XAxis dataKey="time" stroke="#2a5c43" />
            <YAxis stroke="#2a5c43" />
            <Tooltip
              contentStyle={{
                backgroundColor: "white",
                border: "2px solid #2a7d2f",
                borderRadius: "0.75rem",
                padding: "12px",
              }}
            />

            <Line
              type="monotone"
              dataKey="weedsPerHour"
              stroke="#2a7d2f"
              strokeWidth={3}
              name="Weeds/Hour"
              dot={{ fill: "#2a7d2f", r: 4 }}
              activeDot={{ r: 6 }}
            />
          </LineChart>
        </ResponsiveContainer>
      </Card>
    </div>
  );
}