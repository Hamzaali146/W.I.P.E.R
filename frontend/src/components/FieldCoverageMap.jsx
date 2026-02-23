import { Card } from "./ui/card";
import { useState } from "react";
import TruckMap from "./ui/TruckMap";


export function FieldCoverageMap() {
  const [startZone, setStartZone] = useState("A1");
  const [destinationZone, setDestinationZone] = useState("A3");
  const [currentProgress, setCurrentProgress] = useState(68); // 68% of route completed

  // Calculate current truck position based on progress
  // const getTruckPosition = () => {
  //   if (routePath.length < 2) return { x: 15, y: 70 };
    
  //   const totalSegments = routePath.length - 1;
  //   const progressDecimal = currentProgress / 100;
  //   const currentSegment = Math.floor(progressDecimal * totalSegments);
  //   const segmentProgress = (progressDecimal * totalSegments) - currentSegment;
    
  //   if (currentSegment >= totalSegments) {
  //     return routePath[routePath.length - 1];
  //   }
    
  //   const start = routePath[currentSegment];
  //   const end = routePath[currentSegment + 1];
    
  //   return {
  //     x: start.x + (end.x - start.x) * segmentProgress,
  //     y: start.y + (end.y - start.y) * segmentProgress,
  //   };
  // };

  // const truckPos = getTruckPosition();

  // const getCompletedPath = () => {
  //   if (routePath.length < 2) return "";
  //   const pathString = routePath
  //     .slice(0, Math.ceil((currentProgress / 100) * routePath.length))
  //     .map((point, idx) => `${idx === 0 ? 'M' : 'L'} ${point.x}% ${point.y}%`)
  //     .join(' ');
  //   return pathString;
  // };

  // const getRemainingPath = () => {
  //   if (routePath.length < 2) return "";
  //   const startIdx = Math.floor((currentProgress / 100) * routePath.length);
  //   const remaining = routePath.slice(startIdx);
  //   if (remaining.length < 2) return "";
  //   const pathString = remaining
  //     .map((point, idx) => `${idx === 0 ? 'M' : 'L'} ${point.x}% ${point.y}%`)
  //     .join(' ');
  //   return pathString;
  // };

  return (
    <Card className="p-4 sm:p-6 bg-gradient-to-br from-white to-emerald-50/30 border-2 border-[#2a7d2f]/30 shadow-lg">
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between mb-2 sm:mb-4 gap-2">
        <h2 className="text-[#0a3d2c]">Field Coverage</h2>
      </div>
      {/* Map with Route Overlay */}
      {/* <div className="relative rounded-xl overflow-hidden shadow-md border-2 border-gray-300"> */}
        {/* Start Marker */}
        {/* {routePath.length >= 2 && (
          <div 
            className="absolute"
            style={{ 
              left: `${routePath[0].x}%`, 
              top: `${routePath[0].y}%`,
              transform: "translate(-50%, -50%)"
            }}
          >
            <div className="relative">
              <div className="w-12 h-12 bg-[#0a3d2c] rounded-full border-4 border-white shadow-lg flex items-center justify-center">
                <span className="text-white text-xs font-bold">{startZone}</span>
              </div>
              <div className="absolute -bottom-6 left-1/2 transform -translate-x-1/2 whitespace-nowrap">
                <span className="text-xs bg-[#0a3d2c] text-white px-2 py-1 rounded shadow-md">Start</span>
              </div>
            </div>
          </div>
        )} */}

        {/* Destination Marker */}
        {/* {routePath.length >= 2 && (
          <div 
            className="absolute"
            style={{ 
              left: `${routePath[routePath.length - 1].x}%`, 
              top: `${routePath[routePath.length - 1].y}%`,
              transform: "translate(-50%, -50%)"
            }}
          >
            <div className="relative">
              <div className="w-12 h-12 bg-[#2a7d2f] rounded-full border-4 border-white shadow-lg flex items-center justify-center">
                <span className="text-white text-xs font-bold">{destinationZone}</span>
              </div>
              <div className="absolute -bottom-6 left-1/2 transform -translate-x-1/2 whitespace-nowrap">
                <span className="text-xs bg-[#2a7d2f] text-white px-2 py-1 rounded shadow-md">Destination</span>
              </div>
            </div>
          </div>
        )} */}

        {/* Tractor Position Marker - tractor image */}
       
      {/* </div> */}


      {/* Stats */}
      <div className="grid grid-cols-3 gap-2 sm:gap-3  sm:mt-6">
        <div className="text-center p-2 sm:p-3 bg-white rounded-xl border-2 border-[#2a7d2f]/20 shadow-sm">
          <p className="text-xs text-[#2a5c43] mb-1">Coverage</p>
          <p className="text-sm sm:text-base text-[#2a7d2f] font-semibold">{currentProgress}%</p>
        </div>
        <div className="text-center p-2 sm:p-3 bg-white rounded-xl border-2 border-[#2a7d2f]/20 shadow-sm">
          <p className="text-xs text-[#2a5c43] mb-1">Distance</p>
          <p className="text-sm sm:text-base text-[#2a7d2f] font-semibold">2.4 mi</p>
        </div>
        <div className="text-center p-2 sm:p-3 bg-white rounded-xl border-2 border-[#2a7d2f]/20 shadow-sm">
          <p className="text-xs text-[#2a5c43] mb-1">Weeds</p>
          <p className="text-sm sm:text-base text-[#2a7d2f] font-semibold">847</p>
        </div>
      </div>
      <div>
        <TruckMap/>
      </div>
    </Card>
  );
}
