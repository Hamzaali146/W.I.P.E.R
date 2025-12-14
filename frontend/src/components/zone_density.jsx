import { Box, Typography, Chip, Stack } from "@mui/material";
import { BarChart } from "@mui/x-charts/BarChart";

const dataset = [
  { zone: "Zone A", value: 85 },
  { zone: "Zone B", value: 45 },
  { zone: "Zone C", value: 92 },
  { zone: "Zone D", value: 38 },
  { zone: "Zone E", value: 66 },
  { zone: "Zone F", value: 70 },
];

const getColor = (value) => {
  if (value <= 40) return "#22c55e";   // Low
  if (value <= 60) return "#facc15";   // Medium
  if (value <= 80) return "#fb923c";   // High
  return "#ef4444";                    // Critical
};

export default function WeedDensityChart() {
  return (
    <Box
      sx={{
        p: 4,
        borderRadius: 3,
        border: "2px solid #cce3d4",
        background: "linear-gradient(135deg, #f6fffa, #ffffff)",
        maxWidth: 700,
      }}
    >
      <Box display="flex" justifyContent="space-between" mb={2}>
        <Typography variant="h6" fontWeight={600}>
          Weed Density by Zone
        </Typography>
        <Typography variant="body2" color="text.secondary">
          Weeds per 100 sq ft
        </Typography>
      </Box>

      <BarChart
        dataset={dataset}
        xAxis={[
          {
            scaleType: "band",
            dataKey: "zone",
          },
        ]}
        yAxis={[{ min: 0, max: 100 }]}
        series={[
          {
            dataKey: "value",

            color: (params) => getColor(params.value),
          },
        ]}
        height={300}
        sx={{
          ".MuiChartsGrid-line": {
            strokeDasharray: "4 4",
          },
        }}
      />
      <Stack direction="row" spacing={2} justifyContent="center" mt={3} flexWrap="wrap">
        <Chip label="Low (0-40)" sx={{ bgcolor: "#22c55e", color: "#fff" }} />
        <Chip label="Medium (41-60)" sx={{ bgcolor: "#facc15" }} />
        <Chip label="High (61-80)" sx={{ bgcolor: "#fb923c", color: "#fff" }} />
        <Chip label="Critical (81+)" sx={{ bgcolor: "#ef4444", color: "#fff" }} />
      </Stack>
    </Box>
  );
}
