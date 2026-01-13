# PSS Memory Visualization Tool

## Overview

This tool generates executive-level graphs comparing memory consumption (PSS - Proportional Set Size) before and after optimization. The visualizations are designed for CEO-level presentations with professional styling and clear improvement metrics.

## Features

- **Comprehensive Comparisons**: Side-by-side comparison of memory consumption before and after optimization
- **Multiple Metrics**: Tracks both Current PSS Total and Average PSS over time
- **Peak Analysis**: Identifies peak memory usage and calculates improvement percentages
- **Executive Dashboard**: Combined view of all metrics in a single professional dashboard
- **High-Quality Output**: 300 DPI images suitable for presentations and reports

## Requirements

- Python 3.6 or higher
- matplotlib
- numpy

## Installation

Install the required dependencies:

```bash
pip install matplotlib numpy
```

Or using conda:

```bash
conda install matplotlib numpy
```

## Usage

Run the script from the scripts directory:

```bash
cd /home/runner/work/ort/ort/scripts
python3 pss_memory_visualization.py
```

## Output Files

The script generates four PNG images:

1. **pss_comparison_total.png** - Time series comparison of Current PSS Total
2. **pss_comparison_average.png** - Time series comparison of Average PSS
3. **pss_peak_comparison.png** - Bar chart comparison of peak values with improvement metrics
4. **pss_executive_summary.png** - Comprehensive dashboard combining all visualizations (recommended for presentations)

## Key Metrics Displayed

### Peak PSS Total
- **Before**: 118 MB
- **After**: 107 MB
- **Improvement**: 11 MB (9.3%)

### Peak Average PSS
- **Before**: 102 MB
- **After**: 87 MB
- **Improvement**: 15 MB (14.7%)

## Customization

To use different data:

1. Open `pss_memory_visualization.py`
2. Modify the `BEFORE_DATA` and `AFTER_DATA` arrays
3. Each tuple format: `(time_in_seconds, current_pss_total_mb, average_pss_mb)`

Example:
```python
BEFORE_DATA = [
    (1, 68, 68),  # time=1s, total=68MB, avg=68MB
    (2, 68, 68),
    # ... more data points
]
```

## Graph Features

### Time Series Graphs
- Dual-line plots showing before (red) and after (green) measurements
- Shaded improvement zone highlighting the memory savings
- Grid lines for easy reading
- Legend with clear labels

### Peak Comparison Bar Charts
- Side-by-side bars for before/after comparison
- Value labels on each bar
- Prominent improvement callouts with MB and percentage
- Color-coded: Red (before) and Green (after)

### Executive Dashboard
- Four-panel layout with all key visualizations
- Summary table with detailed metrics
- Professional color scheme
- Optimized for presentation slides

## Use Cases

- **Performance Reports**: Document memory optimization results
- **Executive Presentations**: Show clear business impact of technical improvements
- **Technical Reviews**: Analyze memory consumption patterns
- **Benchmarking**: Compare different optimization strategies

## Tips for Presentations

1. Use **pss_executive_summary.png** for comprehensive overview slides
2. Use individual graphs for detailed technical discussions
3. The improvement percentages are prominently displayed for easy reference
4. All graphs use consistent color coding (Red=Before, Green=After)

## License

This script is part of the OSS Review Toolkit (ORT) project.
