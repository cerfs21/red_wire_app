### Red Wire Web App.

You can run this application locally without setting up a web server:
- Clone this repo et change to the just created 'red_wire_app' directory
- Copy the 'assets' and 'data' directories into /var/www/red-wire on your machine (alternatively: edit 'app_path' in red_wire_app.py to match your local application directory)
- Install requirements with pip install -r requirements
- Start the web app. with 'python3 red_wire_app.py'
- Connect to http://127.0.0.1:8050/

#### List of files in db directories:

+ user_connect_db.sqlite: database of users and past connections
+ REE_data.csv: REE raw data imported from JSON API to CSV format
+ REE_data_aggregated_by_10mn.csv: REE data aggregated by 10 mn
+ REE_data_aggregated_by_1d.csv: " " " " 1 day
+ REE_data_aggregated_by_1h.csv: " " " " 1 hour

Note: this web app. is linked to a Machine Learning project @ https://github.com/LosseniSangare/serie_temporelle_machine_learning 
