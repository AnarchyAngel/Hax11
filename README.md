# Hax11
x11 exploit tool

One of the features of HaX11 is the ability to open a full screen browser on the target machine to any URL you like. 
It is intended to be used in a social engineering attack on the target to attempt to get passwords or other sensitive 
information but you can use it for what ever you can imagine. Its easy to use, but does require you to have a web server 
running somewhere the target machine can access.

This attack also has a higher success rate as far as executing relative to the apps other functions on the target machine 
because rather then depending on the configuration of the target to share windows/desktops, you share a window to it!

Another thought I was playing around with was a type of ransomeware attack where you just keep popping the window until they 
give you bitcoins. The idea is the victim will have no idea whats really going on and might assume they really are infected 
with some of the ransomeware they see on TV. The scareware approach might work as well. Anyway that just a few ideas, but how 
you use it is really up to you

**UPDATE**
 I have updated Hax11 to connect to non-default display ports. The previous version only allowed connecting to display 0 "port 6000", but now you can connect to any a system has available. 

Example:

If you want to connect to display 1 "port 6001" use this command:

python hax11.py ip.addr.here 1
If you want to connect to display 0 use the old command style:

python hax11.py ip.addr.here
You can connect to display 1, 2, 3, and so on. I know it seems like a small change, but it doubles or more your attack surface. So while the change is small, the impact is big. Enjoy! 
