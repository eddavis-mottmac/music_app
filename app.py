#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from email.headerregistry import ParameterizedMIMEHeader
import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import FlaskForm, Form
from forms import *
from flask_migrate import Migrate
import pandas as pd
from forms import *
import logging
import sys
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.debug=True
moment = Moment(app)
app.config.from_object('config')
app.app_context().push()
db = SQLAlchemy(app)
migrate = Migrate(app, db)
logging.basicConfig(level=logging.INFO)

# DONE: connection established to a local MS SSMS database

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Component(db.Model):
    __tablename__ = 'Components'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    component_type = db.Column(db.String(120))
    datasheet_link = db.Column(db.String(500))


#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format, locale='en')

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  return render_template('pages/home.html')


#  Components
#  ----------------------------------------------------------------

@app.route('/components')
def components():
    """
    Renders the 'components.html' template with a list of all Component records
    from the database.

    Returns:
        str: A rendered HTML template containing a table of all Component records.
    """
    components = Component.query.all()
    return render_template('pages/components.html', components=components)

@app.route('/venues/search', methods=['POST'])
def search_venues():

    text = request.form['search_term'].lower()

    source_data=pd.DataFrame.from_records([vars(venue) for venue in Venue.query.all()])

    result = source_data[source_data['name'].str.lower().str.contains(text)]
    


    count=len(result)
    tier1_list={"count": count}
    tier2_list=[]

    for i in range(len(result)):
        temp = result.iloc[i].to_dict()
        tier2_list.append(temp)
    tier1_list.update({"data": tier2_list})
    response=tier1_list
    sql_debug(response)
    #response={
    #"count": 1,
    #"data": [{
    #    "id": 2,
    #    "name": "The Dueling Pianos Bar",
    #    "num_upcoming_shows": 0,
    #}]
    #}
    return render_template('pages/search_venues.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/components/<int:component_id>')
def show_component(component_id):
  # shows the venue page with the given venue_id
  # DONE: replace with real venue data from the venues table, using venue_id

  # source_data=pd.DataFrame.from_records([vars(venue) for venue in Venue.query.filter_by(id=venue_id)])

  component = Component.query.get(component_id)

  print(component)


  return render_template('pages/show_component.html', component=component)

#  Create Venue
#  ----------------------------------------------------------------

@app.route('/components/create', methods=['GET'])
def create_component_form():
  form = ComponentForm()
  return render_template('forms/new_component.html', form=form)

@app.route('/components/create', methods=['POST'])
def create_component_submission():
    form_temp = ComponentForm(request.form)
    if form_temp.validate():
        try:
            name=request.form.get('name')
            component_type=request.form.get('component_type')
            datasheet_link=request.form.get('datasheet_link')
            

            component = Component(name=name, component_type=component_type, datasheet_link=datasheet_link)             
            print(component)
            db.session.add(component)
            db.session.commit()
            flash('Component ' + request.form['name'] + ' was successfully listed!')
        except:
            flash('Component ' + request.form['name'] + ' was not successfully listed!')
            db.session.rollback()
        finally:
            db.session.close()
            return render_template('pages/home.html')
    else:
        flash('Component ' + request.form['name'] + ' was not successfully listed!')
        print("Not successfully submitted")
        print(form_temp.errors)
        return render_template('forms/new_component.html', form=form_temp) 



@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
  # DONE: Complete this endpoint for taking a venue_id, and using
  # SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.

  # BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
  # clicking that button delete it from the db then redirect the user to the homepage
  try:
    venue = Venue.query.get(venue_id)
    db.session.delete(venue)
    db.session.commit()
  except:
    db.session.rollback()
    print(sys.exc_info())
  finally:
    db.session.close()
  return None

#  Artists
#  ----------------------------------------------------------------
@app.route('/artists')
def artists():
  # DONE: replace with real data returned from querying the database
  Artist.query.all()

  try:
      artists = Artist.query.all()
      data = []
      for artist in artists:
          data.append({
              "id": artist.id,
              "name": artist.name
          })
      result = {
          "count": len(data),
          "data": data
      }
  except:
      db.session.rollback()
      print(sys.exc_info())
  finally:
      db.session.close()

  return render_template('pages/artists.html', artists=data)

@app.route('/artists/search', methods=['POST'])
def search_artists():
  # DONE: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for "A" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band".
  # search for "band" should return "The Wild Sax Band".

  text = request.form['search_term'].lower()

  source_data=pd.DataFrame.from_records([vars(artist) for artist in Artist.query.all()])

  result = source_data[source_data['name'].str.lower().str.contains(text)]
  


  count=len(result)
  tier1_list={"count": count}
  tier2_list=[]

  for i in range(len(result)):
      temp = result.iloc[i].to_dict()
      tier2_list.append(temp)
  tier1_list.update({"data": tier2_list})
  response=tier1_list
  sql_debug(response)


  return render_template('pages/search_artists.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  # shows the artist page with the given artist_id
  # DONE: replace with real artist data from the artist table, using artist_id

    artist = Artist.query.get(artist_id)

    data={
      "id": artist.id,
      "name": artist.name,
      "genres": artist.genres.split(','),
      "city": artist.city,
      "state": artist.state,
      "phone": artist.phone,
      "website": artist.website_link,
      "facebook_link": artist.facebook_link,
      "seeking_talent": artist.seeking_talent,
      "seeking_description": artist.seeking_description,
      "image_link": artist.image_link,
      # "past_shows": past_shows,
      # "upcoming_shows": upcoming_shows,
      # "past_shows_count": len(past_shows),
      # "upcoming_shows_count": len(upcoming_shows)
    }
    return render_template('pages/show_artist.html', artist=data)

#  Update
#  ----------------------------------------------------------------
@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  
  
  artist = Artist.query.get(artist_id)

  form = ArtistForm(obj=artist)

  # Set default selected genres in the genres field
  selected_genres = [genre.strip() for genre in artist.genres.split(',')]
  form.genres.data = selected_genres

  # Populate other fields with data
  form.name.data = artist.name
  form.city.data = artist.city
  form.state.data = artist.state
  form.phone.data = artist.phone
  form.image_link.data = artist.image_link
  form.facebook_link.data = artist.facebook_link
  form.website_link.data = artist.website_link
  form.seeking_talent.data = artist.seeking_talent
  form.seeking_description.data = artist.seeking_description
  

  # DONE: populate form with fields from artist with ID <artist_id>
  return render_template('forms/edit_artist.html', form=form, artist=artist)

@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  # DONE: take values from the form submitted, and update existing
  # artist record with ID <artist_id> using the new attributes

   # Get the artist record to update
  artist = Artist.query.get(artist_id)

  # Update the attributes with the new values from the form
  artist.name = request.form['name']
  artist.city = request.form['city']
  artist.state = request.form['state']
  artist.phone = request.form['phone']
  artist.genres = ','.join(request.form.getlist('genres'))
  artist.facebook_link = request.form['facebook_link']
  artist.image_link = request.form['image_link']
  artist.website_link = request.form['website_link']
  artist.seeking_talent = True if request.form.get('seeking_talent') == 'y' else False
  artist.seeking_description = request.form['seeking_description']

  # Commit the changes to the database
  db.session.commit()

  return redirect(url_for('show_artist', artist_id=artist_id))

@app.route('/components/<int:component_id>/edit', methods=['GET'])
def edit_component(component_id):

  component = Component.query.get(component_id)


  form = ComponentForm(obj=component)

  # Populate other fields with data
  form.name.data = component.name
  form.component_type.data = component.component_type
  form.datasheet_link.data = component.datasheet_link

  return render_template('forms/edit_component.html', form=form, component=component)

@app.route('/components/<int:component_id>/edit', methods=['POST'])
def edit_component_submission(component_id):
  # DONE: take values from the form submitted, and update existing
  # venue record with ID <venue_id> using the new attributes

  component = Component.query.get(component_id)

  # Update the attributes with the new values from the form
  component.name = request.form['name']
  component.component_type = request.form['component_type']
  component.datasheet_link = request.form['datasheet_link']


  # Commit the changes to the database
  db.session.commit()

  return redirect(url_for('show_component', component_id=component_id))

#  Create Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  # called upon submitting the new artist listing form
  # DONE: insert form data as a new Venue record in the db, instead
  # DONE: modify data to be the data object returned from db insertion

  form_temp = ArtistForm(request.form)
  if form_temp.validate():
    try:
        name=request.form.get('name')
        city=request.form.get('city')
        state=request.form.get('state')
        phone=request.form.get('phone')
        image_link=request.form.get('image_link')
        genres=request.form.getlist('genres')
        facebook_link=request.form.get('facebook_link')
        website_link=request.form.get('website_link')
        seeking_talent=request.form.get('seeking_talent')
        seeking_talent = 1 if seeking_talent == 'y' else 0
        genres = ", ".join(genres)
        seeking_description=request.form.get('seeking_description')
        
        

        artist = Artist(name=name, city=city, state=state, phone=phone, image_link=image_link, genres=genres, facebook_link=facebook_link, website_link=website_link, seeking_talent=seeking_talent, seeking_description=seeking_description)             
        db.session.add(artist)
        db.session.commit()
        flash('Artist ' + request.form['name'] + ' was successfully listed!')
    except Exception as e:
        print(e)
        flash('Artist ' + request.form['name'] + ' was not successfully listed!')
        db.session.rollback()
        
    finally:
        db.session.close()
        return render_template('pages/home.html')
  else:
      flash('Artist ' + request.form['name'] + ' was not successfully listed!')
      print("Not successfully submitted")
      print(form_temp.errors)
      return render_template('forms/new_artist.html', form=form_temp)




#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
  # displays list of shows at /shows
  # Done: replace with real venues data.

  data = db.session.query(
        Show.venue_id,
        Venue.name.label('venue_name'),
        Show.artist_id,
        Artist.name.label('artist_name'),
        Artist.image_link.label('artist_image_link'),
        Show.start_time
    ).join(Venue).join(Artist).all()

  shows_data = []
  for show in data:
        show_data = {
            "venue_id": show.venue_id,
            "venue_name": show.venue_name,
            "artist_id": show.artist_id,
            "artist_name": show.artist_name,
            "artist_image_link": show.artist_image_link,
            "start_time": str(show.start_time) # convert datetime object to string
        }
        print(str(show.start_time))
        shows_data.append(show_data)

  return render_template('pages/shows.html', shows=shows_data)

  # data=[{
  #   "venue_id": 1,
  #   "venue_name": "The Musical Hop",
  #   "artist_id": 4,
  #   "artist_name": "Guns N Petals",
  #   "artist_image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
  #   "start_time": "2019-05-21T21:30:00.000Z"
  # }, {
  #   "venue_id": 3,
  #   "venue_name": "Park Square Live Music & Coffee",
  #   "artist_id": 5,
  #   "artist_name": "Matt Quevedo",
  #   "artist_image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
  #   "start_time": "2019-06-15T23:00:00.000Z"
  # }, {
  #   "venue_id": 3,
  #   "venue_name": "Park Square Live Music & Coffee",
  #   "artist_id": 6,
  #   "artist_name": "The Wild Sax Band",
  #   "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
  #   "start_time": "2035-04-01T20:00:00.000Z"
  # }, {
  #   "venue_id": 3,
  #   "venue_name": "Park Square Live Music & Coffee",
  #   "artist_id": 6,
  #   "artist_name": "The Wild Sax Band",
  #   "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
  #   "start_time": "2035-04-08T20:00:00.000Z"
  # }, {
  #   "venue_id": 3,
  #   "venue_name": "Park Square Live Music & Coffee",
  #   "artist_id": 6,
  #   "artist_name": "The Wild Sax Band",
  #   "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
  #   "start_time": "2035-04-15T20:00:00.000Z"
  # }]
  # return render_template('pages/shows.html', shows=data)

@app.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  # called to create new shows in the db, upon submitting new show listing form
  # TODO: insert form data as a new Show record in the db, instead
    form_temp = ShowForm(request.form)
    if form_temp.validate():
        try:
            artist_id=request.form.get('artist_id')
            venue_id=request.form.get('venue_id')
            start_time=request.form.get('start_time')
            

            show = Show(artist_id=artist_id, venue_id=venue_id, start_time=start_time)             
            db.session.add(show)
            db.session.commit()
            flash('Show was successfully listed!')
        except:
            flash('Show was not successfully listed!')
            db.session.rollback()
        finally:
            db.session.close()
            return render_template('pages/home.html')
    else:
        flash('Show was not successfully listed!')
        print("Not successfully submitted")
        print(form_temp.errors)
        return render_template('forms/new_venue.html', form=form_temp)  


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run(debug=True)

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''

#debugging function
def sql_debug(text):
    print(text)
    return text

#app.after_request(sql_debug)