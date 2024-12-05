# CSC 249 – Project 3 – Secure RPC

For this project, you'll be buidling upon your previous projects, this time buiding a (simulated) secure client and server, still communicating through a VPN.

I’ve placed some starter code in this Git repo [https://github.com/abpw/csc-249-p3-secure-RPC], which you are welcome to clone. Your job will be to fill in the "TLS_handshake_client()" function in "secure_client.py" and the "TLS_handshake_server()" function in "secure_server.py", and, optionally, the "process_message()" function in "secure_server.py()". There are detailed instructions in the comments, and you'll make heavy use of the simulated cryptographic primitives in "cryptography_simulator.py" as well as the certificate authority provided in "certificate_authority.py".

Like last time, by default, the server, VPN server, client, and certificate authority are configured to run on compatible sockets, but if you'd like to change any ip addresses or ports you can use command line arguments to do so. To use secure_server.py's command line arguments, for example, you can run "python3 secure_server.py --help" from command line in the directory the secure_server.py file is stored.

Note that all four files must be stored in the same direcory as "arguments.py" to run correctly, and the certificate authority should be started before the secure server, and the secure client should be run last.

Although "echo-server.py" is included as a test server, your client and VPN should be able to interact with any server with any functionality that follows this type of protocol:

* Take as input over a socket a message of up to 1000 bytes in a particular format
* Return to the sender along the same TCP connection a message of up to 1000 bytes (possibly an error message)

## Design Requirements

Your secure client and secure server should be, well, secure. As the "man in the middle", your VPN should not be able to read any sensitive communications between the secure client and the secure server unless those communications are properly simulated secure. Make sure that 

* Your client must obtain the desired message to be sent through the VPN from the terminal command line. This functionality is already provided in the client.py file.
* As they run, the client and the VPN applications must generate tracing messages that document significant program milestones, e.g., when connections are made, when messages and sent and received, and what was sent and what was received. (Good examples of tracing messages can be found in the sample code provided.)
* The client and server should be designed to anticipate and gracefully handle reasonable errors which could occur at either end of the communication channel. For example, the client should attempt to prevent malformed requests to the server, and the server should avoid crashing if it receives a malformed request. Remember, in the real world there is no guarantee that your server will only have to deal with communications from your (presumably friendly) client!
* Source code of your client and server must be appropriately documented. Comments should be sufficient to allow a third party to understand your code, run it, and confirm that it works.

## Deliverables

Your work on this project must be submitted for grading by **Monday, December 2nd at 11:59PM**. Extensions may be obtained by sending me a message on Slack before the original due date.

All work must be submitted in Gradescope.

You must submit these work products:

1. Source code for your secure client and secure server.
2. A **text** (.txt or .md) document with a written description of your client-VPN message format (that is, a description of all implemented client and VPN messages, and how the various components of each message are represented). Your goal in writing this document should be to convey enough information in enough detail to allow a competent programmer **without access to your source code** to write either a new secure client that communicates properly with your secure server, or a new secure server that communicates properly with your client. This document should include at least **six** sections:
    1. Overview of Application
    2. Format of an unsigned certificate
    3. Example output
    4. **A walkthorough of the steps of a TLS handshake, and what each step accomplishes**
        * For example, one step will be: "The client encrypts the generated symmetric key before sending it to the server. If it doesn't, the VPN will be able to read the symmetric key in transit and use it to decrypt further secure communications between the client and server encrypted and HMAC'd with that key."
    5. A description of two ways in which our simulation fails to achieve real security, and how these failures might be exploited by a malicious party. This is one place you can earn extra credit by discussing some less-obvious exploits. Some options for discussion are:
        * The asymmetric key generation scheme
        * The encryption/decryption/HMAC/verification algorithms
        * The certificate authority's public key distribution system
        * The use of python's "eval()" function
    6. Acknowledgements
    7. (Optional) Client->Server and Server->Client application layer message format if you decide to change "process_message()" in "secure_server.py". This can be another source of extra credit if you're creative with your application.
3. Command-line traces showing the secure client, VPN, secure server, and certificate authority in operation.

## Teamwork Policy

**For this project, all work must be submitted individually – no team submissions will be allowed**. You are free to collaborate and exchange ideas, but each student must submit their own original work. To the extent you obtain ideas and feedback from other students, you should give them proper credit in the Acknowledgments section of your specification document. For example, "Jane Austen helped me think through the different messages that my ATM server might need to be able to handle", "Sophia Smith helped me understand the purpose of the htons() function". **You should not use the Acknowledgments section to acknowledge help from the course instructor or teaching assistant.** The purpose of the section is to allow students to give appropriate credit for any peer assistance in conceiving and completing individual assignments.

## Grading Rubric

Your work on this project will be graded on a five-point scale. Fractional points and extra credit may be awarded.

_0 pts:_ No deliverables were received by the due date or requested extension date.

_1 pt:_ Incomplete deliverables were received by the due date or extension date.

_2 pts:_ Required deliverables were received but are deficient in various ways (e.g., incomplete documentation, code doesn’t run)

_3 pts:_ Complete and adequate deliverables. Code runs but is deficient in various ways.

_4 pts:_ Code runs and does most but not all of what is required.

_5 pts:_ Nailed it. Complete deliverables, code runs and does what is required.
