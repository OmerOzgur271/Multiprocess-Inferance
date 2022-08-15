from concurrent.futures import ThreadPoolExecutor
import json

def pred(path):
	models = [model1,model2]
	
	
	for model_idx in range(len(models)):
        
		image = Image.open(fs.open(path)).convert("RGB")
		width, height = image.size
		image_batch_tensor = tf.expand_dims(image, axis=0)
		
		
		detections = models[model_idx](image_batch_tensor)
	
	
	
def consumer():

    while True:
        
        
        for messages in input_queue.receive_messages(QueueUrl="https://sqs.eu-c03/inpuc",WaitTimeSeconds=20):

            pred(json.loads(messages.body)['ImagePath'],json.loads(messages.body)['ImageId'])
            messages.delete()       
            time.sleep(0.1)
	
	
executor = ThreadPoolExecutor() 
for i in range(7):
    executor.submit(consumer)

while True:
    time.sleep(25)
    print('wake up')
