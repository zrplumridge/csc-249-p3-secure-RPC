# CSC 249 – Project 2 – Simple VPN

For this project, you'll be buidling a VPN server and client that will work with sockets.

I’ve placed some starter code in this Git repo [https://github.com/abpw/csc-249-p2-simple-VPN-server], which you are welcome to clone. Your job will be to fill in the "encode_message()" function in "client.py", the "parse_message()" function in "VPN.py", and fill in the rest of the functionality of a VPN in "VPN.py".

I've also included a slightly modified version of the "echo-server.py" file from project 1 for you to test your VPN with: by default, the echo server, VPN server, and VPN client are configured to run on compatible sockets, but if you'd like to change any ip addresses you can use command line arguments to do so. To use echo-server.py's command line arguments, for example, you can run "python3 echo-server.py --help" from command line in the directory the echo-server.py file is stored.

Note that all three files must be stored in the same direcory as "arguments.py" to run correctly.

Although "echo-server.py" is included as a test server, your client and VPN should be able to interact with any server with any functionality that follows this type of protocol:

* Take as input over a socket a message of up to 1000 bytes in a particular format
* Return to the sender along the same TCP connection a message of up to 1000 bytes (possibly an error message)

For example, you may have created a server like this for your project 1. If you did, and if you type exactly the right format of message as input for the VPN client you'll write in this project, you should be able to interact with your project 1 server as well as echo-server.py. In other words, the protocol you defined in project 1 should allow you to create a new client for this project that is somewhat interoperable with your server from the last project.

Like the echo application, your VPN should terminate after successfully processing a client message, and your client should terminate after successfully receiving a response to its request.

## Design Requirements

Your server must be able to process at least two different requested operations (i.e., it must understand at least two "verbs"). This means that an indication of the requested operation needs to be passed from client to server.

* Your client must obtain the desired message to be sent through the VPN from the terminal command line. This functionality is already provided in the client.py file.
* As they run, the client and the VPN applications must generate tracing messages that document significant program milestones, e.g., when connections are made, when messages and sent and received, and what was sent and what was received. (Good examples of tracing messages can be found in the sample code provided.)
* The client and server should be designed to anticipate and gracefully handle reasonable errors which could occur at either end of the communication channel. For example, the client should attempt to prevent malformed requests to the server, and the server should avoid crashing if it receives a malformed request. Remember, in the real world there is no guarantee that your server will only have to deal with communications from your (presumably friendly) client!
* Source code of your client and server must be appropriately documented. Comments should be sufficient to allow a third party to understand your code, run it, and confirm that it works.

## Deliverables

Your work on this project must be submitted for grading by **Thursday, October 10th at 11:59PM**. Extensions may be obtained by sending me a message on Slack before the original due date.

All work must be submitted in Gradescope.

You must submit these work products:

1. Source code for your client and VPN.
2. A **text** (.txt or .md) document with a written description of your client-VPN message format (that is, a description of all implemented client and VPN messages, and how the various components of each message are represented). Your goal in writing this document should be to convey enough information in enough detail to allow a competent programmer **without access to your source code** to write either a new client that communicates properly with your VPN server, or a new VPN server that communicates properly with your client. This document should include at least **six** sections: Overview of Application, Client->VPN Server Message Format, VPN Server->Client Message Format, Example Output, **a description of how the network layers are interacting when you run your server, VPN server, and client**, and Acknowledgments.
3. A command-line trace showing the client and server in operation. 

## Teamwork Policy

**For this project, all work must be submitted individually – no team submissions will be allowed**. You are free to collaborate and exchange ideas, but each student must submit their own original work. To the extent you obtain ideas and feedback from other students, you should give them proper credit in the Acknowledgments section of your specification document. For example, "Jane Austen helped me think through the different messages that my ATM server might need to be able to handle", "Sophia Smith helped me understand the purpose of the htons() function". **You should not use the Acknowledgments section to acknowledge help from the course instructor or teaching assistant.** The purpose of the section is to allow students to give appropriate credit for any peer assistance in conceiving and completing individual assignments.

## Grading Rubric

Your work on this project will be graded on a five-point scale. Fractional points may be awarded.

_0 pts:_ No deliverables were received by the due date or requested extension date.

_1 pt:_ Incomplete deliverables were received by the due date or extension date.

_2 pts:_ Required deliverables were received but are deficient in various ways (e.g., incomplete documentation, code doesn’t run)

_3 pts:_ Complete and adequate deliverables. Code runs but is deficient in various ways.

_4 pts:_ Code runs and does most but not all of what is required.

_5 pts:_ Nailed it. Complete deliverables, code runs and does what is required.
