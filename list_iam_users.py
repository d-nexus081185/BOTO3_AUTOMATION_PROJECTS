# Import all the modules and Libraries
import boto3
# Open Management Console with "default" as the user created using the AWS configure command
aws_management_console = boto3.session.Session(profile_name="default")
# Open IAM console
iam_console = aws_management_console.client(service_name="iam")
iam_users = iam_console.list_users()
for each_iam_user in iam_users['Users']:
    print(each_iam_user['UserName'])