"""Charts used as the image for each case study (docs 3a–3f).

Photo hosts are blocked in the cloud sessions, so each case gets a chart drawn from figures in its sources.
usage: case_charts.py <outdir>
"""
import os, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker

INK, MUTED, GRID = '#262626', '#6b6b6b', '#e3e3e3'
BLUE, ORANGE, GREEN, RED = '#2f6db5', '#d9822b', '#3a8f5c', '#b8473d'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 9, 'axes.edgecolor': MUTED,
                     'axes.labelcolor': INK, 'xtick.color': INK, 'ytick.color': INK})
SIZE = (6.3, 2.75)  # inches, fits 16 cm width


def tidy(ax):
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    ax.yaxis.grid(True, color=GRID, lw=0.8)
    ax.set_axisbelow(True)


def amazon(path):
    # INPE PRODES, Legal Amazon, Aug–Jul years; 2025 preliminary
    years = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
    km2 = [7536, 10129, 10851, 13038, 11568, 9001, 6288, 5796]
    fig, ax = plt.subplots(figsize=SIZE)
    cols = [RED if 2019 <= y <= 2022 else (GREEN if y >= 2023 else MUTED) for y in years]
    bars = ax.bar(years, km2, color=cols, width=0.68)
    bars[-1].set_hatch('///'); bars[-1].set_edgecolor('white')
    for x, v in zip(years, km2):
        ax.text(x, v + 250, f"{v:,}", ha='center', va='bottom', fontsize=8, color=INK)
    ax.set_ylim(0, 15500)
    ax.set_xticks(years)
    ax.set_ylabel('Forest cleared (km²)')
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:,.0f}"))
    ax.text(2020.5, 14800, 'Bolsonaro govt 2019–22: enforcement cut', ha='center', color=RED, fontsize=8.5)
    ax.text(2024, 11000, 'Lula govt 2023–:\nenforcement restored', ha='center', color=GREEN, fontsize=8.5)
    ax.text(2025, 400, 'prelim.', ha='center', color='white', fontsize=7)
    tidy(ax)
    fig.tight_layout(); fig.savefig(path, dpi=220); plt.close(fig)


def cape_town(path):
    labels = ['City water use, Feb 2015', 'City water use, 12 Mar 2018',
              'Temporary desalination\ncapacity, 2018']
    vals = [1200, 511, 16]
    fig, ax = plt.subplots(figsize=SIZE)
    y = range(len(vals))[::-1]
    ax.barh(list(y), vals, color=[MUTED, BLUE, ORANGE], height=0.55)
    for yi, v in zip(y, vals):
        ax.text(v + 15, yi, f"{v:,} million L/day", va='center', fontsize=8.5, color=INK)
    ax.axvline(450, color=RED, ls='--', lw=1.2)
    ax.text(458, 2.42, 'Target to avoid Day Zero: 450', color=RED, fontsize=8, va='center')
    ax.set_yticks(list(y)); ax.set_yticklabels(labels)
    ax.set_xlim(0, 1650); ax.set_xlabel('Million litres per day')
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    ax.xaxis.grid(True, color=GRID, lw=0.8); ax.set_axisbelow(True)
    fig.tight_layout(); fig.savefig(path, dpi=220); plt.close(fig)


def nigeria(path):
    events = [
        (2006, 'Last census:\n140.4 million counted', BLUE, 1),
        (2016, 'UN-recommended census\nnot held', RED, -1),
        (2023, 'Census set for Mar, moved to\nMay, then postponed indefinitely', RED, 1),
        (2025, 'GDP rebased (2010→2019 base):\n2024 GDP revised up 41.7%', ORANGE, -1),
    ]
    fig, ax = plt.subplots(figsize=SIZE)
    ax.axhline(0, color=MUTED, lw=1.5, zorder=1)
    ax.axvspan(2006, 2026.6, ymin=0.47, ymax=0.53, color='#f3d9d6', zorder=0)
    for x, text, c, side in events:
        ax.plot([x, x], [0, 0.55 * side], color=c, lw=1.2, zorder=2)
        ax.scatter([x], [0], s=40, color=c, zorder=3)
        tx = x - 1.6 if x == 2023 else x
        ax.text(tx, 0.6 * side, text, ha='center', va='bottom' if side > 0 else 'top', fontsize=8, color=INK)
    ax.scatter([2026.6], [0], s=40, color=INK, zorder=3)
    ax.text(2026.6, 0.12, 'Jun 2026:\n20 years,\nno census', ha='center', va='bottom', fontsize=8, color=INK)
    ax.text(2011, -0.12, '20 years of estimates,\nnot counts', fontsize=8, color=RED, ha='center', va='top')
    ax.set_xlim(2004, 2028.5); ax.set_ylim(-1.15, 1.2)
    ax.set_xticks([2006, 2010, 2016, 2020, 2023, 2025]); ax.set_yticks([])
    for s in ('top', 'right', 'left'):
        ax.spines[s].set_visible(False)
    fig.tight_layout(); fig.savefig(path, dpi=220); plt.close(fig)


if __name__ == '__main__':
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    amazon(os.path.join(out, '1_1_amazon.png'))
    cape_town(os.path.join(out, '1_1_cape_town.png'))
    nigeria(os.path.join(out, '1_1_nigeria.png'))
    print('ok')
