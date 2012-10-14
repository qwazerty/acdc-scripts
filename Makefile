check_presence:
		./script/check_presence.py

check_archive: clean
		./script/check_archive.py

clean:
		rm -rf unzip/

cleanall: clean
		rm -rf rendu/*
