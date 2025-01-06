import boto3 # type: ignore
from botocore.exceptions import ClientError # type: ignore

def delete_iam_user():
    try:
        # Get the user name dynamically from input
        user_name = input("Enter the IAM username to delete: ")

        # Initialize the IAM client
        iam_client = boto3.client('iam')
        
        print(f"Deleting user: {user_name}")
        
        # Step 1: Remove the user from groups
        print("Removing user from groups...")
        groups = iam_client.list_groups_for_user(UserName=user_name)
        for group in groups['Groups']:
            iam_client.remove_user_from_group(GroupName=group['GroupName'], UserName=user_name)
            print(f"Removed user from group: {group['GroupName']}")
        
        # Step 2: Detach managed policies
        print("Detaching managed policies...")
        policies = iam_client.list_attached_user_policies(UserName=user_name)
        for policy in policies['AttachedPolicies']:
            iam_client.detach_user_policy(UserName=user_name, PolicyArn=policy['PolicyArn'])
            print(f"Detached policy: {policy['PolicyName']}")
        
        # Step 3: Delete inline policies
        print("Deleting inline policies...")
        inline_policies = iam_client.list_user_policies(UserName=user_name)
        for policy_name in inline_policies['PolicyNames']:
            iam_client.delete_user_policy(UserName=user_name, PolicyName=policy_name)
            print(f"Deleted inline policy: {policy_name}")
        
        # Step 4: Delete access keys
        print("Deleting access keys...")
        access_keys = iam_client.list_access_keys(UserName=user_name)
        for access_key in access_keys['AccessKeyMetadata']:
            iam_client.delete_access_key(UserName=user_name, AccessKeyId=access_key['AccessKeyId'])
            print(f"Deleted access key: {access_key['AccessKeyId']}")
        
        # Step 5: Deactivate and delete MFA devices
        print("Deleting MFA devices...")
        mfa_devices = iam_client.list_mfa_devices(UserName=user_name)
        for mfa_device in mfa_devices['MFADevices']:
            iam_client.deactivate_mfa_device(UserName=user_name, SerialNumber=mfa_device['SerialNumber'])
            print(f"Deactivated MFA device: {mfa_device['SerialNumber']}")
        
        # Step 6: Delete the user
        print("Deleting the user...")
        iam_client.delete_user(UserName=user_name)
        print(f"User '{user_name}' deleted successfully.")
    
    except ClientError as e:
        print(f"Error: {e.response['Error']['Message']}")

# Call the function
delete_iam_user()

#List the current IAM users
import boto3 # type: ignore
aws_management_console = boto3.session.Session(profile_name="default")
iam_console = aws_management_console.resource('iam')

for each_user in iam_console.users.all():
    print(each_user.name)