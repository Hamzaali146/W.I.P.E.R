import { useState } from "react";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "./components/ui/tabs";

import { LiveDeviceStatus } from "./components/LiveDeviceStatus";
import { SessionHistoryEnhanced } from "./components/SessionHistoryEnhanced";
import { EfficiencyMetrics } from "./components/EfficiencyMetrics";
import { FieldsOverview } from "./components/FieldsOverview";
// import { InteractiveZoneMap } from "./components/InteractiveZoneMap";
import { FieldCoverageMap } from "./components/FieldCoverageMap";
import { AlertsPanel } from "./components/AlertsPanel";
import { PerformanceComparison } from "./components/PerformanceComparison";
import { QuickActions } from "./components/QuickActions";

import { Menu, Bell, Settings, Target } from "lucide-react";
import { Button } from "./components/ui/button";
import { Badge } from "./components/ui/badge";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "./components/ui/dropdown-menu";

export default function App() {
  const [notificationCount] = useState(2);

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="bg-gradient-to-r from-[#0a3d2c] via-[#2a5c43] to-[#2a7d2f] text-white border-b-4 border-[#2a7d2f] sticky top-0 z-10 shadow-xl">
        <div className="container mx-auto px-4 py-5">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-4">
              <Button
                variant="ghost"
                size="icon"
                className="lg:hidden text-white hover:bg-white/20"
              >
                <Menu className="w-5 h-5" />
              </Button>

              <div className="flex items-center gap-3">
                <div className="p-3 bg-white/15 rounded-xl backdrop-blur-md border border-white/20 shadow-lg">
                  <Target className="w-7 h-7 text-[#86efac]" />
                </div>
                <div>
                  <h1 className="text-white text-2xl tracking-tight">
                    W.I.P.E.R
                  </h1>
                  <p className="text-sm text-emerald-100">
                    Weed Identification, Prediction and Eradication Robot
                  </p>
                </div>
              </div>
            </div>

            <div className="flex items-center gap-3">
              <Badge className="bg-white/15 text-white backdrop-blur-md border border-white/20 hidden sm:flex px-4 py-2">
                <span className="w-2.5 h-2.5 bg-emerald-400 rounded-full mr-2 animate-pulse shadow-lg shadow-emerald-400/50"></span>
                Device Online
              </Badge>

              {/* Notifications */}
              <DropdownMenu>
                <DropdownMenuTrigger asChild>
                  <Button
                    variant="ghost"
                    size="icon"
                    className="text-white hover:bg-white/20 rounded-xl relative"
                  >
                    <Bell className="w-5 h-5" />
                    {notificationCount > 0 && (
                      <span className="absolute -top-1 -right-1 bg-red-500 text-white rounded-full w-5 h-5 text-xs flex items-center justify-center">
                        {notificationCount}
                      </span>
                    )}
                  </Button>
                </DropdownMenuTrigger>

                <DropdownMenuContent className="w-80">
                  <DropdownMenuLabel>
                    Notifications ({notificationCount} new)
                  </DropdownMenuLabel>
                  <DropdownMenuSeparator />

                  <DropdownMenuItem className="flex flex-col items-start py-3">
                    <span className="text-sm">Device Status Update</span>
                    <span className="text-xs text-muted-foreground">
                      Battery level at 87%, optimal performance
                    </span>
                  </DropdownMenuItem>

                  <DropdownMenuItem className="flex flex-col items-start py-3">
                    <span className="text-sm">Field Coverage Alert</span>
                    <span className="text-xs text-muted-foreground">
                      Zone A3 nearing completion
                    </span>
                  </DropdownMenuItem>

                  <DropdownMenuItem className="flex flex-col items-start py-3">
                    <span className="text-sm">Weekly Report Ready</span>
                    <span className="text-xs text-muted-foreground">
                      Performance metrics available
                    </span>
                  </DropdownMenuItem>
                </DropdownMenuContent>
              </DropdownMenu>

            </div>
          </div>
        </div>
      </header>

      {/* Main */}
      <main className="container mx-auto px-2 sm:px-4 py-4 sm:py-8">
        <Tabs defaultValue="dashboard" className="space-y-4 sm:space-y-6">
          <TabsList className="grid w-full max-w-3xl grid-cols-5 h-10 sm:h-12 bg-white/60 backdrop-blur-sm border-2 border-[#2a7d2f]/20 shadow-md text-xs sm:text-sm">
            <TabsTrigger
              value="dashboard"
              className="data-[state=active]:bg-[#2a7d2f] data-[state=active]:text-white"
            >
              Dashboard
            </TabsTrigger>
            <TabsTrigger
              value="live"
              className="data-[state=active]:bg-[#2a7d2f] data-[state=active]:text-white"
            >
              Live
            </TabsTrigger>
            <TabsTrigger
              value="analytics"
              className="data-[state=active]:bg-[#2a7d2f] data-[state=active]:text-white"
            >
              Analytics
            </TabsTrigger>
            <TabsTrigger
              value="fields"
              className="data-[state=active]:bg-[#2a7d2f] data-[state=active]:text-white"
            >
              Fields
            </TabsTrigger>
            <TabsTrigger
              value="history"
              className="data-[state=active]:bg-[#2a7d2f] data-[state=active]:text-white"
            >
              History
            </TabsTrigger>
          </TabsList>

          {/* Dashboard */}
          <TabsContent value="dashboard" className="space-y-4 sm:space-y-6">
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-4 sm:gap-6">
              <div className="lg:col-span-2 space-y-4 sm:space-y-6">
                <QuickActions />
                <EfficiencyMetrics />
              </div>
              <div className="space-y-4 sm:space-y-6">
                <AlertsPanel />
                <FieldCoverageMap />
              </div>
            </div>
          </TabsContent>

          {/* Live */}
          <TabsContent value="live" className="space-y-4 sm:space-y-6">
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-4 sm:gap-6">
              <div className="lg:col-span-2 space-y-4 sm:space-y-6">
                <LiveDeviceStatus />
              </div>
              <div className="space-y-4 sm:space-y-6">
                <AlertsPanel />
                <FieldCoverageMap />
              </div>
            </div>
          </TabsContent>

          {/* Analytics */}
          <TabsContent value="analytics" className="space-y-4 sm:space-y-6">
            <EfficiencyMetrics />
            <PerformanceComparison />
          </TabsContent>

          {/* Fields */}
          <TabsContent value="fields" className="space-y-4 sm:space-y-6">
            <FieldsOverview />
          </TabsContent>

          {/* History */}
          <TabsContent value="history" className="space-y-4 sm:space-y-6">
            <SessionHistoryEnhanced />
          </TabsContent>
        </Tabs>
      </main>
    </div>
  );
}