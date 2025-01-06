import boto3 # type: ignore
from botocore.exceptions import ClientError # type: ignore

def create_iam_user_with_admin_access():
    try:
        # Get the user name dynamically from input
        user_name = input("Enter the IAM username to create: ")

        # Initialize the IAM client
        iam_client = boto3.client('iam')
        
        # Step 1: Create the IAM user
        print(f"Creating user '{user_name}'...")
        response = iam_client.create_user(UserName=user_name)
        print(f"User '{user_name}' created successfully.")
        
        # Step 2: Attach the AdministratorAccess policy
        print("Attaching AdministratorAccess policy...")
        iam_client.attach_user_policy(
            UserName=user_name,
            PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
        )
        print("AdministratorAccess policy attached successfully.")
        
        # Step 3: Create access keys (optional)
        print("Creating access keys for the user...")
        access_key_response = iam_client.create_access_key(UserName=user_name)
        access_key_id = access_key_response['AccessKey']['AccessKeyId']
        secret_access_key = access_key_response['AccessKey']['SecretAccessKey']
        print("Access keys created successfully.")
        
        # Display the access keys (store them securely)
        print(f"Access Key ID: {access_key_id}")
        print(f"Secret Access Key: {secret_access_key}")
        
        return {
            "UserName": user_name,
            "AccessKeyId": access_key_id,
            "SecretAccessKey": secret_access_key
        }
    except ClientError as e:
        print(f"Error: {e.response['Error']['Message']}")
        return None

# Call the function
create_iam_user_with_admin_access()

#List the current IAM users
import boto3 # type: ignore
aws_management_console = boto3.session.Session(profile_name="default")
iam_console = aws_management_console.resource('iam')

for each_user in iam_console.users.all():
    print(each_user.name)