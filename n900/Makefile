
RULES = $(wildcard *.rules)

install:
	mkdir -p $(DESTDIR)/lib/udev/rules.d
	install -m 0644 $(RULES) $(DESTDIR)/lib/udev/rules.d
