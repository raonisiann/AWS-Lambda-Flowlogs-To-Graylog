import gzip
import json
import os
import socket
from io import BytesIO

def lambda_handler(event, context):
    # get parameters from environment
    UDP_IP = os.environ['GRAYLOG_IP']
    UDP_PORT = int(os.environ['GRAYLOG_UDP_PORT'])
       
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  
    encodedLogsData = str(event['awslogs']['data'])   
    zipped = encodedLogsData.decode('base64','strict')
    decodedLogsData = gzip.GzipFile(fileobj=BytesIO(zipped)).read()
    allEvents = json.loads(decodedLogsData)
   
    records = []
    
    for event in allEvents['logEvents']:
    # Send to graylog via UDP    
        sock.sendto(str(event['message']), (UDP_IP, UDP_PORT))