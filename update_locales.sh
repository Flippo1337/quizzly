#!/bin/sh

# detect all strings to transalte
xgettext -L Python Playground_locale.py -o base.po --from-code=utf-8

# replace CHARSET with UTF-8
sed -i 's/charset=CHARSET/charset=UTF-8/g' base.po

# merge into exiting translation files
msgcat --use-first base.po ./locales/de/LC_MESSAGES/base.po -o ./locales/de/LC_MESSAGES/base.po
msgcat --use-first base.po ./locales/en/LC_MESSAGES/base.po -o ./locales/en/LC_MESSAGES/base.po

# compile translation files
msgfmt ./locales/de/LC_MESSAGES/base.po -o ./locales/de/LC_MESSAGES/base.mo
msgfmt ./locales/en/LC_MESSAGES/base.po -o ./locales/en/LC_MESSAGES/base.mo
