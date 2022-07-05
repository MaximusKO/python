with open('nginx_logs.txt', 'r', encoding='utf-8') as f:

   for line in f:
      logs = f.readline().split(" ")
      #print(log)
      remote_addr =logs[0]
      request_type = logs[5].strip(' "')
      requested_resource = logs[6]
      print(f'{remote_addr},{request_type},{requested_resource}')