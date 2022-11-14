import httpx


class Server:
    """
    TShock Server Object
    """

    def __init__(self, host: str, port: int, token: str, timeout: int = 5):
        """
        Initialize a TShock Server Object
        :param host: Server host
        :param port: Server port
        :param token: Server token
        """
        self.host = host
        self.port = port
        self.token = token
        self.timeout = timeout

    def request(self, endpoint: str, **kwargs) -> dict:
        """
        send a request to the server endpoint
        """
        url = f"http://{self.host}:{self.port}/{endpoint}"
        return httpx.get(
            url=url, params=dict({"token": self.token}, **kwargs), timeout=self.timeout
        ).json()

    def status(self) -> dict:
        """
        /status

        Description:

        Prints out a basic information about the servers status

        Returns:

        name - Server name

        port - Port the server is running on

        playercount - Number of players currently online

        players - Player names separated by a comma

        :return: a result dict
        """
        return self.request("status")

    def tokentest(self) -> dict:
        """
        /tokentest

        Description:

        Tests the token to see if it is valid

        Returns:

        response - A response message

        :return: a result dict
        """
        return self.request("tokentest")

    def v2_token_create(self, username: str, password: str) -> dict:
        """
        /v2/token/create

        Description:

        Creates an authenticated token for use with other endpoints

        Returns:

        HTTP 200 if the authentication succeeds

        HTTP 403 if the authentication fails

        response - Error message if the authentication failed, else an authenticated token.

        :param username: User with which to authenticate the token
        :param password: User's password
        :return: a result dict
        """
        return self.request("v2/token/create", username=username, password=password)

    def v2_server_broadcast(self, msg: str) -> dict:
        """
        /v2/server/broadcast

        Description:

        Performs a server broadcast to all players on the server

        Returns:

        response - A response message

        :param msg: The message to broadcast
        :return: a result dict
        """
        return self.request("v2/server/broadcast", msg=msg)

    def v2_server_off(self, confirm: bool = False, nosave: bool = False) -> dict:
        """
        /v2/server/off

        Description:

        Shuts down the server

        Returns:

        response - A response message

        :param confirm: A bool value confirming whether or not to shut down the server
        :param nosave: A bool value indicating whether or not to save the world before shutting down the server
        :return: a result dict
        """
        return self.request("v2/server/off", confirm=confirm, nosave=nosave)

    def v2_server_status(self, players: bool = False, rules: bool = False) -> dict:
        """
        /v2/server/status

        Description:

        Prints out details about the status of the currently running server

        Returns:

        name - Server name

        port - Port the server is running on

        playercount - Number of players currently online

        maxplayers - The maximum number of players the server support

        world - The name of the currently running world

        players - (optional) an array of players including the following information: nickname, username, ip, group, active, state, team

        rules - (optional) an array of server rules which are name value pairs e.g. AutoSave, DisableBuild etc

        :param players: A bool value indicating if the status response should include player information
        :param rules: A bool value indicating if the status response should include rule information
        :return: a result dict
        """
        return self.request("v2/server/status", players=players, rules=rules)

    def v3_server_rawcmd(self, cmd: str) -> dict:
        """
        Description:

        Issues a raw command on the server just as if you typed it into the console.

        Returns:

        response - The response from the executed command User Commands

        :param cmd: The command to execute on the server
        :return: a result dict
        """
        return self.request("v3/server/rawcmd", cmd=cmd)

    def v2_users_activelist(self) -> dict:
        """
        Description:

        Returns a list of currently active users on the server

        Returns:

        activeusers - List of active users separated by a tab character

        :return: a result dict
        """
        return self.request("v2/users/activelist")

    def v2_users_read(self, type: str, user: str) -> dict:
        """
        Description:

        Returns information about a specified user

        Returns:

        group - The group the user belong's to

        id - The user's ID

        name - The name of the user

        ip - The ip of the user

        :param type: name, id or ip indicating what the "user" parameter refers to
        :param user: The name, ip or id of a currently registered user
        :return: a result dict
        """
        return self.request("v2/users/read", type=type, user=user)

    def v2_users_create(
            self, type: str, user: str, password: str, group: str, ip: str
    ) -> dict:
        """
        Description:

        Creates a user in the database

        Returns:

        response - A response message

        :param type:  name, id or ip indicating what the "user" parameter refers to
        :param user: The name of the user to register
        :param password: The password you wish to assign to the user
        :param group: The group you wish to assign to the user
        :param ip: The ip you wish to assign to the user
        :return: a result dict
        """
        return self.request(
            "v2/users/create", type=type, user=user, password=password, group=group, ip=ip
        )

    def v2_users_destroy(self, type: str, user: str) -> dict:
        """
        Returns:

        response - A response message

        :param type: name, id or ip indicating what the "user" parameter refers to
        :param user: The name, ip or id of a currently registered user
        :return: a result dict
        """
        return self.request("v2/users/destroy", type=type, user=user)

    def v2_users_update(self, type: str, user: str, password: str = -1, group: str = -1):
        """
        Description:

        Edits the settings of a user

        Returns:

        response - A response message

        :param type: name, id or ip indicating what the "user" parameter refers to
        :param user: The name, ip or id of a currently registered user
        :param password: The new password you wish to assign to that user (optional)
        :param group: The new group you wish to assign to that user (optional)
        :return: a result dict
        """
        d = {"type": type, "user": user}
        if password != -1:
            d["password"] = password
        if group != -1:
            d["group"] = group
        return self.request("v2/users/update", **d)

    def v3_bans_create(self, identifier: str, reason: str = -1, start: str = -1, end: str = -1):
        """
        Description:

        Create a new ban entry.

        Returns:

        response - A response message

        :param identifier: The identifier to ban.
        :param reason: The reason to assign to the ban.
        :param start: The datetime at which the ban should start.
        :param end: The datetime at which the ban should end.
        :return: a result dict
        """
        d = {"identifier": identifier}
        if reason != -1:
            d["reason"] = reason
        if start != -1:
            d["start"] = start
        if end != -1:
            d["end"] = end
        return self.request("v3/bans/create", **d)

    def v3_bans_destroy(self, ticketNumber: str, fullDelete: bool = False):
        """
        Description:

        Delete an existing ban entry.

        Returns:

        response - A response message

        :param ticketNumber: The ticket number of the ban to delete.
        :param fullDelete: Whether or not to completely remove the ban from the system.
        :return: a result dict
        """
        return self.request("v3/bans/destroy", ticketNumber=ticketNumber, fullDelete=fullDelete)

    def v3_bans_read(self, ticketNumber: str):
        """
        Description:

        View the details of a specific ban.

        Returns:

        ticket_number - The ticket number of the ban.

        identifier - The identifier of the ban.

        reason - The reason for the ban.

        banning_user - The user who created the ban.

        start_data_ticks - The start date of the ban in ticks.

        end_date_ticks - The end date of the ban in ticks.

        :param ticketNumber: The ticket number to search for.
        :return: a result dict
        """
        return self.request("v3/bans/read", ticketNumber=ticketNumber)

    def v3_bans_list(self):
        """
        Description:

        View all bans in the TShock database.

        Returns:

        bans - A list of all bans in the TShock database.

        :return: a result dict
        """
        return self.request("v3/bans/list")

    def v2_players_kick(self, player: str, reason: str = -1):
        """
        Description:

        Kick a player off the server.

        Returns:

        response - A response message

        :param player: The player to kick.
        :param reason: The reason the player was kicked.
        :return: a result dict
        """
        d = {"player": player}
        if reason != -1:
            d["reason"] = reason
        return self.request("v2/players/kick", **d)

    def v2_players_kill(self, player: str, from_: str = -1):
        """
        Description:

        Kill a player.

        Returns:

        response - A response message

        :param from_: Who killed the player.
        :param player: The player to kill.
        :return: a result dict
        """
        d = {"player": player}
        if from_ != -1:
            d["from"] = from_
        return self.request("v2/players/kill", **d)

    def v2_players_list(self):
        """
        Description:

        Fetches detailed user information on all connected users, and can be filtered by specifying a key value pair
        filter users where the key is a field and the value is a users field value. No special permissions are
        required for this route.

        Returns:

        players -  A list of all current players on the server, separated by a comma.

        :return: a result dict
        """
        return self.request("v2/players/list")

    def v2_players_mute(self, player: str):
        """
        Description:

        Mute a player.

        Returns:

        response - A response message

        :param player: The player to mute.
        :return: a result dict
        """
        return self.request("v2/players/mute", player=player)

    def v4_players_read(self, player: str):
        """
        Description:

        The player to lookup

        Returns:

        nickname - The nickname of the player.

        username - The username of the player.

        ip - The IP address of the player.

        group - The group of the player.

        registered - Whether or not the player is registered.

        muted - Whether or not the player is muted.

        position - The position of the player.

        items - The inventory of the player.

        buffs - The buffs of the player.

        :param player: The player to lookup.
        :return: a result dict
        """
        return self.request("v4/players/read", player=player)

    def v2_players_unmute(self, player: str):
        """
        Description:

        Unmute a player.

        Returns:

        response - A response message

        :param player: The player to unmute.
        :return: a result dict
        """
        return self.request("v2/players/unmute", player=player)

    def v3_server_motd(self):
        """
        Description:

        Returns the motd, if it exists. No special permissions are required for this route.

        Returns:

        motd - The current MOTD.

        :return: a result dict
        """
        return self.request("v3/server/motd")

    def v3_server_reload(self):
        """
        Description:

        Reload config files for the server.

        Returns:

        response - A response message

        :return: a result dict
        """
        return self.request("v3/server/reload")

    def v3_server_rules(self):
        """
        Description:

        Returns the rules, if they exist. No special permissions are required for this route.

        Returns:

        rules - The current rules.

        :return: a result dict
        """
        return self.request("v3/server/rules")

    def v3_world_bloodmoon(self):
        """
        Description:

        Toggle the status of blood moon.

        Returns:

        response - A response message

        :return: a result dict
        """
        return self.request("v3/world/bloodmoon")

    def v2_world_butcher(self, killfriendly: bool = False):
        """
        Description:

        Butcher npcs.

        Returns:

        response - A response message

        :param killfriendly: Should friendly npcs be butchered.
        :return: a result dict
        """
        return self.request("v2/world/butcher", killfriendly=killfriendly)

    def world_meteor(self):
        """
        Description:

        Drops a meteor on the world.

        Returns:

        response - A response message

        :return: a result dict
        """
        return self.request("world/meteor")