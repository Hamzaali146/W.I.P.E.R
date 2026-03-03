import { useEffect, useMemo, useState } from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Legend,
} from "recharts";

import { Card } from "./ui/card";

const dummyWeeklyTrends = [
  { week: "Week 1", efficiency: 95.2, weeds: 250 },
  { week: "Week 2", efficiency: 96.8, weeds: 230 },
  { week: "Week 3", efficiency: 97.5, weeds: 680 },
  { week: "Week 4", efficiency: 98.2, weeds: 892 },
];

export function PerformanceComparison({ data }) {
  const [weeklyTrends, setWeeklyTrends] = useState(
    Array.isArray(data) && data.length ? data : dummyWeeklyTrends
  );

  useEffect(() => {
    if (Array.isArray(data) && data.length) {
      setWeeklyTrends(data);
    }
  }, [data]);

  const calculateChange = (current, previous) => {
    if (!previous || previous === 0) {
      return { value: "0.0", isPositive: true, isNeutral: true };
    }

    const change = ((current - previous) / previous) * 100;
    return {
      value: Math.abs(change).toFixed(1),
      isPositive: change > 0,
      isNeutral: Math.abs(change) < 0.5,
    };
  };

  const { currentWeek, previousWeek, weedsChange } = useMemo(() => {
    const current = weeklyTrends[weeklyTrends.length - 1] || {
      weeds: 0,
      efficiency: 0,
      week: "-",
    };
    const previous = weeklyTrends[weeklyTrends.length - 2] || {
      weeds: 0,
      efficiency: 0,
      week: "-",
    };

    return {
      currentWeek: current,
      previousWeek: previous,
      weedsChange: calculateChange(current.weeds, previous.weeds),
    };
  }, [weeklyTrends]);

  return (
    <Card className="p-6 surface-card">
      <div className="flex items-center justify-between mb-6">
        <h2 className="section-title">Weekly Performance</h2>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
        <div className="p-4 metric-tile-light chip-cyan">
          <div className="flex items-center justify-between mb-2">
            <p className="text-sm text-muted-foreground">Weeds Eliminated</p>

            <div
              className={`flex items-center gap-1 text-sm ${
                weedsChange.isNeutral
                  ? "text-muted-foreground"
                  : weedsChange.isPositive
                    ? "text-primary"
                    : "text-orange-500"
              }`}
            >
              <span>
                {weedsChange.isNeutral
                  ? "~ 0.0%"
                  : `${weedsChange.isPositive ? "+" : "-"}${weedsChange.value}%`}
              </span>
            </div>
          </div>

          <p className="text-primary text-2xl">{Number(currentWeek.weeds || 0).toLocaleString()}</p>
          <p className="text-xs text-muted-foreground mt-1">Compared to {previousWeek.week}</p>
        </div>
      </div>

      <ResponsiveContainer width="100%" height={220}>
        <BarChart data={weeklyTrends}>
          <CartesianGrid strokeDasharray="3 3" stroke="#3f5e5438" />
          <XAxis dataKey="week" stroke="#4e655c" />
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
          <Legend />
          <Bar yAxisId="left" dataKey="weeds" fill="#0f766e" name="Weeds Eliminated" radius={[8, 8, 0, 0]} />
          <Bar yAxisId="right" dataKey="efficiency" fill="#f97316" name="Efficiency %" radius={[8, 8, 0, 0]} />
        </BarChart>
      </ResponsiveContainer>
    </Card>
  );
}
