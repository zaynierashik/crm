// Assuming you have set this data from your Django context
const companyTrendData = JSON.parse(document.getElementById('company-trend-data').textContent);

const lineConfig = {
  type: 'line',
  data: {
    labels: companyTrendData.dates,  // Use the dates provided by your Django context
    datasets: [
      {
        label: 'Companies Added',
        backgroundColor: '#0694a2',
        borderColor: '#0694a2',
        data: companyTrendData.counts,  // Use the counts provided by your Django context
        fill: false,
      }
    ],
  },
  options: {
    responsive: true,
    legend: {
      display: false,
    },
    tooltips: {
      mode: 'index',
      intersect: false,
    },
    hover: {
      mode: 'nearest',
      intersect: true,
    },
    scales: {
      x: {
        display: true,
        scaleLabel: {
          display: true,
          labelString: 'Date',
        },
      },
      y: {
        display: true,
        scaleLabel: {
          display: true,
          labelString: 'Companies Added',
        },
      },
    },
  },
};

// Change this to the id of your chart element in HTML
const lineCtx = document.getElementById('line');
window.myLine = new Chart(lineCtx, lineConfig);
