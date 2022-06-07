from flask import Flask, render_template, session, request, redirect
from utilities.db_coords import db_coords

app = Flask(__name__)
app.config.from_pyfile('settings.py')


@app.route('/change_name', methods=['POST'])
def new_name():
    name = request.form['new_name']
    x_pos = request.form['x_pos']
    y_pos = request.form['y_pos']
    floor_name = request.form['floor_name']
    db_coords.change_name(name, x_pos, y_pos, floor_name)
    if (db_coords.check_exist_coordinates(x_pos, y_pos, floor_name)):
        message='השם שונה בהצלחה'
        locations = db_coords.get_Existing_locations(floor_name)
        details = db_coords.get_floor_details(floor_name)
        if (floor_name == 'Minus_2'):
            return render_template('Minus_2.html', locations=locations, details=details, name=name,message=message)
        if (floor_name == 'Gallery_minus_1'):
            return render_template('Gallery_minus_1.html', locations=locations, details=details, name=name,message=message)
        if (floor_name == 'Lobby_minus_1'):
            return render_template('Lobby_minus_1.html', locations=locations, details=details, name=name,message=message)
        if (floor_name == 'Turkish_1'):
            return render_template('Turkish_1.html', locations=locations, details=details, name=name,message=message)
        if (floor_name == 'Turkish_0'):
            return render_template('Turkish_0.html', locations=locations, details=details, name=name,message=message)
        if (floor_name == 'Outside'):
            return render_template('Outside.html' ,locations=locations, details=details, name=name, message=message)
        if (floor_name == 'Back_2nd_floor'):
            return render_template('Back_2nd_floor.html' ,locations=locations, details=details, name=name, message=message)
        return True

    else:
        locations = db_coords.get_Existing_locations(floor_name)
        details = db_coords.get_floor_details(floor_name)
        message = 'הקואורדינטות הנבחרות לא תואמות את המפה שהוגדרה'
        name=''
        message1=''
        if (floor_name == 'Minus_2'):
            return render_template('Minus_2.html', locations=locations, details=details, name=name, message=message,message1=message1 )
        if (floor_name == 'Gallery_minus_1'):
            return render_template('Gallery_minus_1.html', locations=locations, details=details, name=name,
                                   message=message,message1=message1 )
        if (floor_name == 'Lobby_minus_1'):
            return render_template('Lobby_minus_1.html', locations=locations, details=details, name=name,
                                   message=message, message1=message1 )
        if (floor_name == 'Turkish_1'):
            return render_template('Turkish_1.html', locations=locations, details=details, name=name, message=message, message1=message1)
        if (floor_name == 'Turkish_0'):
            return render_template('Turkish_0.html', locations=locations, details=details, name=name, message=message, message1=message1)
        if (floor_name == 'Outside'):
            return render_template('Outside.html', locations=locations, details=details, name=name, message=message, message1=message1)
        if (floor_name == 'Back_2nd_floor'):
            return render_template('Back_2nd_floor.html', locations=locations, details=details, name=name, message=message, message1=message1)
        return True



@app.route('/change_location', methods=['POST'])
def new_location():
    name = request.form['name']
    x_pos = request.form['x_pos']
    y_pos = request.form['y_pos']
    floor_name = request.form['floor_name']
    if ( db_coords.check_exist_name(name, floor_name)):
        message = ''
        db_coords.change_location(x_pos, y_pos, name, floor_name)
        message1 = 'המיקום שונה בהצלחה'
        locations = db_coords.get_Existing_locations(floor_name)
        details = db_coords.get_floor_details(floor_name)
        if (floor_name == 'Minus_2'):
            return render_template('Minus_2.html', locations=locations, details=details, message=message, name=name ,message1=message1)
        if (floor_name == 'Gallery_minus_1'):
            return render_template('Gallery_minus_1.html', locations=locations, details=details, message=message, name=name ,message1=message1)
        if (floor_name == 'Lobby_minus_1'):
            return render_template('Lobby_minus_1.html', locations=locations, details=details, message=message, name=name ,message1=message1)
        if (floor_name == 'Turkish_1'):
            return render_template('Turkish_1.html', locations=locations, details=details, message=message, name=name, message1=message1)
        if (floor_name == 'Turkish_0'):
            return render_template('Turkish_0.html', locations=locations, details=details, message=message, name=name, message1=message1)
        if (floor_name == 'Outside'):
            return render_template('Outside.html', locations=locations, details=details, message=message, name=name, message1=message1)
        if (floor_name == 'Back_2nd_floor'):
            return render_template('Back_2nd_floor.html', locations=locations, details=details, message=message, name=name, message1=message1)
        return True

    else:
        name = ''
        message = ''
        locations = db_coords.get_Existing_locations(floor_name)
        details = db_coords.get_floor_details(floor_name)
        message1 = 'הקואורדינטות הנבחרות לא תואמות את המפה שהוגדרה'
        if (floor_name == 'Minus_2'):
            return render_template('Minus_2.html', locations=locations, details=details, name=name, message=message, message1=message1)
        if (floor_name == 'Gallery_minus_1'):
            return render_template('Gallery_minus_1.html', locations=locations, details=details, name=name,
                                   message=message,message1=message1)
        if (floor_name == 'Lobby_minus_1'):
            return render_template('Lobby_minus_1.html', locations=locations, details=details, name=name,
                                   message=message,message1=message1)
        if (floor_name == 'Turkish_1'):
            return render_template('Turkish_1.html', locations=locations, details=details, name=name, message=message, message1=message1)
        if (floor_name == 'Turkish_0'):
            return render_template('Turkish_0.html', locations=locations, details=details, name=name, message=message, message1=message1)
        if (floor_name == 'Outside'):
            return render_template('Outside.html', locations=locations, details=details, name=name, message=message, message1=message1)
        if (floor_name == 'Back_2nd_floor'):
            return render_template('Back_2nd_floor.html', locations=locations, details=details, name=name, message=message, message1=message1)
        return True

@app.route('/')
def start_screen():  # put application's code here
    return render_template('home.html')

@app.route('/Minus_2')
def Minus_2():  # put application's code here
    locations = db_coords.get_Existing_locations('Minus_2')
    details = db_coords.get_floor_details('Minus_2')
    return render_template('Minus_2.html', details=details, locations=locations )

@app.route('/Gallery_minus_1')
def Gallery_minus_1():  # put application's code here
    locations = db_coords.get_Existing_locations('Gallery_minus_1')
    details = db_coords.get_floor_details('Gallery_minus_1')
    return render_template('Gallery_minus_1.html', details=details, locations=locations )

@app.route('/Lobby_minus_1')
def Lobby_minus_1():  # put application's code here
    locations = db_coords.get_Existing_locations('Lobby_minus_1')
    details = db_coords.get_floor_details('Lobby_minus_1')
    return render_template('Lobby_minus_1.html', details=details, locations=locations )

@app.route('/Turkish_1')
def Turkish_1():  # put application's code here
    locations = db_coords.get_Existing_locations('Turkish_1')
    details = db_coords.get_floor_details('Turkish_1')
    return render_template('Turkish_1.html', details=details, locations=locations)

@app.route('/Turkish_0')
def Turkish_0():  # put application's code here
    locations = db_coords.get_Existing_locations('Turkish_0')
    details = db_coords.get_floor_details('Turkish_0')
    return render_template('Turkish_0.html', details=details, locations=locations)

@app.route('/Outside')
def Turkish():  # put application's code here
    locations = db_coords.get_Existing_locations('Outside')
    details = db_coords.get_floor_details('Outside')
    return render_template('Outside.html', details=details, locations=locations)

@app.route('/Back_2nd_floor')
def Back_2nd_floor():  # put application's code here
    locations = db_coords.get_Existing_locations('Back_2nd_floor')
    details = db_coords.get_floor_details('Back_2nd_floor')
    return render_template('Back_2nd_floor.html', details=details, locations=locations)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
