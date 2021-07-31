# I used the cli to extract the parameters for extract_messages (e.g. for keywords)
# But we could als ouse the cli method directly
# from babel.messages.frontend import CommandLineInterface
# argv = ['/opt/project/quiz_app/update_translations.py', 'extract', '-F', 'babel.cfg', '-k', 'lazy_gettext', '-o', 'messages.pot', '.']
# CommandLineInterface().run(argv)

# extract all messages
from babel.messages.frontend import extract_messages
msg = extract_messages()
msg.mapping_file = "babel.cfg"
msg.output_file = 'messages.pot'
msg.input_paths = ['.']
msg.keywords = {'_': None, 'gettext': None, 'ngettext': (1, 2), 'ugettext': None, 'ungettext': (1, 2), 'dgettext': (2,), 'dngettext': (2, 3), 'N_': None, 'pgettext': ((1, 'c'), 2), 'npgettext': ((1, 'c'), 2, 3), 'lazy_gettext': None}
msg.add_comments = []
msg.run()

# merge messages into translations
from babel.messages.frontend import update_catalog
update = update_catalog()
update.input_file = 'messages.pot'
update.output_dir = 'translations'
update.run()
# pybabel update -i messages.pot -d translations

#TODO: delete messages.pot when done