fetch('data/demo_signals.json')
  .then(response => response.json())
  .then(data => {
      const trace = {
          x: data.t,
          y: data.signal,
          mode: 'lines',
          name: 'Robot Signal'
      };
      Plotly.newPlot('plot', [trace], {title: 'Sleepy → Alarmed'});
  });
