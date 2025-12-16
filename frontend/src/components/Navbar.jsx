import { useState } from "react";

export default function Navbar() {
  const [showSettings, setShowSettings] = useState(false);

  const newNotificationsCount = 2; //will make it dynamic later

  return (
    <header className="relative">
      <div className="bg-gradient-to-r from-[#1f4f3a] to-[#2f7d4a] border-b border-green-300/40">
        <div className="max-w-7xl mx-auto px-6 py-6 flex items-center justify-between">
          
          <div className="flex items-center gap-3">
            <img className="h-7 w-7" src="mainlogo.png" alt="mainlogo" />
            <div>
              <h1 className="text-white font-semibold text-lg leading-none">
                W.I.P.E.R
              </h1>
              <p className="text-green-200 text-xs">
                Weed Identification, Prediction and Eradication Robot
              </p>
            </div>
          </div>

          <div className="flex items-center gap-4">
            <div className="flex items-center gap-2 px-4 py-1.5 rounded-full bg-green-800/40 border border-green-300/40">
              <span className="w-2 h-2 rounded-full bg-green-400"></span>
              <span className="text-green-100 text-sm">Device Online</span>
            </div>

            <div className="relative">
              <img
                src="bell (1).png"
                alt="notifications"
              />

              {newNotificationsCount > 0 && (
                <span className="absolute -top-2 -right-2 bg-red-500 text-white text-xs w-5 h-5 rounded-full flex items-center justify-center">
                  {newNotificationsCount}
                </span>
              )}
            </div>

            <button onClick={() => setShowSettings(!showSettings)} className="cursor-pointer">
              <img src="settings.png" alt="settingsicon"  />
            </button>
          </div>
        </div>
      </div>

      {showSettings && (
        <div className="absolute right-6 top-full mt-4 w-72 bg-white border rounded-lg shadow-lg p-5 z-50">
          <h3 className="font-semibold text-gray-700 mb-4">
            General Settings
          </h3>

          <div className="flex flex-col gap-4 text-sm">
            {/* <label className="flex justify-between items-center">
              Dark Mode
              <input type="checkbox" />
            </label> */}

            <label className="flex justify-between items-center">
              Enable Notifications
              <input type="checkbox" defaultChecked />
            </label>

            <label className="flex justify-between items-center">
              Auto System Updates
              <input type="checkbox" defaultChecked />
            </label>

            <label className="flex justify-between items-center">
              Device Sounds
              <input type="checkbox" />
            </label>

            <button className="text-red-500 text-left mt-3">
              Reset to Default
            </button>
          </div>
        </div>
      )}
    </header>
  );
}
