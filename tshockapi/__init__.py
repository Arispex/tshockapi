from pydantic import BaseModel
import httpx


class Server(BaseModel):
    """
    TShock Server Object
    """
    host: str
    port: int
    token: str
    timeout: int = 5

    def __init__(self, host: str, port: int, token: str):
        """
        Initialize a TShock Server Object
        :param host: Server host
        :param port: Server port
        :param token: Server token
        """
        super().__init__(host=host, port=port, token=token)

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