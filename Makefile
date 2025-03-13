# Makefile to run the Python main.py script

.PHONY: run

# Default target
run:
	cd src && python3 main.py
