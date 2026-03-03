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
      <Card className="p-6 surface-card">
        <div className="flex items-center justify-between mb-6">
          <h2 className="section-title">Hourly Performance</h2>

          <button
            onClick={loadHourlyData}
            className="text-sm px-3 py-1 rounded-lg transition-colors chip-cyan"
            style={{ color: "#0f766e" }}
          >
            Reload
          </button>
        </div>

        <ResponsiveContainer width="100%" height={250}>
          <LineChart data={hourlyData}>
            <CartesianGrid strokeDasharray="3 3" stroke="#3f5e5438" />
            <XAxis dataKey="time" stroke="#4e655c" />
            <YAxis yAxisId="left" stroke="#4e655c" />
            <YAxis yAxisId="right" orientation="right" stroke="#4e655c" domain={[90, 100]} />
            <Tooltip
              contentStyle={{
                backgroundColor: "rgba(255, 255, 255, 0.94)",
                border: "1px solid rgba(19, 35, 26, 0.14)",
                borderRadius: "0.95rem",
                padding: "12px",
              }}
            />

            <Line
              type="monotone"
              yAxisId="left"
              dataKey="weedsPerHour"
              stroke="#0f766e"
              strokeWidth={3}
              name="Weeds/Hour"
              dot={{ fill: "#f97316", r: 4 }}
              activeDot={{ r: 6, fill: "#0f766e" }}
            />
            <Line
              type="monotone"
              yAxisId="right"
              dataKey="efficiency"
              stroke="#f97316"
              strokeWidth={2.5}
              strokeDasharray="6 4"
              name="Efficiency %"
              dot={{ fill: "#22d3ee", r: 3.5 }}
              activeDot={{ r: 5, fill: "#f97316" }}
            />
          </LineChart>
        </ResponsiveContainer>
      </Card>
    </div>
  );
}
