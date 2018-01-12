#!/usr/bin/python3
# Mars Team Client Example written in Python
# Requires the following library to install: sudo [pip|pip3] install websocket-client
import requests
import websocket
import json
import sys

# Please update theses Global Variables and your Strategy
server_target = '127.0.0.1:8080'
team_name = sys.argv[1] if len(sys.argv) > 1 else 'NoName'

def my_team_strategy(team, control):
    # This is your main strategy to implement here
    print(team)

    # Example strategy:
    if team['life'] >= 95:
        # If life is enough, close the shield
        print("\nGameMove: Team: {0} Action: Shield DOWN!| Energy: {1}".format(team_name, str(team['energy'])))
        control.shield_down()
    elif team['shield'] != True and team['energy'] > 40:
        # Check if Shield is up and shield energy is larger than 10%
        print("\nGameMove: Team: {0} Action: Shield UP!| Energy: {1}".format(team_name, str(team['energy'])))
        control.shield_up()
    else:
        # No action..
        print("\nTeam: {0} Action: None| Energy: {1}".format(team_name, str(team['energy'])))



######################################################################
# @@@ Please DO NOT MODIFY ANY FOLLOWING CODES !!!!!!!!!!!!
######################################################################
# Server Method Calls ------------------------------------------------
# >>>>>>>>>>>>>
# >>>>>>>

server_url = 'http://' + server_target + '/api'   # URL of the SERVER API
server_ws = 'ws://' + server_target + '/ws'       # URL of the Sensors Websocket

def register_team(team_name):
    """
    Registers the Team in the Server
    :param team_name:The team name
    :return:The Team authentication Token
    """

    url = server_url + "/join/" + team_name
    print('Server API URL: ' + url)
    payload = ''

    # POST with form-encoded data
    response = requests.post(url, data=payload)

    team_auth = response.text
    # print ('Team Authentication Code:' + team_auth )

    if response.status_code == 200:
        print ('Team \'' + team_name + '\' joined the game!')
        print (team_name + ' authentication Code: ' + team_auth)
    else:
        print ('Team \'' + team_name + '\' joining game Failed!')
        print ("HTTP Code: " + str(response.status_code) + " | Response: " + response.text)
        exit(0)

    return team_auth


# Shield Method Calls ------------------------------------------------
def team_shield_up(team_name, team_auth):
    """
    Sets the team shield up
    curl -i -H 'X-Auth-Token: 1335aa6af5d0289f' -X POST http://localhost:8080/api/shield/enable
    :param team_name:The team name
    :param team_auth:The team authentication token
    :return: nothing
    """
    url = server_url + '/shield/enable'
    auth_header = {'X-Auth-Token': team_auth}
    shield_up = requests.post(url, headers=auth_header)
    if shield_up.status_code == 200:
        print ('Server: Team: ' + team_name + ' Shield is UP!')
    else:
        print ('Server: Team: ' + team_name + ' Shield UP! request Failed!')
        print ("HTTP Code: " + str(shield_up.status_code) + " | Response: " + shield_up.text)


def team_shield_down(team_name, team_auth):
    """
    Sets the team shield Down
    curl -i -H 'X-Auth-Token: 1335aa6af5d0289f' -X POST http://localhost:8080/api/shield/disable
    :param team_name:The team name
    :param team_auth:The team authentication token
    :return: nothing
    """
    url = server_url + '/shield/disable'
    auth_header = {'X-Auth-Token': team_auth}
    shield_down = requests.post(url, headers=auth_header)
    if shield_down.status_code == 200:
        print ('Server: Team: ' + team_name + ' Shield is DOWN!')
    else:
        print ('Server: Team: ' + team_name + ' Shield DOWN! request Failed!')
        print ("HTTP Code: " + str(shield_down.status_code) + " | Response: " + shield_down.text)


def data_recording(parsed_json):
    """
    Saves the Mars sensor data in data repository
    :param parsed_json:Readings from Mars Sensors
    :return:Nothing
    """
    # print("\nData Recording: Saving Data row for persistence. Time: " + str(parsed_json['startedAt']))
    pass


class Control:

    def shield_up(self):
        team_shield_up(self.team_name, self.team_auth)

    def shield_down(self):
        team_shield_down(self.team_name, self.team_auth)


def run_AI(parsed_json):
    teams_list = parsed_json['teams']
    control = Control()
    control.team_name = team_name
    control.team_auth = team_auth

    # Find this team
    for team in teams_list:
        if team['name'] == team_name:
            my_team_strategy(team, control)


# Register the Team

team_auth = register_team(team_name)


# Create the WebSocket for Listening
ws = websocket.create_connection(server_ws)

while True:

    json_string = ws.recv()  # Receives the the json information

    # Received '{"running":false,"startedAt":"2015-08-04T00:44:40.854306651Z","readings":{"solarFlare":false,"temperature":-3.
    # 960996217958863,"radiation":872},"teams":[{"name":"TheBorgs","energy":100,"life":0,"shield":false},{"name":"QuickFandang
    # o","energy":100,"life":0,"shield":false},{"name":"InTheBigMessos","energy":32,"life":53,"shield":false},{"name":"MamaMia
    # ","energy":100,"life":100,"shield":false}]}'

    parsed_json = json.loads(json_string)

    # Check if the game has started
    print("Game Status: " + str(parsed_json['running']))

    if not parsed_json['running']:
        print('Ready and waiting for the Game Start ..')
    else:
        data_recording(parsed_json)
        run_AI(parsed_json)

ws.close()

print("Good bye!")
