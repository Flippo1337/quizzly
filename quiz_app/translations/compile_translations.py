from babel.messages.frontend import compile_catalog
compiler = compile_catalog()
compiler.domain = ['messages']
compiler.directory = './'
compiler.run()