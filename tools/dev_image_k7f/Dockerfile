FROM ghcr.io/inti-cmnb/kicad_auto_test:ki7
MAINTAINER Salvador E. Tropea <stropea@inti.gob.ar>
LABEL Description="KiCad 6 with KiBot and other automation scripts"

RUN     dpkg --remove kicost kibot && \
	apt-get update && \
	curl https://codeload.github.com/INTI-CMNB/KiBot/zip/refs/heads/dev --output pp.zip && \
	unzip pp.zip && \
	pip3 install --no-compile KiBot-dev/ && \
	rm -rf KiBot-dev pp.zip && \
	curl https://codeload.github.com/hildogjr/KiCost/zip/refs/heads/master --output pp.zip && \
	unzip pp.zip && \
	pip3 install KiCost-master/ && \
	rm -rf KiCost-master pp.zip && \
	rm -rf /var/lib/apt/lists/*

# kidiff depends on KiAuto
# 	dpkg --remove kiauto && \
# 	curl https://codeload.github.com/INTI-CMNB/KiAuto/zip/refs/heads/master --output pp.zip && \
# 	unzip pp.zip && \
# 	pip3 install KiAuto-master/ && \
# 	rm -rf KiAuto-master/ pp.zip && \
