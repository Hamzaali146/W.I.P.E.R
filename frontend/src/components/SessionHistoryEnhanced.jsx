import { useMemo, useState } from "react";
import { Card } from "./ui/card";
import { Badge } from "./ui/badge";
import { Button } from "./ui/button";
import { Input } from "./ui/input";
import {
  Calendar,
  Clock,
  Zap,
  MapPin,
  Download,
  Search,
  Filter,
} from "lucide-react";

const dummySessions = [
  {
    id: 1,
    date: "Dec 12, 2025",
    time: "06:30 AM",
    duration: "2h 15m",
    field: "North Field A",
    weedsEliminated: 1247,
    areaCovered: 12.4,
    efficiency: 98.2,
  },
  {
    id: 2,
    date: "Dec 11, 2025",
    time: "07:00 AM",
    duration: "3h 45m",
    field: "South Field B",
    weedsEliminated: 2156,
    areaCovered: 18.3,
    efficiency: 97.8,
  },
  {
    id: 3,
    date: "Dec 10, 2025",
    time: "06:45 AM",
    duration: "2h 30m",
    field: "East Field C",
    weedsEliminated: 1893,
    areaCovered: 15.2,
    efficiency: 96.5,
  },
  {
    id: 4,
    date: "Dec 9, 2025",
    time: "07:15 AM",
    duration: "1h 50m",
    field: "North Field A",
    weedsEliminated: 987,
    areaCovered: 10.1,
    efficiency: 99.1,
  },
  {
    id: 5,
    date: "Dec 8, 2025",
    time: "06:20 AM",
    duration: "2h 05m",
    field: "West Field D",
    weedsEliminated: 1542,
    areaCovered: 13.8,
    efficiency: 97.4,
  },
  {
    id: 6,
    date: "Dec 7, 2025",
    time: "07:30 AM",
    duration: "3h 10m",
    field: "South Field B",
    weedsEliminated: 1876,
    areaCovered: 16.7,
    efficiency: 98.6,
  },
];

export function SessionHistoryEnhanced({
  data, 
  onFilterClick,
}) {
  const sessions = Array.isArray(data) && data.length ? data : dummySessions;

  const [searchTerm, setSearchTerm] = useState("");

  const filteredSessions = useMemo(() => {
    const q = searchTerm.trim().toLowerCase();
    if (!q) return sessions;

    return sessions.filter((s) => {
      const field = (s.field || "").toLowerCase();
      const date = (s.date || "").toLowerCase();
      return field.includes(q) || date.includes(q);
    });
  }, [searchTerm, sessions]);

  const handleExport = () => {
    const headers = [
      "Date",
      "Time",
      "Duration",
      "Field",
      "Weeds Eliminated",
      "Area Covered (acres)",
      "Efficiency (%)",
    ];

    const rows = filteredSessions.map((s) => [
      s.date,
      s.time,
      s.duration,
      s.field,
      s.weedsEliminated,
      s.areaCovered,
      s.efficiency,
    ]);

    const csvContent = [headers.join(","), ...rows.map((r) => r.join(","))].join(
      "\n"
    );

    const blob = new Blob([csvContent], { type: "text/csv" });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `weedbot-sessions-${new Date().toISOString().split("T")[0]}.csv`;
    a.click();
    window.URL.revokeObjectURL(url);
  };

  const totalWeeds = useMemo(
    () =>
      filteredSessions.reduce(
        (sum, s) => sum + (Number(s.weedsEliminated) || 0),
        0
      ),
    [filteredSessions]
  );

  const avgEfficiency = useMemo(() => {
    if (!filteredSessions.length) return 0;
    const sum = filteredSessions.reduce(
      (acc, s) => acc + (Number(s.efficiency) || 0),
      0
    );
    return sum / filteredSessions.length;
  }, [filteredSessions]);

  return (
    <Card className="p-6 bg-gradient-to-br from-white to-emerald-50/30 border-2 border-[#2a7d2f]/30 shadow-lg">
      <div className="flex items-center justify-between mb-6">
        <h2 className="text-[#0a3d2c]">Session History</h2>

        <Button
          onClick={handleExport}
          size="sm"
          className="bg-gradient-to-r from-[#2a7d2f] to-[#0a3d2c] hover:from-[#0a3d2c] hover:to-[#2a5c43] text-white shadow-md"
        >
          <Download className="w-4 h-4 mr-2" />
          Export CSV
        </Button>
      </div>

      {/* Search + Filter */}
      <div className="mb-6 flex gap-3">
        <div className="relative flex-1">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-[#2a5c43]" />
          <Input
            type="text"
            placeholder="Search by field or date..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="pl-10 bg-white border-[#2a7d2f]/30 focus:border-[#2a7d2f]"
          />
        </div>

        <Button
          variant="outline"
          size="icon"
          onClick={onFilterClick}
          className="border-[#2a7d2f]/30 text-[#2a5c43] hover:bg-[#2a7d2f]/10"
          title="Filter (connect later)"
        >
          <Filter className="w-4 h-4" />
        </Button>
      </div>

      {/* List */}
      <div className="space-y-3 max-h-96 overflow-y-auto">
        {filteredSessions.map((session) => (
          <div
            key={session.id}
            className="p-4 border-2 border-[#2a7d2f]/20 rounded-xl hover:border-[#2a7d2f] hover:bg-emerald-50/50 transition-all hover:shadow-md bg-white"
          >
            <div className="flex items-start justify-between mb-3">
              <div className="flex items-center gap-2">
                <Calendar className="w-4 h-4 text-[#2a5c43]" />
                <span className="text-sm text-[#0a3d2c]">{session.date}</span>

                <span className="text-[#2a5c43]">•</span>

                <Clock className="w-4 h-4 text-[#2a5c43]" />
                <span className="text-sm text-[#2a5c43]">{session.time}</span>
              </div>

              <Badge
                variant="outline"
                className="bg-[#2a7d2f]/10 text-[#0a3d2c] border-[#2a7d2f]"
              >
                {session.duration}
              </Badge>
            </div>

            <div className="flex items-center gap-2 mb-3">
              <MapPin className="w-4 h-4 text-[#2a5c43]" />
              <span className="text-[#0a3d2c]">{session.field}</span>
            </div>

            <div className="grid grid-cols-3 gap-3 text-sm">
              <div>
                <p className="text-[#2a5c43] mb-1">Weeds Eliminated</p>
                <div className="flex items-center gap-1">
                  <Zap className="w-3 h-3 text-[#2a7d2f]" />
                  <span className="text-[#2a7d2f]">
                    {Number(session.weedsEliminated || 0).toLocaleString()}
                  </span>
                </div>
              </div>

              <div>
                <p className="text-[#2a5c43] mb-1">Area Covered</p>
                <p className="text-[#0a3d2c]">{session.areaCovered} acres</p>
              </div>

              <div>
                <p className="text-[#2a5c43] mb-1">Efficiency</p>
                <p className="text-[#2a7d2f]">{session.efficiency}%</p>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Empty State */}
      {filteredSessions.length === 0 && (
        <div className="text-center py-12">
          <Search className="w-12 h-12 text-[#2a5c43] mx-auto mb-3 opacity-50" />
          <p className="text-[#2a5c43]">No sessions found</p>
          <p className="text-sm text-[#2a5c43] mt-1">
            Try adjusting your search
          </p>
        </div>
      )}

      {/* Summary */}
      <div className="mt-6 pt-6 border-t-2 border-[#2a7d2f]/20">
        <div className="grid grid-cols-3 gap-4 text-center">
          <div className="p-3 bg-white rounded-xl border border-[#2a7d2f]/20 shadow-sm">
            <p className="text-sm text-[#2a5c43] mb-1">Total Sessions</p>
            <p className="text-[#2a7d2f]">{filteredSessions.length}</p>
          </div>

          <div className="p-3 bg-white rounded-xl border border-[#2a7d2f]/20 shadow-sm">
            <p className="text-sm text-[#2a5c43] mb-1">Total Weeds</p>
            <p className="text-[#2a7d2f]">{totalWeeds.toLocaleString()}</p>
          </div>

          <div className="p-3 bg-white rounded-xl border border-[#2a7d2f]/20 shadow-sm">
            <p className="text-sm text-[#2a5c43] mb-1">Avg Efficiency</p>
            <p className="text-[#2a7d2f]">{avgEfficiency.toFixed(1)}%</p>
          </div>
        </div>
      </div>
    </Card>
  );
}