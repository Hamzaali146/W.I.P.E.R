export default function Navbar() {
  return (
    <header>
      <div className="bg-gradient-to-r from-[#1f4f3a] to-[#2f7d4a] border-b border-green-300/40">
        <div className="max-w-7xl mx-auto px-6 py-6 flex items-center justify-between">
          
          <div className="flex items-center gap-3">
            <img className="h-7 w-7" src="mainlogo.png" alt="mainlogo" />
            {/* <div className="w-10 h-10 rounded-xl bg-green-700/40 flex items-center justify-center border border-green-300/40">
              <div className="w-4 h-4 rounded-full border-2 border-green-300"></div>
            </div> */}
            <div>
              <h1 className="text-white font-semibold text-lg leading-none">WeedBot</h1>
              <p className="text-green-200 text-xs">Precision Laser Weed Control</p>
            </div>
          </div>
          <div className="flex items-center gap-4">
            <div className="flex items-center gap-2 px-4 py-1.5 rounded-full bg-green-800/40 border border-green-300/40">
              <span className="w-2 h-2 rounded-full bg-green-400"></span>
              <span className="text-green-100 text-sm">Device Online</span>
            </div>

            <button className="text-green-100 hover:text-white transition">
              <img src="bell (1).png" alt="" />
            </button>
            <button className="text-green-100 hover:text-white transition">
              <img src="settings.png" alt="settingsicon" />
            </button>
          </div>
        </div>
      </div>
    </header>
  );
}
