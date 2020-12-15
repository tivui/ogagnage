from app import app

if "__main__" == __name__:
    app.config["ENV"] = 'dev'
    app.run(debug=True)