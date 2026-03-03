import { useState, useEffect } from "react";
import { MapPin } from "lucide-react";

import { Card } from "./ui/card";
import { ImageWithFallback } from "./figma/ImageWithFallback";

const dummyFields = [
  {
    id: 1,
    name: "North Field A",
    crop: "Wheat",
    area: "15 acres",
    image:
      "https://images.unsplash.com/photo-1498408040764-ab6eb772a145?auto=format&fit=crop&w=1080&q=80",
  },
  {
    id: 2,
    name: "South Field B",
    crop: "Corn",
    area: "22 acres",
    image:
      "https://images.unsplash.com/photo-1634729609724-755326675bbb?auto=format&fit=crop&w=1080&q=80",
  },
  {
    id: 3,
    name: "East Field C",
    crop: "Rice",
    area: "18 acres",
    image:
      "https://images.unsplash.com/photo-1655903724829-37b3cd3d4ab9?auto=format&fit=crop&w=1080&q=80",
  },
  {
    id: 4,
    name: "West Field D",
    crop: "Mustard",
    area: "20 acres",
    image:
      "https://images.unsplash.com/photo-1715194717972-bc42451ec72c?auto=format&fit=crop&w=1080&q=80",
  },
];

export function FieldsOverview({ data }) {
  const [fields, setFields] = useState(Array.isArray(data) && data.length ? data : dummyFields);

  useEffect(() => {
    if (Array.isArray(data) && data.length) {
      setFields(data);
    }
  }, [data]);

  return (
    <Card className="p-6 surface-card">
      <h2 className="mb-6 section-title">Fields Overview</h2>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {fields.map((field) => (
          <Card key={field.id} className="overflow-hidden list-row">
            <div className="relative h-40">
              <ImageWithFallback src={field.image} alt={field.name} className="w-full h-full object-cover" />
            </div>

            <div className="p-4">
              <div className="mb-2">
                <h3 className="text-foreground">{field.name}</h3>
                <p className="text-muted-foreground">{field.crop}</p>
              </div>

              <div className="flex items-center gap-1 text-sm text-muted-foreground mt-3">
                <MapPin className="w-4 h-4" />
                <span>{field.area}</span>
              </div>
            </div>
          </Card>
        ))}
      </div>
    </Card>
  );
}
