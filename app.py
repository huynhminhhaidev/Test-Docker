from website import create_app

app = create_app()

@app.route('/home')
def home():
    return 'Living like dead!'


if __name__ == "__main__":
    app.run(debug=True, port=9999)