
RULES = $(wildcard *.rules)
UDEV_LIB_DIR = usr/lib/udev

install:
	mkdir -p $(DESTDIR)/$(UDEV_LIB_DIR)/rules.d
	install -m 0644 $(RULES) $(DESTDIR)/$(UDEV_LIB_DIR)/rules.d
