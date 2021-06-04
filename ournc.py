#! /usr/bin/python3
import sys
import os
import base64

class main():
    def command(self):
        commands_whitelist = ["nc","id","whoami","pwd","ls"] # the allowed commands to execute
        ips_whitelist = ["192.168.1.102","192.168.1.221","192.168.1.112","192.168.1.122"] # the allowed IP's
        porst_whitelist = ["1234","9994","8898","2233","4432"] # the allowed ports
        argv = sys.argv[1] # get an input
        try:
            decoded_argv = base64.b64decode(argv).decode("utf-8").strip("\n") # try if it's base64-decodable so decode utf-8 and remove "\n"
            if decoded_argv in commands_whitelist:
                #print(decoded_argv + " if")
                os.system(decoded_argv)
            elif decoded_argv.split(" ")[0] in commands_whitelist and decoded_argv.split(" ")[1] in ips_whitelist and decoded_argv.split(" ")[2]in porst_whitelist :
                # if command from commands_whitelist and ip from ips_whitelist and port from porst_whitelist you can run it
                os.system(decoded_argv)
            else:
                #print(decoded_argv + " else")
                print(str(decoded_argv + ": command not found"))
        except:
            #print(decoded_argv.decode("utf-8"))
            print(str(argv + ": command not found"))


execute = main()
execute.command()
