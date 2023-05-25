import unittest
import boto3
from moto import mock_ec2
from app import app

class MyTestCase(unittest.TestCase):
    @mock_ec2
    def test_start_instance(self):
        ec2 = boto3.client('ec2')
        # EC2を作成
        ec2.run_instances(
            ImageId='xxxxx',
            MinCount=1,
            MaxCount=1,
            KeyName="ec2-1",
            TagSpecifications=[{'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'ec2-1'}]}])
        # appファイルを実行
        app.describe()

if __name__ == '__main__':
    unittest.main()

