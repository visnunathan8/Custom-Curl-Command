# Custom curl like command using socket programming
## We gonna name the command as httpc and you customize it based on your requirement.


#TO INSTALL THE HTTPC COMMAND ON YOUR LOCAL MACHINE
#pip install --editable .


1. Option -v enables a verbose output from the command-line.
2. To pass the headers value to your HTTP operation, you could use -h option. 
3. -d gives the user the possibility to associate the body of the HTTP Request with the inline data, meaning a set of characters for standard input. 
4. Similarly, to -d, -f associate the body of the HTTP Request with the data from a given file. 
5. get/post options are used to execute GET/POST requests respectively. post should have either -d or -f but not both. However, get option should not be used with the options -d or -f.



<img width="1565" alt="Screenshot 2022-12-11 at 9 28 36 PM" src="https://user-images.githubusercontent.com/30067377/206948048-77443d0f-82f5-4954-9a9a-9c8d9162d1c9.png">



# GET SAMPLE COMMAND
 httpc get https://www.httpbin.org    

<img width="908" alt="Screenshot 2022-12-11 at 9 29 20 PM" src="https://user-images.githubusercontent.com/30067377/206948106-7d783f4f-50d8-4ca8-9f86-801ecf95a95f.png">


# GET SAMPLE COMMAND WITH VERBOSE OPTION
 httpc get https://www.stackoverflow.com/questions/9573244/how-to-check-if-the-string-is-empty -v                      
-v option represents the verbose nature of the command -> it gives all the header details along with the request.
<img width="1015" alt="Screenshot 2022-12-11 at 9 29 48 PM" src="https://user-images.githubusercontent.com/30067377/206948171-84b483ab-1a7e-47fb-8547-c20314177795.png">

## The below commands are used for testing my spring boot application(Attendance management system which is there in my github account)
## For using this you have to comment out two lines and uncomment two lines
 curl post -H 'Content-Type: application/json' -d '{"username":"rocketvisnu@gmail.com","password":"Visnu@123"}' https://www.reqbin.com/api/v1/account/login
 httpc post -h 'Content-Type: application/json' --d '{ "type": "3", "password": "admin", "employeeId": "admin"}'          
 http://www.localhost.com/userAccount/adduseraccount/
 curl -H 'Content-Type: application/json' -d '{ "type": "3", "password": "admin", "employeeId": "admin"}' http://localhost:8081/userAccount/adduseraccount/
# With file
 httpc post -h 'Content-Type: application/json' -f '/Users/macbook/Desktop/COURSE WORK/Networks/Sockets/sampledata.txt'  
 http://www.localhost.com/userAccount/adduseraccount/
# Outputing a file 
 httpc post -h 'Content-Type: application/json' -f '/Users/macbook/Desktop/COURSE WORK/Networks/Sockets/sampledata.txt' -o '/Users/macbook/Desktop/COURSE WORK/Networks/Sockets/sampleoutput.txt' http://www.localhost.com/userAccount/adduseraccount/

# Post command to httpbin file
 httpc post -h "Content-Type: application/json" http://www.httpbin.org/post -v
<img width="890" alt="Screenshot 2022-12-11 at 9 32 49 PM" src="https://user-images.githubusercontent.com/30067377/206948478-4b24cef4-4fe1-4cd9-9ead-7aa91ca95d1d.png">

# Post command to httpbin file using headers and body content along with verbose option
 httpc post -h "Content-Type: application/json"  --d '{"Assignment": 1}' http://www.httpbin.org/post -v
 
<img width="1023" alt="Screenshot 2022-12-11 at 9 44 32 PM" src="https://user-images.githubusercontent.com/30067377/206949712-eb48f070-9fd9-485b-98bc-41af0a3dde98.png">
