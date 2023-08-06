#!/usr/bin/env python
# Enumerate available xkb layouts
import lxml.etree
repository = "/usr/share/X11/xkb/rules/base.xml"
with open(repository) as f:
    tree = lxml.etree.parse(f)
layouts = tree.xpath("//layout")
for layout in layouts:
    layoutName = layout.xpath("./configItem/name")[0].text
    print(layoutName)
    for variant in layout.xpath("./variantList/variant/configItem/name"):
        variantName = variant.text
        print(layoutName, variantName)

