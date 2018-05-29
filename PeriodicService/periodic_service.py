import grequests
import sys
import redis
import json

def configuration():
	try :
		with open('config.json') as f:
			data = json.load(f)
			f.close()
			return data
	except :
		print('config file is in PeriodicService directory please execute the script from PeriodicService Directory.')
		exit()

def trigger_call():
	config = configuration()
	url = config['end_point']
	parallel_req_count = config['concurrency']
	req_list = []
	
	for i in range(parallel_req_count):
		req = grequests.get(url)
		req_list.append(req)

	max_response_time, min_response_time, average_response_time = [0, sys.maxsize, 0];

	# send 'em all at same time
	all_responses = grequests.map(req_list)	

	# calculate min, max, average response times
	for response in all_responses:
		response_time = response.elapsed.total_seconds()
		if response_time < min_response_time:
			min_response_time = response_time
		if response_time > max_response_time:
			max_response_time = response_time
		average_response_time += response_time

	average_response_time /= parallel_req_count

	data = {"max_response_time":max_response_time, "min_response_time": min_response_time, "average_response_time": average_response_time}

	# dump data into redis
	cache = redis.Redis(host=config['redis_host'], port=config['redis_port'], db=0)
	# Using List Data type
	# LPUSH 'cause the latest response times come first
	cache.lpush('response_times', json.dumps(data))

	# If count is > 50 Do RREM
	# if cache.llen('response_times') > 50:
	cache.ltrim('response_times', 0, config['list_size'])

	print(data)
   
if __name__ == '__main__':
   trigger_call()
