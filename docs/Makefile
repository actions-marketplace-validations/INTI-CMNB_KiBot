#!/usr/bin/make

all: ../README.md  samples/generic_plot.kibot.yaml ../kibot/resources/report_templates/report_full_svg.txt ../kibot/resources/config_templates/bom/MacroFab_XYRS.kibot.yaml \
	../kibot/resources/config_templates/gerber/Elecrow.kibot.yaml ../kibot/resources/config_templates/gerber/FusionPCB.kibot.yaml \
	../kibot/resources/config_templates/gerber/JLCPCB.kibot.yaml ../kibot/resources/config_templates/gerber/PCBWay.kibot.yaml ../src/kibot-check

../kibot/resources/config_templates/gerber/%.kibot.yaml: samples/%.kibot.yaml
	cp $< $@

../kibot/resources/config_templates/bom/%.kibot.yaml: samples/%.kibot.yaml
	cp $< $@

../README.md: README.in replace_tags.pl ../kibot/out_*.py ../kibot/pre_*.py ../kibot/var_*.py ../kibot/fil_*.py ../kibot/__main__.py ../kibot/config_reader.py ../kibot/globals.py ../kibot/dep_downloader.py
	cat README.in | perl replace_tags.pl > ../README.md

../src/kibot-check: ../src/kibot-check.in replace_tags.pl ../kibot/out_*.py ../kibot/pre_*.py ../kibot/var_*.py ../kibot/registrable.py ../kibot/misc.py ../kibot/config_reader.py ../kibot/dep_downloader.py
	cat ../src/kibot-check.in | perl replace_tags.pl > ../src/kibot-check

samples/generic_plot.kibot.yaml: ../kibot/out_*.py ../kibot/pre_*.py ../kibot/config_reader.py
	rm -f example_template.kibot.yaml
	../src/kibot -v --example
	mv example_template.kibot.yaml $@

../kibot/resources/report_templates/report_full_svg.txt: ../kibot/resources/report_templates/report_full.txt
	sed -e 's/layer_pdfs/layer_svgs/' $< > $@
