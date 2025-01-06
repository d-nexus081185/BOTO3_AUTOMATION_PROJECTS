# Using Boto3, you can query a variety of IAM entities:

# Users
# Groups
# Roles
# Policies
# Instance Profiles
# Access Keys
# Server Certificates
# Each of these entities provides methods to retrieve and manage their details


import boto3
aws_management_console = boto3.session.Session(profile_name="default")
iam_console = aws_management_console.resource('iam')

for each_user in iam_console.users.all():
    print(each_user.name)

for each_group in iam_console.groups.all():
    print(each_group.name)

for each_role in iam_console.roles.all():
    print(each_role.name)

for each_policy in iam_console.policies.all():
    print(each_policy.policy_name)

for each_instance_profile in iam_console.instance_profiles.all():
    print(each_instance_profile.name)

for cert in iam_console.server_certificates.all():
    print(cert.name)





