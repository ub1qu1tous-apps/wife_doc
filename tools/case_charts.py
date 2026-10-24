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
        ax.text(0.5, 0.62, big, ha='center', va='center', fontsize=17 if len(big) <= 7 else 13.5, color=c, weight='bold', transform=ax.transAxes)
        ax.text(0.5, 0.3, small_, ha='center', va='center', fontsize=7.9, color=INK, transform=ax.transAxes)
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


# ---------- Topic 1.2 (doc 3b) ----------
def hbars(path, labels, vals, colours, fmt, xlabel, xmax, note=None):
    fig, ax = plt.subplots(figsize=SIZE)
    y = list(range(len(vals)))[::-1]
    ax.barh(y, vals, color=colours, height=0.62)
    for yi, v in zip(y, vals):
        ax.text(v + xmax * 0.01, yi, fmt(v), va='center', fontsize=8, color=INK)
    ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=8.5)
    ax.set_xlim(0, xmax); ax.set_xlabel(xlabel)
    for s_ in ('top', 'right'):
        ax.spines[s_].set_visible(False)
    ax.xaxis.grid(True, color=GRID, lw=0.8); ax.set_axisbelow(True)
    if note:
        ax.set_title(note, fontsize=8.5, color=MUTED, loc='left')
    save(fig, path)


def sea_hdi(path):
    names = ['Singapore', 'Brunei', 'Malaysia', 'Thailand', 'Vietnam', 'Indonesia', 'Philippines', 'Laos', 'Myanmar', 'Cambodia']
    v = [0.949, 0.823, 0.807, 0.803, 0.726, 0.713, 0.710, 0.620, 0.608, 0.600]
    cols = [GREEN if x >= 0.8 else (BLUE if x >= 0.7 else ORANGE) for x in v]
    hbars(path, names, v, cols, lambda x: f"{x:.3f}", 'Human Development Index, 2022 (UNDP)', 1.08,
          note='green = very high, blue = high, orange = medium')


def vietnam_flows(path):
    fig, (a1, a2) = plt.subplots(1, 2, figsize=SIZE)
    bars(a1, ['2010', '2023'], [14, 5.7], [MUTED, GREEN], lambda v: f"{v:g}%", title='Poverty rate (national line)', ymax=17)
    a2.bar(['Exports'], [72], color=BLUE, width=0.9); a2.bar(['Exports'], [28], bottom=[72], color=MUTED, width=0.9)
    a2.text(0, 36, 'Foreign-invested\nfirms ~72%', ha='center', va='center', color='white', fontsize=8.5)
    a2.text(0, 86, 'Vietnamese\nfirms ~28%', ha='center', va='center', color='white', fontsize=8.5)
    a2.set_ylim(0, 100); a2.set_xlim(-0.6, 0.6); a2.set_title("Who makes Vietnam's exports", fontsize=9, loc='left')
    tidy(a2)
    save(fig, path)


def philippines(path):
    hbars(path, ['United States', 'Singapore', 'Saudi Arabia', 'All other countries'], [40.6, 7.2, 6.4, 45.8],
          [BLUE, ORANGE, ORANGE, MUTED], lambda v: f"{v:g}%", 'Share of cash remittances, 2024 (%)', 55,
          note='Total 2024: US$38.34 bn = 8.3% of GDP')


def ethiopia(path):
    fig, (a1, a2) = plt.subplots(1, 2, figsize=SIZE)
    bars(a1, ['Planned', 'Nov 2023'], [60000, 28000], [MUTED, ORANGE], lambda v: f"{v:,}", title='Hawassa park jobs', ymax=72000)
    bars(a2, ['Hawassa', 'Mekelle', 'Bole Lemi', 'Other'], [4321, 2885, 1097, 3197], [RED, RED, RED, MUTED],
         lambda v: f"{v:,}", title='Jobs lost after AGOA suspension', ymax=5200)
    save(fig, path)


def china_services(path):
    fig, (a1, a2) = plt.subplots(1, 2, figsize=SIZE)
    bars(a1, ['A decade ago', 'Now'], [44, 53], [MUTED, BLUE], lambda v: f"{v:g}%", title='China: services share of activity', ymax=62)
    bars(a2, ['2010', '2015'], [3, 8], [MUTED, ORANGE], lambda v: f"{v:g}%", title='Bangladesh + Vietnam: share of world\nclothing, footwear, furniture exports', ymax=10)
    save(fig, path)


def chip_shortage(path):
    fig, (a1, a2) = plt.subplots(1, 2, figsize=SIZE)
    bars(a1, ['May 2021\nforecast', 'Sep 2021\nforecast'], [110, 210], [MUTED, RED], lambda v: f"US${v}bn", title='Car industry revenue lost, 2021', ymax=250)
    bars(a2, ['May 2021\nforecast', 'Sep 2021\nforecast'], [3.9, 7.7], [MUTED, RED], lambda v: f"{v}m", title='Vehicles not built, 2021', ymax=9.2)
    a2.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}"))
    save(fig, path)


def apple_india(path):
    fig, ax = plt.subplots(figsize=SIZE)
    bars(ax, ['2024', '2025'], [36, 55], [MUTED, ORANGE], lambda v: f"{v}m iPhones", ylabel='iPhones assembled in India (m)', ymax=66)
    ax.text(0.5, 61, 'About 1 in 4 iPhones made in India in 2025 (Bloomberg); China still the largest', ha='center', fontsize=8.5, color=ORANGE)
    save(fig, path)


def bd_garments(path):
    fig, (a1, a2) = plt.subplots(1, 2, figsize=SIZE)
    bars(a1, ['Workers\nasked', 'Govt\nset'], [20390, 12500], [MUTED, RED], lambda v: f"Tk {v:,}", title='Monthly minimum wage, 2023', ymax=24000)
    bars(a2, ['Buriganga', 'Turag'], [166, 58], [RED, ORANGE], lambda v: f"{v}", title='Pollution outlets into Dhaka rivers', ymax=195)
    save(fig, path)


def dyson(path):
    even_timeline(path, [
        ('2002', 'Manufacturing moves\nfrom Malmesbury\nto Malaysia', ORANGE, 1),
        ('2013', 'Singapore plant\nfor digital motors', ORANGE, -1),
        ('2019', 'Head office moves\nto Singapore', ORANGE, 1),
        ('2024', '1,000 UK jobs cut\n(over a quarter of\n3,500 UK staff)', RED, -1),
        ('Today', 'Malmesbury stays the\nR&D base and Dyson\nInstitute', GREEN, 1)])


def tiktok(path):
    tiles(path, [('20', 'Indian soldiers killed\nin border clash with\nChina, 15 Jun 2020', RED),
                 ('59', 'Chinese apps banned\n29 Jun 2020,\nincl. TikTok', ORANGE),
                 ('47', 'clone apps banned\na month later', ORANGE),
                 ('~267', 'Chinese apps\nbanned in total', MUTED)])


def ireland(path):
    fig, ax = plt.subplots(figsize=SIZE)
    parts = [('Top 3 groups', 46, RED), ('Next 7 groups', 14, ORANGE), ('All other firms', 40, MUTED)]
    left = 0
    for name, v, c in parts:
        ax.barh([0], [v], left=left, color=c, height=0.5)
        ax.text(left + v / 2, 0, f"{name}\n{v}%", ha='center', va='center', color='white', fontsize=9)
        left += v
    ax.set_xlim(0, 100); ax.set_ylim(-0.6, 0.9); ax.set_yticks([])
    ax.set_xlabel("Share of Ireland's corporation tax, 2024 (%)")
    ax.text(50, 0.55, 'A few TNCs pay most of the tax: top 3 groups 46%, top 10 almost 60% (2024)',
            ha='center', fontsize=8.5, color=INK)
    for s_ in ('top', 'right', 'left'):
        ax.spines[s_].set_visible(False)
    save(fig, path)


def tsmc_arizona(path):
    even_timeline(path, [
        ('2022', 'Investment raised\nto US$40 bn\nfor two fabs', BLUE, 1),
        ('Jul 2023', 'Start delayed to 2025:\ntoo few skilled\ninstallers', RED, -1),
        ('2023', '~500 experienced\nTaiwanese staff\nsent to help', ORANGE, 1),
        ('Apr 2024', 'Trial production\n(4 nm chips)', GREEN, -1),
        ('Jan 2025', 'Volume production;\nyields match Taiwan', GREEN, 1)])


def uaw(path):
    fig, (a1, a2) = plt.subplots(1, 2, figsize=SIZE)
    bars(a1, ['Base raise', 'With cost-of-\nliving pay'], [25, 33], [BLUE, GREEN], lambda v: f"{v}%", title='Pay rise won (top workers, to 2028)', ymax=40)
    bars(a2, ['Rehired', 'New battery\nplant'], [1200, 1000], [GREEN, GREEN], lambda v: f"{v:,}", title='Belvidere jobs (plant was to close)', ymax=1450)
    save(fig, path)


def amazon_union(path):
    import numpy as np
    fig, ax = plt.subplots(figsize=SIZE)
    x = np.arange(2)
    no, yes = [1798, 993], [738, 875]
    ax.bar(x - 0.18, no, 0.34, color=MUTED, label='Against union')
    ax.bar(x + 0.18, yes, 0.34, color=BLUE, label='For union')
    for xi, a, b in zip(x, no, yes):
        ax.text(xi - 0.18, a + 30, f"{a:,}", ha='center', fontsize=8.5)
        ax.text(xi + 0.18, b + 30, f"{b:,}", ha='center', fontsize=8.5)
    ax.set_xticks(x); ax.set_xticklabels(['Apr 2021 vote', '2022 re-run\n(416 ballots challenged)'])
    ax.set_ylim(0, 2100); ax.set_ylabel('Votes, Bessemer warehouse'); ax.legend(frameon=False, fontsize=8)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:,.0f}"))
    tidy(ax); save(fig, path)


def platform_workers(path):
    tiles(path, [('70,000+', 'delivery riders and\nride-hail drivers\ncovered', BLUE),
                 ('1 Jan 2025', 'Platform Workers\nAct in force', GREEN),
                 ('CPF', 'compulsory for\nworkers born 1995\nor later', ORANGE),
                 ('Injury', 'cover at the same\nlevel as employees,\nwhile on a job', MUTED)])


def rcep(path):
    tiles(path, [('15', 'countries: 10 ASEAN\n+ China, Japan, Korea,\nAustralia, NZ', BLUE),
                 ('2.2 bn', 'people, 30% of\nthe world', ORANGE),
                 ('US$38 tn', 'combined GDP,\nabout 1/3 of\nthe world', GREEN),
                 ('~92%', 'of goods traded\nbetween members\nto be tariff-free', MUTED)])


def wto_nickel(path):
    even_timeline(path, [
        ('Dec 2019', 'WTO Appellate Body\nstops working\n(too few members)', MUTED, 1),
        ('Jan 2020', 'Indonesia bans\nnickel ore exports', ORANGE, -1),
        ('30 Nov 2022', 'WTO panel: ban breaks\ntrade rules; EU wins\nall claims', BLUE, 1),
        ('Dec 2022', "Indonesia appeals\n'into the void'", RED, -1),
        ('After', 'Ban stays; EU\nexplores counter-\nmeasures', RED, 1)])


def doing_business(path):
    years = ['2014', '2015', '2016', '2017', '2018', '2019']
    rank = [142, 131, 130, 100, 77, 63]
    fig, ax = plt.subplots(figsize=SIZE)
    ax.plot(years, rank, color=BLUE, marker='o', lw=2)
    for x, r in zip(years, rank):
        ax.text(x, r - 6, str(r), ha='center', va='bottom', fontsize=8.5, color=INK)
    ax.invert_yaxis(); ax.set_ylim(155, 40)
    ax.axhline(50, color=GREEN, ls='--', lw=1); ax.text(0, 47, "Government target: top 50", color=GREEN, fontsize=8)
    ax.set_ylabel("India's Doing Business rank\n(1 = best, of 190)")
    tidy(ax); save(fig, path)



# ---------- Topic 2.1 (doc 3c) ----------
def climate_zones(path):
    fig, ax = plt.subplots(figsize=SIZE)
    names = ['Singapore (Af)\nhumid tropics', 'Niamey, Niger (BSh)\nsemi-arid', 'Riyadh (BWh)\ndesert']
    mid, lo, hi = [2166, 575, 112], [2166, 550, 100], [2166, 600, 125]
    ax.bar(names, mid, color=[GREEN, ORANGE, RED], width=0.55)
    ax.errorbar([1, 2], mid[1:], yerr=[[mid[1]-lo[1], mid[2]-lo[2]], [hi[1]-mid[1], hi[2]-mid[2]]], fmt='none', ecolor=INK, capsize=4)
    for i, (v, t) in enumerate(zip(mid, ['~2,166 mm', '~550–600 mm', '~100–125 mm'])):
        ax.text(i, v + 95, t, ha='center', fontsize=8.5)
    ax.set_ylabel('Average annual rainfall (mm)'); ax.set_ylim(0, 2550)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:,.0f}"))
    tidy(ax); save(fig, path)


def sahel_2020(path):
    tiles(path, [('2.7 m', 'people hit by floods\nin 18 countries,\nWest & Central Africa', RED),
                 ('Record', 'Niger River level\nat Niamey,\nall-time high', BLUE),
                 ('226,000', 'displaced in Niger;\nat least 45 dead', ORANGE),
                 ('ITCZ', 'surged north of its\nusual August\nposition', MUTED)])


def india_monsoon(path):
    fig, ax = plt.subplots(figsize=SIZE)
    bars(ax, ['Normal August', 'August 2023'], [254.9, 162.7], [MUTED, RED], lambda v: f"{v:g} mm",
         ylabel='All-India rainfall (mm)', ymax=300)
    ax.text(0.5, 280, 'About 36% below normal: driest August since 1901 (IMD)', ha='center', fontsize=8.5, color=RED)
    save(fig, path)


def freddy(path):
    tiles(path, [('31+ days', 'beat (or matched)\nthe old 31-day\nlifespan record', BLUE),
                 ('ACE 86', 'estimated cyclone\nenergy: just above\nthe old record (85)', ORANGE),
                 ('200+', 'deaths in Malawi\nand Mozambique\n(mostly Malawi)', RED),
                 ('85', 'deaths in Blantyre\nalone, from floods\nand mudslides', MUTED)])


def lismore(path):
    fig, ax = plt.subplots(figsize=SIZE)
    bars(ax, ['Town levee', 'Old record\n(Feb 1954)', 'Feb 2022 peak'], [10, 12.27, 14.4], [MUTED, ORANGE, RED],
         lambda v: f"{v:g} m", ylabel='Wilsons River at Lismore (m)', ymax=17)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}"))
    save(fig, path)


def rio_negro(path):
    fig, ax = plt.subplots(figsize=SIZE)
    bars(ax, ['June 2021\n(record high)', 'October 2023\n(record low)'], [30.02, 12.70], [BLUE, ORANGE],
         lambda v: f"{v:.2f} m", ylabel='Rio Negro at Manaus port (m)', ymax=35)
    ax.text(0.5, 33, 'A 17 m swing in just over two years', ha='center', fontsize=8.5, color=INK)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}"))
    save(fig, path)


def jakarta_storage(path):
    tiles(path, [('40%', 'of Jakarta not on\npiped water: relies\non groundwater', BLUE),
                 ('1–15 cm', 'sinking per year\non average', ORANGE),
                 ('25 cm', 'per year in parts\nof North Jakarta', RED),
                 ('~50%', 'of the city now\nbelow sea level', MUTED)])


def chennai(path):
    tiles(path, [('1,324 mm', 'average yearly rain;\n60% falls in the\nOct–Dec monsoon', BLUE),
                 ('289', 'deaths in two worst-\nhit districts\n(CAG audit)', RED),
                 ('300+', 'water bodies lost\nto building', ORANGE),
                 ('1.4 lakh', '(140,000) illegal\nstructures counted\nby the CMDA', MUTED)])


def kerala(path):
    fig, ax = plt.subplots(figsize=SIZE)
    bars(ax, ['Average,\n1 Jun–19 Aug', '2018,\n1 Jun–19 Aug'], [1676.3, 2378.71], [MUTED, RED], lambda v: f"{v:,.0f} mm",
         ylabel='Kerala rainfall (mm)', ymax=2950)
    ax.text(0.5, 2790, 'About 42% above normal; 8–19 August alone was 362% above normal', ha='center', fontsize=8.5, color=RED)
    save(fig, path)


def pakistan(path):
    fig, ax = plt.subplots(figsize=SIZE)
    bars(ax, ['Men', 'Women', 'Children'], [601, 273, 481], [MUTED, ORANGE, RED], lambda v: f"{v}",
         ylabel='Deaths (NDMA, early Sep 2022)', ymax=720)
    ax.text(1, 680, 'Final toll: 1,739 deaths; 33 million people affected', ha='center', fontsize=8.5, color=INK)
    save(fig, path)


def smart_tunnel(path):
    fig, ax = plt.subplots(figsize=SIZE)
    bars(ax, ['Design capacity\n(one diversion)', 'Sep 2020\nflash flood', 'Dec 2021\nstorm'], [3, 3, 5], [MUTED, BLUE, ORANGE],
         lambda v: f"{v:g} million m³", ylabel='Floodwater diverted (million m³)', ymax=6.2)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}"))
    save(fig, path)


def jakarta_flood(path):
    fig, (a1, a2) = plt.subplots(1, 2, figsize=SIZE)
    bars(a1, ['Planned', 'Done by 2026'], [33.69, 17.14], [MUTED, ORANGE], lambda v: f"{v:g} km", title='Ciliwung river works', ymax=40)
    bars(a2, ['Rain, 1 Jan 2020\n(Halim)'], [377], [RED], lambda v: f"{v} mm", title='One day of rain', ymax=440)
    a2.set_xlim(-1, 1)
    save(fig, path)



# ---------- Topic 2.2 (doc 3d) ----------
def angkor(path):
    tiles(path, [('Wet–dry', 'cycles swell and\nshrink clay in the\nsandstone', BLUE),
                 ('Salt', 'crystals (gypsum,\ncalcite) grow in\npores and flake stone', ORANGE),
                 ('Sun', 'direct heating and\ndrying of exposed\nblocks', RED),
                 ('Microbes', 'cyanobacteria soften\nthe surface, speeding\nweathering', GREEN)])


def petropolis(path):
    tiles(path, [('258 mm', 'of rain in 3 hours,\n15 Feb 2022: more than\nthe previous 30 days', BLUE),
                 ('269+', 'landslides counted\n(Civil Defence;\nother counts 370+)', ORANGE),
                 ('231', 'deaths: the city\'s\ndeadliest landslide\ndisaster', RED),
                 ('1,021', 'of 1,700 buildings in\nthe study area sit on\n20–45° slopes', MUTED)])


def mekong_sand(path):
    tiles(path, [('114 Mt', 'of sand licensed\nfor mining in five\nprovinces in a decade', ORANGE),
                 ('600+ ha', 'of river bank and\ncoast lost to erosion\neach year', RED),
                 ('1,808', 'houses fell into\nrivers or the sea,\n2018–2020', MUTED),
                 ('Dams', 'upstream trap the\nsediment that would\nrebuild banks', BLUE)])


def halong(path):
    tiles(path, [('1,133', 'limestone islands\nand islets in\nHa Long Bay', BLUE),
                 ('360+', 'more islands in the\nCat Ba archipelago\n(added 2023)', GREEN),
                 ('Tower', "karst invaded by the\nsea: 'fengcong' and\n'fenglin' forms", ORANGE),
                 ('Dolines', 'drowned as lakes,\nsome of them\ntidal', MUTED)])


def son_doong(path):
    tiles(path, [('38.4 m m³', 'volume of the largest\nknown cave passage', BLUE),
                 ('2–5 m yrs', 'age of the cave;\nthe limestone is far\nolder (Carboniferous)', ORANGE),
                 ('2', 'collapsed dolines\nlet in light and\ngrow jungle', GREEN),
                 ('500–800', 'visitor permits a\nyear, about\nUS$3,000 each', MUTED)])


def perak_snails(path):
    fig, ax = plt.subplots(figsize=SIZE)
    bars(ax, ['Land snail species\nfound', 'Found on only\none hill', 'Possibly new\nto science'], [122, 34, 30],
         [BLUE, ORANGE, RED], lambda v: f"{v}", ylabel='Species (Perak survey, 2016)', ymax=145)
    save(fig, path)


def majuli(path):
    fig, ax = plt.subplots(figsize=SIZE)
    bars(ax, ['1971', '2016'], [1256, 524.29], [MUTED, RED], lambda v: f"{v:,.0f} km²", ylabel='Area of Majuli island (km²)', ymax=1600)
    ax.text(0.5, 1500, 'Lost more than half its area; 67 villages eroded away (Dialogue Earth)', ha='center', fontsize=8.5, color=RED)
    save(fig, path)


def mekong_delta(path):
    tiles(path, [('50%+', 'of the 600+ km delta\nshoreline now\neroding', RED),
                 ('37–54%', 'less sediment reaching\nthe coast (2000–22 vs\n1988–99)', ORANGE),
                 ('15%', 'maximum yearly\nmangrove loss to\nerosion', GREEN),
                 ('1990s', 'when sediment supply\nfell sharply (dams,\nsand mining)', MUTED)])


def sundarbans(path):
    tiles(path, [('2.5 m', 'people depend on\nthe forest for\ntheir livelihoods', GREEN),
                 ('Shield', 'cut storm surge and\nwind in Cyclone\nAmphan (2020)', BLUE),
                 ('Rampal', 'coal plant built just\nnorth of the forest', RED),
                 ('UNESCO', 'and IUCN urged the\nplant be moved', MUTED)])



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
    for name, fn in (('sea_hdi', sea_hdi), ('vietnam_flows', vietnam_flows), ('philippines', philippines),
                     ('ethiopia', ethiopia), ('china_services', china_services), ('chip_shortage', chip_shortage),
                     ('apple_india', apple_india), ('bd_garments', bd_garments), ('dyson', dyson), ('tiktok', tiktok),
                     ('ireland', ireland), ('tsmc_arizona', tsmc_arizona), ('uaw', uaw), ('amazon_union', amazon_union),
                     ('platform_workers', platform_workers), ('rcep', rcep), ('wto_nickel', wto_nickel),
                     ('doing_business', doing_business)):
        fn(os.path.join(out, f'1_2_{name}.png'))
    for name, fn in (('climate_zones', climate_zones), ('sahel_2020', sahel_2020), ('india_monsoon', india_monsoon),
                     ('freddy', freddy), ('lismore', lismore), ('rio_negro', rio_negro), ('jakarta_storage', jakarta_storage),
                     ('chennai', chennai), ('kerala', kerala), ('pakistan', pakistan), ('smart_tunnel', smart_tunnel),
                     ('jakarta_flood', jakarta_flood)):
        fn(os.path.join(out, f'2_1_{name}.png'))
    for name, fn in (('angkor', angkor), ('petropolis', petropolis), ('mekong_sand', mekong_sand), ('halong', halong),
                     ('son_doong', son_doong), ('perak_snails', perak_snails), ('majuli', majuli),
                     ('mekong_delta', mekong_delta), ('sundarbans', sundarbans)):
        fn(os.path.join(out, f'2_2_{name}.png'))
    print('ok')
