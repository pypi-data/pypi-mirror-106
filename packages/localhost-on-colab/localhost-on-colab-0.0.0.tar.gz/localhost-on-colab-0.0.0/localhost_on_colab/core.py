import pyngrok
from pyngrok import ngrok
import nest_asyncio
import multiprocessing 


class LocalHostOnColab():
    """
    Helps you easily run your localhost stuff on google colab

    Example:
    ```python
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello :)"

    bridge = LocalHostOnColab()

    url = bridge.run(
        function = app.run,
        kwargs = {'port': 8989},
        port = 8989,
    )

    print(url)    
    ```
    """
    def __init__(self):
        self.name = 'some name'

    def run(self, function, kwargs = {}, port =  5000, bind_tls = True):
        """[summary]

        Args:
            function : function that needs to be called
            kwargs (dict, optional): Dictionary containing kwargs. Defaults to {}.
            port (int, optional): Port number, this should match the port number being used in the function. Defaults to 5000.
            bind_tls (bool, optional): I really dont know what it is, but setting it to True enables us to use n seperate LocalHostOnColab instances. Defaults to True.

        Returns:
            url: url to ngrok tunnel
        """
        
        try:
            self.ngrok_tunnel = ngrok.connect(port, bind_tls = bind_tls)
        except pyngrok.exception.PyngrokNgrokHTTPError:
            # print('connect nahi huaa bsdk')
            return None

        nest_asyncio.apply()
        self.thread = multiprocessing.Process(target= function, kwargs = kwargs)
        self.thread.start()

        return self.ngrok_tunnel.public_url

    def stop(self):

        self.thread.terminate()
        ngrok.disconnect(self.ngrok_tunnel.public_url)