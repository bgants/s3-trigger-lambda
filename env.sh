# run `source env.sh` to set these before doing any CDK deployment actions
export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)
export AWS_PRIMARY_REGION=<change-me>
export AWS_SECONDARY_REGION=<change-me>
export AWS_DOMAIN_NAME=<change-me>
export JSII_SILENCE_WARNING_UNTESTED_NODE_VERSION=1
