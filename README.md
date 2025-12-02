# MarvinSirius
Mail Bot

Designed to execute python scripts via email activation.
Intended use, email marving the following:

To: marvin@example.com
From: self@example.com
Subject: CommandName
Body:
Line1: Parameter 1
Line2: Parameter 2
Line3: Parameter 3

Marvin periodically checks 'his' inbox and when emails arrive processes them. Once an email has been fully executed he deletes it, keeping the inbox clean. Any python file in his functions folder can be executed, it uses system arguments for parameters. 
