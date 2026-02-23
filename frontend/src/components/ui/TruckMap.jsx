import { useEffect, useState } from "react";
import { GoogleMap, Marker, useLoadScript } from "@react-google-maps/api";

export default function TruckMap() {
  const [position, setPosition] = useState(null);

  useEffect(() => {
    const watchId = navigator.geolocation.watchPosition(
      (pos) => {
        setPosition({
          lat: pos.coords.latitude,
          lng: pos.coords.longitude,
        });
      },
      (err) => console.error(err),
      { enableHighAccuracy: true }
    );

    return () => navigator.geolocation.clearWatch(watchId);
  }, []);

  const { isLoaded } = useLoadScript({
    googleMapsApiKey: import.meta.env.VITE_GOOGLE_MAPS_KEY,
  });

  if (!isLoaded) return <p>Loading...</p>;

  return (
    <GoogleMap
      mapContainerStyle={{ width: "100%", height: "500px" }}
      center={position || { lat: 24.8607, lng: 67.0011 }}
      zoom={15}
    >
      {position && (
        <Marker
          position={position}
          icon={{
            url: "/tractor.png",
            scaledSize: new window.google.maps.Size(70, 70),
          }}
        />
      )}
    </GoogleMap>
  );
}
