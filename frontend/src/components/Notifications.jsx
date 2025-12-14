import { useState, useEffect } from "react";

const Notifications = () => {
  const [notifications, setNotifications] = useState([
    {
      id: 1,
      type: "battery",
      title: "Battery Low",
      message: "Device battery at 25%. Consider charging soon.",
      time: "2 min ago",
      status: "new",
    },
    {
      id: 2,
      type: "session",
      title: "Session Complete",
      message: "North Field A completed with 98.2% efficiency.",
      time: "15 min ago",
      status: "new",
    },
    {
      id: 3,
      type: "weed",
      title: "High Weed Density",
      message: "Zone C showing elevated weed density (92/100 sq ft).",
      time: "1 hr ago",
      status: "read",
    },
    {
      id: 4,
      type: "laser",
      title: "Laser Temperature High",
      message: "Laser temperature reached 65°C. System paused for cooling.",
      time: "3 hrs ago",
      status: "read",
    },
    {
      id: 5,
      type: "laser",
      title: "Laser Temperature High",
      message: "Laser temperature reached 65°C. System paused for cooling.",
      time: "3 hrs ago",
      status: "read",
    },
    {
      id: 6,
      type: "laser",
      title: "Laser Temperature High",
      message: "Laser temperature reached 65°C. System paused for cooling.",
      time: "3 hrs ago",
      status: "read",
    },
  ]);

  const markAllAsRead = () => {
    setNotifications((prev) =>
      prev.map((n) => ({ ...n, status: "read" }))
    );
  };

  return (
    <div className="p-4 bg-white rounded-lg border border-green-200 w-full  ">
      <div className="flex justify-between items-center mb-4">
        <h2 className="font-semibold text-lg flex items-center gap-2">
          <img className="w-10 h-10" src="bell.png" alt="bell" /> Alerts & Notifications
        </h2>
        <button
          onClick={markAllAsRead}
          className="text-green-600 text-sm hover:underline cursor-pointer"
        >
          Mark all as read
        </button>
      </div>

      <div className="flex flex-col gap-3 max-h-96 overflow-y-auto ">
        {notifications.map((n) => (
          <div
            key={n.id}
            className={`p-3 rounded-lg border ${
              n.type === "battery"
                ? "border-orange-300"
                : n.type === "session"
                ? "border-green-300"
                : n.type === "weed"
                ? "border-blue-300"
                : "border-red-300"
            } flex justify-between items-start`}
          >
            <div>
              <h3 className="font-semibold">{n.title}</h3>
              <p className="text-sm text-gray-600">{n.message}</p>
            </div>
            <div className="flex flex-col items-end">
              <span className="text-xs text-gray-400">{n.time}</span>
              {n.status === "new" && (
                <div className="w-10 rounded-lg px-1 bg-green-500 text-sm mt-1">new</div>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Notifications;
