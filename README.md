# Event Table Discord Bot
 - A Discord bot that can read and write to a database.
 - Database can be AWS S3 or local memory.
 
## Configuration

These files are needed for configuration:
All configuration files are INI-format (key=value) files.
Here are files with important keys

### Third Party Setup
1. Create a discord bot with access to the target server and channel
2. Create an AWS S3 bucket with an administrator account - [see here](https://docs.aws.amazon.com/quickstarts/latest/s3backup/step-1-create-bucket.html)
3. Create access keys so this App can access the S3 bucket - [see here](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-creds)

### Configuration Files
*These files need to be created and edited locally*  
`secrets.conf`: contains config just used by this app
```buildoutcfg
bot_token=<Bot token from Discord developer portal>
guild_name=<Discord server name>
```

`aws.conf`: contains config read by AWS boto3 library
```buildoutcfg
aws_access_key_id=<AwsPublicCredential>
aws_secret_access_key_id=<AwsPrivateCredential>
```

### CLI Parameters
*Configuration can be changed at runtime with these run flags:*  
```buildoutcfg
-bucket <AwsBucketName> : Change which S3 bucket this app reads/writes to
```

Alternatively, you can set CLI arguments in secrets.conf by adding `arg_` before the flag name.  

For example, adding this line to secrets.conf would set the `-bucket` command line argument.  
`secrets.conf`  
```buildoutcfg
...
arg_bucket=mybucket
```

## How To Setup & Self Host

todo