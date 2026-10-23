#!/usr/bin/env bash
# Builds prereq-chart.pdf; intermediate files go in build/.
# Needs Graphviz, poppler, python3, and pdflatex. On WSL with no Linux pdflatex,
# it uses the Windows TeX Live.
set -e
cd "$(dirname "$0")"
PDFLATEX=$(command -v pdflatex || echo /mnt/c/texlive/2025/bin/windows/pdflatex.exe)
mkdir -p build
dot -Tpdf  prereq-graph.gv  -o build/prereq-graph.pdf
dot -Tjson prereq-graph.gv  -o build/prereq-graph.json
dot -Tpdf  prereq-legend.gv -o build/prereq-legend.pdf
python3 -I make-links.py build/prereq-graph.json build/prereq-graph.pdf build/prereq-links.tex
python3 -I place-legend.py build/prereq-graph.pdf build/prereq-legend.pdf build/prereq-legend-pos.tex
if ! "$PDFLATEX" -interaction=nonstopmode -output-directory=build prereq-chart.tex > /dev/null; then
  grep -A3 '^!' build/prereq-chart.log
  exit 1
fi
cp build/prereq-chart.pdf .
echo "built prereq-chart.pdf"
