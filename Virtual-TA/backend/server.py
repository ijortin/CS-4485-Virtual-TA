# Import flask and datetime module for showing date and time
from flask import Flask, request
import datetime
  

  
# Initializing flask app
app = Flask(__name__)
  
  
# Route for seeing a data
@app.route('/predict',methods = ['POST'])
def received():
   if request.method == 'POST':
        print("message received")
        return "test"
    # Returning an api for showing in  reactjs
    

def get():
    x = datetime.datetime.now()
    print('here')
    # Returning an api for showing in  reactjs
    return x
@app.route('/data')
def get_time():
    return {
        'Message': get()
        }
  
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)