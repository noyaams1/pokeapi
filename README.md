# ec2_rds_project

This project deploys a complete AWS infrastructure using Terraform, including a VPC with public and private subnets, an EC2 web server, and an RDS MySQL database.

## Architecture Overview

The infrastructure includes:

- **VPC**: A Virtual Private Cloud with public and private subnets across two availability zones
- **EC2 Instance**: A web server in the public subnet with Apache HTTP server
- **RDS Instance**: A MySQL database in private subnets for security
- **Security Groups**: Properly configured security groups for web and database tiers
- **NAT Gateway**: For outbound internet access from private subnets

## Prerequisites

Before you begin, ensure you have:

1. **AWS CLI** installed and configured with appropriate credentials
2. **Terraform** installed (version 0.14 or later)
3. **AWS Key Pair** created in your target region for EC2 SSH access

## Project Structure

```
├── main.tf                 # Root module orchestrating all resources
├── variables.tf            # Input variables for the root module
├── outputs.tf              # Output values from the infrastructure
├── README.md              # This file
└── modules/
    ├── vpc/               # VPC module with subnets and networking
    ├── ec2/               # EC2 instance module with user data
    ├── rds/               # RDS MySQL database module
    ├── security_groups/   # Security groups module
    └── db_subnet_group/   # Database subnet group module
```

## Configuration

### Default Configuration

The project comes with sensible defaults:

- **Region**: us-west-2
- **VPC CIDR**: 10.0.0.0/16
- **Instance Type**: t2.micro
- **Database Engine**: MySQL 8.0
- **Database Instance**: db.t3.medium

### Customization

You can customize the deployment by:

1. **Creating a terraform.tfvars file**:

```hcl
vpc_name = "my-custom-vpc"
ec2_instance_name = "my-web-server"
db_instance_identifier = "my-database"
db_username = "admin"
db_password = "your-secure-password"
key_name = "your-key-pair-name"
```

2. **Modifying variables.tf** for permanent changes

## Deployment Instructions

### 1. Clone and Initialize

```bash
# Clone the repository (if using version control)
git clone <repository-url>
cd terraform-aws-infrastructure

# Initialize Terraform
terraform init
```

### 2. Plan the Deployment

```bash
# Review what will be created
terraform plan
```

### 3. Deploy the Infrastructure

```bash
# Apply the configuration
terraform apply
```

Type `yes` when prompted to confirm the deployment.

### 4. Verify the Deployment

After deployment completes, you can:

1. **Access the web server**: Use the public IP output to access your web server
2. **SSH to the instance**: Use your key pair to connect via SSH
3. **Check database connectivity**: The web server automatically tests the database connection

## Web Server Features

The EC2 instance is automatically configured with:

- **Apache HTTP Server**: Serves web content
- **MySQL Client**: For database connectivity testing
- **Automatic Database Test**: Runs a connectivity test on startup
- **Custom Index Page**: Displays the RDS endpoint information

## Security Configuration

### Web Server Security Group

- **Inbound**: HTTP (port 80) from anywhere
- **Inbound**: SSH (port 22) from anywhere (consider restricting to your IP)
- **Outbound**: All traffic allowed

### Database Security Group

- **Inbound**: MySQL (port 3306) from web server security group only
- **Outbound**: No outbound rules needed

## Outputs

After successful deployment, you'll receive:

- **VPC ID**: The ID of the created VPC
- **Subnet IDs**: Public and private subnet identifiers
- **Web Server Public IP**: Public IP address of the web server
- **RDS Endpoint**: Database connection endpoint (sensitive)
- **Instance IDs**: EC2 and RDS instance identifiers

## Management Commands

### View Current State

```bash
# Show current infrastructure state
terraform show

# List all resources
terraform state list
```

### Update Infrastructure

```bash
# Plan changes
terraform plan

# Apply changes
terraform apply
```

### Destroy Infrastructure

```bash
# Remove all resources (use with caution!)
terraform destroy
```

## Troubleshooting

### Common Issues

1. **Key Pair Not Found**: Ensure your key pair exists in the target region
2. **Permission Denied**: Check your AWS credentials and IAM permissions
3. **Resource Limits**: Verify you haven't exceeded AWS service limits

### Debugging

1. **Check EC2 User Data Logs**:

```bash
ssh -i your-key.pem ec2-user@<public-ip>
sudo cat /var/log/cloud-init-output.log
```

2. **Test Database Connection**:

```bash
# On the EC2 instance
cat /tmp/mysql_test.log
```

3. **Check Apache Status**:

```bash
sudo systemctl status httpd
```

## Cost Considerations

This infrastructure includes:

- **EC2 t2.micro**: Free tier eligible
- **RDS db.t3.medium**: Paid instance (consider db.t3.micro for testing)
- **NAT Gateway**: Hourly charges apply
- **Data Transfer**: Charges for data transfer
