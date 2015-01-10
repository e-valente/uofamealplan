 # We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for
from datetime import date
from datetime import datetime


# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def main():
    mymsg = "Oi! :))"
    return mymsg

@app.route('/mp')
def form():
    return render_template('form_submit.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is
# accepting: POST requests in this case
@app.route('/mp-result/', methods=['POST'])
def hello():
    mealplan=request.form['mealplan']
    catcash=request.form['catcash']
    mydate=request.form['mydate']
    trip_days = request.form['trip_select_days']

    '''
    if(mealplan.isnumeric() == False or \
      catcash.isnumeric() == False):
      return render_template('form_submit.html')
    '''

    try:
      mealplan = float(mealplan)
      catcash = float(catcash)
    except:
      return render_template('form_submit.html')



    '''
    if(len(mealplan) == 0 and len(catcash) == 0):
      return render_template('form_submit.html')

    if(len(mealplan) == 0):
      return render_template('form_submit.html')
    '''
    trip_days = int(trip_days)
    #date handling

    mydatelist = mydate.split('-')
    mydate = date(int(mydatelist[0]), int(mydatelist[1]), int(mydatelist[2]))
    now = datetime.now()
    delta = mydate - now.date()
    mydays = abs(delta.days)


    #update days by trip

    '''
    if(len(mealplan) > 0 and len(catcash) == 0):
      mealplan = float(mealplan)
      catcash = 0.0
    else:
      mealplan = float(mealplan)
      catcash = float(catcash)
    '''

    total_per_day = (mealplan + catcash) / (mydays - trip_days)
    total_per_day = "{0:.2f}".format(total_per_day)

    #boulevard
    total_days_boulevard = catcash / 24.0
    total_days_boulevard = "{0:.2f}".format(total_days_boulevard)

    total_days_uofa = mealplan / 24.0
    total_days_uofa = "{0:.2f}".format(total_days_uofa)

    ideal_balance = 24.0 * (mydays - trip_days)
    mybalance =  (mealplan + catcash) - ideal_balance
    mybalance = "{0:.2f}".format(mybalance)



    #return render_template('form_action.html', total=total, mealplan=mealplan, catcash=catcash, mydays=mydays)
    return render_template('form_action.html', total_per_day=total_per_day, total_days_boulevard=total_days_boulevard,\
      total_days_uofa = total_days_uofa, mybalance = mybalance, total_days_left=mydays, trip_days=trip_days)
# Run the app :)
if __name__ == '__main__':
  app.run(
        host="0.0.0.0",
        port=int("80"),
        debug=True
  )
