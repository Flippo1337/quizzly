from quiz_app import create_app

app, db = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
