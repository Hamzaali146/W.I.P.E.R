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

const buildDummyHourly = () => {
  const now = new Date();
  const out = [];
  for (let offset = 5; offset >= 0; offset--) {
    const h = now.getHours() - offset;
    if (h < 0) continue;
    out.push({
      time: `${String(h).padStart(2, "0")}:00`,
      weedsPerHour: 0,
      efficiency: 0,
    });
  }
  return out;
};

export function EfficiencyMetrics({ data }) {
  const [hourlyData, setHourlyData] = useState(
    data && data.length ? data : buildDummyHourly()
  );

  useEffect(() => {
    if (Array.isArray(data) && data.length) {
      setHourlyData(data);
    }
  }, [data]);

  const reload = () => {
    setHourlyData(buildDummyHourly());
  };

  return (
    <div className="space-y-6">
      <Card className="p-6 surface-card">
        <div className="flex items-center justify-between mb-6">
          <h2 className="section-title">Per-Hour Performance</h2>

          <button
            onClick={reload}
            className="text-sm px-3 py-1 rounded-lg transition-colors chip-cyan text-primary"
          >
            Reload
          </button>
        </div>

        <ResponsiveContainer width="100%" height={250}>
          <LineChart data={hourlyData}>
            <CartesianGrid strokeDasharray="3 3" stroke="hsl(150, 30%, 85%)" />
            <XAxis dataKey="time" stroke="hsl(148, 13%, 35%)" />
            <YAxis yAxisId="left" stroke="hsl(148, 13%, 35%)" allowDecimals={false} />
            <YAxis yAxisId="right" orientation="right" stroke="hsl(148, 13%, 35%)" domain={[0, 100]} />
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
              stroke="hsl(174, 78%, 26%)"
              strokeWidth={3}
              name="Weeds Eliminated / Hour"
              dot={{ fill: "hsl(25, 95%, 53%)", r: 4 }}
              activeDot={{ r: 6, fill: "hsl(174, 78%, 26%)" }}
            />
            <Line
              type="monotone"
              yAxisId="right"
              dataKey="efficiency"
              stroke="hsl(25, 95%, 53%)"
              strokeWidth={2.5}
              strokeDasharray="6 4"
              name="Efficiency %"
              dot={{ fill: "hsl(174, 78%, 26%)", r: 3.5 }}
              activeDot={{ r: 5, fill: "hsl(25, 95%, 53%)" }}
            />
          </LineChart>
        </ResponsiveContainer>
      </Card>
    </div>
  );
}
