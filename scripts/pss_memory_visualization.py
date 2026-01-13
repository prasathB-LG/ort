#!/usr/bin/env python3
"""
PSS Memory Visualization Tool

This script generates executive-level graphs comparing memory consumption (PSS - Proportional Set Size)
before and after optimization. It creates professional visualizations suitable for CEO presentations.

Usage:
    python3 pss_memory_visualization.py

Output:
    - pss_comparison_total.png: Comparison of Current PSS Total over time
    - pss_comparison_average.png: Comparison of Average PSS over time
    - pss_peak_comparison.png: Peak PSS comparison with improvement metrics
    - pss_executive_summary.png: Combined executive summary dashboard
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
import numpy as np

# Data from the problem statement
BEFORE_DATA = [
    (1, 68, 68), (2, 68, 68), (3, 68, 68), (4, 68, 68), (5, 68, 68),
    (6, 68, 68), (7, 68, 68), (8, 68, 68), (9, 68, 68), (10, 68, 68),
    (11, 65, 67), (12, 67, 67), (13, 68, 67), (14, 68, 67), (15, 68, 67),
    (16, 69, 67), (17, 67, 67), (18, 100, 69), (19, 108, 71), (20, 110, 73),
    (21, 107, 75), (22, 110, 76), (23, 111, 78), (24, 108, 79), (25, 109, 80),
    (26, 109, 81), (27, 110, 82), (28, 107, 83), (29, 109, 84), (30, 110, 85),
    (31, 111, 86), (32, 109, 86), (33, 113, 87), (34, 110, 88), (35, 111, 88),
    (36, 116, 89), (37, 116, 90), (38, 116, 91), (39, 117, 91), (40, 118, 92),
    (41, 118, 93), (42, 118, 93), (43, 118, 94), (44, 114, 94), (45, 114, 95),
    (46, 114, 95), (47, 115, 95), (48, 118, 96), (49, 115, 96), (50, 116, 97),
    (51, 117, 97), (52, 117, 97), (53, 118, 98), (54, 118, 98), (55, 114, 98),
    (56, 115, 99), (57, 116, 99), (58, 117, 99), (59, 118, 100), (60, 115, 100),
    (61, 116, 100), (62, 117, 100), (63, 118, 101), (64, 118, 101), (65, 118, 101),
    (66, 118, 101), (67, 118, 102), (68, 118, 102), (69, 66, 101), (70, 67, 101),
    (71, 68, 100), (72, 68, 100), (73, 68, 100), (74, 68, 99), (75, 68, 99)
]

AFTER_DATA = [
    (1, 61, 61), (2, 61, 61), (3, 61, 61), (4, 61, 61), (5, 61, 61),
    (6, 61, 61), (7, 61, 61), (8, 61, 61), (9, 61, 61), (10, 61, 61),
    (11, 61, 61), (12, 61, 61), (13, 61, 61), (14, 61, 61), (15, 61, 61),
    (16, 61, 61), (17, 61, 61), (18, 60, 60), (19, 97, 62), (20, 98, 64),
    (21, 99, 66), (22, 99, 67), (23, 99, 69), (24, 100, 70), (25, 101, 71),
    (26, 100, 72), (27, 100, 73), (28, 101, 74), (29, 100, 75), (30, 100, 76),
    (31, 101, 77), (32, 102, 77), (33, 102, 78), (34, 102, 79), (35, 102, 80),
    (36, 103, 80), (37, 103, 81), (38, 103, 81), (39, 103, 82), (40, 102, 82),
    (41, 104, 83), (42, 105, 83), (43, 105, 84), (44, 106, 84), (45, 107, 85),
    (46, 106, 85), (47, 105, 86), (48, 105, 86), (49, 106, 87), (50, 106, 87),
    (51, 106, 87), (52, 63, 87), (53, 62, 86), (54, 62, 86), (55, 61, 85),
    (56, 61, 85), (57, 61, 85), (58, 61, 84), (59, 61, 84), (60, 61, 83),
    (61, 61, 83), (62, 61, 83), (63, 61, 82), (64, 61, 82), (65, 61, 82),
    (66, 61, 81), (67, 61, 81), (68, 61, 81), (69, 61, 80), (70, 61, 80),
    (71, 61, 80), (72, 61, 80), (73, 61, 79), (74, 61, 79)
]


def parse_data(data):
    """Parse data into separate arrays."""
    time = [item[0] for item in data]
    total = [item[1] for item in data]
    average = [item[2] for item in data]
    return time, total, average


def calculate_metrics(before_data, after_data):
    """Calculate peak PSS and improvement metrics."""
    _, before_total, before_avg = parse_data(before_data)
    _, after_total, after_avg = parse_data(after_data)
    
    peak_before_total = max(before_total)
    peak_after_total = max(after_total)
    peak_before_avg = max(before_avg)
    peak_after_avg = max(after_avg)
    
    improvement_total_mb = peak_before_total - peak_after_total
    improvement_total_pct = (improvement_total_mb / peak_before_total) * 100
    
    improvement_avg_mb = peak_before_avg - peak_after_avg
    improvement_avg_pct = (improvement_avg_mb / peak_before_avg) * 100
    
    return {
        'peak_before_total': peak_before_total,
        'peak_after_total': peak_after_total,
        'peak_before_avg': peak_before_avg,
        'peak_after_avg': peak_after_avg,
        'improvement_total_mb': improvement_total_mb,
        'improvement_total_pct': improvement_total_pct,
        'improvement_avg_mb': improvement_avg_mb,
        'improvement_avg_pct': improvement_avg_pct
    }


def create_comparison_graph(before_data, after_data, metric='total', filename='pss_comparison.png'):
    """Create a comparison graph for Total or Average PSS."""
    time_before, total_before, avg_before = parse_data(before_data)
    time_after, total_after, avg_after = parse_data(after_data)
    
    if metric == 'total':
        before_values = total_before
        after_values = total_after
        title = 'Memory Consumption Comparison - Current PSS Total'
        ylabel = 'Current PSS Total (MB)'
    else:
        before_values = avg_before
        after_values = avg_after
        title = 'Memory Consumption Comparison - Average PSS'
        ylabel = 'Average PSS (MB)'
    
    plt.figure(figsize=(14, 8))
    
    # Plot before and after data
    plt.plot(time_before, before_values, 'o-', color='#E74C3C', linewidth=2.5, 
             markersize=4, label='Before Optimization', alpha=0.8)
    plt.plot(time_after, after_values, 's-', color='#27AE60', linewidth=2.5, 
             markersize=4, label='After Optimization', alpha=0.8)
    
    # Add shaded area to show improvement
    max_time = max(max(time_before), max(time_after))
    plt.fill_between(range(1, max_time + 1), 
                     [max(before_values)] * max_time,
                     [max(after_values)] * max_time,
                     alpha=0.15, color='#27AE60', label='Improvement Zone')
    
    # Styling
    plt.xlabel('Time (seconds)', fontsize=14, fontweight='bold')
    plt.ylabel(ylabel, fontsize=14, fontweight='bold')
    plt.title(title, fontsize=18, fontweight='bold', pad=20)
    plt.legend(fontsize=12, loc='upper left', frameon=True, shadow=True)
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.tight_layout()
    
    # Save the figure
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"✓ Generated: {filename}")
    plt.close()


def create_peak_comparison(metrics, filename='pss_peak_comparison.png'):
    """Create a bar chart comparing peak PSS values."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # Peak Total Comparison
    categories = ['Before\nOptimization', 'After\nOptimization']
    values_total = [metrics['peak_before_total'], metrics['peak_after_total']]
    colors = ['#E74C3C', '#27AE60']
    
    bars1 = ax1.bar(categories, values_total, color=colors, alpha=0.8, edgecolor='black', linewidth=2)
    ax1.set_ylabel('Peak PSS Total (MB)', fontsize=14, fontweight='bold')
    ax1.set_title('Peak Current PSS Total Comparison', fontsize=16, fontweight='bold', pad=20)
    ax1.set_ylim([0, max(values_total) * 1.3])
    ax1.grid(True, alpha=0.3, axis='y', linestyle='--')
    
    # Add value labels on bars
    for bar, value in zip(bars1, values_total):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 2,
                f'{int(value)} MB', ha='center', va='bottom', fontsize=13, fontweight='bold')
    
    # Add improvement annotation
    improvement_text = f'Improvement:\n{int(metrics["improvement_total_mb"])} MB\n({metrics["improvement_total_pct"]:.1f}%)'
    ax1.text(0.5, max(values_total) * 0.7, improvement_text,
            ha='center', fontsize=14, fontweight='bold',
            bbox=dict(boxstyle='round,pad=1', facecolor='#F39C12', alpha=0.8, edgecolor='black', linewidth=2))
    
    # Peak Average Comparison
    values_avg = [metrics['peak_before_avg'], metrics['peak_after_avg']]
    bars2 = ax2.bar(categories, values_avg, color=colors, alpha=0.8, edgecolor='black', linewidth=2)
    ax2.set_ylabel('Peak Average PSS (MB)', fontsize=14, fontweight='bold')
    ax2.set_title('Peak Average PSS Comparison', fontsize=16, fontweight='bold', pad=20)
    ax2.set_ylim([0, max(values_avg) * 1.3])
    ax2.grid(True, alpha=0.3, axis='y', linestyle='--')
    
    # Add value labels on bars
    for bar, value in zip(bars2, values_avg):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 2,
                f'{int(value)} MB', ha='center', va='bottom', fontsize=13, fontweight='bold')
    
    # Add improvement annotation
    improvement_text_avg = f'Improvement:\n{int(metrics["improvement_avg_mb"])} MB\n({metrics["improvement_avg_pct"]:.1f}%)'
    ax2.text(0.5, max(values_avg) * 0.7, improvement_text_avg,
            ha='center', fontsize=14, fontweight='bold',
            bbox=dict(boxstyle='round,pad=1', facecolor='#F39C12', alpha=0.8, edgecolor='black', linewidth=2))
    
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"✓ Generated: {filename}")
    plt.close()


def create_executive_dashboard(before_data, after_data, metrics, filename='pss_executive_summary.png'):
    """Create a comprehensive executive dashboard."""
    fig = plt.figure(figsize=(20, 12))
    gs = GridSpec(3, 2, figure=fig, hspace=0.3, wspace=0.25)
    
    # Parse data
    time_before, total_before, avg_before = parse_data(before_data)
    time_after, total_after, avg_after = parse_data(after_data)
    
    # Main title
    fig.suptitle('Memory Optimization Executive Summary', fontsize=24, fontweight='bold', y=0.98)
    
    # 1. Current PSS Total Comparison (top left)
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.plot(time_before, total_before, 'o-', color='#E74C3C', linewidth=2.5, 
             markersize=3, label='Before', alpha=0.8)
    ax1.plot(time_after, total_after, 's-', color='#27AE60', linewidth=2.5, 
             markersize=3, label='After', alpha=0.8)
    ax1.set_xlabel('Time (seconds)', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Current PSS Total (MB)', fontsize=11, fontweight='bold')
    ax1.set_title('Current PSS Total Over Time', fontsize=14, fontweight='bold')
    ax1.legend(fontsize=10, loc='upper left')
    ax1.grid(True, alpha=0.3, linestyle='--')
    
    # 2. Average PSS Comparison (top right)
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.plot(time_before, avg_before, 'o-', color='#E74C3C', linewidth=2.5, 
             markersize=3, label='Before', alpha=0.8)
    ax2.plot(time_after, avg_after, 's-', color='#27AE60', linewidth=2.5, 
             markersize=3, label='After', alpha=0.8)
    ax2.set_xlabel('Time (seconds)', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Average PSS (MB)', fontsize=11, fontweight='bold')
    ax2.set_title('Average PSS Over Time', fontsize=14, fontweight='bold')
    ax2.legend(fontsize=10, loc='upper left')
    ax2.grid(True, alpha=0.3, linestyle='--')
    
    # 3. Peak Total PSS Bar Chart (middle left)
    ax3 = fig.add_subplot(gs[1, 0])
    categories = ['Before', 'After']
    values_total = [metrics['peak_before_total'], metrics['peak_after_total']]
    colors = ['#E74C3C', '#27AE60']
    bars = ax3.bar(categories, values_total, color=colors, alpha=0.8, edgecolor='black', linewidth=2)
    ax3.set_ylabel('Peak PSS Total (MB)', fontsize=11, fontweight='bold')
    ax3.set_title('Peak Current PSS Total', fontsize=14, fontweight='bold')
    ax3.set_ylim([0, max(values_total) * 1.2])
    ax3.grid(True, alpha=0.3, axis='y', linestyle='--')
    for bar, value in zip(bars, values_total):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{int(value)} MB', ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    # 4. Peak Average PSS Bar Chart (middle right)
    ax4 = fig.add_subplot(gs[1, 1])
    values_avg = [metrics['peak_before_avg'], metrics['peak_after_avg']]
    bars = ax4.bar(categories, values_avg, color=colors, alpha=0.8, edgecolor='black', linewidth=2)
    ax4.set_ylabel('Peak Average PSS (MB)', fontsize=11, fontweight='bold')
    ax4.set_title('Peak Average PSS', fontsize=14, fontweight='bold')
    ax4.set_ylim([0, max(values_avg) * 1.2])
    ax4.grid(True, alpha=0.3, axis='y', linestyle='--')
    for bar, value in zip(bars, values_avg):
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{int(value)} MB', ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    # 5. Key Metrics Summary (bottom, spanning both columns)
    ax5 = fig.add_subplot(gs[2, :])
    ax5.axis('off')
    
    # Create metrics table
    summary_text = [
        ['Metric', 'Before', 'After', 'Improvement'],
        ['Peak Current PSS Total', f'{int(metrics["peak_before_total"])} MB', 
         f'{int(metrics["peak_after_total"])} MB', 
         f'{int(metrics["improvement_total_mb"])} MB ({metrics["improvement_total_pct"]:.1f}%)'],
        ['Peak Average PSS', f'{int(metrics["peak_before_avg"])} MB', 
         f'{int(metrics["peak_after_avg"])} MB', 
         f'{int(metrics["improvement_avg_mb"])} MB ({metrics["improvement_avg_pct"]:.1f}%)']
    ]
    
    # Create table
    table = ax5.table(cellText=summary_text, cellLoc='center', loc='center',
                     colWidths=[0.3, 0.2, 0.2, 0.3])
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 3)
    
    # Style header row
    for i in range(4):
        cell = table[(0, i)]
        cell.set_facecolor('#34495E')
        cell.set_text_props(weight='bold', color='white', fontsize=13)
    
    # Style data rows
    for i in range(1, 3):
        for j in range(4):
            cell = table[(i, j)]
            if j == 3:  # Improvement column
                cell.set_facecolor('#D5F4E6')
                cell.set_text_props(weight='bold', color='#27AE60')
            else:
                cell.set_facecolor('#ECF0F1')
    
    # Add title for metrics section
    ax5.text(0.5, 0.95, 'Performance Improvement Summary', 
            ha='center', va='top', fontsize=16, fontweight='bold',
            transform=ax5.transAxes)
    
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"✓ Generated: {filename}")
    plt.close()


def main():
    """Main function to generate all visualizations."""
    print("\n" + "="*60)
    print("PSS Memory Visualization Tool")
    print("="*60 + "\n")
    
    # Calculate metrics
    print("Calculating metrics...")
    metrics = calculate_metrics(BEFORE_DATA, AFTER_DATA)
    
    print(f"\nKey Findings:")
    print(f"  Peak Current PSS Total - Before: {int(metrics['peak_before_total'])} MB")
    print(f"  Peak Current PSS Total - After:  {int(metrics['peak_after_total'])} MB")
    print(f"  Improvement: {int(metrics['improvement_total_mb'])} MB ({metrics['improvement_total_pct']:.1f}%)")
    print(f"\n  Peak Average PSS - Before: {int(metrics['peak_before_avg'])} MB")
    print(f"  Peak Average PSS - After:  {int(metrics['peak_after_avg'])} MB")
    print(f"  Improvement: {int(metrics['improvement_avg_mb'])} MB ({metrics['improvement_avg_pct']:.1f}%)")
    
    print(f"\nGenerating visualizations...\n")
    
    # Generate individual graphs
    create_comparison_graph(BEFORE_DATA, AFTER_DATA, metric='total', 
                           filename='pss_comparison_total.png')
    create_comparison_graph(BEFORE_DATA, AFTER_DATA, metric='average', 
                           filename='pss_comparison_average.png')
    create_peak_comparison(metrics, filename='pss_peak_comparison.png')
    
    # Generate executive dashboard
    create_executive_dashboard(BEFORE_DATA, AFTER_DATA, metrics, 
                              filename='pss_executive_summary.png')
    
    print(f"\n" + "="*60)
    print("✓ All visualizations generated successfully!")
    print("="*60)
    print("\nGenerated files:")
    print("  1. pss_comparison_total.png - Current PSS Total comparison")
    print("  2. pss_comparison_average.png - Average PSS comparison")
    print("  3. pss_peak_comparison.png - Peak PSS comparison with metrics")
    print("  4. pss_executive_summary.png - Executive dashboard (recommended)")
    print("\n")


if __name__ == '__main__':
    main()
