// import LineChartGraph from "./LineChart";
// import Notifications from "./Notifications";
// function Dashboard(){
//     return(
//     <>
//     <div className="p-10 gap-5 bg-[#f8fcfa] flex">
//         <div className="w-[70%]" >
//     <div className="bg-gradient-to-r from-[#0a3d2c] to-[#2a5c43] text-white p-6 border border-[#2a7d2f] rounded-3xl">
//         <p>Today's Summary</p>
//         <div className="flex justify-evenly gap-4 m-4">
//             <div className="bg-[#2a7d2f] p-4 px-4 w-[25%] rounded-md flex flex-col items-center justify-center "><img src="weed.png" className="h-7 w-7" alt="weed logo" />
//             <p>Weed Eliminated</p>
//             <p>2569</p>
//             </div>
//             <div className="bg-[#2a7d2f] p-4 px-4 w-[25%] rounded-md flex flex-col items-center justify-center "><img src="Navigate.png" className="h-10 w-10" alt="area logo" />
//             <p>Area Covered</p>
//             <p>9 acres</p>
//             </div>
//             <div className="bg-[#2a7d2f] p-4 px-4 w-[25%] rounded-md flex flex-col items-center justify-center "><img src="time.png" className="h-7 w-7" alt="time logo" />
//             <p>Active Time</p>
//             <p>2h 9min</p>
//             </div>
//             <div className="bg-[#2a7d2f] p-4 px-4 w-[25%] rounded-md flex flex-col items-center justify-center "><img src="energy-efficient.png" className="h-7 w-7" alt="efficiency logo" />
//             <p>Efficiency</p>
//             <p>80%</p>
//             </div>
//         </div>
//         </div>

//         <div className="border border-[#2a7d2f] rounded-3xl my-3 p-6">
//             <p> Quick Actions</p>
//             <div className="flex gap-4 my-2">
//             <button className="flex border border-[#2a7d2f] rounded-lg p-4 gap-2 items-center w-full cursor-pointer"><img src="weed.png" className="h-7 w-7" alt="start logo" /><div><p>Start New Session</p><p className="text-sm text-left">Begin Weed Detection</p></div></button>
//             <button className="flex border border-red-700  rounded-lg p-4 gap-2 items-center w-full cursor-pointer"><img src="weed.png" className="h-7 w-7"alt="stop logo" /><div><p className="text-red-700">Emergency Stop</p><p className="text-sm text-left text-red-500">Immediate halt</p></div></button>
//             </div>
//             <div className="flex gap-4">
//             <button className="flex border border-[#2a7d2f]  rounded-lg p-4 gap-2 items-center w-full cursor-pointer"><img src="weed.png" className="h-7 w-7"alt="resume logo" /><div className="flex flex-col items-left"><p>Resume Last Session</p><p className="text-sm text-left">Zone</p></div></button>
//             <button className="flex border border-[#2a7d2f]  rounded-lg p-4 gap-2 items-center w-full cursor-pointer"><img src="weed.png" className="h-7 w-7" alt="report logo" /><div><p>Export Report</p><p className="text-sm text-left">Download data</p></div></button>
//             </div>
//         </div>

//         <div className="border border-[#2a7d2f] rounded-3xl my-3 p-6">
//             <div className="flex justify-between mb-4"><p>System Satus</p><div className="px-3 flex items-center justify-center rounded-4xl gap-2 text-white text-sm bg-[#0b470f]"><div className="bg-[#d0fae5] rounded-full h-2 w-2"></div>All System Operational</div></div>
//             <div className="flex flex-col gap-2">
//             <div className="flex justify-between border-2 border-green-700 p-4 rounded-lg">
//                     <div className="flex gap-2">
//                         <img src="weed.png" className="h-7 w-7" alt="laser operating logo" />
//                         <div><p>Laser System</p><p>Operating manually</p></div>
//                     </div>
//                         <div className="px-3 flex items-center justify-center rounded-4xl gap-2 bg-[#d0fae5]"><div className="bg-[#2a7d2f] rounded-full h-2 w-2"></div>Active</div>
//                 </div>
//             <div className="flex justify-between border-2 border-green-700 p-4 rounded-lg">
//                     <div className="flex  gap-2">
//                         <img src="weed.png" className="h-7 w-7" alt="GPS logo" />
//                         <div><p>GPS Tracking</p><p>Signal Strength: Strong</p></div>
//                     </div>
//                        <div className="px-3 flex items-center justify-center rounded-4xl gap-2 bg-[#d0fae5]"><div className="bg-[#2a7d2f] rounded-full h-2 w-2"></div>Active</div>
//             </div>
//             <div className="flex justify-between border-2 border-green-700 p-4 rounded-lg">
//                     <div className="flex  gap-2">
//                         <img src="weed.png" className="h-7 w-7" alt="Battery logo" />
//                         <div><p>Battery Logo</p><p>47% remaining</p></div>
//                     </div>
//                         <div className="px-3 flex items-center justify-center rounded-4xl gap-2 bg-[#d0fae5]"><div className="bg-[#2a7d2f] rounded-full h-2 w-2"></div>Active</div>
//             </div>
//             </div>
//         </div>

//         <div>
//             <p>Hourly Performance</p>
            
//             {/* <LineChart
//   xAxis={[{ data: xData, scaleType: 'point' }]}
//   series={[{ data }]}
//   margin={margin}
// /> */}
// <LineChartGraph/>
// </div>
            
//         </div>
//         <div className="w-[30%]" >
//             <Notifications/>

//         </div>
// </div>
//     </>
//     )
// }
// export default Dashboard;



import LineChartGraph from "./LineChart";
import Notifications from "./Notifications";
import Zone_Density from "./zone_density";

function Dashboard() {
  return (
    <div className="p-4 md:p-10 gap-5 bg-[#f8fcfa] flex flex-col md:flex-row">
      
      {/* Left Section */}
      <div className="w-full md:w-7/12 flex flex-col gap-6">
        
        {/* Today's Summary */}
        <div className="bg-gradient-to-r from-[#0a3d2c] to-[#2a5c43] text-white p-6 border border-[#2a7d2f] rounded-3xl">
          <p>Today's Summary</p>
          <div className="flex flex-wrap gap-4 m-4 justify-between">
            {[
              { img: "weed.png", label: "Weed Eliminated", value: "2569" },
              { img: "Navigate.png", label: "Area Covered", value: "9 acres" },
              { img: "time.png", label: "Active Time", value: "2h 9min" },
              { img: "energy-efficient.png", label: "Efficiency", value: "80%" },
            ].map((card, i) => (
              <div key={i} className="bg-[#2a7d2f] p-4 flex-1 min-w-[120px] rounded-md flex flex-col items-center justify-center">
                <img src={card.img} className="h-7 w-7" alt={card.label} />
                <p>{card.label}</p>
                <p>{card.value}</p>
              </div>
            ))}
          </div>
        </div>

       

        <div className="border border-[#2a7d2f] rounded-3xl p-6 flex flex-col gap-4">
  <p>Quick Actions</p>

  <div className="flex flex-wrap gap-4 justify-center">
    {[
      { img: "weed.png", title: "Start New Session", subtitle: "Begin Weed Detection", color: "border-[#2a7d2f]" },
      { img: "weed.png", title: "Emergency Stop", subtitle: "Immediate halt", color: "border-red-700 text-red-700" },
      { img: "weed.png", title: "Resume Last Session", subtitle: "Zone", color: "border-[#2a7d2f]" },
      { img: "weed.png", title: "Export Report", subtitle: "Download data", color: "border-[#2a7d2f]" },
    ].map((btn, i) => (
      <button
        key={i}
        className={`flex ${btn.color} border rounded-lg p-4 gap-2 items-center
w-9/20 max-sm:w-full cursor-pointer`}

      >
        <img src={btn.img} className="h-7 w-7" />
        <div className="flex flex-col items-start">
          <p>{btn.title}</p>
          <p className="text-sm text-gray-600">{btn.subtitle}</p>
        </div>
      </button>
    ))}
  </div>
</div>

        <div className="border border-[#2a7d2f] rounded-3xl p-6 flex flex-col gap-4">
          <div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-4 gap-2">
            <p>System Status</p>
            <div className="px-3 flex items-center justify-center rounded-full gap-2 text-white text-sm bg-[#0b470f]">
              <div className="bg-[#d0fae5] rounded-full h-2 w-2"></div>
              All System Operational
            </div>
          </div>
          <div className="flex flex-col gap-2">
            {["Laser System", "GPS Tracking", "Battery Logo"].map((system, i) => (
              <div key={i} className="flex flex-col md:flex-row justify-between border-2 border-green-700 p-4 rounded-lg gap-2">
                <div className="flex gap-2 items-center">
                  <img src="weed.png" className="h-7 w-7" alt={system} />
                  <div>
                    <p>{system}</p>
                    <p>Operating manually</p>
                  </div>
                </div>
                <div className="px-3 flex items-center justify-center rounded-full gap-2 bg-[#d0fae5]">
                  <div className="bg-[#2a7d2f] rounded-full h-2 w-2"></div>
                  Active
                </div>
              </div>
            ))}
          </div>
        </div>

        <div>
          <p>Hourly Performance</p>
          <LineChartGraph />
        </div>
      </div>

      <div className="w-full flex flex-col gap-6 md:w-5/12 mt-6 md:mt-0">
        <Notifications />
        <Zone_Density/>
      </div>
    </div>
  );
}

export default Dashboard;
