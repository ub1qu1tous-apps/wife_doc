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



# ---------- shared helpers for slots 4–15 ----------
def bars(ax, labels, vals, colours, fmt, ylabel=None, title=None, ymax=None):
    b = ax.bar(labels, vals, color=colours, width=0.6)
    top = ymax or max(vals) * 1.22
    for x, v in zip(labels, vals):
        ax.text(x, v + top * 0.02, fmt(v), ha='center', va='bottom', fontsize=8.5, color=INK)
    ax.set_ylim(0, top)
    if ylabel: ax.set_ylabel(ylabel)
    if title: ax.set_title(title, fontsize=9, color=INK, loc='left')
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:,.0f}"))
    tidy(ax)
    return b


def save(fig, path):
    fig.tight_layout(); fig.savefig(path, dpi=220); plt.close(fig)


def timeline(path, events, xlim, ticks, band=None, shift=None):
    """events: (x, text, colour, side +1 above / -1 below)."""
    shift = shift or {}
    fig, ax = plt.subplots(figsize=SIZE)
    ax.axhline(0, color=MUTED, lw=1.5, zorder=1)
    if band:
        x0, x1, c = band
        ax.axvspan(x0, x1, ymin=0.47, ymax=0.53, color=c, zorder=0)
    for x, text, c, side in events:
        ax.plot([x, x], [0, 0.55 * side], color=c, lw=1.2, zorder=2)
        ax.scatter([x], [0], s=40, color=c, zorder=3)
        ax.text(x + shift.get(x, 0), 0.6 * side, text, ha='center', va='bottom' if side > 0 else 'top',
                fontsize=8, color=INK)
    ax.set_xlim(*xlim); ax.set_ylim(-1.25, 1.25)
    ax.set_xticks(ticks); ax.set_xticklabels([str(t) for t in ticks]); ax.set_yticks([])
    for s_ in ('top', 'right', 'left'):
        ax.spines[s_].set_visible(False)
    save(fig, path)


def sri_lanka(path):
    fig, ax = plt.subplots(figsize=SIZE)
    bars(ax, ['2021', '2022', '2023'], [13.1, 25.0, 25.9], [MUTED, RED, RED], lambda v: f"{v:.1f}%",
         ylabel='Poverty rate (% of people)', ymax=32)
    ax.text(1.5, 29.5, 'Poverty roughly doubled in one year (World Bank, US$3.65/day line)',
            ha='center', fontsize=8.5, color=RED)
    save(fig, path)


def lithium(path):
    import numpy as np
    names = ['Argentina', 'Bolivia', 'Chile']
    res, rsv = [28, 23, 13], [4.4, 0, 9.2]
    x = np.arange(3)
    fig, ax = plt.subplots(figsize=SIZE)
    ax.bar(x - 0.18, res, 0.34, color=BLUE, label='Identified resources')
    ax.bar(x + 0.18, rsv, 0.34, color=ORANGE, label='Reserves (economic to extract now)')
    for xi, a, b in zip(x, res, rsv):
        ax.text(xi - 0.18, a + 0.6, f"{a:g}", ha='center', fontsize=8.5)
        ax.text(xi + 0.18, b + 0.6, f"{b:g}" if b else '0 recorded', ha='center', fontsize=8.5)
    ax.set_xticks(x); ax.set_xticklabels(names)
    ax.set_ylabel('Million tonnes of lithium'); ax.set_ylim(0, 33)
    ax.legend(frameon=False, fontsize=8, loc='upper right')
    tidy(ax); save(fig, path)


def tiles(path, items):
    fig, axs = plt.subplots(1, len(items), figsize=SIZE)
    for ax, (big, small_, c) in zip(axs, items):
        ax.add_patch(plt.Rectangle((0.03, 0.05), 0.94, 0.9, color=c, alpha=0.12, transform=ax.transAxes))
        ax.text(0.5, 0.62, big, ha='center', va='center', fontsize=17, color=c, weight='bold', transform=ax.transAxes)
        ax.text(0.5, 0.3, small_, ha='center', va='center', fontsize=8.3, color=INK, transform=ax.transAxes)
        ax.axis('off')
    save(fig, path)


def indonesia_fires(path):
    tiles(path, [('2.6 m ha', 'burned, Jun–Oct 2015\n(mainly Sumatra\nand Borneo)', RED),
                 ('US$16.1 bn', 'economic cost\n= 1.9% of GDP\n(World Bank)', ORANGE),
                 ('100,000+', 'premature deaths in\nIndonesia, Malaysia\nand Singapore', BLUE),
                 ('~1 Gt', 'greenhouse gases\nreleased, mostly\nfrom burning peat', MUTED)])


def senegal(path):
    fig, (a1, a2) = plt.subplots(1, 2, figsize=SIZE)
    bars(a1, ['Before', 'Now'], [29, 17.8], [MUTED, RED], lambda v: f"{v:g} kg", title='Fish eaten per person per year', ymax=35)
    bars(a2, ['2017', '2024'], [400, 46000], [MUTED, RED], lambda v: f"{v:,}", title='Migrants reaching the Canary Islands', ymax=55000)
    save(fig, path)


def bangladesh(path):
    fig, (a1, a2) = plt.subplots(1, 2, figsize=SIZE)
    bars(a1, ['2015–16', '2023'], [35.0, 39.1], [MUTED, GREEN], lambda v: f"{v:g} Mt", title='Rice output (million tonnes)', ymax=46)
    bars(a2, ['1980', '2017'], [3.5, 25], [MUTED, RED], lambda v: f"{v:g} m", title='Depth to groundwater, Nachole (Barind)', ymax=30)
    save(fig, path)


def vietnam_solar(path):
    fig, ax = plt.subplots(figsize=SIZE)
    bars(ax, ['End 2018', 'Mid 2019', 'End 2020'], [0.134, 4.0, 16.5], [MUTED, ORANGE, ORANGE],
         lambda v: (f"{v:g}+ GW" if v == 4.0 else f"{v:g} GW") if v >= 1 else f"{v*1000:.0f} MW", ylabel='Installed solar (GW)', ymax=20)
    ax.text(1.5, 18.2, 'Feed-in tariff rush: 0.1 GW → 16.5 GW in two years', ha='center', fontsize=8.5, color=ORANGE)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}"))
    save(fig, path)


def laos(path):
    fig, (a1, a2) = plt.subplots(1, 2, figsize=SIZE)
    bars(a1, ['2021', '2025'], [8100, 16900], [MUTED, ORANGE], lambda v: f"{v:,}", title='Electricity surplus (GWh) it cannot use', ymax=20000)
    bars(a2, ['2021'], [88], [RED], lambda v: f"{v:g}%", title='Public debt (% of GDP)', ymax=100)
    a2.set_xlim(-1, 1)
    save(fig, path)


def mekong(path):
    fig, ax = plt.subplots(figsize=SIZE)
    xs = [0.6, 2.4, 4.0, 5.6, 7.2]
    names = ["China\n(Lancang:\nupstream dams)", "Chiang Saen,\nThailand", "Laos\n(own dams,\ne.g. Xayaburi)", "Cambodia\n(Tonle Sap lake)", "Vietnam\n(Mekong Delta)"]
    cols = [RED, BLUE, ORANGE, BLUE, BLUE]
    ax.plot([0.2, 7.8], [0, 0], color=BLUE, lw=6, alpha=0.35, solid_capstyle='round')
    ax.annotate('', xy=(7.9, 0), xytext=(7.3, 0), arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=2))
    for x, n, c in zip(xs, names, cols):
        ax.scatter([x], [0], s=110, color=c, zorder=3)
        ax.text(x, -0.25, n, ha='center', va='top', fontsize=8, color=INK)
    ax.text(0.6, 0.35, 'Held back wet-season\nflow in 2019', ha='center', va='bottom', fontsize=8, color=RED)
    ax.text(2.4, 0.35, 'Usual monsoon rise\nin river level: absent\nfor 5 months', ha='center', va='bottom', fontsize=8, color=INK)
    ax.text(5.6, 0.35, 'Fish and rice depend\non the flood pulse', ha='center', va='bottom', fontsize=8, color=INK)
    ax.text(4.0, 1.25, 'River flows downstream →', ha='center', fontsize=8.5, color=BLUE)
    ax.set_xlim(0, 8.1); ax.set_ylim(-1.3, 1.45); ax.axis('off')
    save(fig, path)


def central_asia(path):
    timeline(path, [
        (2016, 'Karimov dies; Mirziyoyev\nbecomes president', MUTED, 1),
        (2018.2, 'Mar 2018: visit to Dushanbe;\nUzbekistan drops objection to Rogun', GREEN, -1),
        (2024.4, 'Jun 2024: 3 energy ministries\nsign Kambarata-1 agreement', GREEN, 1),
        (2025.1, 'Jan 2025: key principles agreed\nwith World Bank (34/33/33 shares)', GREEN, -1)],
        (2014.5, 2027), [2016, 2018, 2020, 2022, 2024, 2026], shift={2024.4: -1.3, 2025.1: 0.3})


def indus(path):
    even_timeline(path, [
        ('1960', 'Treaty signed,\nWorld Bank broker', GREEN, 1),
        ('1960–2025', 'Treaty survives\ndecades of hostility', GREEN, -1),
        ('Apr 2025', 'Pahalgam attack (26 dead);\nIndia holds treaty\n"in abeyance"', RED, 1),
        ('Apr 2025', "Pakistan: 'act of war';\nairspace and\ntrade closed", RED, -1),
        ('Aug 2026', 'Court of Arbitration:\ntreaty still in force', ORANGE, 1),
        ('Aug 2026', 'India rejects the\ncourt and its award', RED, -1)])


def oyu_tolgoi(path):
    fig, (a1, a2) = plt.subplots(1, 2, figsize=SIZE)
    bars(a1, ['2019\n(open pit)', '2028–36\n(planned avg)'], [146300, 500000], [MUTED, ORANGE],
         lambda v: f"{v/1000:,.0f}k t", title='Copper output per year', ymax=600000)
    a1.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v/1000:,.0f}k"))
    bars(a2, ['2015\nestimate', '2022\nreforecast'], [5.3, 7.06], [MUTED, RED], lambda v: f"US${v:g}bn",
         title='Underground expansion cost', ymax=8.5)
    a2.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}"))
    save(fig, path)


def guyana_nigeria(path):
    fig, (a1, a2) = plt.subplots(1, 2, figsize=SIZE)
    bars(a1, ['2019', '2023', 'Early 2024'], [0, 391, 645], [MUTED, GREEN, GREEN], lambda v: f"{v:,}k" if v else 'start',
         title='Guyana oil output (000 barrels/day)', ymax=780)
    bars(a2, ['Sabotage /\ntheft', 'Other\ncauses'], [3628, 1291], [RED, MUTED], lambda v: f"{v:,}",
         title='Niger Delta spills, 2015–Mar 2021', ymax=4400)
    save(fig, path)


def nickel(path):
    fig, ax = plt.subplots(figsize=SIZE)
    bars(ax, ['2020', '2023'], [1.4, 34.8], [MUTED, GREEN], lambda v: f"US${v:g} bn",
         ylabel='Value added by nickel (US$ bn)', ymax=42)
    ax.text(0.5, 38.5, 'After the Jan 2020 ore export ban (govt estimate)', ha='center', fontsize=8.5, color=GREEN)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}"))
    save(fig, path)


def even_timeline(path, ev):
    """Events evenly spaced, dates in the labels: used when the real gaps are too uneven to label clearly."""
    fig, ax = plt.subplots(figsize=SIZE)
    ax.axhline(0, color=MUTED, lw=1.5, zorder=1)
    for i, (d, text, c, side) in enumerate(ev):
        ax.plot([i, i], [0, 0.5 * side], color=c, lw=1.2, zorder=2)
        ax.scatter([i], [0], s=40, color=c, zorder=3)
        ax.text(i, 0.55 * side, f"{d}\n{text}", ha='center', va='bottom' if side > 0 else 'top', fontsize=8, color=INK)
    ax.set_xlim(-0.7, len(ev) - 0.3); ax.set_ylim(-1.45, 1.45); ax.axis('off')
    save(fig, path)


def brumadinho(path):
    even_timeline(path, [('Nov 2015', 'Mariana dam fails\n(19 dead)', RED, 1),
          ('Jan 2019', 'Brumadinho dam fails\n(about 270 dead)', RED, -1),
          ('2019', 'New upstream dams banned;\nold ones to close by\nAug 2021', ORANGE, 1),
          ('Feb 2021', 'Vale settles for\nabout US$7 bn', MUTED, -1),
          ('Later', 'Deadlines extended up\nto 4 years', ORANGE, 1),
          ('2035', 'Vale: full closure of its\nupstream dams not before', RED, -1)])


if __name__ == '__main__':
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    amazon(os.path.join(out, '1_1_amazon.png'))
    cape_town(os.path.join(out, '1_1_cape_town.png'))
    nigeria(os.path.join(out, '1_1_nigeria.png'))
    for name, fn in (('sri_lanka', sri_lanka), ('lithium', lithium), ('indonesia_fires', indonesia_fires),
                     ('senegal', senegal), ('bangladesh', bangladesh), ('vietnam_solar', vietnam_solar),
                     ('laos', laos), ('mekong', mekong), ('central_asia', central_asia), ('indus', indus),
                     ('oyu_tolgoi', oyu_tolgoi), ('guyana_nigeria', guyana_nigeria), ('nickel', nickel),
                     ('brumadinho', brumadinho)):
        fn(os.path.join(out, f'1_1_{name}.png'))
    print('ok')
