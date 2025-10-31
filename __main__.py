import pulumi
import pulumi_aws as aws

# Create an S3 bucket
bucket = aws.s3.Bucket(
    "my.srini212",
    acl="private",
    tags={
        "Environment": "Dev",
        "Owner": "PulumiPython",
    }
)

# Export the bucket name
pulumi.export("bucket_name", bucket.id)
