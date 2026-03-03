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

  if (!isLoaded) {
    return (
      <div
        className="metric-tile-light flex items-center justify-center text-sm text-muted-foreground"
        style={{ height: "320px" }}
      >
        Loading live map...
      </div>
    );
  }

  const mapContainerStyle = {
    width: "100%",
    height: "min(58vh, 360px)",
    borderRadius: "16px",
  };

  const mapOptions = {
    disableDefaultUI: true,
    zoomControl: true,
    streetViewControl: false,
    mapTypeControl: false,
    fullscreenControl: false,
  };

  return (
    <GoogleMap
      mapContainerStyle={mapContainerStyle}
      options={mapOptions}
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
