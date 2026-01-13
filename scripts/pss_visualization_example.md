# PSS Memory Visualization - Quick Start Example

## Overview

This example demonstrates how to use the PSS memory visualization tool to create executive-level performance graphs.

## Quick Start

```bash
# Navigate to the scripts directory
cd /home/runner/work/ort/ort/scripts

# Install dependencies (if not already installed)
pip install matplotlib numpy

# Run the visualization tool
python3 pss_memory_visualization.py
```

## Expected Output

The script will:
1. Parse the before/after PSS memory data
2. Calculate improvement metrics
3. Generate 4 professional graphs

```
============================================================
PSS Memory Visualization Tool
============================================================

Calculating metrics...

Key Findings:
  Peak Current PSS Total - Before: 118 MB
  Peak Current PSS Total - After:  107 MB
  Improvement: 11 MB (9.3%)

  Peak Average PSS - Before: 102 MB
  Peak Average PSS - After:  87 MB
  Improvement: 15 MB (14.7%)

Generating visualizations...

✓ Generated: pss_comparison_total.png
✓ Generated: pss_comparison_average.png
✓ Generated: pss_peak_comparison.png
✓ Generated: pss_executive_summary.png
```

## Generated Files

### 1. pss_comparison_total.png
Time-series graph showing Current PSS Total over time for both before and after optimization.
- Clear visualization of memory consumption patterns
- Green shaded "Improvement Zone" highlighting the memory savings
- Suitable for technical presentations

### 2. pss_comparison_average.png
Time-series graph showing Average PSS over time for both before and after optimization.
- Shows the running average memory consumption
- Demonstrates sustained improvement over time
- Useful for understanding long-term memory behavior

### 3. pss_peak_comparison.png
Side-by-side bar charts comparing peak values:
- **Peak Current PSS Total**: 118 MB → 107 MB (11 MB / 9.3% improvement)
- **Peak Average PSS**: 102 MB → 87 MB (15 MB / 14.7% improvement)
- Prominent improvement callouts
- Perfect for quick executive summaries

### 4. pss_executive_summary.png (Recommended for CEO presentations)
Comprehensive dashboard combining all visualizations:
- 4 graphs in a single view
- Detailed metrics table
- Professional layout optimized for presentations
- All key information at a glance

## Customizing with Your Own Data

To use your own memory data:

1. Open `pss_memory_visualization.py`
2. Locate the `BEFORE_DATA` and `AFTER_DATA` arrays
3. Update the data tuples with your measurements

Data format:
```python
BEFORE_DATA = [
    (time_seconds, current_pss_total_mb, average_pss_mb),
    (1, 68, 68),
    (2, 68, 68),
    # ... add more measurements
]
```

## Use Cases

### For Technical Teams
- Document memory optimization efforts
- Track performance improvements over time
- Identify memory consumption patterns
- Support technical design reviews

### For Executives
- Show business impact of optimization work
- Justify resource allocation for performance improvements
- Present clear ROI metrics
- Support strategic decision-making

## Graph Features

All graphs include:
- **High resolution** (300 DPI) for print quality
- **Professional color scheme** (Red=Before, Green=After)
- **Clear legends and labels**
- **Grid lines** for easy value reading
- **Consistent styling** across all visualizations

## Tips for Presentations

1. **For executive meetings**: Use `pss_executive_summary.png` - it provides complete context in one slide
2. **For technical deep-dives**: Use individual graphs to discuss specific aspects
3. **For reports**: Include all 4 graphs to provide comprehensive documentation
4. **For quick updates**: Use `pss_peak_comparison.png` to show key metrics

## Technical Details

- **Language**: Python 3.6+
- **Dependencies**: matplotlib, numpy
- **Output Format**: PNG (300 DPI)
- **Chart Types**: Line plots, bar charts, data tables
- **Color Palette**: Professional, color-blind friendly

## Support

For more information, see [PSS_VISUALIZATION_README.md](PSS_VISUALIZATION_README.md)
