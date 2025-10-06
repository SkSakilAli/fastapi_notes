Web Sockets allows full duplex communication between client and server

From Google
-- Initially Websocket connections are initiated through and HTTP GET Request which contains specific headers like Upgrade: websocket and Connection: upgrade to signal its intent to switch protocols. If the server supports web sockets , it responds with an HTTP 101 switching Protocol status and the connection is then upgrades to WebSocket Protocol. After the Handshake, the communication switches entirely to the Websocket protocol which operates over a single persistent TCP Connection, enabling full duplex bi-directional between client and server.

--Installing websockets in project
pip install websockets

 
