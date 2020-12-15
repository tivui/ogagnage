from app import app

if "__main__" == __name__:
    app.config["ENV"] = 'prod'
    app.run(debug=True)