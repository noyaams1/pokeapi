# 🧬 Pokemon API Collection with AWS DynamoDB

A Python-based interactive application that connects to the [PokeAPI](https://pokeapi.co/) and stores Pokémon data in AWS DynamoDB. Includes automated AWS infrastructure deployment using Terraform and EC2.

---

## 🎯 Project Overview

This project enables users to:

- Interactively draw random Pokémon from PokeAPI
- Check if a Pokémon already exists in DynamoDB
- Download and save new Pokémon to the database
- Display Pokémon data in a nicely formatted output
- Automatically deploy the app and infrastructure to AWS

---

## 📋 Features

### ✅ Core Features

- **Interactive CLI**: Prompts the user to draw Pokémon
- **Smart Storage**: Avoids duplicate data fetches by checking DynamoDB
- **Live API Integration**: Pulls Pokémon data from [pokeapi.co](https://pokeapi.co/)
- **Data Persistence**: Stores all Pokémon data in a DynamoDB table
- **Pretty Output**: Presents Pokémon details clearly and colorfully

### 🚀 Deployment Features

- **Infrastructure as Code**: Terraform for provisioning EC2, DynamoDB, and networking
- **App Hosting**: Python application installed and launched on EC2
- **Auto-Startup**: App starts on boot using user data script
- **Security-Aware**: Uses IAM roles and security groups for EC2 <-> DynamoDB access
- **Schema Creation**: Creates DynamoDB table with required attributes

---

## 🏗️ Architecture Diagram

```
User Input (CLI)
      ↓
[Draw Pokémon]
      ↓
[Check DynamoDB]
   ↓           ↓
Exists       Doesn't Exist
  ↓                ↓
Show from DB   Fetch from PokeAPI → Save to DynamoDB → Show to User

+ Deployment:
  - EC2 Instance with IAM Role
  - DynamoDB Table
  - Security Group and Networking via Terraform
```

---

## 📊 Data Schema

### 🔹 Stored Attributes per Pokémon

- **pokemon_id** (Number) – Global Secondary Index key(GSI)
- **pokemon_name** (String) – Hash key
- **pokemon_height** (Number)
- **pokemon_weight** (Number)
- **pokemon_types** (List of Strings)

### 🔹 DynamoDB Schema Example

```json
{
  "TableName": "pokemons_collection",
  "KeySchema": [{ "AttributeName": "pokemon_name", "KeyType": "HASH" }],
  "AttributeDefinitions": [
    { "AttributeName": "pokemon_id", "AttributeType": "N" },
    { "AttributeName": "pokemon_name", "AttributeType": "S" }
  ],
  "GlobalSecondaryIndexes": [
    {
      "IndexName": "pokemon_id_index",
      "KeySchema": [{ "AttributeName": "pokemon_id", "KeyType": "HASH" }],
      "Projection": { "ProjectionType": "ALL" }
    }
  ]
}
```

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.8+
- AWS CLI configured (`aws configure`)
- boto3 and requests installed
- Terraform installed
- AWS account with permissions for EC2 + DynamoDB

---

## 🖥️ Local Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/noyaams1/pokeapi.git
   cd pokeapi
   ```

2. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app locally**
   ```bash
   python main.py
   ```

---

## ☁️ AWS Deployment

### Step 1: Configure AWS credentials

```bash
aws configure
```

### Step 2: Deploy infrastructure

```bash
terraform init
terraform apply
```

### Step 3: Connect and test the application

The application will be automatically installed and started on the EC2 instance via the user data script. You can SSH to the instance to monitor:

```bash
ssh -i your-key.pem ec2-user@<public-ip>
# Check application logs
tail -f /var/log/cloud-init-output.log
```

### Step 4: Application runs automatically

The application starts automatically on boot through the user data script configuration.

---

```text
How would you like to draw your Pokémon?

🎲 Adding new Pokémon: Pikachu

🎯 Pokémon Drawn:
 Name: Pikachu
 ID: 25
 Height: 4
 Weight: 60
 Types: electric

```

---

## 📦 Project Structure

```
pokeapi/
├── main.py                    # Main interactive application entry point
├── api.py                     # Functions for calling the PokeAPI
├── constant_vars.py           # Application constants and configuration
├── utilities.py               # Utility functions for data processing
├── ui_messages.py             # User interface messages and formatting
├── deploy.tf                  # Terraform infrastructure deployment
├── user_data.sh               # EC2 user data script for auto-setup
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```
