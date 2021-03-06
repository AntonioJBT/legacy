##!/usr/bin/env python
##coding=utf-8

from svgutils.compose import *
import cairosvg

Figure("16cm", "6.5cm",
        Panel(
              SVG("sigmoid_fit.svg"),
              Text("A", 25, 20, size=12, weight='bold')
             ),
        Panel(
              SVG("anscombe.svg").scale(0.5),
              Text("B", 25, 20, size=12, weight='bold')
             ).move(280, 0)
        ).save("fig_final_compose.svg")

# Convert SVG file to PDF:
cairosvg.svg2pdf(url='fig_final_compose.svg', write_to='fig_final_compose.pdf')
