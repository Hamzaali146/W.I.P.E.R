import { Card } from "./ui/card";
import { Sprout, Cloud, CheckCircle2, TrendingUp } from "lucide-react";

function StatCard({ title, value, icon, trend, trendUp }) {
  return (
    <Card className="p-6 bg-gradient-to-br from-white to-emerald-50/30 border-2 border-[#2a7d2f]/30 shadow-lg hover:shadow-xl transition-shadow">
      <div className="flex items-start justify-between">
        <div className="flex-1">
          <p className="text-[#2a5c43]">{title}</p>
          <h3 className="mt-2 text-[#0a3d2c]">{value}</h3>

          {trend ? (
            <div className="flex items-center gap-1 mt-2">
              <TrendingUp
                className={`w-4 h-4 ${
                  trendUp ? "text-[#2a7d2f]" : "text-red-600 rotate-180"
                }`}
              />
              <span
                className={`text-sm ${
                  trendUp ? "text-[#2a7d2f]" : "text-red-600"
                }`}
              >
                {trend}
              </span>
            </div>
          ) : null}
        </div>

        <div className="p-3 bg-gradient-to-br from-[#2a7d2f] to-[#0a3d2c] rounded-xl shadow-md">
          {icon}
        </div>
      </div>
    </Card>
  );
}

export function DashboardStats() {
  const stats = [
    {
      title: "Active Fields",
      value: "12",
      icon: <Sprout className="w-6 h-6 text-white" />,
      trend: "2 new this month",
      trendUp: true,
    },
    {
      title: "Weather Status",
      value: "Sunny 28°C",
      icon: <Cloud className="w-6 h-6 text-white" />,
    },
    {
      title: "Tasks Completed",
      value: "24/30",
      icon: <CheckCircle2 className="w-6 h-6 text-white" />,
      trend: "80% completion",
      trendUp: true,
    },
    {
      title: "Expected Yield",
      value: "4,500 kg",
      icon: <TrendingUp className="w-6 h-6 text-white" />,
      trend: "+12% vs last year",
      trendUp: true,
    },
  ];

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      {stats.map((s, idx) => (
        <StatCard
          key={idx}
          title={s.title}
          value={s.value}
          icon={s.icon}
          trend={s.trend}
          trendUp={s.trendUp}
        />
      ))}
    </div>
  );
}