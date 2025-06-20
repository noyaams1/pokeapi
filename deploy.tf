# Extracting the default vpc created in the lab

data "aws_vpc" "default" {
  default = true
}

# Extracting the most recent Amazon Linux AMI ID 
data "aws_ami" "amazon_linux_latest" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["al2023-ami-*-x86_64"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}


# Creating the Pokemon's app server security group

resource "aws_security_group" "app_sg" {
  name        = "app_sg"
  description = "Allow SSH inbound traffic to the pokemon's app server"
  vpc_id      = data.aws_vpc.default.id
  
 ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "app_sg"
  }
}

# Creating the ec2 instance running the pokemon's app

resource "aws_instance" "pokemon_app" {
  ami           = data.aws_ami.amazon_linux_latest.id
  instance_type = "t2.micro"
  key_pair="vockey"
  iam_instance_profile = "LabInstanceProfile"
  user_data     = file("user_data.sh")
  vpc_security_group_ids = [aws_security_group.app_sg.id]
  associate_public_ip_address = true

  tags = {
    Name = "pokemon_app"
  }
}

# Creating 'pokemons_collection' database on aws dynamodb
resource "aws_dynamodb_table" "pokemons_collection" {
  name         = "pokemons_collection"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "name"

  attribute {
  name = "name"                            #Primary Key
  type = "S"
  }

  attribute {
    name = "id"                            #Secondary key
    type = "N"
  }

  tags = {
    Name        = "pokemons_collection"
  }
}







