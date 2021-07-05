# Encrypt & Uploads Secrets to s3 using KMS  
## Usage  
` python app.py --secret --bucket --alias --profile --name `  
secret: a string with comma seperated values - e.g "secret_name,secret_value"    
bucket: the name of the s3 bucket where the secret will be stored    
alias: the KMS alias that will be used to encrypt the secret  
profile: the AWS profile in .aws/credential to be used  
name: the name of the secret to be stored in s3    
