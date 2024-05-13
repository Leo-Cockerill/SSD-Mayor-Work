from myproject import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) #This will run the app in debug mode. Debug mode allows us to see the changes we make to the app in real time.

