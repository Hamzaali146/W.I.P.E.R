import { useEffect, useMemo, useState } from "react";
import { Card } from "./ui/card";
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

const dummyWeeklyTrends = [
  { week: "Week 1", efficiency: 95.2, weeds: 250 },
  { week: "Week 2", efficiency: 96.8, weeds: 230 },
  { week: "Week 3", efficiency: 97.5, weeds: 680 },
  { week: "Week 4", efficiency: 98.2, weeds: 892 },
];

export function PerformanceComparison({ data }) {
  // If parent passes data later, it will use it, otherwise dummy data
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
      week: "—",
    };
    const previous = weeklyTrends[weeklyTrends.length - 2] || {
      weeds: 0,
      efficiency: 0,
      week: "—",
    };

    return {
      currentWeek: current,
      previousWeek: previous,
      weedsChange: calculateChange(current.weeds, previous.weeds),
    };
  }, [weeklyTrends]);

  return (
    <Card className="p-6 bg-gradient-to-br from-white to-emerald-50/30 border-2 border-[#2a7d2f]/30 shadow-lg">
      <div className="flex items-center justify-between mb-6">
        <h2 className="text-[#0a3d2c]">Weekly Performance</h2>
      </div>

      {/* Summary */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
        <div className="p-4 bg-white rounded-xl border-2 border-[#2a7d2f]/20 shadow-sm">
          <div className="flex items-center justify-between mb-2">
            <p className="text-sm text-[#2a5c43]">Weeds Eliminated</p>

            <div
              className={`flex items-center gap-1 text-sm ${
                weedsChange.isNeutral
                  ? "text-[#2a5c43]"
                  : weedsChange.isPositive
                  ? "text-[#2a7d2f]"
                  : "text-orange-500"
              }`}
            >
              <span>
                {weedsChange.isNeutral
                  ? "≈ 0.0%"
                  : `${weedsChange.isPositive ? "+" : "-"}${weedsChange.value}%`}
              </span>
            </div>
          </div>

          <p className="text-[#2a7d2f] text-2xl">
            {Number(currentWeek.weeds || 0).toLocaleString()}
          </p>

          <p className="text-xs text-[#2a5c43] mt-1">
            Compared to {previousWeek.week}
          </p>
        </div>
      </div>

      {/* Chart */}
      <ResponsiveContainer width="100%" height={200}>
        <BarChart data={weeklyTrends}>
          <CartesianGrid strokeDasharray="3 3" stroke="#2a7d2f" opacity={0.2} />
          <XAxis dataKey="week" stroke="#2a5c43" />
          <YAxis yAxisId="left" stroke="#2a5c43" />
          <YAxis yAxisId="right" orientation="right" stroke="#2a5c43" />
          <Tooltip
            contentStyle={{
              backgroundColor: "white",
              border: "2px solid #2a7d2f",
              borderRadius: "0.75rem",
              padding: "12px",
            }}
          />
          <Legend />
          <Bar
            yAxisId="left"
            dataKey="weeds"
            fill="#3b82f6"
            name="Weeds Eliminated"
            radius={[8, 8, 0, 0]}
          />
        </BarChart>
      </ResponsiveContainer>
    </Card>
  );
}