# xgettext -L Python Playground_locale.py -o base.po --from-code=utf-8
# sed -i 's/charset=CHARSET/charset=UTF-8/g' base.po
# msgfmt ./locales/de/LC_MESSAGES/base.po -o ./locales/de/LC_MESSAGES/base.mo
# msgfmt ./locales/en/LC_MESSAGES/base.po -o ./locales/en/LC_MESSAGES/base.mo

# msgcat --use-first base.po ./locales/de/LC_MESSAGES/base.po -o ./locales/de/LC_MESSAGES/base.po

# _ = gettext.gettext
import gettext

# gettext.install('myapplication')

el = gettext.translation('base', localedir='locales', languages=['de'])
_ = el.gettext
# or to do it in very package el.install()


if __name__ == '__main__':
    a = 4
    print(_(f"duda {a} world"))
    print(_("whats up"))

    #render qr code
    import io
    import qrcode
    img = qrcode.make('http://google.de')

    png = io.BytesIO()
    img.save(png, 'png')