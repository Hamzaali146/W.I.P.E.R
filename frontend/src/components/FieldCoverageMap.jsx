import { Card } from "./ui/card";
import TruckMap from "./ui/TruckMap";

export function FieldCoverageMap() {
  const currentProgress = 68;

  return (
    <Card className="p-4 sm:p-6 surface-card">
      <div className="mb-4">
        <h2 className="section-title">Field Coverage</h2>
        <p className="section-subtitle">Live tractor position and route performance</p>
      </div>

      <div className="grid grid-cols-3 gap-2 sm:gap-3 sm:mt-3 stagger-list">
        <div className="text-center p-2 sm:p-3 metric-tile-light chip-cyan">
          <p className="text-xs text-muted-foreground mb-1">Coverage</p>
          <p className="text-sm sm:text-base text-primary font-semibold">{currentProgress}%</p>
        </div>
        <div className="text-center p-2 sm:p-3 metric-tile-light chip-lime">
          <p className="text-xs text-muted-foreground mb-1">Distance</p>
          <p className="text-sm sm:text-base text-primary font-semibold">2.4 mi</p>
        </div>
        <div className="text-center p-2 sm:p-3 metric-tile-light chip-orange">
          <p className="text-xs text-muted-foreground mb-1">Weeds</p>
          <p className="text-sm sm:text-base text-primary font-semibold">847</p>
        </div>
      </div>

      <div className="mt-4">
        <div className="flex items-center justify-between mb-2">
          <p className="text-xs text-muted-foreground">Mission Progress</p>
          <p className="text-xs text-primary">{currentProgress}% complete</p>
        </div>
        <div className="progress-shell">
          <div className="progress-bar" style={{ width: `${currentProgress}%` }} />
        </div>
      </div>

      <div className="mt-4">
        <TruckMap />
      </div>
    </Card>
  );
}
