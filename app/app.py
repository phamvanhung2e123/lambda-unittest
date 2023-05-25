import boto3

def describe():
    ec2 = boto3.client('ec2')
    # インスタンスIDを取得
    instances = ec2.describe_instances()
    instance_id = [instance['InstanceId'] for r in instances.get('Reservations') for instance in r.get('Instances')]
    print(instance_id)