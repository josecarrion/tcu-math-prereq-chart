# Prerequisite chart

[`prereq-chart.pdf`](https://github.com/josecarrion/tcu-math-prereq-chart/releases/latest/download/prereq-chart.pdf) is the TCU Mathematics prerequisite chart for the 2026-27 undergraduate catalog. It is vector, and each course box links to its catalog page.

## Changing the chart

Edit `prereq-graph.gv` and open a pull request. GitHub builds the chart for the pull request and puts the PDF on the build's summary page. Merging publishes it at the link above.

## Building locally

Run `./build.sh`. It needs Graphviz, poppler (`pdfinfo`, `pdftoppm`), Python 3, and pdflatex with the `standalone` package. On WSL, use the WSL Graphviz, not the Windows `dot.exe`; if there is no Linux pdflatex, `build.sh` uses the Windows TeX Live. Intermediate files go in `build/`.

The font is DejaVu Sans. GitHub builds with Graphviz 2.42.2 (Ubuntu 24.04). Other versions may lay out the arrows differently.

Without Python: `dot -Tpdf prereq-graph.gv -o chart.pdf` gives the chart without the legend, links included. For the legend but no links, run `dot -Tpdf` on both `.gv` files with the output in `build/`, then `pdflatex prereq-chart.tex`.

## Files

- `prereq-graph.gv`: the course graph. Edit prerequisites here. The comments at the top say what is left off on purpose and how to restore the colors.
- `prereq-legend.gv`: the legend.
- `prereq-chart.tex`: puts the graph, the legend, and the links together.
- `make-links.py`: pdflatex drops the links of an included PDF, so this script recreates them from the dot layout.
- `place-legend.py`: puts the legend in the bottom-left corner if it is blank, else in the first blank spot down the left edge.
- `check-links.py`: checks that each catalog link loads and names the right course. Run it after each Coursedog catalog update, which tends to change the page IDs. GitHub also runs it on the 1st of each month.
- `.github/workflows/`: the GitHub build and the monthly link check.
- `Archive/prereq-chart-colors-snapshot.pdf`: the colored version, not rebuilt.
