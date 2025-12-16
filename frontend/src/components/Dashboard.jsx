import LineChartGraph from "./LineChart";
import Notifications from "./Notifications";
import Zone_Density from "./zone_density";
import TruckMap from "./TruckMap";
import Navbar from "./Navbar";

function Dashboard() {
  return (
    <>
      <div className="fixed top-0 left-0 w-full z-50">
      <Navbar/>
      </div>
    <div className="p-4 md:p-10 gap-5 bg-[#f8fcfa] flex flex-col md:flex-row mt-20">
      <div className="w-full md:w-7/12 flex flex-col gap-6">
      
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
      { img: "play.png", title: "Start New Session", subtitle: "Begin Weed Detection", color: "border-[#2a7d2f]" },
      { img: "pause-button.png", title: "Emergency Stop", subtitle: "Immediate halt", color: "border-red-700 text-red-700" },
      { img: "end.png", title: "Resume Last Session", subtitle: "Zone", color: "border-[#2a7d2f]" },
      { img: "file.png", title: "Export Report", subtitle: "Download data", color: "border-[#2a7d2f]" },
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
            {[{img: "laser-gun.png", title: "Laser System"},{img: "gps.png", title: "GPS Tracking"},{img: "car-battery.png", title: "Battery Level"}].map((system, i) => (
              <div key={i} className="flex flex-col md:flex-row justify-between border-2 border-green-700 p-4 rounded-lg gap-2">
                <div className="flex gap-2 items-center">
                  <img src={system.img} className="h-7 w-7" alt={system} />
                  <div>
                    <p>{system.title}</p>
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

        <div className="border border-[#2a7d2f] rounded-3xl p-6">
          <p className="mb-2">Hourly Performance</p>
          <LineChartGraph />
        </div>
         <div className="border border-[#2a7d2f] rounded-3xl p-6">
          <p className="mb-3">Real time Tracking</p>
          <TruckMap/>
        </div>
      </div>

      <div className="w-full flex flex-col gap-6 md:w-5/12 mt-6 md:mt-0">
        <Notifications />
        <Zone_Density/>
      </div>
    </div>
    </>
  );
}

export default Dashboard;
