# Prerequisite chart

`prereq-chart.pdf` is the prerequisite chart for the 2026-27 undergraduate catalog. It is vector, and each course box links to its catalog page.

## Build

Run `./build.sh` from WSL. Graphviz is the WSL one (it has DejaVu Sans, the chart's font), not the Windows `dot.exe`. It also needs poppler (`pdfinfo`, `pdftoppm`) and the Windows TeX Live `pdflatex`, whose path is at the top of `build.sh`. Intermediate files go in `build/`.

## Files

- `prereq-graph.gv`: the course graph. Edit prerequisites here. The comments at the top say what is left off on purpose and how to restore the colors.
- `prereq-legend.gv`: the legend.
- `prereq-chart.tex`: puts the graph, the legend, and the links together.
- `make-links.py`: pdflatex drops the links of an included PDF, so this script recreates them from the dot layout.
- `place-legend.py`: puts the legend in the bottom-left corner if it is blank, else in the first blank spot down the left edge.
- `check-links.py`: checks that each catalog link loads and names the right course. Run it after each Coursedog catalog update, which tends to change the page IDs. Needs network; not part of the build.
- `Archive/prereq-chart-colors-snapshot.pdf`: the colored version, not rebuilt.
- `Archive/2021 originals/`: the 2021 chart, not in git. Its legend was added in Photoshop as a 300 ppi raster.
