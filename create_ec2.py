import boto3

def create_ec2_instance(instance_name="MyEC2Instance"):
    # Use the 'default' profile configured in the AWS CLI
    session = boto3.Session(profile_name='default')

    # Create EC2 client
    ec2_client = session.client('ec2')

    # Specify instance details
    instance_details = {
        'ImageId': 'ami-0e2c8caa4b6378d8c',  # Replace with valid AMI ID specific to your region
        'InstanceType': 't2.micro',
        'MinCount': 1,
        'MaxCount': 1,
        'KeyName': 'my_key_pair',  # Use a valid key pair
        'SecurityGroupIds': ['sg-0e711f9f86eaeee6c'],  # Replace with your specified security group ID
        'TagSpecifications': [
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': instance_name  # Assign the specified instance name
                    }
                ]
            }
        ]
    }

    try:
        # Launch the EC2 instance
        response = ec2_client.run_instances(**instance_details)
        
        # Retrieve instance ID
        instance_id = response['Instances'][0]['InstanceId']
        print(f"EC2 Instance created successfully! Instance ID: {instance_id}")

        # Wait for instance to be in running state
        ec2_resource = session.resource('ec2')
        instance = ec2_resource.Instance(instance_id)
        print("Waiting for the instance to be in running state...")
        instance.wait_until_running()
        instance.load()

        # Retrieve and print public and private IP addresses
        public_ip = instance.public_ip_address
        private_ip = instance.private_ip_address
        print(f"Public IP: {public_ip}")
        print(f"Private IP: {private_ip}")

        return instance_id

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Provide a name for the EC2 instance
    create_ec2_instance(instance_name="CodeBuild_Server")
