import { LineChart } from '@mui/x-charts';
import { useState } from 'react';

function LineChartGraph() {
  const [data] = useState([30, 40, 50, null, 20,10]);
  const [xData] = useState(['6:00', '7:00', '8:00', '9:00', '10:00','11:00']);

  const margin = { top: 20, bottom: 40, left: 50, right: 20 };

  return (
    <LineChart
      xAxis={[{ data: xData, scaleType: 'point' }]}
      series={[{ data, color: '#2a7d2f',connectNulls: false }]}
      margin={margin}
      height={300}
    />
  );
}

export default LineChartGraph;
